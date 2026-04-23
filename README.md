# 🎮 Git과 Python을 이용해 동작하는 퀴즈게임 만들기

## 📌 프로젝트 개요
Python을 기반으로 제작된 **Codyssey 퀴즈게임**입니다.  
터미널 환경에서 실행되며, 퀴즈 풀기 / 추가 / 목록 확인 / 점수 확인 기능을 제공합니다.

---

## 💡 퀴즈 주제 선정 이유
이 프로젝트는 **Codyssey** 학습 내용을 퀴즈 형태로 복습하기 위해 제작되었습니다.  
Git과 Python의 기초 활용 능력을 키우는 것을 목표로 합니다.

---

## ▶️ 실행 방법

### 1. 저장소 클론
```bash
git clone https://github.com/PBK98/QuizGame.git
cd Quiz
```

### 2. 실행
```bash
python main.py
```

> Python 3.x 버전이 필요합니다.

---
# Git clone, pull, merge, checkout
```text
bumkyu84259392@c4r4s8 QuizGame % git pull
Already up to date.
```

```text
bumkyu84259392@c4r4s8 QuizGame % git add .  
```

```text
bumkyu84259392@c4r4s8 QuizGame % git commit -m "QuizGame.py 1줄 수정/README 작성용"
[main 729cb8e] QuizGame.py 1줄 수정/README 작성용
 1 file changed, 2 insertions(+), 2 deletions(-)
```

```text
bumkyu84259392@c4r4s8 QuizGame % git push
Enumerating objects: 15, done.
Counting objects: 100% (15/15), done.
Delta compression using up to 6 threads
Compressing objects: 100% (10/10), done.
Writing objects: 100% (10/10), 1.43 KiB | 1.43 MiB/s, done.
Total 10 (delta 5), reused 0 (delta 0), pack-reused 0 (from 0)
remote: Resolving deltas: 100% (5/5), completed with 3 local objects.
To https://github.com/PBK98/QuizGame.git
   8235a54..729cb8e  main -> main
```
# 로컬에서 QuizGame 파일 삭제 후 clone 실행 
``` text
bumkyu84259392@c4r4s8 ~ % git clone https://github.com/PBK98/QuizGame.git
Cloning into 'QuizGame'...
remote: Enumerating objects: 47, done.
remote: Counting objects: 100% (47/47), done.
remote: Compressing objects: 100% (34/34), done.
remote: Total 47 (delta 15), reused 40 (delta 11), pack-reused 0 (from 0)
Receiving objects: 100% (47/47), 22.15 KiB | 7.38 MiB/s, done.
Resolving deltas: 100% (15/15), done.
```
```text
bumkyu84259392@c4r4s8 ~ % cd QuizGame                                    
```
```text
bumkyu84259392@c4r4s8 QuizGame % git pull                                       
Already up to date.
```
# Git Merge 실행

# 현재 존재하는 branch 확인
```text
bumkyu84259392@c4r4s8 Quiz % git branch
* main
```

# Quiz branch 생성 및 재확인

```text
bumkyu84259392@c5r8s4 QuizGame % git branch -c feature/README
bumkyu84259392@c5r8s4 QuizGame % git branch
  feature/README
* main

```
# Main -> Quiz branch 전환
```text
umkyu84259392@c5r8s4 QuizGame % git switch feature/README   
Switched to branch 'feature/README'
Your branch is up to date with 'origin/main'.
```

# Merge를 위한 퀴즈 추가
```text
bumkyu84259392@c4r4s8 Quiz % python main.py
```
```text
===== 파이썬 퀴즈 게임 =====
1. 퀴즈 풀기
2. 퀴즈 추가
3. 퀴즈 목록 보기
4. 점수 확인
5. 힌트 추가
6. 퀴즈 삭제
0. 종료
메뉴를 선택하세요: 2

===== 퀴즈 추가 =====
질문을 입력하세요: git merge 테스트 용  문제 생성입니다.
1번 보기를 입력하세요: test 
2번 보기를 입력하세요: test
3번 보기를 입력하세요: test
4번 보기를 입력하세요: test
정답 번호를 입력하세요 (1~4): 1
힌트를 입력하세요 (없으면 Enter): test
[+] 퀴즈가 추가되었습니다.
```
# Quiz branch 에서 변경 내용 add 후 commit
```text
bumkyu84259392@c4r4s8 QuizGame % git add .
bumkyu84259392@c4r4s8 QuizGame % git commit -m "Merge test"
[Quiz 7ac4e89] Merge test
 4 files changed, 68 insertions(+)
```

