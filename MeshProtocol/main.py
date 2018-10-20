from flask import Flask
from Routes import API


app = Flask(__name__)
app.register_blueprint(API.mod)

app.run(debug=True)