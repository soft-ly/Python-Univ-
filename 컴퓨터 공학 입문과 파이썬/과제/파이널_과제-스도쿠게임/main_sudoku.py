from tkinter import * # 이 두 모듈을 사용함. tkinter은 파이썬 기본 탑재
import sudoku
#풀어주는 함수
def my_solver():
   global puzzle_to_ui
   for i in range(9):
       for x in range(9):
           puzzle_to_ui[i][x].config(text=solved_board[i][x])
#화면 설정
root = Tk()
root.geometry('810x860')
root.resizable(False,False)
root.title('Sudoku')
#기본적인 틀 그리기
Shape= Canvas(root, height='810',width='810',relief='solid', bd=2)
line=Shape.create_line(270,0,270,810, fill='black', width=2)
line=Shape.create_line(540,0,540,810, fill='black', width=2)
line=Shape.create_line(0,270,810,270, fill='black', width=2)
line=Shape.create_line(0,540,810,540, fill='black', width=2)
Shape.pack()
#스도쿠 만들어주는 코드
puzzle = sudoku.Sudoku()
difficulty_level = 0.5
puzzle.set_difficulty(difficulty_level)
puzzle_value = puzzle.board
puzzle_to_ui = puzzle.board
puzzle.solve()
solved_board = puzzle.board
for i in range(9):
   for x in range(9):
       puzzle_to_ui[i][x]=Button(root, text=puzzle_value[i][x],width=4, height=4, bd=0, relief='solid')
       puzzle_to_ui[i][x].place(x =10+90*(x), y=10+90*(i))


#풀어주는 기능을 부르고, 버튼을 생성
solve_button = Button(root, text='Solve', width=4, height= 1, command=my_solver)
solve_button.pack(anchor='s')
#창을 계속 열어줌
root.mainloop()