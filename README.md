# 명일방주 리세 매크로

명일방주 한섭 리세 매크로입니다.

- 단순히 리세 매크로를 사용하고 싶은거면 [USAGE.md](USAGE.md)를 읽어주세요. (아직 미완성)
- 직접 리세 매크로에 기여하고 싶으시다면 [CONTRIBUTING.md](CONTRIBUTING.md)를 읽어주세요.
- 그냥 코드만 받아서 빌드해보고 싶다면 계속 README.md를 읽어주세요.

## 빌드하는 법

### 요구사항

1. [Python](https://www.python.org/downloads/) 설치 후 `pip install MaaFw`
1. [MaaFramework](https://github.com/MaaXYZ/MaaFramework/releases) 받아서 deps 아래에 **폴더 풀어서** 복사  
  즉, deps/bin, deps/docs ... 등등의 폴더가 있어야 함
1. [MFAAvalonia](https://github.com/SweetSmellFox/MFAAvalonia/releases) 받아서 deps 아래에 **폴더 그대로** 복사  
  폴더명은 MFAAvalonia로, 즉 deps/MFAAvalonia 폴더가 있어야 함

다 됐으면 아래 코드 실행

```powershell
git submodule update --init --recursive
python ./configure.py
```

위 과정은 한 번만 하면 됩니다.

### 빌드 & 실행

```powershell
Remove-Item -Recurse -Force .\install\*
python ./install.py
Copy-Item -Recurse -Force .\deps\MFAAvalonia\* .\install\
.\install\MFAAvalonia.exe
```

또는 위 내용이 적혀있는 `./build.ps1`을 실행하셔도 됩니다.

프로세스가 똑바로 안 꺼지면 `Remove-Item -Recurse -Force .\install\*`가 실패하던데 (로그파일을 다른 프로세스가 쓰고 있다는 에러) 그냥 install 폴더를 직접 지워도 되긴 합니다.  
아니면 해봤자 로그파일이니까 에러를 무시하시고 그대로 쓰셔도 됩니다.
