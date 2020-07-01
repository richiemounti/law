from flask import (
    Blueprint,
    flash,
    redirect,
    render_template,
    url_for
)
from app.admin.forms import BlogForm
from app.models import Blog, Category
from app import db
from flask_login import login_required

admin = Blueprint('admin', __name__)

@admin.before_request
@login_required
def require_login():
    pass


@admin.route('/admin')
@admin.route('/admin/index')
def index():
    blog_items = Blog.query.all()
    return render_template('admin/index.html',
                            blog_items=blog_items,
                            title="blog items"
                            )

@admin.route('/admin/new', methods=['GET', 'POST'])
def new():
    categories = Category.query.all()
    form = BlogForm()
    form.category_id.choices = [(c.id, c.name) for c in categories]

    if form.validate_on_submit():
        blog_items = Blog()
        form.populate_obj(blog_items)
        db.session.add(blog_items)
        db.session.commit()
        flash('New blog created!', 'success')
        return redirect(url_for('admin.index'))

    return render_template('admin/new.html',
                            form=form,
                            title="Blog items"
                            )


@admin.route('/admin/edit/<id>', methods=['GET', 'POST'])
def edit(id):
    blog_items = Blog.query.filter_by(id=id).first_or_404()
    categories = Category.query.all()
    form = BlogForm(obj=blog_items)
    form.category_id.choices = [
        (m.id, m.name) for m in categories
    ]

    if form.validate_on_submit():
        form.populate_obj(blog_items)
        db.session.add(blog_items)
        db.session.commit()
        flash('Blog items updated')
        return redirect(url_for('admin.index'))

    categories = Category.query.all()   

    return render_template('admin/edit.html',
                            form=form,
                            title="Blog items"
                            )



@admin.route('/details/<id>')
def details(id):
    blog_items = Blog.query.filter_by(id=id).first_or_404()

    return render_template('admin/details.html',
                            blog_items=blog_items,
                            title="Blog items"
                            )