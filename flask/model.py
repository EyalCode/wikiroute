from config import db

# Create table(model)
class Links(db.Model):
    _key = db.Column("key", db.Integer, primary_key=True)
    from_id = db.Column(db.Integer)
    to_id = db.Column(db.Integer)

    def __init__(self, from_id, to_id):
        self.from_id = from_id
        self.to_id = to_id