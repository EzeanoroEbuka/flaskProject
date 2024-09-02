from flask import request, jsonify

from models import task_list


def add_task():
    data = request.get_json()
    title = data.get('title')
    description = data.get('content')
    email = data.get('user_email')
    if verify_title(title):
        return jsonify({"message": "Task Already Exist"}), 400
    else:
        task_list.task.insert_one({'title': title, 'content': description, 'user_email': email})
        return jsonify({"message": "success"}), 201


def get_task():
    data = request.get_json()
    title = data.get('title')
    if verify_title(title):
        found_task = task_list.task.find_one({"title": title})
        found_task.pop('_id', None)
        return jsonify(found_task), 202
    else:
        return jsonify({"message": "Title Not Found"}), 400


def delete():
    data = request.get_json()
    title = data.get('title')
    if verify_title(title):
        found_task = task_list.task.find_one({"title": title})
        task_list.task.delete_one(found_task)
        return jsonify({"message": "successfully Deleted"}), 202
    else:
        return jsonify({"message": "Title Not Found"}), 400


def update(old_title):
    data = request.get_json()
    title = data.get('title')
    content = data.get('content')
    if verify_title(old_title):
        found_title = task_list.task.find_one({"title": old_title})
        task_list.task.update_one(found_title, {"$set": {'title': title, 'content': content}})
        return jsonify({"message": "Updated successfully"}), 200
    else:
        return jsonify({"message": "Title Not Found"}), 400


def email_exists(userEmail) -> bool:
    pass


def allTask(userEmail):
    if email_exists(userEmail):
        all_task = []
        all_task = task_list.task.find({"user_email": userEmail})
        return all_task
    else:
        return jsonify({"message": "Email does not Exist"}), 400


def verify_title(title) -> bool:
    existing_title = task_list.task.find_one({"title": title})
    if existing_title is not None:
        return True
    else:
        return False
