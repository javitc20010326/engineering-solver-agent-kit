import json
import os
import shutil
import sys
from pathlib import Path


def add_dependency_paths():
    home = Path.home()
    candidates = [
        home / ".codex" / "tools" / "paper-latex-layout" / "pydeps",
        Path(__file__).resolve().parents[1] / "pydeps",
    ]
    for path in candidates:
        if path.exists():
            sys.path.insert(0, str(path))


add_dependency_paths()

from matplotlib.backends.backend_agg import FigureCanvasAgg
from matplotlib.figure import Figure
from PIL import Image as PILImage
from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import cm
from reportlab.platypus import (
    Image,
    KeepTogether,
    PageBreak,
    Paragraph,
    SimpleDocTemplate,
    Spacer,
    Table,
    TableStyle,
)


def render_math(expr, out_dir, name, fontsize=16, width=7.0, height=0.45):
    out_dir.mkdir(parents=True, exist_ok=True)
    fig = Figure(figsize=(width, height), dpi=240)
    fig.patch.set_alpha(0)
    canvas = FigureCanvasAgg(fig)
    ax = fig.add_axes([0, 0, 1, 1])
    ax.set_axis_off()
    ax.text(0.01, 0.5, expr, fontsize=fontsize, va="center", ha="left")
    raw_path = out_dir / f"{name}_raw.png"
    path = out_dir / f"{name}.png"
    canvas.print_png(str(raw_path))
    with PILImage.open(raw_path) as im:
        im = im.convert("RGBA")
        bbox = im.getbbox()
        if bbox:
            left = max(0, bbox[0] - 8)
            upper = max(0, bbox[1] - 6)
            right = min(im.width, bbox[2] + 8)
            lower = min(im.height, bbox[3] + 6)
            im = im.crop((left, upper, right, lower))
        im.save(path)
    raw_path.unlink(missing_ok=True)
    return path


def equation_image(expr, out_dir, name, width_cm=15.0, fontsize=16, height=0.45, scale=0.78):
    path = render_math(expr, out_dir, name, fontsize=fontsize, height=height)
    with PILImage.open(path) as im:
        w_px, h_px = im.size
    width = width_cm * cm * scale
    height_pts = width * h_px / w_px
    img = Image(str(path), width=width, height=height_pts)
    img.hAlign = "LEFT"
    return img


def make_table(headers, rows, widths=None, font_size=8.4, keep_together=True):
    data = [headers] + rows
    if widths is None:
        widths = [16.5 * cm / len(headers)] * len(headers)
    table = Table(data, colWidths=[w * cm if isinstance(w, (int, float)) else w for w in widths], hAlign="LEFT", repeatRows=1)
    table.setStyle(
        TableStyle(
            [
                ("GRID", (0, 0), (-1, -1), 0.35, colors.HexColor("#B8C3CF")),
                ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#E8EEF5")),
                ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
                ("FONTNAME", (0, 1), (-1, -1), "Helvetica"),
                ("FONTSIZE", (0, 0), (-1, -1), font_size),
                ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
                ("LEFTPADDING", (0, 0), (-1, -1), 5),
                ("RIGHTPADDING", (0, 0), (-1, -1), 5),
                ("TOPPADDING", (0, 0), (-1, -1), 4),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 4),
            ]
        )
    )
    return KeepTogether([table]) if keep_together else table


def styles():
    sample = getSampleStyleSheet()
    sample.add(
        ParagraphStyle(
            name="DocTitle",
            parent=sample["Title"],
            fontName="Helvetica-Bold",
            fontSize=16.5,
            leading=20,
            alignment=TA_CENTER,
            textColor=colors.HexColor("#0B2545"),
            spaceAfter=6,
        )
    )
    sample.add(
        ParagraphStyle(
            name="Heading",
            parent=sample["Heading1"],
            fontName="Helvetica-Bold",
            fontSize=12.3,
            leading=14.5,
            textColor=colors.HexColor("#1F4D78"),
            spaceBefore=7,
            spaceAfter=4,
        )
    )
    sample.add(
        ParagraphStyle(
            name="Body",
            parent=sample["BodyText"],
            fontName="Helvetica",
            fontSize=9.2,
            leading=11.8,
            spaceAfter=4,
        )
    )
    sample.add(
        ParagraphStyle(
            name="Step",
            parent=sample["BodyText"],
            fontName="Helvetica-Bold",
            fontSize=9.2,
            leading=11.8,
            spaceBefore=3,
            spaceAfter=2,
        )
    )
    return sample


def build(spec_path, pdf_path):
    spec_path = Path(spec_path)
    pdf_path = Path(pdf_path)
    pdf_path.parent.mkdir(parents=True, exist_ok=True)
    spec = json.loads(spec_path.read_text(encoding="utf-8"))
    math_dir = pdf_path.parent / f"{pdf_path.stem}_math"
    if math_dir.exists():
        shutil.rmtree(math_dir)
    math_dir.mkdir(parents=True, exist_ok=True)

    doc = SimpleDocTemplate(
        str(pdf_path),
        pagesize=A4,
        rightMargin=1.55 * cm,
        leftMargin=1.55 * cm,
        topMargin=1.35 * cm,
        bottomMargin=1.45 * cm,
        title=spec.get("title", "Document"),
    )
    st = styles()
    story = []
    story.append(Paragraph(spec.get("title", "Document"), st["DocTitle"]))
    if spec.get("subtitle"):
        story.append(Paragraph(spec["subtitle"], st["Body"]))

    eq_count = 0
    for section in spec.get("sections", []):
        if section.get("heading"):
            story.append(Paragraph(section["heading"], st["Heading"]))
        for block in section.get("blocks", []):
            kind = block.get("type", "paragraph")
            if kind == "paragraph":
                story.append(Paragraph(block["text"], st["Body"]))
            elif kind == "step":
                story.append(Paragraph(block["text"], st["Step"]))
            elif kind == "equation":
                eq_count += 1
                story.append(
                    equation_image(
                        block["latex"],
                        math_dir,
                        f"eq_{eq_count:03d}",
                        width_cm=block.get("width_cm", 15.0),
                        fontsize=block.get("fontsize", 16),
                        height=block.get("height", 0.45),
                        scale=block.get("scale", 0.78),
                    )
                )
            elif kind == "table":
                story.append(
                    make_table(
                        block["headers"],
                        block["rows"],
                        widths=block.get("widths"),
                        font_size=block.get("font_size", 8.4),
                        keep_together=block.get("keep_together", True),
                    )
                )
            elif kind == "pagebreak":
                story.append(PageBreak())
            elif kind == "spacer":
                story.append(Spacer(1, block.get("height_cm", 0.25) * cm))
            else:
                raise ValueError(f"Unknown block type: {kind}")
    doc.build(story)


if __name__ == "__main__":
    if len(sys.argv) != 3:
        raise SystemExit("Usage: python build_academic_pdf.py input.json output.pdf")
    build(sys.argv[1], sys.argv[2])
