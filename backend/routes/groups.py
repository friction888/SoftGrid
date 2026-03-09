from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from app import db
from models import Group

groups_bp = Blueprint('groups', __name__)

@groups_bp.route('/', methods=['GET'])
@jwt_required()
def get_groups():
    """Get all groups for current user"""
    user_id = get_jwt_identity()
    groups = Group.query.filter_by(user_id=user_id).order_by(Group.order).all()
    
    return jsonify([{
        'id': g.id,
        'name': g.name,
        'color': g.color,
        'order': g.order
    } for g in groups]), 200

@groups_bp.route('/', methods=['POST'])
@jwt_required()
def create_group():
    """Create a new group"""
    user_id = get_jwt_identity()
    data = request.get_json()
    
    if not data or not data.get('name'):
        return jsonify({'error': 'Group name is required'}), 400
    
    group = Group(
        user_id=user_id,
        name=data['name'],
        color=data.get('color', '#3B82F6'),
        order=data.get('order', 0)
    )
    
    db.session.add(group)
    db.session.commit()
    
    return jsonify({'id': group.id, 'message': 'Group created'}), 201

@groups_bp.route('/<int:group_id>', methods=['GET'])
@jwt_required()
def get_group(group_id):
    """Get a specific group"""
    user_id = get_jwt_identity()
    group = Group.query.filter_by(id=group_id, user_id=user_id).first()
    
    if not group:
        return jsonify({'error': 'Group not found'}), 404
    
    return jsonify({
        'id': group.id,
        'name': group.name,
        'color': group.color,
        'order': group.order
    }), 200

@groups_bp.route('/<int:group_id>', methods=['PUT'])
@jwt_required()
def update_group(group_id):
    """Update a group"""
    user_id = get_jwt_identity()
    group = Group.query.filter_by(id=group_id, user_id=user_id).first()
    
    if not group:
        return jsonify({'error': 'Group not found'}), 404
    
    data = request.get_json()
    
    group.name = data.get('name', group.name)
    group.color = data.get('color', group.color)
    group.order = data.get('order', group.order)
    
    db.session.commit()
    return jsonify({'message': 'Group updated'}), 200

@groups_bp.route('/<int:group_id>', methods=['DELETE'])
@jwt_required()
def delete_group(group_id):
    """Delete a group"""
    user_id = get_jwt_identity()
    group = Group.query.filter_by(id=group_id, user_id=user_id).first()
    
    if not group:
        return jsonify({'error': 'Group not found'}), 404
    
    db.session.delete(group)
    db.session.commit()
    
    return jsonify({'message': 'Group deleted'}), 200
