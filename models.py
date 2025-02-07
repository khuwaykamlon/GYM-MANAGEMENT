class Class(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    instructor = db.Column(db.String(80), nullable=False)
    time = db.Column(db.String(50), nullable=False)
    available_slots = db.Column(db.Integer, nullable=False)  # Max capacity
