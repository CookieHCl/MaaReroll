# 준비

1. [MaaFramework](https://github.com/MaaXYZ/MaaFramework/releases) 받아서 deps 아래에 **폴더 풀어서** 복사  
  즉, deps/bin, deps/docs ... 등등의 폴더가 있어야 함
1. [MFAAvalonia](https://github.com/maynut02/MFAAvalonia-ko/releases/) 받아서 deps 아래에 **폴더 그대로** 복사  
  폴더명은 MFAAvalonia로, 즉 deps/MFAAvalonia 폴더가 있어야 함

다 됐으면 아래 코드 실행

```powershell
pip install MaaFw
git submodule update --init --recursive
python ./configure.py
```

# 빌드 & 실행

```powershell
Remove-Item -Recurse -Force .\install\*
python ./install.py
Copy-Item -Recurse -Force .\deps\MFAAvalonia\* .\install\
.\install\MFAAvalonia.exe
```

또는 위 내용이 적혀있는 `./build.ps1`

# 개발

MaaFramework의 [PipelineProtocol](https://maafw.xyz/en/docs/3.1-PipelineProtocol.html)과 [ProjectInterface](https://maafw.xyz/en/docs/3.2-ProjectInterface.html) 참고.  
roi 좌표, 이미지 등은 [MFATools](https://github.com/SweetSmellFox/MFATools/releases)를 반드시 사용하자.
