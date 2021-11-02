from flask import jsonify, abort, request, Blueprint
from requests import api
from datasource import data, genderize

API = Blueprint('api', __name__)


def get_blueprint():
    """Return the blueprint for the main app module"""
    return API


# adding datasource
data_source = "https://reqres.in/"

source = data.DataSource(data_source)

# adding lookup api
gender = genderize.GenderStatistics()


@API.route("/registered-members", methods=["GET"])
def get_members():
    """
    Return all registered members
    @return: 200: an array of all registered members as a \
    flask/response object.
    """
    result_set = source.get_all_users()
    print(result_set)
    return jsonify(result_set)


@API.route("/registered-members/<int:id>", methods=["GET"])
def get_registered_member(id):
    """
    Get registered member details by their id
    @param _id: the id
    @return: 200: registered member detail as a flask/response object.
    @raise 404: if the id is not found
    """
    if source.check_for_registered_user(id) is False:
        return abort(404)
    result_set = source.get_single_user(id)
    return result_set


@API.route("/statistical-information", methods=["GET"])
def get_statistical_information():
    """
    Return all registered members
    @return: 200: statical information of all registered members as a \
    flask/response object with application/json mimetype.
    """
    names = source.get_all_users_names()
    result_set = gender.get_names_gender_statistics(names)
    print(result_set)
    return result_set
