from flask import Flask, request
from flask_restful import Api, Resource, reqparse, abort
from sqlalchemy import null


app = Flask(__name__)
api = Api(app)


class Figure:
    def __init__(self, x ,y):
        self.x = x
        self.y = y

    def move(self, x, y):
        self.x = x
        self.y = y

    def list_available_moves(self):
        pass

    def validate_move(self, dest_field):
        pass


class KingFigure(Figure):
    def __init__(self, x ,y):
        super().__init__(x ,y)

    def list_allowed_moves(self):
        allowed_move = []
        X = [1, -1,0, 0, 1, -1, -1, 1]
        Y = [0, 0, 1, -1, 1, -1,  1, -1]

        for i in range(8):
            x = self.x+ X[i]
            y = self.y + Y[i]
            if 0 <= x < 8 and 0 <= y < 8:
                allowed_move.append((x,y))
        return allowed_move


figures_dict = {}

figures = {"king": KingFigure}
cords = [0, 1, 2, 3, 4, 5, 6, 7, 8]

def abort_if_figure_doesent_exist(url_figure):
    if url_figure not in figures:
        abort(404, message="Figure is not valid...")


class Chess(Resource):
    def get(self, url_figure, x, y):
        abort_if_figure_doesent_exist(url_figure)
        if url_figure not in figures:
            err = "Figure is not valid..."
        else:
            err = None

        if x or y not in cords:
            err = "Cords is not valid..."
        else:
            err = None

        
        figure = figures.get(url_figure)
        args = figure(x, y).list_allowed_moves()
        figures_dict["allowed_moves"] = str(args)
        figures_dict["error"] = err
        figures_dict["figure"] = str(url_figure)
        figures_dict["current_field"] = str(x) + "," + str(y)
        return figures_dict


class ChessValid(Resource):
    def get(self, url_figure, x, y, a, b):
        abort_if_figure_doesent_exist(url_figure)
        if url_figure not in figures:
            err = "Figure is not valid..."
        else:
            err = None

        if x or y not in cords:
            err = "Cords is not valid..."
        else:
            err = None

        validation = str(a) + "," + str(b)
        
        figure = figures.get(url_figure)
        args = figure(x, y).list_allowed_moves()
        figures_dict["move"] = validation
        figures_dict["allowed_moves"] = str(args)
        figures_dict["error"] = err
        figures_dict["figure"] = str(url_figure)
        figures_dict["current_field"] = str(x) + "," + str(y)
        return figures_dict


api.add_resource(Chess, "/api/v1/<string:url_figure>/<int:x>/<int:y>")
api.add_resource(ChessValid, "/api/v1/<string:url_figure>/<int:x>/<int:y>/<int:a>/<int:b>")

if __name__ == "__main__":
    app.run(debug=True)