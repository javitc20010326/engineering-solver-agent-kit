@echo off
powershell.exe -NoProfile -ExecutionPolicy Bypass -File "%~dp0build_latex_pdf.ps1" %*
