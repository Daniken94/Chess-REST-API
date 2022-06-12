from main import (
    Figure,
    KingFigure,
    QueenFigure,
    BishopFigure,
    RookFigure,
    KnightFigure,
    PawnFigure,
    ChessValid,
)


class TestKingMoves:
    def test_move_in_range(self):
        k1 = KingFigure(4, 5)
        assert k1.list_allowed_moves() == [
            (5, 5),
            (3, 5),
            (4, 6),
            (4, 4),
            (5, 6),
            (3, 4),
            (3, 6),
            (5, 4),
        ]

    def test_move_out_of_range(self):
        k2 = KingFigure(9, 8)
        assert k2.list_allowed_moves() == []

    def test_king_valid(self):
        figure = KingFigure(4, 5)
        args = figure.list_allowed_moves()
        validation = Figure.validate_move(KingFigure, 5, 5)
        result = str(validation)[1:5] in str(args)
        assert result == True

    def test_king_invalid(self):
        figure = KingFigure(4, 5)
        args = figure.list_allowed_moves()
        validation = Figure.validate_move(KingFigure, 5, 2)
        result = str(validation)[1:5] in str(args)
        assert result == False


class TestQueenMoves:
    def test_move_in_range(self):
        k1 = QueenFigure(4, 5)
        assert k1.list_allowed_moves() == [
            (0, 1),
            (1, 2),
            (3, 4),
            (2, 7),
            (5, 4),
            (2, 3),
            (6, 7),
            (5, 6),
            (7, 2),
            (3, 6),
            (6, 3),
        ]

    def test_move_out_of_range(self):
        k2 = QueenFigure(9, 9)
        assert k2.list_allowed_moves() == []

    def test_queen_valid(self):
        figure = QueenFigure(4, 5)
        args = figure.list_allowed_moves()
        validation = Figure.validate_move(QueenFigure, 0, 1)
        result = str(validation)[1:5] in str(args)
        assert result == True

    def test_queen_invalid(self):
        figure = QueenFigure(4, 5)
        args = figure.list_allowed_moves()
        validation = Figure.validate_move(QueenFigure, 5, 2)
        result = str(validation)[1:5] in str(args)
        assert result == False


class TestBishopMoves:
    def test_move_in_range(self):
        k1 = BishopFigure(4, 5)
        assert k1.list_allowed_moves() == [
            (0, 1),
            (1, 2),
            (3, 4),
            (2, 7),
            (5, 4),
            (2, 3),
            (6, 7),
            (5, 6),
            (7, 2),
            (3, 6),
            (6, 3),
        ]

    def test_move_out_of_range(self):
        k2 = BishopFigure(9, 9)
        assert k2.list_allowed_moves() == []

    def test_bishop_valid(self):
        figure = BishopFigure(4, 5)
        args = figure.list_allowed_moves()
        validation = Figure.validate_move(QueenFigure, 0, 1)
        result = str(validation)[1:5] in str(args)
        assert result == True

    def test_bishop_invalid(self):
        figure = BishopFigure(4, 5)
        args = figure.list_allowed_moves()
        validation = Figure.validate_move(QueenFigure, 5, 2)
        result = str(validation)[1:5] in str(args)
        assert result == False


class TestRookMoves:
    def test_move_in_range(self):
        k1 = RookFigure(4, 5)
        assert k1.list_allowed_moves() == [
            (4, 0),
            (4, 1),
            (4, 2),
            (4, 3),
            (4, 4),
            (4, 6),
            (4, 7),
            (0, 5),
            (1, 5),
            (2, 5),
            (3, 5),
            (5, 5),
            (6, 5),
            (7, 5),
        ]

    def test_move_out_of_range(self):
        k2 = RookFigure(9, 9)
        assert k2.list_allowed_moves() == []

    def test_rook_valid(self):
        figure = RookFigure(4, 5)
        args = figure.list_allowed_moves()
        validation = Figure.validate_move(RookFigure, 4, 1)
        result = str(validation)[1:5] in str(args)
        assert result == True

    def test_rook_invalid(self):
        figure = RookFigure(4, 5)
        args = figure.list_allowed_moves()
        validation = Figure.validate_move(RookFigure, 5, 2)
        result = str(validation)[1:5] in str(args)
        assert result == False


class TestKnightMoves:
    def test_move_in_range(self):
        k1 = KnightFigure(4, 5)
        assert k1.list_allowed_moves() == [
            (6, 6),
            (5, 7),
            (3, 7),
            (2, 6),
            (2, 4),
            (3, 3),
            (5, 3),
            (6, 4),
        ]

    def test_move_out_of_range(self):
        k2 = KnightFigure(9, 9)
        assert k2.list_allowed_moves() == []

    def test_knight_valid(self):
        figure = KnightFigure(4, 5)
        args = figure.list_allowed_moves()
        validation = Figure.validate_move(KnightFigure, 6, 6)
        result = str(validation)[1:5] in str(args)
        assert result == True

    def test_knight_invalid(self):
        figure = KnightFigure(4, 5)
        args = figure.list_allowed_moves()
        validation = Figure.validate_move(KnightFigure, 5, 2)
        result = str(validation)[1:5] in str(args)
        assert result == False


class TestPawnMoves:
    def test_move_in_range(self):
        k1 = PawnFigure(4, 1)
        assert k1.list_allowed_moves() == [(4, 2), (4, 3)]

    def test_move_out_of_range(self):
        k2 = PawnFigure(9, 9)
        assert k2.list_allowed_moves() == []

    def test_pawn_valid(self):
        figure = PawnFigure(4, 1)
        args = figure.list_allowed_moves()
        validation = Figure.validate_move(PawnFigure, 4, 2)
        result = str(validation)[1:5] in str(args)
        assert result == True

    def test_pawn_invalid(self):
        figure = PawnFigure(4, 1)
        args = figure.list_allowed_moves()
        validation = Figure.validate_move(PawnFigure, 5, 2)
        result = str(validation)[1:5] in str(args)
        assert result == False
