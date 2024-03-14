from app import db
print("models connected")
class User(db.Model):
    
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    password = db.Column(db.String(20), nullable=False)
    email = db.Column(db.String(25), unique=True, nullable=False)
    
    # testAccount >>> user = User(username="Jack", password="123", email="x@gmail.com")
    
    def __repr__(self):
        return f"<User: {self.username}>"