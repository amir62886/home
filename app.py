from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///DB.db'
app.app_context().push()
db = SQLAlchemy (app)

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)   
    name = db.Column(db.String, nullable=False)
    price = db.Column(db.Float)   
    description = db.Column(db.String)   
    imageName = db.Column(db.String) 
      
@app.route("/")   
def home():
    products = Product.query.all()
    return render_template("homePage.html", products = products)

@app.route("/product/<int:id>")
def product(id):
    product = Product.query.get(id)
    return render_template("product.html", product = product)

@app.route("/addproduct", methods=['GET', 'POST'])
def addproduct():
    if request.method == 'GET':
        return render_template ("addproduct.html")  
    else:
        name = request.form['name']
        price = request.form['price']
        description = request.form['description']
        imageName = request.form['imageName']
        product = Product(name = name, price = price, description = description, imageName = imageName)
        db.session.add(product)
        db.session.commit()
        return redirect("/") 
    
@app.route("/product/<int:id>/delete")
def deleteproduct(id):
    product = Product.query.get(id)
    db.session.delete(product)
    db.session.commit()
    return redirect("/")


    
@app.route("/about")
def about():
    return "О нас"