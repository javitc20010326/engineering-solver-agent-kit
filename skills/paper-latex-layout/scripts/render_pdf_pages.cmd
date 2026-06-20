@echo off
powershell.exe -NoProfile -ExecutionPolicy Bypass -File "%~dp0render_pdf_pages.ps1" %*