# Merge를 위해 main branch로 전환 후 Merge 실행
```text
bumkyu84259392@c4r4s8 QuizGame % git switch main
Switched to branch 'main'
Your branch is up to date with 'origin/main'.
bumkyu84259392@c4r4s8 QuizGame % git merge main Quiz
Updating 925ced9..7ac4e89
Fast-forward
 Quiz/__pycache__/Quiz.cpython-312.pyc     | Bin 2243 -> 2243 bytes
 Quiz/__pycache__/QuizGame.cpython-312.pyc | Bin 9337 -> 9337 bytes
 Quiz/state.json                           |  11 +++++++++++
 README.md                                 |  57 +++++++++++++++++++++++++++++++++++++++++++++++++++++++++
 4 files changed, 68 insertions(+)
```

```text
bumkyu84259392@c4r4s8 QuizGame % git push

{
    "questions": [
        ...
        {
            "question": "git merge 테스트  문제 생성입니다.",
            "choices": [
                "1. test",
                "2. test",
                "3. test",
                "4. test"
            ],
            "answer": "1. test",
            "hint": "test"
        }
    ]
}
```

# checkout 으로 branch 생성, 이동
```text
bumkyu84259392@c4r4s8 QuizGame % git checkout -b test 
Switched to a new branch 'test'
bumkyu84259392@c4r4s8 QuizGame % git branch
  Quiz
  main
* test
```

# checkout 으로 test에서 변경한 내용 옮기기
```text
bumkyu84259392@c5r8s4 QuizGame % git checkout -b feature/QuizGame
Switched to a new branch 'feature/QuizGame'
bumkyu84259392@c5r8s4 QuizGame % git branch
* feature/QuizGame
  feature/README
  main
```

# checkout 과 switch의 차이
  checkout -> 이동과 함께 변경내용을 해당 폴더에 적용
  switch -> 이동만 수행

---

## ⚙️ 기능 목록

| 기능 | 설명 |
|------|------|
| 퀴즈 풀기 | 저장된 퀴즈를 풀고 정답 여부를 확인 |
| 퀴즈 추가 | 새로운 퀴즈를 추가 |
| 퀴즈 목록 | 저장된 퀴즈 전체 목록 확인 |
| 점수 확인 | 사용자의 퀴즈 점수 확인 |
| 힌트 추가 | 퀴즈 목록 확인 후 선택하여 힌트 추가 |
| 퀴즈 삭제 | 퀴즈 목록 확인 후 선택하여 퀴즈 삭제 |
| 종료 | main.py 종료 |

---

## 📁 파일 구조

```
QuizGame/
├── main.py             # 프로그램 시작 및 메인 메뉴 관리
├── QuizGame.py         # 핵심 로직 및 기능 클래스 모음
├── Quiz.py             # 퀴즈 풀기 선택 시 실행되는 클래스
├── user.json           # 사용자 정보 데이터베이스
├── state.json          # 퀴즈 데이터 저장 파일
└── defaultstate.json  # state.json 손상 시 복구용 기본 데이터
```

---

## 📂 데이터 파일 설명

### 📄 state.json
퀴즈의 핵심 데이터가 저장되는 파일입니다.

| 항목 | 설명 |
|------|------|
| 질문 | 퀴즈 문제 텍스트 |
| 선택지 | 객관식 보기 목록 |
| 정답 | 정답 번호, 텍스트 |
| 힌트 | 텍스트, 힌트 없을시 공백 |

```json
{
  "questions": [
    {
      "question": "질문 내용",
      "choices": [
        "1. 선택지1",
        "2. 선택지2",
        "3. 선택지3",
        "4. 선택지4"
      ],
      "answer": "1. 정답",
      "hint": ""
    }
  ]
}
```

### 📄 user.json
사용자 정보 및 점수 데이터가 저장되는 파일입니다.
사용자 목록과 전체 최고 기록을 나누어 관리합니다.
```json
{
    "users": {
        "test": {
            "score": 50,
            "solved_count": 2
        }
    },
    "best_score": {
        "username": "test",
        "score": 50,
        "solved_count": 2
    }
}
```
---

## 🛠️ 사용 기술
- **Language** : Python
- **Version Control** : Git / GitHub