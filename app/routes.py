from flask import Blueprint
from app.models.board import Board
from app.models.memo import Memo
from flask import Blueprint, jsonify, make_response, request
from app import db


####--------------- Blueprints ---------------####

hello_world_bp = Blueprint("hello_world_bp", __name__)
board_bp = Blueprint("board_bp", __name__, url_prefix="/boards")
memo_bp = Blueprint("memo_bp", __name__, url_prefix="/memos")


####--------------- BOARD ROUTES ---------------####

#GET
@board_bp.route("", methods=["GET"])
def get_all_boards():
    boards = Board.query.all()

    if not boards:
        return jsonify([]), 200

    res=[]
    for board in boards:
        res.append(board.board_json())
    return jsonify(res), 200

@board_bp.route("/<board_id>", methods=["GET"])
def get_board(board_id):
    board= Board.query.get(board_id)

    if not board:
        return make_response({"message": f"Board {board_id} was not found", "status": 404})

    response_body = {
        "board": (board.board_json())
    }
    return jsonify(response_body), 200

@board_bp.route("/<board_id>/memos")
def get_all_memoss_from_board(board_id):
    board = Board.query.get(board_id)
    if board is None:
        return make_response({"message": f"Board {board_id} was not found", "status": 404})
    
    return jsonify(board.all_memos_json()), 200

@board_bp.route("", methods=["POST"])
def create_board():
    request_body = request.get_json()
    items = ["title", "owner"]
    
    for item in items:
        if item not in request_body:
            return make_response({"details": f"Request body must include {item}","status": 222})
    
    new_board = Board(title=request_body["title"],
                    owner=request_body["owner"])

    db.session.add(new_board)
    db.session.commit()

    return jsonify(new_board.board_json()), 201

@board_bp.route("/<board_id>/memos", methods =["POST"])
def post_memos_to_given_board(board_id):
    request_body = request.get_json()
    board= Board.query.get(board_id)

    if not board:
        return make_response({"message": f"Board {board_id} does not exist", "status": 404})

    new_memo = Memo(message=request_body["message"],board_id= board_id)
    db.session.add(new_memo)
    db.session.commit()

    return jsonify(new_memo.memo_json()), 201


#DELETE
@board_bp.route("/<board_id>", methods=["DELETE"])
def delete_board(board_id):
    board= Board.query.get(board_id)

    if not board:
        return make_response({"message": f"Board {board_id} does not exist","status": 404})
    db.session.delete(board)
    db.session.commit()

    return make_response({"message": f"Board deleted successfully", "status": 204})


####--------------- MEMO ROUTES ---------------####
@memo_bp.route("/<memo_id>", methods=["DELETE"])

def delete_memo(memo_id):
    memo = Memo.query.get(memo_id)
    db.session.delete(memo)
    db.session.commit()

    if not memo:
        return make_response({{"message": f"memo {memo_id} was not found"}: 404})

    return {
            "details":\
            (f"Memo {memo_id} successfully deleted")
            }
    

@memo_bp.route("", methods=["PUT"])
def add_likes(memo_id):
    memo = Memo.query.get(memo_id)
    memo.likes_count +=1
    db.session.commit()

    return make_response(memo.memo_json()), 200



