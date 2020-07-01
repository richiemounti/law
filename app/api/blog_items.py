from app.api import api
from app import db
from app.decorators import admin_required
from app.models import Blog
from flask import (
    jsonify,
    request
)
from flask_login import login_required
from sqlalchemy import func


@api.route('/api/blogitems', defaults={'query':None})
@login_required
@admin_required
def get_blog_items(query):
    query = request.args.get('query')
    blog_item_query = Blog.query

    if query:
        blog_item_query = \
            blog_item_query.filter(func.lower(Blog.first_title).contains(func.lower(query)) |
                                      func.lower(Blog.last_title).contains(func.lower(query)))
    
    blog_items = blog_item_query.all()
    res = jsonify([blog_item.to_dict() for blog_item in blog_items])

    return res


@api.route('/api/blogitems/<id>', methods=['DELETE'])
@login_required
@admin_required
def delete_blog_items(id):
    Blog.filter_by(id=id).delete()
    db.session.commit()

    res = jsonify({'data': 'success'})

    return res, 204