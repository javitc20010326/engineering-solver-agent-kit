$candidates = @(
    "$env:USERPROFILE\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe",
    "$env:LOCALAPPDATA\Programs\Python\Python313\python.exe",
    "$env:LOCALAPPDATA\Programs\Python\Python312\python.exe"
)

foreach ($candidate in $candidates) {
    if (Test-Path -LiteralPath $candidate) {
        Write-Output $candidate
        exit 0
    }
}

$cmd = Get-Command python -ErrorAction SilentlyContinue
if ($cmd) {
    Write-Output $cmd.Source
    exit 0
}

$py = Get-Command py -ErrorAction SilentlyContinue
if ($py) {
    Write-Output $py.Source
    exit 0
}

Write-Error "No usable Python executable found."
exit 1
