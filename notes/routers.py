from flask import render_template, request, redirect, url_for,Blueprint,flash
from models import Note, db

notes_bp = Blueprint("notes", __name__)





@notes_bp.route("/note_created/<title_note>/<content_note>")
def note_created(title_note, content_note):
    return render_template("note_created.html", title=title_note, content=content_note)


@notes_bp.route("/create-note", methods=["GET", "POST"])
def create_note():
    if request.method == "POST":
        note_title = request.form.get("title", "No title provided")
        note_content = request.form.get("content", "No content provided")
        if not note_title:
            return "Title is required", 400
        if not note_content:
            return "Content is required", 400
        note_db = Note(title=note_title, content=note_content)
        db.session.add(note_db)
        db.session.commit()
        flash("Created note", "success")
        return redirect(
            url_for(
                "notes.note_created", title_note=note_db.title, content_note=note_db.content
            )
        )
    else:
        return render_template("notes_form.html", title="Create Note")


@notes_bp.route("/edit-note/<int:note_id>", methods=["GET", "POST"])
def edit_note(note_id):
    note = Note.query.get_or_404(note_id)
    if request.method == "POST":
        note.title = request.form.get("title", note.title)
        note.content = request.form.get("content", note.content)
        db.session.commit()
        return redirect(url_for("index"))
    else:
        return render_template("edit_notes_form.html", note=note)


@notes_bp.route("/delete-note/<int:note_id>", methods=["GET", "POST"])
def delete_note(note_id):
    note = Note.query.get_or_404(note_id)
    if request.method == "POST":
        db.session.delete(note)
        db.session.commit()
        return redirect(url_for("index"))
    else:
        return render_template("delete_note.html", note=note)
