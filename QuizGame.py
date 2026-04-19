import json #json의 표준 라이브러리를 가져와서 json의 기능을 사용하겠다.
from Quiz import Quiz # Quiz.py 를 가져와서 그 안의 Quiz 클래스를 사용하겠다.

# --- 데이터 로드/저장 함수 (이전과 동일) ---
# load_data(filename) 에서 filename은 이 함수를 사용해서 불러올 파일명을 담을 변수이고, load_data는 함수의 이름이다.
def load_data(filename):
    try:
        # json의 open 함수를 사용해서 filename에 담긴 파일을 읽기 모드('r')로 열고, encoding은 utf-8로 설정한다. 그리고 그 파일을 f라는 변수에 담는다.(as f)
        with open(filename, 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        if "user" in filename:
            return {"username": "Guest", "solved_count": 0, "score": 0}
        if "state" in filename:
            return {"questions": []}
        return None

def save_data(filename, data):
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4, ensure_ascii=False)
class QuizGame:
    def __init__(self):
        pass

    # ──────────────────────────────────────────
    # 1. 퀴즈 풀기
    # ──────────────────────────────────────────
    def solve_quiz(self):
        pass
    
    # ──────────────────────────────────────────
    # 2. 퀴즈 추가
    # ──────────────────────────────────────────
    def add_quiz(self):
        pass

    # ──────────────────────────────────────────
    # 3. 퀴즈 목록 보기
    # ──────────────────────────────────────────
    def view_quizzes(self):
        pass

    # ──────────────────────────────────────────
    # 4. 점수 확인
    # ──────────────────────────────────────────
    def check_score(self):
        pass

    # ──────────────────────────────────────────
    # 5. 힌트 추가
    # ──────────────────────────────────────────
    def add_hint(self):
        pass

    # ──────────────────────────────────────────
    # 6. 퀴즈 삭제
    # ──────────────────────────────────────────
    def delete_quiz(self):
        pass