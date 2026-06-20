from __future__ import annotations

import argparse
from textwrap import dedent


EN = """\
Installed and ready.

This is not just a PDF template or a prompt pack. This kit turns Codex/Claude into a local engineering study agent for one university course: it can organize course material, build live context files, solve exercises step by step, verify calculations, generate LaTeX PDFs, review your attempts, create formula sheets, prepare mock exams, transcribe notes from photos, and track your progress.

Important rule: use one installation/workspace per course. Do not mix different subjects in the same workspace.

First, answer this short setup questionnaire:

1. Course name:
2. University and degree/program:
3. Target exam or assessment:
4. Current level: A very weak / B basic / C intermediate / D strong
5. Explanation style: A very step-by-step / B balanced / C concise exam style / D conceptual first

Then go to your university virtual classroom for that course, download a ZIP or folder with all available material, and give it to me: slides, notes, problem sheets, exams, official solutions, assignments, rubrics, handwritten photos, or screenshots.

After I analyze the material, I will create the course workspace, store and connect the files, build the live context files, and show you a project map with the main Markdown files, scripts, folders, and what each one contains for your specific course.

Then you can ask things like:

- "Solve this exam problem step by step and generate a LaTeX PDF."
- "Review my handwritten attempt and tell me where the first error appears."
- "Make a formula sheet for Topic 3 with units and when to use each equation."
- "Create a mock exam using this teacher's style."
- "Explain only this step; I do not understand where this formula comes from."
- "Transcribe these notes from photos and connect them with the theory."
"""


ES = """\
Instalado y listo.

Esto no es solo una plantilla de PDF ni un pack de prompts. Este kit convierte Codex/Claude en un agente local de estudio para una asignatura de ingenieria: puede organizar el material, construir archivos vivos de contexto, resolver ejercicios paso a paso, verificar calculos, generar PDFs en LaTeX, corregir tus intentos, crear formularios, preparar simulacros y guardar tu progreso.

Regla importante: una instalacion/carpeta de trabajo debe ser para una unica asignatura. No mezcles varias asignaturas en el mismo workspace.

Primero responde este pequeno cuestionario:

1. Nombre de la asignatura:
2. Universidad y grado/carrera:
3. Examen o evaluacion objetivo:
4. Nivel actual: A muy verde / B basico / C intermedio / D fuerte pero quiero pulir examen
5. Estilo de explicacion: A muy paso a paso / B equilibrado / C conciso de examen / D concepto primero y ecuaciones despues

Despues ve al aula virtual de tu universidad, entra en esa asignatura, descarga un ZIP o carpeta con todo el material disponible y damelo: diapositivas, apuntes, boletines, examenes, soluciones oficiales, entregables, rubricas, fotos de apuntes o capturas.

Cuando analice el material, creare la carpeta de la asignatura, guardare e interconectare los archivos, construire los archivos vivos de contexto y te mostrare un mapa del proyecto con los Markdown, scripts, carpetas y que contiene cada uno para tu asignatura concreta.

Luego podras pedirme cosas como:

- "Resuelve este problema de examen paso a paso y genera PDF en LaTeX."
- "Corrige mi intento escrito a mano y dime donde aparece el primer error."
- "Hazme un formulario del Tema 3 con unidades y cuando usar cada ecuacion."
- "Creame un simulacro con el estilo de este profesor."
- "Explicame solo este paso, no entiendo de donde sale esta formula."
- "Transcribe estos apuntes en fotos y conectalos con la teoria."
"""


def get_message(lang: str = "en") -> str:
    return dedent(ES if lang == "es" else EN).strip()


def main() -> None:
    parser = argparse.ArgumentParser(description="Print the first-run onboarding message.")
    parser.add_argument("--lang", choices=["en", "es"], default="en")
    args = parser.parse_args()

    print(get_message(args.lang))


if __name__ == "__main__":
    main()
