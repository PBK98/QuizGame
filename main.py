from QuizGame import QuizGame # QuizGame.py를 가져와서 그 안의 함수들을 사용하겠다.

quizgame = QuizGame()

if __name__ == "__main__":
    while True:
        print("\n===== 파이썬 퀴즈 게임 =====")
        print("1. 퀴즈 풀기")
        print("2. 퀴즈 추가")
        print("3. 퀴즈 목록 보기")
        print("4. 점수 확인")
        print("5. 힌트 추가")
        print("6. 퀴즈 삭제")
        print("0. 종료")


        try:

            choice = int(input("메뉴를 선택하세요: "))

            if choice == 1:
                quizgame.solve_quiz()
            elif choice == 2:
                quizgame.add_quiz()
            elif choice == 3:
                quizgame.view_quizzes()
            elif choice == 4:
                quizgame.check_score()
            elif choice == 5:
                quizgame.add_hint()
            elif choice == 6:
                quizgame.delete_quiz()
            elif choice == 0:
                print("게임을 종료합니다.")
                break
            else:
              print("\n[!] 잘못된 입력입니다. 다시 선택해주세요.")
        
        except ValueError:
            print("\n[!] 숫자로 된 메뉴 번호를 입력해주세요.")

        # ✨ KeyboardInterrupt (Ctrl+C)를 별도로 처리합니다.
        except KeyboardInterrupt:
            print("\n\n[!] 작업을 취소하고 메뉴로 돌아갑니다.")

        # ✨ 그 외 예상치 못한 모든 오류에 대한 안전망
        except Exception as e:
            print(f"\n[!] 예상치 못한 오류가 발생했습니다: {e}")
            print("메뉴로 돌아갑니다.")
