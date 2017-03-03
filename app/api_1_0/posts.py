from . import api
from .authentication import auth
from flask import jsonify, g, request, url_for, current_app
from ..models import Post, Permission
from .decorators import permission_required
from .. import db
from errors import forbidden



@api.route('/posts/')
@auth.login_required
def get_posts():
    page = request.args.get('page', 1, type=int)
    pagination = Post.query.paginate(page,
                                     per_page=current_app.config['PW_POSTS_PER_PAGE='],
                                     error_out=False)
    posts = pagination.items
    prev = None
    if pagination.has_prev:
        prev = url_for('api.get_posts', page=page-1, _external=True)
    next = None
    if pagination.has_next:
        next = url_for('api.get_posts', page=page+1, _external=True)
    return jsonify({'prev': prev,
                    'next': next,
                    'count': pagination.total,
                    'posts': [post.to_json() for post in posts]
                    })


@api.route('/post/<int:id>')
@auth.login_required
def get_post(id):
    post = Post.query.get_or_404(id)
    return jsonify({'post': post.to_json()})


@permission_required(Permission.WRITE_ARTICLES)
@api.route('/posts/', methods=['POST'])
def new_post():
    post = Post.from_json(request.json)
    post.author = g.current_user
    db.session.add(post)
    db.session.commit()
    return jsonify(post.to_json()), 201, \
                {'Location': url_for('api.get_post', id=post.id, _external=True)}


@permission_required(Permission.WRITE_ARTICLES)
@api.route('/post/<int:id>', methods=['PUT'])
def edit_post(id):
    post = Post.query.get_or_404(id)
    if post.author != g.current_user and not g.current_user.can(Permission.ADMINISTER):
        return forbidden('Insufficient permissions')
    post.body = request.json.get('body', post.body)
    db.session.add(post)
    db.session.commit()
    return jsonify(post.to_json())


















