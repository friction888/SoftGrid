from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from app import db
from models import Bookmark, Group

bookmarks_bp = Blueprint('bookmarks', __name__)

@bookmarks_bp.route('/', methods=['GET'])
@jwt_required()
def get_bookmarks():
    """Get all bookmarks for current user"""
    user_id = get_jwt_identity()
    bookmarks = Bookmark.query.filter_by(user_id=user_id).order_by(Bookmark.order).all()
    
    return jsonify([{
        'id': b.id,
        'title': b.title,
        'url': b.url,
        'icon': b.icon,
        'group_id': b.group_id,
        'order': b.order
    } for b in bookmarks]), 200

@bookmarks_bp.route('/', methods=['POST'])
@jwt_required()
def create_bookmark():
    """Create a new bookmark"""
    user_id = get_jwt_identity()
    data = request.get_json()
    
    if not data or not data.get('title') or not data.get('url'):
        return jsonify({'error': 'Title and URL are required'}), 400
    
    # Verify group belongs to user if provided
    if data.get('group_id'):
        group = Group.query.filter_by(id=data['group_id'], user_id=user_id).first()
        if not group:
            return jsonify({'error': 'Group not found'}), 404
    
    bookmark = Bookmark(
        user_id=user_id,
        title=data['title'],
        url=data['url'],
        icon=data.get('icon'),
        group_id=data.get('group_id'),
        order=data.get('order', 0)
    )
    
    db.session.add(bookmark)
    db.session.commit()
    
    return jsonify({'id': bookmark.id, 'message': 'Bookmark created'}), 201

@bookmarks_bp.route('/<int:bookmark_id>', methods=['GET'])
@jwt_required()
def get_bookmark(bookmark_id):
    """Get a specific bookmark"""
    user_id = get_jwt_identity()
    bookmark = Bookmark.query.filter_by(id=bookmark_id, user_id=user_id).first()
    
    if not bookmark:
        return jsonify({'error': 'Bookmark not found'}), 404
    
    return jsonify({
        'id': bookmark.id,
        'title': bookmark.title,
        'url': bookmark.url,
        'icon': bookmark.icon,
        'group_id': bookmark.group_id
    }), 200

@bookmarks_bp.route('/<int:bookmark_id>', methods=['PUT'])
@jwt_required()
def update_bookmark(bookmark_id):
    """Update a bookmark"""
    user_id = get_jwt_identity()
    bookmark = Bookmark.query.filter_by(id=bookmark_id, user_id=user_id).first()
    
    if not bookmark:
        return jsonify({'error': 'Bookmark not found'}), 404
    
    data = request.get_json()
    
    bookmark.title = data.get('title', bookmark.title)
    bookmark.url = data.get('url', bookmark.url)
    bookmark.icon = data.get('icon', bookmark.icon)
    bookmark.group_id = data.get('group_id', bookmark.group_id)
    bookmark.order = data.get('order', bookmark.order)
    
    db.session.commit()
    return jsonify({'message': 'Bookmark updated'}), 200

@bookmarks_bp.route('/<int:bookmark_id>', methods=['DELETE'])
@jwt_required()
def delete_bookmark(bookmark_id):
    """Delete a bookmark"""
    user_id = get_jwt_identity()
    bookmark = Bookmark.query.filter_by(id=bookmark_id, user_id=user_id).first()
    
    if not bookmark:
        return jsonify({'error': 'Bookmark not found'}), 404
    
    db.session.delete(bookmark)
    db.session.commit()
    
    return jsonify({'message': 'Bookmark deleted'}), 200
