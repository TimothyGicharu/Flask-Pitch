from flask import render_template, url_for, flash, redirect, request, abort, Blueprint
from flask_login import current_user, login_required
from pitch import db
from pitch.models import Post
from pitch.pitches.forms import PitchForm


pitches = Blueprint('pitches', __name__)


@pitches.route('/pitch/new', methods=['GET', 'POST'])
@login_required
def new_pitch():
    form = PitchForm()
    if form.validate_on_submit():
        post = Post(title=form.title.data, content=form.content.data,
                    category=form.category.data, author=current_user)
        db.session.add(post)
        db.session.commit()
        flash('Your post has been created!', 'success')
        return redirect(url_for('home'))
    return render_template('create_pitch.html', title='New Pitch', form=form, legend='Create Pitch')


@pitches.route('/pitch/<int:post_id>')
def pitch(post_id):
    pitch = Post.query.get_or_404(post_id)
    return render_template('post.html', title=pitch.title, pitch=pitch)


@pitches.route('/pitch/<int:post_id>/update', methods=['GET', 'POST'])
@login_required
def update_pitch(post_id):
    pitch = Post.query.get_or_404(post_id)
    if pitch.author != current_user:
        abort(403)
    form = PitchForm()
    if form.validate_on_submit():
        pitch.title = form.title.data
        pitch.content = form.content.data
        pitch.category = form.category.data
        db.session.commit()
        flash('Your post has been updated!', 'success')
        return redirect(url_for('pitch', post_id=pitch.id))
    elif request.method == 'GET':
        form.title.data = pitch.title
        form.content.data = pitch.content
        form.category.data = pitch.category
    return render_template('create_pitch.html', title='Update Pitch',
                           form=form, legend='Update Post')


@pitches.route('/pitch/<int:post_id>/delete', methods=['POST'])
@login_required
def delete_pitch(post_id):
    pitch = Post.query.get_or_404(post_id)
    if pitch.author != current_user:
        abort(403)
    db.session.delete(pitch)
    db.session.commit()
    flash('Pitch deleted', 'success')
    return redirect(url_for('home'))
