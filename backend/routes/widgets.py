from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from app import db
from models import Widget

widgets_bp = Blueprint('widgets', __name__)

@widgets_bp.route('/', methods=['GET'])
@jwt_required()
def get_widgets():
    """Get all widgets for current user"""
    user_id = get_jwt_identity()
    widgets = Widget.query.filter_by(user_id=user_id).order_by(Widget.order).all()
    
    return jsonify([{
        'id': w.id,
        'widget_type': w.widget_type,
        'config': w.config,
        'position_x': w.position_x,
        'position_y': w.position_y,
        'width': w.width,
        'height': w.height,
        'enabled': w.enabled
    } for w in widgets]), 200

@widgets_bp.route('/', methods=['POST'])
@jwt_required()
def create_widget():
    """Create a new widget"""
    user_id = get_jwt_identity()
    data = request.get_json()
    
    if not data or not data.get('widget_type'):
        return jsonify({'error': 'Widget type is required'}), 400
    
    widget = Widget(
        user_id=user_id,
        widget_type=data['widget_type'],
        config=data.get('config', {}),
        position_x=data.get('position_x', 0),
        position_y=data.get('position_y', 0),
        width=data.get('width', 2),
        height=data.get('height', 2),
        enabled=data.get('enabled', True)
    )
    
    db.session.add(widget)
    db.session.commit()
    
    return jsonify({'id': widget.id, 'message': 'Widget created'}), 201

@widgets_bp.route('/<int:widget_id>', methods=['GET'])
@jwt_required()
def get_widget(widget_id):
    """Get a specific widget"""
    user_id = get_jwt_identity()
    widget = Widget.query.filter_by(id=widget_id, user_id=user_id).first()
    
    if not widget:
        return jsonify({'error': 'Widget not found'}), 404
    
    return jsonify({
        'id': widget.id,
        'widget_type': widget.widget_type,
        'config': widget.config,
        'position_x': widget.position_x,
        'position_y': widget.position_y,
        'width': widget.width,
        'height': widget.height,
        'enabled': widget.enabled
    }), 200

@widgets_bp.route('/<int:widget_id>', methods=['PUT'])
@jwt_required()
def update_widget(widget_id):
    """Update a widget"""
    user_id = get_jwt_identity()
    widget = Widget.query.filter_by(id=widget_id, user_id=user_id).first()
    
    if not widget:
        return jsonify({'error': 'Widget not found'}), 404
    
    data = request.get_json()
    
    widget.widget_type = data.get('widget_type', widget.widget_type)
    widget.config = data.get('config', widget.config)
    widget.position_x = data.get('position_x', widget.position_x)
    widget.position_y = data.get('position_y', widget.position_y)
    widget.width = data.get('width', widget.width)
    widget.height = data.get('height', widget.height)
    widget.enabled = data.get('enabled', widget.enabled)
    
    db.session.commit()
    return jsonify({'message': 'Widget updated'}), 200

@widgets_bp.route('/<int:widget_id>', methods=['DELETE'])
@jwt_required()
def delete_widget(widget_id):
    """Delete a widget"""
    user_id = get_jwt_identity()
    widget = Widget.query.filter_by(id=widget_id, user_id=user_id).first()
    
    if not widget:
        return jsonify({'error': 'Widget not found'}), 404
    
    db.session.delete(widget)
    db.session.commit()
    
    return jsonify({'message': 'Widget deleted'}), 200
