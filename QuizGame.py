import json
from Quiz import Quiz

# --- 데이터 로드/저장 함수 ---
def load_data(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        # [수정] user.json이 없을 경우, 새로운 데이터 구조에 맞게 기본값을 반환
        if "user" in filename:
            return {"users": {}, "best_score": {}}
        if "state" in filename:
            return {"questions": []}
        return None

def save_data(filename, data):
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4, ensure_ascii=False)

class QuizGame:
    def __init__(self):
        self.state_data = load_data('state.json')
        
        # [수정] user.json 데이터를 불러와 users와 best_score로 분리
        data = load_data('user.json')
        self.users = data.get('users', {})
        self.best_score = data.get('best_score', {})
        
        self.current_user = None

    # ──────────────────────────────────────────
    # 1. 퀴즈 풀기
    # ──────────────────────────────────────────
    def solve_quiz(self):
        username = input("사용자 이름을 입력하세요: ").strip()

        # self.users에 사용자 등록 및 확인
        if username not in self.users:
            print(f"[+] '{username}' 사용자를 새로 등록합니다.")
            self.users[username] = {"score": 0, "solved_count": 0}
        self.current_user = username

        questions = self.state_data.get('questions', [])
        if not questions:
            print("[!] 등록된 퀴즈가 없습니다.")
            return

        quiz = Quiz(questions)
        score, total = quiz.run_quiz()

        print(f"\n===== 결과 =====")
        print(f"맞힌 문제: {score // 10} / {total}")
        print(f"획득 점수: {score}점")

        # self.users에서 사용자 데이터 업데이트
        current_score = self.users[username].get('score', 0)
        if score > current_score:
            self.users[username]['score'] = score
            print(f"[+] 최고 점수가 갱신되었습니다. ({current_score} → {score})")
        else:
            print(f"[-] 이전 점수({current_score})보다 낮아 저장되지 않았습니다. (현재: {score})")
        
        self.users[username]['solved_count'] += 1

        self._update_best_score()

        # [수정] 분리된 데이터를 다시 합쳐서 저장
        data_to_save = {
            'users': self.users,
            'best_score': self.best_score
        }
        save_data('user.json', data_to_save)

    # ──────────────────────────────────────────
    # 2. 퀴즈 추가
    # ──────────────────────────────────────────
    def add_quiz(self):
        print("\n===== 퀴즈 추가 =====")
        question = input("질문을 입력하세요: ").strip()
        if not question:
            print("[!] 질문을 입력해야 합니다.")
            return
        choices = [f"{i}. {input(f'{i}번 보기를 입력하세요: ').strip()}" for i in range(1, 5)]
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
        hint = input("힌트를 입력하세요 (없으면 Enter): ").strip()
        new_quiz = {"question": question, "choices": choices, "answer": answer, "hint": hint}
        self.state_data['questions'].append(new_quiz)
        save_data('state.json', self.state_data)
        print(f"[+] 퀴즈가 추가되었습니다.")

    # ──────────────────────────────────────────
    # 3. 퀴즈 목록 보기 (변경 없음)
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
            if q.get('hint'):
                print(f"   힌트: {q['hint']}")

    # ──────────────────────────────────────────
    # 4. 점수 확인
    # ──────────────────────────────────────────
    def check_score(self):
        # [수정] self.users를 기준으로 확인
        if not self.users:
            print("[!] 등록된 사용자가 없습니다.")
            return

        print("\n===== 점수 현황 =====")
        for username, info in self.users.items():
            print(f"{username}")
            print(f"   총 점수     : {info.get('score', 0)}점")
            print(f"   퀴즈 참여 수: {info.get('solved_count', 0)}회")

        # [추가] 전체 최고 기록 표시
        if self.best_score:
            print("\n--- 전체 최고 기록 ---")
            print(f"사용자: {self.best_score.get('username', 'N/A')}")
            print(f"점수  : {self.best_score.get('score', 0)}점")

    # ──────────────────────────────────────────
    # 5. 힌트 추가
    # ──────────────────────────────────────────
    def add_hint(self):
        questions = self.state_data.get('questions', [])
        if not questions:
            print("[!] 등록된 퀴즈가 없습니다.")
            return
        print("\n===== 힌트 추가 =====")
        for i, q in enumerate(questions, start=1):
            hint_status = "✅ 있음" if q.get('hint') else "❌ 없음"
            print(f"{i}. {q['question']} [힌트: {hint_status}]")
        while True:
            try:
                num = int(input("힌트를 추가할 문제 번호를 선택하세요: "))
                if 1 <= num <= len(questions):
                    break
                else:
                    print(f"[!] 1~{len(questions)} 사이의 번호를 입력하세요.")
            except ValueError:
                print("[!] 숫자를 입력하세요.")
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
        print("\n===== 퀴즈 삭제 =====")
        for i, q in enumerate(questions, start=1):
            print(f"{i}. {q['question']}")
        while True:
            try:
                num = int(input("삭제할 문제 번호를 선택하세요: "))
                if 1 <= num <= len(questions):
                    break
                else:
                    print(f"[!] 1~{len(questions)} 사이의 번호를 입력하세요.")
            except ValueError:
                print("[!] 숫자를 입력하세요.")
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
        """[수정] self.users를 읽어 self.best_score를 업데이트합니다."""
        if not self.users:
            return

        top_user = max(self.users, key=lambda user: self.users[user].get('score', 0))
        top_score = self.users[top_user].get('score', 0)

        current_best_score = self.best_score.get('score', 0)
        if top_score > current_best_score:
            self.best_score = {'username': top_user, 'score': top_score}
            print(f"[!] 전체 최고 점수가 갱신되었습니다. 현재 1위 : {top_user} ({top_score}점)")