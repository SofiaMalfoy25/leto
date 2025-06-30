from app import db

class Review(db.Model):
    __tablename__ = 'reviews'
    
    id = db.Column(db.Integer, primary_key=True)
    author = db.Column(db.String(100), nullable=False)
    rating = db.Column(db.Integer, nullable=False)  # 1-5
    text = db.Column(db.Text, nullable=False)
    date = db.Column(db.DateTime, default=datetime.utcnow)
    tour_id = db.Column(db.Integer, db.ForeignKey('tours.id'))
    likes = db.Column(db.Integer, default=0)

class Tour(db.Model):
    __tablename__ = 'tours'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150), nullable=False)
    description = db.Column(db.Text)
    price = db.Column(db.Float)
    duration = db.Column(db.String(50))
    image = db.Column(db.String(100))
    
    reviews = db.relationship('Review', backref='tour', lazy=True)