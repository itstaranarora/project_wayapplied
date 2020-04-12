from flask import Blueprint, jsonify
from ..model import Websites

admin = Blueprint("admin", __name__, url_prefix="/api/admin")

# Get All Websites
@admin.route("/getAll", methods=["GET"])
def getAll():
    websites = Websites().all()
    if not websites:
        return jsonify({"msg": "table is emptey"})
    else:
        return jsonify(websites)

@admin.route("/toggleStatus/<int:id>", methods=["PUT"])
def toggleStatus(id):
    return (jsonify(Websites().toggleStatus(id)))

#Delete a websites
@admin.route("/deleteById/<int:id>", methods=["DELETE"])
def deleteWebsite(id):
    return jsonify(Websites().deleteById(id))

# Get Published Websites
@admin.route("/getPublished", methods=["GET"])
def Published():
    published_websites = Websites().allByStatus()
    if not published_websites:
        return jsonify({"msg": "table is emptey"})
    else:
        return jsonify(published_websites)


# Get Unpublished Websites
@admin.route("/getUnpublished", methods=["GET"])
def Unpublished():
    unpublished_websites = Websites().allByStatus(False)
    if not unpublished_websites:
        return jsonify({"msg": "table is emptey"})
    else:
        return jsonify(unpublished_websites)
