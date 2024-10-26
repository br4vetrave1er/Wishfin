from flask import Blueprint,Flask
from profile import register_blueprint

app = Flask(__name__)
app.secret_key = "temp secret key"
register_blueprint(app)



if __name__ == "__main__":
    app.run(debug=True)



