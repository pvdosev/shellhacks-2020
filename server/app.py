from flask import Flask, request, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import os

# Bootstrap the application and hook up to the database

app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + os.path.join(basedir,'db.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
ma = Marshmallow(app)

# Database models

class Medication(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    barcode_id = db.Column(db.String(255), unique=True)
    description = db.Column(db.String(255))

    def __repr__(self):
        return '<Medication %r>' % self.barcode_id

# Marshmallow schemas

class MedicationSchema(ma.SqlAlchemySchema):
    class Meta:
        model = Medication

    id = ma.auto_field()
    barcode_id = ma.auto_field()
    description = ma.auto_field()

# App Routes

@app.route('/')
def index():
    return render_template('index.html')


# Get barcode from the client and query the database to return the medicine
@app.route('/barcode/', methods=['POST'])
def query_barcode():
    if request.method == 'POST':
        barcode_id = request.json["barcode_id"]
        description = request.json["description"]
        return jsonify(name=name, ingredients=ingredients)


if __name__=="__main__":
    app.run(debug=True)