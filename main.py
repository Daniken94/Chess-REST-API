from flask import Flask, Response
from flask_restful import Api, Resource, abort

app = Flask(__name__)
api = Api(app)


class Figure:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self, x, y):
        self.x = x
        self.y = y

    def validate_move(self, a, b):
        self.a = a
        self.b = b
        new_move = []
        new_move.append(a)
        new_move.append(b)
        return new_move


class KingFigure(Figure):
    def __init__(self, x, y):
        super().__init__(x, y)

    def list_allowed_moves(self):
        allowed_move = []
        X = [1, -1, 0, 0, 1, -1, -1, 1]
        Y = [0, 0, 1, -1, 1, -1, 1, -1]

        for i in range(8):
            x = self.x + X[i]
            y = self.y + Y[i]
            if 0 <= x < 8 and 0 <= y < 8:
                allowed_move.append((x, y))
        return allowed_move


class PawnFigure(Figure):
    def __init__(self, x, y):
        super().__init__(x, y)

    def list_allowed_moves(self):
        if self.x < 8 or self.y < 8:
            allowed_move = []
            if self.y < 7:
                allowed_move.append((self.x, self.y + 1))
                allowed_move.append((self.x, self.y + 2))
            else:
                allowed_move.append((self.x, self.y - 1))
                allowed_move.append((self.x, self.y - 2))
        else:
            allowed_move = []
        return allowed_move


class KnightFigure(Figure):
    def __init__(self, x, y):
        super().__init__(x, y)

    def list_allowed_moves(self):
        allowed_move = []
        X = [2, 1, -1, -2, -2, -1, 1, 2]
        Y = [1, 2, 2, 1, -1, -2, -2, -1]

        for i in range(8):
            x = self.x + X[i]
            y = self.y + Y[i]
            if 0 <= x < 8 and 0 <= y < 8:
                allowed_move.append((x, y))
        return allowed_move


class RookFigure(Figure):
    def __init__(self, x, y):
        super().__init__(x, y)

    def list_allowed_moves(self):
        if self.x < 8 or self.y < 8:
            allowed_move = []
            for Y in range(8):
                if self.y != Y:
                    allowed_move.append((self.x, Y))
            for X in range(8):
                if self.x != X:
                    allowed_move.append((X, self.y))
        else:
            allowed_move = []
        return allowed_move


class BishopFigure(Figure):
    def __init__(self, x, y):
        super().__init__(x, y)

    def list_allowed_moves(self):
        if self.x < 8 or self.y < 8:
            allowed_move = set()

            for i in range(1, 8):
                x = self.x + i
                y = self.y + i
                if 0 <= x < 8 and 0 <= y < 8:
                    allowed_move.add((x, y))

            for i in range(1, 8):
                x = self.x - i
                y = self.y - i
                if 0 <= x < 8 and 0 <= y < 8:
                    allowed_move.add((x, y))

            for i in range(1, 8):
                x = self.x + i
                y = self.y - i
                if 0 <= x < 8 and 0 <= y < 8:
                    allowed_move.add((x, y))

            for i in range(1, 8):
                x = self.x - i
                y = self.y + i
                if 0 <= x < 8 and 0 <= y < 8:
                    allowed_move.add((x, y))
        else:
            allowed_move = []
        return list(allowed_move)


class QueenFigure(Figure):
    def __init__(self, x, y):
        super().__init__(x, y)

    def list_allowed_moves(self):
        if self.x < 8 or self.y < 8:
            allowed_move = set()
            for i in range(1, 8):
                x = self.x + i
                y = self.y + i
                if 0 <= x < 8 and 0 <= y < 8:
                    allowed_move.add((x, y))

            for i in range(1, 8):
                x = self.x - i
                y = self.y - i
                if 0 <= x < 8 and 0 <= y < 8:
                    allowed_move.add((x, y))

            for i in range(1, 8):
                x = self.x + i
                y = self.y - i
                if 0 <= x < 8 and 0 <= y < 8:
                    allowed_move.add((x, y))

            for i in range(1, 8):
                x = self.x - i
                y = self.y + i
                if 0 <= x < 8 and 0 <= y < 8:
                    allowed_move.add((x, y))

            # move horizontal - x the same, y changed
            for Y in range(8):
                if self.y != Y:
                    if 0 <= self.y < 8 and 0 <= y < 8:
                        allowed_move.add((self.x, Y))

            # move vertical - x changed, y the same
            for X in range(8):
                if self.x != X:
                    if 0 <= self.x < 8 and 0 <= y < 8:
                        allowed_move.add((X, self.y))
        else:
            allowed_move = []
        return list(allowed_move)


figures_dict = {}
figures_dict_validation = {}

figures = {
    "king": KingFigure,
    "pawn": PawnFigure,
    "knight": KnightFigure,
    "rook": RookFigure,
    "bishop": BishopFigure,
    "queen": QueenFigure,
}


def abort_if_figure_doesent_exist(url_figure):
    if url_figure not in figures:
        abort(
            404,
            message="Figure is not valid. You must choose from: pawn, rook, bishop, knight, queen, king",
        )


def abort_if_cords_doesent_exist(x, y, a, b):
    if x > 7 or y > 7 or a > 7 or b > 7:
        abort(404, message="Cords is not valid...out of chessboard!")


class Chess(Resource):
    def get(self, url_figure, x, y):
        err = []

        abort_if_figure_doesent_exist(url_figure)
        if url_figure not in figures:
            err.append("Figure is not valid...")

        if x > 7 or y > 7:
            err.append("Cords is not valid...out of chessboard!")

        figure = figures.get(url_figure)
        args = figure(x, y).list_allowed_moves()
        figures_dict["availableMoves"] = str(args)[1:-1] if len(err) < 1 else []
        figures_dict["error"] = None if len(err) < 1 else err[0]
        figures_dict["figure"] = str(url_figure)
        figures_dict["currentField"] = str(x) + ", " + str(y)
        return figures_dict, 200


class ChessValid(Resource):
    def get(self, url_figure_valid, x, y, a, b):
        err = []

        abort_if_figure_doesent_exist(url_figure_valid)
        abort_if_cords_doesent_exist(x, y, a, b)

        figure = figures.get(url_figure_valid)
        args = figure(x, y).list_allowed_moves()
        validation = figure(x, y).validate_move(a, b)

        if str(validation)[1:5] in str(args):
            info = "valid"
        else:
            info = "invalid"
            err.append("Current move is not permitted!")

        figures_dict_validation["move"] = info
        figures_dict_validation["figure"] = str(url_figure_valid)
        figures_dict_validation["error"] = None if len(err) < 1 else err[0]
        figures_dict_validation["currentField"] = str(x) + "," + str(y)
        figures_dict_validation["destField"] = str(a) + "," + str(b)
        return figures_dict_validation, 200


api.add_resource(Chess, "/api/v1/<string:url_figure>/<int:x>/<int:y>")
api.add_resource(
    ChessValid, "/api/v1/<string:url_figure_valid>/<int:x>/<int:y>/<int:a>/<int:b>"
)

if __name__ == "__main__":
    app.run(debug=True)
