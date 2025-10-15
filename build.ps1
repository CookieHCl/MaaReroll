Remove-Item -Recurse -Force .\install\*
python ./install.py
Copy-Item -Recurse -Force .\deps\MFAAvalonia\* .\install\
.\install\MFAAvalonia.exe