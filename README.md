# 준비

(uv run은 그냥 python으로 대체해도 됨)

1. [MaaFramework](https://github.com/MaaXYZ/MaaFramework/releases) 받아서 deps 아래에 **폴더 풀어서** 복사  
  즉, deps/bin, deps/docs ... 등등의 폴더가 있어야 함
2. [MFAAvalonia](https://github.com/maynut02/MFAAvalonia-ko/releases/) 받아서 deps 아래에 **폴더 그대로** 복사  
  폴더명은 MFAAvalonia로, 즉 deps/MFAAvalonia 폴더가 있어야 함

다 됐으면 아래 코드 실행

```powershell
git submodule update --init --recursive
uv run ./configure.py
```

# 빌드 & 실행

```powershell
uv run ./install.py
Copy-Item -Recurse -Force .\deps\MFAAvalonia\* .\install\
.\install\MFAAvalonia.exe
```

또는 위 내용이 적혀있는 `./build.ps1`
