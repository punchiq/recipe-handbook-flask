from flask import Blueprint, abort, render_template

from core.models import recipes


pages = Blueprint("recipes", __name__)



@pages.get("/recipes")
@pages.get("/")
def index():
    return render_template("recipes/index.html", items=recipes())


@pages.get("/recipes/<slug>")
@pages.get("/recipe/<slug>")
def detail(slug):
    recipe = next((item for item in recipes() if item["slug"] == slug), None)
    if recipe is None:
        abort(404)
    return render_template("recipes/detail.html", recipe=recipe)

