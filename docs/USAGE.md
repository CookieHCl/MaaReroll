# 명일방주 리세 매크로 설명서

직무유기중임 나중에 고침

기본적으로 Windows 11 & Mumu Player를 사용한다고 가정합니다.

일단 [챈글](https://arca.live/b/arknights/151089986/790965757)을 확인해주세요.

TODO: md파일이 아니라 걍 github wiki를 쓸 수도 있음 (md 하나로는 못 담을 내용이 많을수도)  
아니면 그냥 docs 폴더 만들고 안에 md 여러개 담는 식도 가능 (MaaFramework에서 사용하는 방식)

TODO: Python Installer라는 요상한 파이썬 버전 매니저가 생겨버려서 (심지어 이게 공식이고 기존 installer는 deprecated됐다고 함) 이걸 사용해서 파이썬 설치하는 방법을 알려줘야함

## 1. python & MaaFW 설치

목표: 터미널에서 `python -m pip freeze`를 입력했을 때 `MaaFw==5.4.2`가 포함된 줄이 있어야 함  
윈도우 키 누른다음 곧바로 `powershell`을 입력한 뒤 **Windows Powershell**을 실행하면 터미널을 실행할 수 있음

[설명서](/docs/1_install_python.md)

## 2. 앱플레이어 인스턴스 생성

목표: 해상도 1280x720, DPI 180, 프레임 60fps인 인스턴스 만들기  
**배럭 만드는 방법도 여기 있음**

[설명서](/docs/2_create_instance.md)

## 3. MaaReroll 다운로드 및 실행

목표: 명일방주 리세 매크로 다운로드 및 실행

[설명서](/docs/3_download_MaaReroll.md)

## 4. MaaReroll 설정

목표: 명일방주 리세 매크로 옵션들 이해하기

[설명서](/docs/4_setup_MaaReroll.md)
