from utttpy.game.action import (
    Action,
)  # You may need to import the Action class if it's not available in the provided code.
from utttpy.game.ultimate_tic_tac_toe import UltimateTicTacToe


def main():
    game = UltimateTicTacToe()

    while not game.is_terminated():
        print(game)  # Display the current game state.

        # Get legal actions and allow the user to choose one.
        legal_actions = game.get_legal_actions()
        print("Legal Actions:")
        for i, action in enumerate(legal_actions):
            print(f"{i + 1}: {action}")

        try:
            choice = int(
                input("Choose your move (1 - {0}): ".format(len(legal_actions))) or "0"
            )
            if 1 <= choice <= len(legal_actions):
                chosen_action = legal_actions[choice - 1]
                game.execute(chosen_action)
            else:
                print("Invalid choice. Please enter a valid move number.")
        except ValueError:
            print("Invalid input. Please enter a valid move number.")

    print(game)  # Display the final game state.
    if game.is_result_X():
        print("X has won!")
    elif game.is_result_O():
        print("O has won!")
    elif game.is_result_draw():
        print("It's a draw!")


if __name__ == "__main__":
    main()
