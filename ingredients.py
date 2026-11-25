from flask import Blueprint, render_template, request

from catalog import recipes

ingredients = Blueprint("ingredients", __name__)


@ingredients.get("/ingredients")
def search():
    query = request.args.get("q", "").strip()
    items = recipes()
    if query:
        items = [item for item in items if any(
            query.casefold() in line.split(" — ")[0].casefold()
            for line in item["ingredients"]
        )]
    return render_template("search.html", items=items, query=query)

