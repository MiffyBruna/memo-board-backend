from email.policy import default
from app import db

class Memo(db.Model):
    memo_id = db.Column(db.Integer, primary_key=True)
    message = db.Column(db.String)
    likes_count = db.Column(db.Integer, default = 0)
    board_id = db.Column(db.Integer, db.ForeignKey('board.board_id'))
    board = db.relationship("Board", back_populates="memo", lazy=True)

    def memo_json(self):
        return {
            "memo_id": self.card_id,
            "message": self.message,
            "likes_count": self.likes_count
        }