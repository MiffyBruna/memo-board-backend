from crypt import methods
from flask import Blueprint
from app.models.board import Board
from flask import Blueprint, jsonify, abort, make_response, request
from app import db


####--------------- Blueprints ---------------####

hello_world_bp = Blueprint("hello_world_bp", __name__)
board_bp = Blueprint("board_bp", __name__, url_prefix="/boards")
memo_bp = Blueprint("memo_bp", __name__, url_prefix="/cards")


####--------------- HELLO WORLD ---------------####
@hello_world_bp.route("/hello-world", methods=["GET"])
def say_hello_world():
    return "Hello, World 🤖!"

####--------------- TODO: BOARD ROUTES ---------------####

####--------------- TODO: MEMO ROUTES ---------------####

