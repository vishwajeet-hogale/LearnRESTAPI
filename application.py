from flask import Flask,request
from flask_sqlalchemy import SQLAlchemy
import json

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
# app.config['SECRET_KEY'] = "aidbaibdadi3jrlwnfnsdkcnkdabcbkdsnlv"

db = SQLAlchemy(app)


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
@app.route("/drinks/<int:id>")
def get_drink(id):
    drink = Drinks.query.get_or_404(id)
    return {"name":drink.name,"description":drink.description}
@app.route("/drink",methods=["POST"])
def add_drink():
    drink = Drinks(name= str(request.json["name"]),description=str(request.json["desc"]))
    db.session.add(drink)
    db.session.commit()
    return {'id':drink.id}
@app.route("/drinks/<id>",methods=["DELETE"])
def delete_drink(id):
    drink = Drinks.query.get(id)
    if drink is None:
        return {"Error":"Not Found"}
    db.session.delete(drink)
    db.session.commit()
    return {"message":"Deleted"}
if __name__ == "__main__":
    db.create_all()
    app.run(debug=True)