from flask import Flask, request
from flask_restful import Api, Resource, reqparse, abort


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


# figure_put_args = reqparse.RequestParser()
# figure_put_args.add_argument("allowed_moves", type=list, required=False)

fig = {}

figures = {"king": KingFigure}
cords = [0, 1, 2, 3, 4, 5, 6, 7, 8]

def abort_if_figure_doesent_exist(url_figure):
    if url_figure not in figures:
        abort(404, message="Figure is not valid...")

def abort_if_cords_doesent_exist(x, y):
    if x or y not in cords:
        abort(404, message="Cords is not valid...")

class Chess(Resource):
    def get(self, url_figure, x, y):
        abort_if_figure_doesent_exist(url_figure)
        abort_if_cords_doesent_exist(x, y)
        figure = figures.get(url_figure)
        args = figure(x, y).list_allowed_moves()
        fig["allowed_moves"] = args
        fig["figure"] = str(figure)
        fig["current_field"] = str(x) + "," + str(y)
        return fig


api.add_resource(Chess, "/api/v1/<string:figure>/<int:x>/<int:y>")

if __name__ == "__main__":
    app.run(debug=True)