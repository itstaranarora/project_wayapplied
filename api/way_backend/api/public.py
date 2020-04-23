from flask import Blueprint, jsonify, request
from ..model import Websites

public = Blueprint("public", __name__, url_prefix="/api/public")


@public.route("/submit/website", methods=["POST"])
def submit():
    email = request.json["email"]
    name = request.json["name"]
    url = request.json["url"]
    description = request.json["description"]
    category_id = request.json["category_id"]
    args = [name, url, email, description, category_id]
    result = Websites().add(*args)
    return jsonify(result)

# Get Published Website
@public.route("/website/<int:id>", methods=['GET'])
def getWebsite(id):
    return jsonify(Websites().getWebsite(id))

# Get Website Categories
@public.route("/websites/categories", methods=['GET'])
def categories(): 
    return jsonify(Websites().getCategories())
