from app import db

class Board(db.Model):
    board_id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String)
    owner = db.Column(db.String)
    memo = db.relationship("Card", back_populates="board", lazy=True)

    def board_json(self):
        return {
            "id": self.board_id,
            "title": self.title,
            "owner": self.owner
        }

    def all_memos_json(self):
        memo_list = []
        for memo in self.memo:
            memo_list.append(memo.memo_json())
        return{
            "id": self.board_id,
            "title": self.title,
            "owner": self.owner,
            "memos": memo_list
        }