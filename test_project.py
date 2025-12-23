from project import check_win, get_win_positions, game_is_winnable


def test_check_win():
    board_size = 3
    win_positions = [[0, 1, 2], [0, 3, 6], [3, 4, 5], [1, 4, 7], [6, 7, 8], [2, 5, 8], [0, 4, 8], [2, 4, 6]]

    assert check_win(board_size, win_positions, ["X", "X", "X", "", "", "", "", "", ""]) == "X"
    assert check_win(board_size, win_positions, ["", "", "", "", "", "", "", "", ""]) is None
    assert check_win(board_size, win_positions, ["X", "X", "", "", "", "X", "", "X", ""]) is None
    assert check_win(board_size, win_positions, ["X", "X", "", "X", "X", "X", "", "", ""]) == "X"
    assert check_win(board_size, win_positions, ["X", "X", "", "O", "O", "O", "O", "X", "X"]) == "O"
    assert check_win(board_size, win_positions, ["X", "X", "", "X", "O", "O", "", "O", "O"]) is None


def test_get_win_positions():
    assert get_win_positions(3) == [
        [0, 1, 2], [0, 3, 6], [3, 4, 5], [1, 4, 7],
        [6, 7, 8], [2, 5, 8], [0, 4, 8], [2, 4, 6]
    ]

    assert get_win_positions(4) == [
        [0, 1, 2, 3], [0, 4, 8, 12], [4, 5, 6, 7], [1, 5, 9, 13], [8, 9, 10, 11],
        [2, 6, 10, 14], [12, 13, 14, 15], [3, 7, 11, 15], [0, 5, 10, 15], [3, 6, 9, 12]
    ]

    assert get_win_positions(5) == [
        [0, 1, 2, 3, 4], [0, 5, 10, 15, 20], [5, 6, 7, 8, 9], [1, 6, 11, 16, 21],
        [10, 11, 12, 13, 14], [2, 7, 12, 17, 22], [15, 16, 17, 18, 19], [3, 8, 13, 18, 23],
        [20, 21, 22, 23, 24], [4, 9, 14, 19, 24], [0, 6, 12, 18, 24], [4, 8, 12, 16, 20]
    ]


def test_game_is_winnable():
    assert game_is_winnable([
        [0, 1, 2], [0, 3, 6], [3, 4, 5], [1, 4, 7],
        [6, 7, 8], [2, 5, 8], [0, 4, 8], [2, 4, 6]],
        [
            "X", "", "O",
            "", "", "",
            "", "", ""], 3) is True

    assert game_is_winnable([
        [0, 1, 2], [0, 3, 6], [3, 4, 5], [1, 4, 7],
        [6, 7, 8], [2, 5, 8], [0, 4, 8], [2, 4, 6]],
        [
            "X", "", "",
            "", "", "",
            "", "", ""], 3) is True

    assert game_is_winnable([
        [0, 1, 2], [0, 3, 6], [3, 4, 5], [1, 4, 7],
        [6, 7, 8], [2, 5, 8], [0, 4, 8], [2, 4, 6]],
        [
            "X", "O", "X",
            "X", "O", "O",
            "O", "X", ""], 3) is False

    assert game_is_winnable([
            [0, 1, 2, 3, 4], [0, 5, 10, 15, 20], [5, 6, 7, 8, 9], [1, 6, 11, 16, 21],
            [10, 11, 12, 13, 14], [2, 7, 12, 17, 22], [15, 16, 17, 18, 19], [3, 8, 13, 18, 23],
            [20, 21, 22, 23, 24], [4, 9, 14, 19, 24], [0, 6, 12, 18, 24], [4, 8, 12, 16, 20]
        ], [
            "X", "", "X", "O", "X",
            "X", "", "X", "O", "O",
            "O", "", "O", "X", "X",
            "X", "", "X", "O", "X",
            "X", "", "X", "O", "X"], 5) is True
