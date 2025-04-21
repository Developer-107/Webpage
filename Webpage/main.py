import os
from flask import Flask, abort, render_template, redirect, url_for, flash, request
from flask_bootstrap import Bootstrap5
from flask_ckeditor import CKEditor
from flask_login import UserMixin, login_user, LoginManager, current_user, logout_user

app = Flask(__name__)
app.config['SECRET_KEY'] =  -- Your Secret Key Here --
ckeditor = CKEditor(app)
Bootstrap5(app)

@app.route('/')
def home():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact", methods=["GET", "POST"])
def contact():
    return render_template("contact.html")


if __name__ == "__main__":
    app.run(debug=False, port=5005)
