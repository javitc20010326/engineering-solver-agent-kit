$ErrorActionPreference = "Stop"
$scriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path
$python = & (Join-Path $scriptDir "python_resolver.ps1")
& $python (Join-Path $scriptDir "render_pdf_pages.py") @args
