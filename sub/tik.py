import random

def print_board(board):
    """현재 게임 보드를 출력합니다."""
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def check_winner(board):
    """승자를 확인합니다. 있으면 승자를 반환하고, 없으면 None을 반환합니다."""
    # 가로, 세로, 대각선 체크
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != " ":
            return board[i][0]
        if board[0][i] == board[1][i] == board[2][i] != " ":
            return board[0][i]
    if board[0][0] == board[1][1] == board[2][2] != " ":
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != " ":
        return board[0][2]
    return None

def is_board_full(board):
    """보드가 가득 찼는지 확인합니다."""
    for row in board:
        if " " in row:
            return False
    return True

def get_user_move(board):
    """사용자의 움직임을 받아 반환합니다."""
    while True:
        try:
            row = int(input("행(1~3)을 선택하세요: ")) - 1
            col = int(input("열(1~3)을 선택하세요: ")) - 1
            if 0 <= row <= 2 and 0 <= col <= 2 and board[row][col] == " ":
                return row, col
            else:
                print("잘못된 위치입니다. 다시 선택하세요.")
        except ValueError:
            print("잘못된 입력입니다. 숫자를 입력하세요.")

def get_computer_move(board):
    """컴퓨터의 움직임을 반환합니다."""
    while True:
        row = random.randint(0, 2)
        col = random.randint(0, 2)
        if board[row][col] == " ":
            return row, col

def play_game():
    """틱택토 게임을 실행합니다."""
    board = [[" " for _ in range(3)] for _ in range(3)]
    print_board(board)

    while True:
        # 사용자 차례
        row, col = get_user_move(board)
        board[row][col] = "X"
        print_board(board)
        if check_winner(board) == "X":
            print("사용자가 이겼습니다!")
            break
        elif is_board_full(board):
            print("무승부입니다!")
            break

        # 컴퓨터 차례
        print("컴퓨터의 차례입니다.")
        row, col = get_computer_move(board)
        board[row][col] = "O"
        print_board(board)
        if check_winner(board) == "O":
            print("컴퓨터가 이겼습니다!")
            break
        elif is_board_full(board):
            print("무승부입니다!")
            break

if __name__ == "__main__":
    play_game()
