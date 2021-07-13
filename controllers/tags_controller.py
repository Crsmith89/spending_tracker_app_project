from flask import Flask, render_template, request, redirect
from flask import Blueprint

from models.tag import Tag

import repositories.tag_repository as tag_repository

tags_blueprint = Blueprint("tags", __name__)

# get tags '/tags'
@tags_blueprint.route("/tags")
def tags():
    tags = tag_repository.select_all()
    return render_template("tags/index.html", tags = tags)
    
# Get tags new
@tags_blueprint.route("/tags/new")
def new_tag():
    return render_template("tags/new.html")

# Create - Post
@tags_blueprint.route("/tags", methods=["POST"])
def create_tag():
    name = request.form["name"]
    description = request.form["description"]
    new_tag = Tag(name, description)
    tag_repository.save(new_tag)
    return redirect("/tags")

# Show - Get
@tags_blueprint.route("/tags/<id>")
def show_tag(id):
    tag = tag_repository.select(id)
    return render_template("tags/show.html", tag = tag)

# Edit
@tags_blueprint.route("/tags/<id>/edit")
def edit_tag(id):
    tag = tag_repository.select(id)
    return render_template("tags/edit.html", tag = tag)

# Update
@tags_blueprint.route("/tags/<id>", methods=["POST"])
def update_tag(id):
    name = request.form["name"]
    description = request.form["description"]
    tag = Tag(name, description, id)
    tag_repository.update(tag)
    return redirect("/tags")

# Delete
@tags_blueprint.route("/tags/<id>/delete", methods=["POST"])
def delete_tag(id):
    tag_repository.delete(id)
    return redirect("/tags")

