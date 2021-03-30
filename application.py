from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import json
#  from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SECRET_KEY'] = "aidbaibdadi3jrlwnfnsdkcnkdabcbkdsnlv"

db = SQLAlchemy(app)
# db = SQLAlchemy()
# def create_app():
#     app = Flask(__name__)
#     db.init_app(app)

#     return app 
# app = create_app()

# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'


class Drinks(db.Model):
    id = db.Column(db.Integer,primary_key = True)
    name = db.Column(db.String(80),unique=True,nullable=False)
    description = db.Column(db.String(120))
    def __repr__(self):
        return f"{self.name} - {self.description}"
    


@app.route("/")
def index():
    
    return "Hello"
@app.route("/drinks")
def get_drinks():
 
    drinks = Drinks.query.all()
    op = []
    for d in drinks:
        drink_data = {"name":d.name,"description":d.description}
        op.append(drink_data)
    return {"drinks":op}
if __name__ == "__main__":
    db.create_all()
    app.run(debug=True)