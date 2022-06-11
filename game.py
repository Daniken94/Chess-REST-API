# import main

# cb = main.Chessboard()
# cb.setup()

# result = None

# while True:
#     main.show(cb)
#     coords = input('Enter the move, as xyXY [xy-from, XY-to, ex. 0103]: ')
#     try:
#         from_x = int(coords[0])
#         from_y = int(coords[1])
#         to_x = int(coords[2])
#         to_y = int(coords[3])
#     except:
#         print('Invalid move!')
#     try:
#         result = cb.move(from_x, from_y, to_x, to_y)
#     except ValueError as err:
#         print('Invalid move:', str(err))
#     except IndexError:
#         print('Invalid move - outside the board!')
#     if result:
#         print()
#         print(result)
#         print()
#         break


from flask import Flask, request
from flask_restful import Api, Resource, reqparse, abort
import main


app = Flask(__name__)
api = Api(app)


cb = main.Chessboard()
cb.setup()

result = None

while True:
    main.show(cb)
    coords = input('Enter the move, as xyXY [xy-from, XY-to, ex. 0103]: ')
    try:
        from_x = int(coords[0])
        from_y = int(coords[1])
        to_x = int(coords[2])
        to_y = int(coords[3])
    except:
        print('Invalid move!')
    try:
        result = cb.move(from_x, from_y, to_x, to_y)
    except ValueError as err:
        print('Invalid move:', str(err))
    except IndexError:
        print('Invalid move - outside the board!')
    if result:
        print()
        print(result)
        print()
        break

chess_result = {}

class Chess(Resource):
    def get(self, availableMoves, error, figure, currentField):
        return chess_result[availableMoves, error, figure, currentField]


api.add_resource(Chess, "/api/v1/<str:figure>/<str:currentField>")

if __name__ == "__main__":
    app.run(debug=True)