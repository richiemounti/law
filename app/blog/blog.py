from app import db
from app.models import Blog, Category

from flask import (
    Blueprint,
    render_template,
    session
)

blog = Blueprint('blog', __name__)

@blog.route('/insights', defaults={'id': None})
@blog.route('/insights/<int:id>')
@blog.route('/insights/index', defaults={'id': None})
@blog.route('/insights/index/<int:id>')
def index(id):
    if id is None:
        blog_items_query = Blog.query
        current_category = '----'
    else:
        blog_items_query = Blog.query.filter_by(category_id=id)
        current_category = Category.query.filter_by(id=id).first_or_404().name
    
    blog_items = blog_items_query \
        .order_by(Blog.title.desc())
    categories = Category.query.order_by(Category.name.desc())
    
    return render_template('insights/index.html',
                            title = 'Insights',
                            blog_items= blog_items,
                            categories=categories,
                            current_category=current_category
                            )