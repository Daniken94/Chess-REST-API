from flask import Flask
from flask_restful import Api, Resource, abort

app = Flask(__name__)
api = Api(app)

# Catching 500 server error


@app.errorhandler(500)
def internal_error(error):
    return "500 error", 500


# Basic Figure class


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


# Next 6 classes is for each chess figure. It's creating their moves.


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

            for Y in range(8):
                if self.y != Y:
                    if 0 <= self.y < 8 and 0 <= y < 8:
                        allowed_move.add((self.x, Y))

            for X in range(8):
                if self.x != X:
                    if 0 <= self.x < 8 and 0 <= y < 8:
                        allowed_move.add((X, self.y))
        else:
            allowed_move = []
        return list(allowed_move)


# Dict are nessesary for catch figure's moves.


figures_dict = {}
figures_dict_validation = {}

# Dict figures for easly catch class name from url endpoint


figures = {
    "king": KingFigure,
    "pawn": PawnFigure,
    "knight": KnightFigure,
    "rook": RookFigure,
    "bishop": BishopFigure,
    "queen": QueenFigure,
}

# Service code 404 while figure is not available


def abort_if_figure_doesent_exist(url_figure):
    if url_figure not in figures:
        abort(
            404,
            message="""Figure is not valid. You must choose from:
            pawn, rook, bishop, knight, queen, king""",
        )


# Service 409 code while cords are out of range.


def abort_if_cords_doesent_exist(x, y, a, b):
    if x > 7 or y > 7 or a > 7 or b > 7:
        abort(409, message="Cords is not valid...out of chessboard!")


# Class for check available moves for figure and it's cords on chessboard
# get in endpoint.

# Can't use abort_if_cords_doesent_exist beacouse I need send error message
# so in the end i check list with error messages. If it's empty send code 200
# but if got a message send code 409 and show this message.


class Chess(Resource):
    def get(self, url_figure, x, y):
        err = []

        abort_if_figure_doesent_exist(url_figure)
        if url_figure not in figures:
            err.append("Figure is not valid...")

        if x > 7 or y > 7:
            err.append("Cords is not valid...out of chessboard!")

        figure = figures.get(url_figure)
        arg = figure(x, y).list_allowed_moves()
        figures_dict["availableMoves"] = str(arg)[1:-1] if len(err) < 1 else []
        figures_dict["error"] = None if len(err) < 1 else err[0]
        figures_dict["figure"] = str(url_figure)
        figures_dict["currentField"] = str(x) + ", " + str(y)

        if figures_dict["error"]:
            return figures_dict, 409
        else:
            return figures_dict, 200


# Class for validate move


class ChessValid(Resource):
    def get(self, url_fig_val, x, y, a, b):
        err = []

        abort_if_figure_doesent_exist(url_fig_val)
        abort_if_cords_doesent_exist(x, y, a, b)

        figure = figures.get(url_fig_val)
        args = figure(x, y).list_allowed_moves()
        validation = figure(x, y).validate_move(a, b)

        if str(validation)[1:5] in str(args):
            info = "valid"
        else:
            info = "invalid"
            err.append("Current move is not permitted!")

        figures_dict_validation["move"] = info
        figures_dict_validation["figure"] = str(url_fig_val)
        figures_dict_validation["error"] = None if len(err) < 1 else err[0]
        figures_dict_validation["currentField"] = str(x) + "," + str(y)
        figures_dict_validation["destField"] = str(a) + "," + str(b)
        return figures_dict_validation, 200


# Avaible endpoints


api.add_resource(Chess, "/api/v1/<string:url_figure>/<int:x>/<int:y>")
api.add_resource(
    ChessValid, "/api/v1/<string:url_fig_val>/<int:x>/<int:y>/<int:a>/<int:b>"
)

if __name__ == "__main__":
    app.run(debug=True)
