from shopee import app
from flask import get_flashed_messages, render_template, url_for, request, redirect, flash
from shopee.models import Products, Courses

# app.config["SQL"]

products = [
    {
        "pid": 1, "name": "apple", "origin": "HongKong",
        "description": "big red apple", "quantity": 10,
        "unit_price": "6.0"
    }
]


@app.route("/")
def home():
    return render_template(
        "home.html"
    )


@app.route('/products')
def index_products():

    return render_template(
        'index.html',
        rows=Products.query.all()
    )



@app.route('/products/<int:pid>')
def products_detail(pid):

    return render_template(
        'details.html',
        info=Products.query.filter_by(pid=pid).first()
    )

@app.route("/courses/")
def index_courses():
    message = get_flashed_messages()
    if message:
        flash(message)
    return render_template(
        "courses/courses.html"
    )


@app.route("/courses/<int:c_id>/")
def course_details(c_id):
    return render_template(
        "courses/course_details.html",
        info=Courses.query.filter_by(c_id)
    )


@app.route("/courses/add")
def add_course():
    return render_template(
        "courses/create.html"
    )
@app.route("/courses/edit")
def edit_course():
    return render_template(
        "courses/edit.html"
    )


@app.route("/courses/delete")
def delete_course():
    return "Course Succesfulley oofed."
