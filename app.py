from flask import Flask

from routes.ingredients import ingredients
from routes.recipes import pages

app = Flask(__name__)
app.register_blueprint(pages)
app.register_blueprint(ingredients)
