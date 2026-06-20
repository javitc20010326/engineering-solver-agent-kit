@echo off
powershell.exe -NoProfile -ExecutionPolicy Bypass -File "%~dp0check_environment.ps1" %*
