from flask import request
from fridgio import app, couch

@app.route("/", methods=["GET"])
def main():
    return "main"

@app.route("/recipe/<recipe>", methods=["GET"])
def get_user(recipe):
    if request.method == "GET":
        document = couch[recipe]
        ingredients = "\n".join(
            ["%s: %s" % (k,v) for k,v in document["ingredients"].items()]
        )
        return ingredients

@app.route("/new_recipe", methods=["POST"])
def add_user():
    if request.method == "POST":
        recipe = request.json
        print(type(recipe))
        recipe_name = recipe["name"]
        document = dict(
            name=recipe_name,
            ingredients={
                "mince": "250gr",
                "onions": "1",
                "tomato": "5",
            }
        )
        id = recipe_name.replace(" ", "_")
        print("ID: ", id)
        couch[id] = document
        return recipe_name + " added"
