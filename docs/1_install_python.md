# 1. Python & MaaFW 설치

## 1.1. Python 설치여부 확인

![Powershell 실행](/docs/image/1/run_powershell.png)

윈도우 키 누른다음 곧바로 `powershell`을 입력한 뒤 **Windows Powershell**을 관리자로 실행하면 터미널을 실행할 수 있습니다.

앞으로 **터미널을 실행한 후~~** 같은 말이 보일때마다 위 과정을 통해 Powershell을 키면 됩니다.  
이때 기존 터미널은 닫아버리고 새 터미널을 실행시켜주세요.

![Python 실행](/docs/image/1/run_python.png)

터미널을 실행한 후 `python`을 입력한 뒤 엔터를 쳤을 때, 위 사진처럼 Python 버전이 뜨면 Python이 이미 설치되어 있는겁니다.  
버전은 3.10 이후면 아마 충분할겁니다.

:white_check_mark: Python이 깔려있는 경우: [1.3.](#13-maafw-설치)으로 넘어가세요.  
:x: Python이 깔려있지 않은 경우: 계속해서 [1.2.](#12-python-설치)를 읽으세요.

## 1.2. Python 설치

![Python 설치](/docs/image/1/install_python.png)

먼저 [Python 다운로드](https://www.python.org/downloads/) 링크로 간 다음, Python install manager 버튼을 눌러주세요.  
다운로드한 `python-manager-xx.x.msix` 파일을 실행하면 Python install manager를 설치할 수 있습니다.

이후 터미널을 실행한 후 `py install 3`을 입력하면 Python이 설치됩니다.

## 1.3. MaaFw 설치

터미널을 실행한 후 `python -m pip install MaaFw==5.4.2 --force-reinstall`을 입력하면 MaaFw가 설치됩니다.  
마지막 줄에 `Successfully installed MaaFw-5.4.2` 같은게 보여야 합니다.

## 1.4. MaaFw 설치 확인

![MaaFw 설치 확인](/docs/image/1/check_maafw.png)

터미널을 실행한 후 `python -m pip freeze`를 입력하세요.  
출력 어딘가에 `MaaFw==5.4.2`가 보이면 설치가 완료된겁니다.
