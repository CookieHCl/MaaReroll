if (Test-Path -Path '.\install') {
    Remove-Item -Recurse -Force '.\install\*'
}
python '.\install.py'
Copy-Item -Recurse -Force '.\deps\MFAAvalonia\*' '.\install\'
Get-Content -Path 'MAAvalonia_config.json' -Raw | New-Item -Path '.\install\config\config.json' -Force
.\install\MFAAvalonia.exe