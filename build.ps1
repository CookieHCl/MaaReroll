if (Test-Path -Path '.\install') {
    Remove-Item -Recurse -Force '.\install\*'
}
python '.\install.py'
Copy-Item -Recurse -Force '.\deps\MFAAvalonia\*' '.\install\'
New-Item -Path '.\install\config\config.json' -Value '{"CurrentLanguage":"en-US,"CurrentTasks":["리세마라<|||>Main"]"}' -Force
.\install\MFAAvalonia.exe