Remove-Item -Recurse -Force .\install\*
uv run ./install.py
Copy-Item -Recurse -Force .\deps\MFAAvalonia\* .\install\
.\install\MFAAvalonia.exe