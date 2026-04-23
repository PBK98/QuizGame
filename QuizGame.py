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
        self.state_data = load_data('state.json')   # 퀴즈 문제들
        self.users_data = load_data('user.json')    # 사용자 정보들
        self.current_user = None                    # 현재 로그인된 사용자


    # ──────────────────────────────────────────
    # 1. 퀴즈 풀기
    # ──────────────────────────────────────────
    def solve_quiz(self):
        # 1) 사용자 이름 입력
        username = input("사용자 이름을 입력하세요: ").strip()

        # 2) 없는 사용자면 새로 등록
        if username not in self.users_data:
            print(f"[+] '{username}' 사용자를 새로 등록합니다.")
            self.users_data[username] = {"score": 0, "solved_count": 0}
            save_data('user.json', self.users_data)

        self.current_user = username

        # 3) 문제가 없으면 종료
        questions = self.state_data.get('questions', [])
        if not questions:
            print("[!] 등록된 퀴즈가 없습니다.")
            return

        # 4) Quiz 클래스에 문제 넘겨서 실행
        quiz = Quiz(questions)
        
        score, total = quiz.run_quiz()

        # 5) 결과 출력
        print(f"\n===== 결과 =====")
        print(f"맞힌 문제: {score // 10} / {total}")
        print(f"획득 점수: {score}점")

        # 6) 사용자 데이터 업데이트 후 저장
        # 문제를 풀기 전 점수를 저장
        current_score = self.users_data[username].get('score', 0)

        # 문제를 풀고 이전 점수와 비교
        if score > current_score:
            self.users_data[username]['score'] = score  # += 가 아닌 = 로 변경
            print(f"[+] 최고 점수가 갱신되었습니다. ({current_score} → {score})")
        else:
            print(f"[-] 이전 점수({current_score})보다 낮아 저장되지 않았습니다. (현재: {score})")
        
        # 문제를 푼 횟수 +1 하고 해당 내용을 저장
        self.users_data[username]['solved_count'] += 1

        self._update_best_score() # 전체 사용자 중 최고 점수 갱신

        save_data('user.json', self.users_data)
    
    # ──────────────────────────────────────────
    # 2. 퀴즈 추가
    # ──────────────────────────────────────────
    def add_quiz(self):
        print("\n===== 퀴즈 추가 =====")

        # 1) 질문 입력
        question = input("질문을 입력하세요: ").strip()
        if not question:
            print("[!] 질문을 입력해야 합니다.")
            return

        # 2) 보기 4개 입력
        choices = []
        for i in range(1, 5):
            choice = input(f"{i}번 보기를 입력하세요: ").strip()
            choices.append(f"{i}. {choice}")

        # 3) 정답 입력
        while True:
            try:
                answer_num = int(input("정답 번호를 입력하세요 (1~4): "))
                if 1 <= answer_num <= 4:
                    answer = choices[answer_num - 1]
                    break
                else:
                    print("[!] 1~4 사이의 번호를 입력하세요.")
            except ValueError:
                print("[!] 숫자를 입력하세요.")

        # 4) 힌트 입력 (선택)
        hint = input("힌트를 입력하세요 (없으면 Enter): ").strip()

        # 5) 새 문제 구성 후 저장
        new_quiz = {
            "question": question,
            "choices": choices,
            "answer": answer,
            "hint": hint
        }

        self.state_data['questions'].append(new_quiz)
        save_data('state.json', self.state_data)
        print(f"[+] 퀴즈가 추가되었습니다.")

    # ──────────────────────────────────────────
    # 3. 퀴즈 목록 보기
    # ──────────────────────────────────────────
    def view_quizzes(self):
        questions = self.state_data.get('questions', [])

        if not questions:
            print("[!] 등록된 퀴즈가 없습니다.")
            return

        print("\n===== 퀴즈 목록 =====")
        for i, q in enumerate(questions, start=1):
            print(f"\nQ{i}. {q['question']}")
            for choice in q['choices']:
                print(f"   {choice}")
            print(f"   정답: {q['answer']}")
            # 힌트가 있을 때만 출력
            if q.get('hint'):
                print(f"   힌트: {q['hint']}")

    # ──────────────────────────────────────────
    # 4. 점수 확인
    # ──────────────────────────────────────────
    def check_score(self):
        if not self.users_data:
            print("[!] 등록된 사용자가 없습니다.")
            return

        print("\n===== 점수 현황 =====")
        for username, info in self.users_data.items():
            if username == 'best_score' or username == 'users':
                continue
            print(f"{username}")
            print(f"   총 점수     : {info.get('score', 0)}점")
            print(f"   퀴즈 참여 수: {info.get('solved_count', 0)}회")

        best = self.users_data.get('best_score', {})
        if best and best.get('username'):
            print("\n--- 전체 최고 기록 ---")
            print(f"🏆 {best['username']}님: {best['score']}점")

    # ──────────────────────────────────────────
    # 5. 힌트 추가
    # ──────────────────────────────────────────
    def add_hint(self):
        questions = self.state_data.get('questions', [])

        if not questions:
            print("[!] 등록된 퀴즈가 없습니다.")
            return

        # 1) 문제 목록 출력
        print("\n===== 힌트 추가 =====")
        for i, q in enumerate(questions, start=1):
            hint_status = "✅ 있음" if q.get('hint') else "❌ 없음"
            print(f"{i}. {q['question']} [힌트: {hint_status}]")

        # 2) 번호 선택
        while True:
            try:
                num = int(input("힌트를 추가할 문제 번호를 선택하세요: "))
                if 1 <= num <= len(questions):
                    break
                else:
                    print(f"[!] 1~{len(questions)} 사이의 번호를 입력하세요.")
            except ValueError:
                print("[!] 숫자를 입력하세요.")

        # 3) 힌트 입력 후 저장
        hint = input("힌트를 입력하세요: ").strip()
        if not hint:
            print("[!] 힌트를 입력해야 합니다.")
            return

        self.state_data['questions'][num - 1]['hint'] = hint
        save_data('state.json', self.state_data)
        print(f"[+] 힌트가 저장되었습니다.")

    # ──────────────────────────────────────────
    # 6. 퀴즈 삭제
    # ──────────────────────────────────────────
    def delete_quiz(self):

        questions = self.state_data.get('questions', [])

        if not questions:
            print("[!] 삭제할 퀴즈가 없습니다.")
            return

        # 1) 문제 목록 출력
        print("\n===== 퀴즈 삭제 =====")
        for i, q in enumerate(questions, start=1):
            print(f"{i}. {q['question']}")

        # 2) 번호 선택
        while True:
            try:
                num = int(input("삭제할 문제 번호를 선택하세요: "))
                if 1 <= num <= len(questions):
                    break
                else:
                    print(f"[!] 1~{len(questions)} 사이의 번호를 입력하세요.")
            except ValueError:
                print("[!] 숫자를 입력하세요.")

        # 3) 삭제 확인
        target = questions[num - 1]['question']
        confirm = input(f"'{target}' 을 삭제하시겠습니까? (y/n): ").strip().lower()

        if confirm == 'y':
            self.state_data['questions'].pop(num - 1)
            save_data('state.json', self.state_data)
            print(f"[+] 퀴즈가 삭제되었습니다.")
        else:
            print("[-] 삭제를 취소했습니다.")

    # ──────────────────────────────────────────
    # 7. 최고 점수 업데이트
    # ──────────────────────────────────────────
    def _update_best_score(self):
        """모든 사용자 중 최고 점수를 찾아 best_score 필드를 업데이트합니다."""
        
        # 1. 'best_score'를 제외한 실제 사용자 데이터만 필터링합니다.
        #    딕셔너리 컴프리헨션을 사용하면 코드가 간결해집니다.
        users_only = {user: data for user, data in self.users_data.items() if user != 'best_score'}

        # 2. 사용자가 한 명이라도 있을 경우에만 최고 점수를 찾습니다.
        if users_only:
            # 3. max() 함수와 lambda를 사용해 점수가 가장 높은 사용자(key)를 찾습니다.
            top_user = max(users_only, key=lambda user: users_only[user].get('score', 0))
            
            # 4. 찾은 사용자의 점수를 가져옵니다.
            top_score = users_only[top_user].get('score', 0)
            top_solved_count = users_only[top_user].get('solved_count', 0)
            
            # 5. self.users_data의 'best_score' 필드를 업데이트합니다.
            self.users_data['best_score'] = {
                'username': top_user,
                'score': top_score,
                "solved_count": top_solved_count
            }
            print(f"[!] 전체 최고 점수가 갱신되었습니다. 사용자 : {top_user} ({top_score}점)")