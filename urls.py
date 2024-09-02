from flask import Blueprint

from views import add_task, get_task, delete, update

bp = Blueprint('app', __name__)


@bp.route("/add_task", methods=['POST'])
def add_task_route():
    return add_task()


@bp.route("/get_task", methods=['GET'])
def get_task_route():
    return get_task()


@bp.route("/delete_task", methods=['DELETE'])
def delete_task_route():
    return delete()


@bp.route("/update_task/<string:old_title>")
def update_task_rout():
    return update()

