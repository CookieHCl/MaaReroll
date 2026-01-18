직무유기중임 나중에 고침

# Contributor's Guide

아직 현생이 바빠서 임시로 적어놓겠습니다....  
11월부터 열심히 해봄

# TODO

interrupt deprecated됨  
MAA 5.0 뉴메타 열심히 공부하기  
MAATools도 업데이트됨??

## 목표

1. 어떤 업데이트 버전에서도 동작하도록 만들어야 합니다. 더 정확히는, 버전이 바뀌더라도 업데이트를 하지 않거나 업데이트를 최소로 해야 합니다. 아래는 이 규칙을 지키기 위해 매크로에 반영한 예시들입니다.
    - [메일함 사진](assets/resource/image/gatcha/5_get_mail.png)은 메일 내용 대신 메일 수령버튼을 확인합니다.
    - [공지 사진](assets/resource/image/gatcha/4_notice.png)은 공지 내용이 들어있지 않습니다.
    - 가챠 개수를 0-1 몇 뽑, 0-11 몇 뽑으로 정해놓는 대신 재화를 전부 사용할 때까지 돌아갑니다. (c.f. [신월동행 매크로](https://github.com/maynut02/fm-reroll)에서 아이디어를 얻음)
    - 어떤 가챠를 돌릴지 정해져 있지 않고, 돌릴 가챠의 배너가 몇 번째인지 유저가 직접 정할 수 있습니다.
    - 현실적으로 이벤트 팝업창은 이벤트마다 달라지기 때문에 언제나 작동하는 매크로를 만들긴 어렵고, 이벤트 팝업창만 고치면 언제든지 쓸 수 있게 만드는게 목표입니다.
      - 최선을 다해서 stablize 될때까지 기다렸다가 X버튼만 누르는 매크로를 만들 수는 있을지도..?
    - 라고 목표를 잡았으면서 월간 출석 체크할때 사진에 10월 넣었네 제가 이렇게 멍청합니다
1. 다양한 옵션들을 제공하여 유저가 원하는 방식대로 매크로를 돌릴 수 있어야 합니다.
    - 이것 역시 [신월동행 매크로](https://github.com/maynut02/fm-reroll)에서 아이디어를 얻었습니다.
    - 사실 리세 방식 선택을 제외하면 이미 구현이 다 되어있습니다.
1. 웬만하면 매크로가 실패 없이 계속 돌아가야 합니다.
    - 만약 실패한다면, 최대한 빠르게 복구 가능해야 합니다.

## 개발환경

- [VSCode](https://code.visualstudio.com/) + 아래 extension들을 사용합니다.
  - [Maa Pipeline Support](https://marketplace.visualstudio.com/items?itemName=nekosu.maa-support)
  - [Python ruff formatter](https://marketplace.visualstudio.com/items?itemName=charliermarsh.ruff)
  - [markdownlint](https://marketplace.visualstudio.com/items?itemName=DavidAnson.vscode-markdownlint)

특히 Maa Pipeline Support은 반드시 깔아둡시다. VSCode에서 곧바로 task를 실행시킬 수 있습니다.  
만약 특정 지점부터 매크로를 돌리고 싶은 경우, 그냥 interface.json의 `현재 화면` 부분을 임시로 수정한 다음에 돌리면 됩니다. 까먹고 커밋하는 일만 없으면 됩니다.

그 외에 화면을 캡쳐해서 이미지를 만들 때는 반드시 앱플레이어를 720p로 만든 뒤, [MFATools](https://github.com/SweetSmellFox/MFATools/releases)를 사용해서 이미지를 캡쳐합니다. 설정 들어가시면 영어로 바꿀 수 있습니다.  
또는 Maa Pipeline Support로 디버깅하는 도중에 이미지를 캡쳐하실 수도 있습니다.
PrintScreen 같은 방식의 캡쳐는 **절대로 하면 안 됩니다!!!**

이후 [README.md](README.md)를 참고하여 빌드를 한 번 해보시기 바랍니다.

## Pipeline 개발

MaaFramework의 [PipelineProtocol](https://maafw.xyz/en/docs/3.1-PipelineProtocol.html)을 참고해 [pipeline](assets/resource/pipeline/)들을, [ProjectInterface](https://maafw.xyz/en/docs/3.2-ProjectInterface.html)를 참고해 [interface.json](assets/interface.json)을 작성하면 됩니다.

Pipeline들은 [assets/resource/pipeline](assets/resource/pipeline/) 폴더에, pipeline에서 사용하는 이미지들은 [assets/resource/image](assets/resource/image/) 폴더에 있습니다.

### Pipeline 팁들

#### next 관련

next가 **매우 비직관적입니다**. PipelineProtocol을 잘 읽어보시기 바랍니다.  
next는 next 배열에 있는 노드들을 하나씩 순회하며, 처음으로 recognition에 성공한 노드로 이동하는 역할입니다.

```json
{
  "A": {
    "next": [
      "B",
      "C"
    ]
  }
}
```

예를 들어 위 노드의 경우 B 노드의 recognition과 C 노드의 recognition을 **반복적으로 수행하며**, 처음으로 recognition이 성공한 노드로 이동하는 노드입니다.  
만약 여기서 B 노드로 이동한 경우, B 노드의 recognition은 A 노드에 있을 때 이미 수행하였으므로, 바로 B 노드의 action 실시 후 next 검사를 수행합니다.

기본 timeout은 20초이며, 이 시간동안 어떤 노드도 recognition에 성공하지 못 했다면 매크로가 실패한 채로 종료됩니다.  
대부분 상황에서 20초면 충분하나, 배럭수가 너무 많아져 RAM이 부족한 경우에 스테이지 로딩이 20초 이상 걸리는 경우가 있습니다. 되도록이면 스테이지 로딩이 필요한 노드는 `"timeout": 60000`을(ms단위) 걸어주시기 바랍니다.  
비직관적인 next 때문에 `"timeout": 60000`은 현재 노드의 recognition에 걸리는 시간이 아니라, **next 노드들의 recognition에 걸리는 시간**입니다. 스테이지 로딩 이후의 노드가 아닌 스테이지 로딩 직전의 노드에 걸어주셔야 됩니다.

여담으로 next를 배열로 쓰는 경우에 마지막 노드는 recognition을 없애서 fallback하는 노드로 쓸 수도 있긴 한데, 화면 전환에 시간이 걸리는 경우 B를 가고 싶었는데 이미지 인식이 화면 전환 하기도 전에 끝나버려서 바로 C로 가버리는 경우가 생깁니다.  
되도록이면 next를 배열로 쓸 때는 모든 노드에 recognition을 걸어주고 fallback은 [아래에](#특정-상황까지-탭하기) 나와있는 대로 interrupt를 사용합시다.

#### 이미지 인식 관련

```json
{
  "Image_recognition": {
    "recognition": {
      "type": "TemplateMatch",
      "param": {
        "template": "reset/1_operator.png", // resource/image 기준 상대경로
        "roi": [671, 0, 543, 149], // "origin roi" : [721,15,443,49]
        "threshold": 0.95
      }
    },
    // action, next 생략
  }
}
```

보통 이런식으로 적습니다.  
명방은 (튜토단계에서) Live2D가 드물고 대부분 이미지가 정적이기 때문에, `"threshold": 0.95`까지 해주셔도 아무 문제 없습니다. (사실 1이 뜨는 경우도 잦습니다.)

roi, origin roi는 MFATools를 사용하였을 때 알려주는 origin roi (실제 이미지 roi)와 recommended roi (origin roi에서 상하좌우 50픽셀씩 늘린 것) 입니다. 아래쪽 TODO에 적혀있다시피 범위를 더 줄일 생각을 하고 있습니다.

#### 특정 상황까지 탭하기

```json
{
  "Wait_Until_Something": {
    "next": "Something_happened",
    "interrupt": "Tap_Until_something"
  },
  "Tap_Until_something": {
    "action": {
      "type": "Click",
      "param": {
        "target": [1, 1, 1, 1]
      }
    }
  },
  "Something_happened": {
    "recognition": {}, // 이미지 인식
    // action, next 생략
  }
}
```

보통 이런식으로 적습니다.  
대표적으로 튜토리얼에서 사용하는데, 대화창이 단순하게 "터치 10번" 같은 식으로 넘어가기엔 변수가 너무 많아서, 그냥 유저 액션이 필요할 때까지 임의의 위치를 계속해서 터치하는 식으로 만들었습니다.

`interrupt`는 `next`가 전부 실패한 경우에 fallback으로 실행하는 코드입니다. (interrupt부터 시작한 task가 끝난 뒤 다시 next 검사를 진행하고, 이를 계속 반복합니다. PipelineProtocol을 잘 읽어보시기 바랍니다.)  
위 경우 본질적으로 `"next": ["Something_happened", "Tap_Until_something"]`와 다를 바가 없으나, 좀 더 명확한 의미전달을 위해 interrupt를 사용했습니다.  
특히 interrupt는 종료된 즉시 기존 노드로 넘어가 next를 적어줄 필요가 없기 때문에 [프롤로그 전투](assets/resource/pipeline/2_prologue.json)처럼 아미야가 지속적으로 말을 걸 때 같은 노드를 재활용 할 수 있게 해줍니다.

## agent 개발

json으로 처리하기 복잡한 로직이나 MaaFramework에서 지원하지 않는 recognition/action이 필요한 경우 임의의 Python 코드를 실행시킬 수 있습니다.

[기본적인 doc](https://maafw.xyz/en/docs/1.1-QuickStarted#approach-2-json-custom-logic-extension-recommended)은 있으나, 아쉽게도 신기능이라 제대로 된 Python API doc은 존재하지 않습니다. [이 예제](https://github.com/MaaXYZ/MaaFramework/tree/main/sample/python)와 [C++ API](https://maafw.xyz/en/docs/2.2-IntegratedInterfaceOverview)만을 가지고 직접 부딪혀가면서 익혀야 합니다.

현재 사용하고 있진 않으나, 아래쪽 TODO에 나와있는 대로 [adb를 사용하기 위해서](#계정-정보-삭제복구-기능) 추후에 agent.py를 개발할 계획입니다.

만약 개발하실 생각이 있으시다면, [assets/agent](assets/agent/) 폴더에 추가하시면 되며, 기존 코드대로 각 reco/action마다 새로운 python 파일을 만드신 다음, [main.py](assets/agent/main.py)에서는 import만 해주시면 감사하겠습니다.

## TODOs

(중요도 랜덤, 그냥 생각나는 대로 막 적음)  
여기 이후는 그냥 생각 적어놓은거라 보라고 적어놓은게 아님; 추후 정리예정

### 메타-프로젝트

- CONTRIBUTING.md에 issue 관련 내용도 적기 & issue 템플릿 만들기?
- CONTRIBUTING.md가 너무 길다; USAGE.md처럼 나중엔 위키나 홈페이지 만들어야 하나?
- USAGE.md 만들기 (일단 완벽하게 0-11 동작하기 전까지 만들 계획 없음)
- 기본적으로 모든 개발자의 MaaFramework, MFAAvalonia 버전이 같아야 함. How?  
  - 그리고 애초에 주어진 install.py는 그냥 파일 복붙밖에 안 함;;; MaaFramework, MFAAvalonia도 git submodule로 관리하고 install.py가 참조하는 파일 경로만 알아서 잘 바꾸면 안 됨?
  - MaaFramework는 바이너리 release라 힘들수도 있음
- github workflow 수정하기 (현재 아예 안 건드려서 작동 안 하는 중)

### 프로젝트 관련

- 사진/pipeline을 1,2,3,4 순서로 만드는게 정말 구리다.. 특히 중간에 작업 삽입/삭제 일어나면 난리남  
  - pipeline까지는 숫자를 붙이고 사진은 숫자를 떼기? pipeline 순서는 거의 바뀔 일 없음
- MFAAvalonia는 자동 업데이트를 지원하는데 그 기능 관심 없어서 손도 안 댔음 -> 손 대기
- MFAAvalonia에서 매크로가 실패했다면 실패했다고 알려주기
  - 특히 어디서 실패했는지 로그에서 알려주면 걍 알아서 MFAAvalonia 캡쳐만 하라고 해도 로그쌀먹 가능함
  - MFAAvalonia에서 사용하는 [focus](https://github.com/SweetSmellFox/MFAAvalonia/blob/master/README_en.md#development-notes)를 보면 failed의 경우 보내는 focus가 있다
- [MFAAvalonia_ko](https://github.com/maynut02/MFAAvalonia-ko) 이어받기?
  - 원작자 허락 필요 (신월동행 매크로 만드신 분이라 챈에 있음)
  - 꼭 저렇게 아예 repo를 새로 파서 매번 main과 sync 맞출바에 그냥 번역해주신분 크레딧에 넣고 번역 파일만 가져오는 방법이 나을수도 (중궈 언어를 한국어로 바꿔버리면 됨)

### 매크로 관련

#### 버그

- 월간 출석 넘길 때 현재 사진에 10월이 포함되어 있는데, 10월 제외하고 1일만 보이도록 만들기

#### 추가 기능 관련

- TR-1런 만들기
  - 정말 아주 약간의 노력만으로 2뽑을 추가로 얻는다. 0-1런이 8분 정도로 겨우 7뽑 얻는거 고려하면 TR-1런이 더 효율적이라고 생각하긴 함
  - 만약 0-1 사료가 많아져서 TR-1에서 10뽑이 가능하면 무조건 TR-1런이 효율적임 (10뽑은 단챠 10번보다 훨씬 빠르다)
  - 다만 뇌피셜로 끝나고 실제로는 구현 안해봤음
- 0-11런 만들기
- 뉴비 미션 받을 때 합성옥 미션 깬 것들 있으면 받는 기능 추가 (TR-1, 0-11런에 필요함)
- 오퍼레이터 창 들어갔을 때 레어도 순으로 정렬하는 기능 추가 (0-11런에 보통 아미야 렙업해서 필요함)
  - 0-11에서 아미야를 1렙으로 두는 수도 있긴 함; (손으로 했을때 큰 차이 없이 깨지는거 확인하긴 함)
  - 여담으로 보통 5성 2정권을 아미야에 박는게 정배라는걸 생각해보면 아미야 1렙으로 두는게 아미야 올인하는 것보다 경험치를 아주 살짝 이득볼 수 있다
- 오피 선택 풀 늘리기?
  - 킹론상 6성 오퍼 종료조건 정할때 모든 오퍼를 다 쓸 수 있었으면 좋겠음...

#### 매크로 안정성 관련

- 배럭 수 늘렸을 때 매크로 끊기는 현상에 대한 확인 필요  
  - 이게 렉이 걸려서 발생하는 딜레이 차이 때문에 끊기는 것인지?
  - 아니면 MaaFramework의 입력이 씹혀서 끊기는 것인지?
- delay 전부 없애고 이미지 인식을 사용하기
- 이미지 인식 범위 조정하기
  - 현재 MFATools에서 쓰는대로 플마 50픽셀을 보고 있는데 명방에서 쓰는 대부분 이미지 인식은 플마 10픽셀이면 충분하다
  - 사실 걍 플마 0픽셀로 정확하게 잡아도 될거 같다 위치가 바뀌는 이미지가 없다
  - 성능이 확연하게 좋아질 것으로 기대됨
- A_gatcha.json에서 메인화면 확인하는 로직이 정말 구리다 (특히 공지 처리하는 로직이 정말정말 구리다)
  - 이제보니까 pipeline에 stablize기능이 있다 그냥 이거 써서 메인화면 stablize 한 1초 될때까지 기다리면 되는거 아님?
  - 여담인데 월간 보상이 기묘하게 잘 넘어가지긴 하는데 이것도 배럭 많아져서 렉 걸리면 정말 운 나쁠때 20초 다 채우고 매크로 터지는 문제 있음 (픽뚫 위셔델만큼 낮은 확률)
- 대화창을 넘기는 문제: 일부 대화창은 터치하면 바로 다음 대사가 나오고 일부 대화창은 터치하면 대사 끝가지 한번에 보여줌. 심지어 이게 0-1 구간에서조차 섞여나옴. 이딴게 게임?
  - 현재는 그냥 특정 화면 나올때까지 계속 터치를 하는 식으로 넘어가는 중 (생각보다 성능이 좋다)
  - 어쩌면 이게 그냥 최선의 방식일 수도 있음

### MaaFramework 관련 (해결 불가능)

- MaaFramework 업데이트 시 interface에서 string, int 등을 받을 수 있음
  - 예시) 6성 개수를 int 범위로 받을 수 있음
  - 예시) 시작 닉네임을 정해줄 수 있음
  - 예시) 원하는 6성 오퍼를 `신시아, 위셔델`처럼 string으로 받은 다음에 간단하게 쉼표로 split해서 오퍼들 전부 확인 가능

### 계정 정보 삭제/복구 기능

매크로 관련이지만 혼자 큰 기능이라 따로 분리해놓음

adb에 접근하는 방법이 뚫린다면 카카오토에 있는 계정 정보 삭제/복구 기능을 만들 수 있음  
물론 임의의 python 코드를 실행할 수 있으므로 당연히 되는거긴 한데 좀 자연스러운(?) 야매가 아닌(?) 방법으로 MaaFramework 상에서 만들고 싶음

1. 루트 권한이 있는 디바이스에서 /data/data.comYoStarKR.Arknights/shared_prefs 폴더를 따로 복사 (폴더명은 뭐 timestamp로 하고)
1. 계정 탈퇴 그대로 진행
1. 이후 복구가 필요하면 timestamp 안에 있는 shared_prefs를 덮어쓰고 명방 재시작 (위 과정에서 탈퇴한 계정을 복붙해온거기 때문에 탈퇴 취소버튼을 눌러주는 과정이 필요함)
1. 추가로 MaaFramework가 string을 받도록 업데이트 한다면

여기서 카카오토와 다르게 계정 탈퇴를 그대로 진행함  
현재 카카오토는 명방을 종료 후 shared_prefs 제거, 광고ID 재설정으로 명방 처음 접속한 것처럼 만드는데  
이렇게 하면 160MB의 요상한 데이터를 추가로 받고 (shared_prefs로 추정) 명방 처음 접속한것처럼 한국어 음성 고르기, 독타 Yostar 연동하세요 같은 창이 뜨게 되는데  
우선 괜히 쓸데없는 이미지 인식과정만 몇 개 더 생기고 그냥 계정 탈퇴하는 것보다 훨씬 느림
