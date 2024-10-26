from flask import Blueprint,render_template, request,redirect, url_for, flash
from .reader import dropdown_options,save_to_csv

router = Blueprint("router", __name__)


@router.route("/", methods=["GET"])
def home():
    options = dropdown_options()
    return render_template("homepage.html", cities=options)


@router.route("/submit", methods=["POST"])
def submit():
    name = request.form.get("name")
    city = request.form.get("city_id")

    if not name or not city:
        # error = "City and Name must be selected"
        flash(" City and Name must be selected ")
        return redirect(url_for("router.home"))

    user_data = {
        "id": city,
        "name": name
    }
    return save_to_csv(user_data)
    # return "hello"
