from flask import Blueprint, jsonify
from ..model import Websites

admin = Blueprint("admin", __name__, url_prefix="/api/admin")

# Get All Websites
@admin.route("/websites", methods=["GET"])
def getAll():
    return jsonify(Websites().all())

# Get Website by Id from all
@admin.route("/website/<int:id>", methods=['GET'])
def getWebsite(id):
    return jsonify(Websites().getWebsiteById(id))

# Change Website Status
@admin.route("/website/<int:id>/toggle-status", methods=["PUT"])
def toggleStatus(id):
    return (jsonify(Websites().toggleStatus(id)))

#Delete a website
@admin.route("/website/<int:id>/delete", methods=["DELETE"])
def deleteWebsite(id):
    return jsonify(Websites().deleteById(id))

# Get Published Websites
@admin.route("/websites/published", methods=["GET"])
def Published():
    return jsonify(Websites().allByStatus())


# Get Unpublished Websites
@admin.route("websites/unpublished", methods=["GET"])
def Unpublished():
    return jsonify(Websites().allByStatus(False))
