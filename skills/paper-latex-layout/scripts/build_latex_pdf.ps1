$ErrorActionPreference = "Stop"
$scriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path
$python = & (Join-Path $scriptDir "python_resolver.ps1")
& $python (Join-Path $scriptDir "build_latex_pdf.py") @args
