from flask import Flask, abort, render_template

from catalog import recipes

app = Flask(__name__)


@app.get("/")
def index():
    return render_template("index.html", items=recipes())


@app.get("/recipes/<slug>")
def detail(slug):
    recipe = next((item for item in recipes() if item["slug"] == slug), None)
    if recipe is None:
        abort(404)
    return render_template("recipe.html", recipe=recipe)

