from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from app import db
from models import UserSettings

settings_bp = Blueprint('settings', __name__)

@settings_bp.route('/', methods=['GET'])
@jwt_required()
def get_settings():
    """Get user settings"""
    user_id = get_jwt_identity()
    settings = UserSettings.query.filter_by(user_id=user_id).first()
    
    if not settings:
        # Create default settings
        settings = UserSettings(user_id=user_id)
        db.session.add(settings)
        db.session.commit()
    
    return jsonify({
        'theme': settings.theme,
        'auto_save': settings.auto_save,
        'sidebar_position': settings.sidebar_position,
        'sidebar_width': settings.sidebar_width,
        'sidebar_collapsible': settings.sidebar_collapsible,
        'grid_columns': settings.grid_columns,
        'custom_settings': settings.custom_settings
    }), 200

@settings_bp.route('/', methods=['PUT'])
@jwt_required()
def update_settings():
    """Update user settings"""
    user_id = get_jwt_identity()
    settings = UserSettings.query.filter_by(user_id=user_id).first()
    
    if not settings:
        settings = UserSettings(user_id=user_id)
        db.session.add(settings)
    
    data = request.get_json()
    
    settings.theme = data.get('theme', settings.theme)
    settings.auto_save = data.get('auto_save', settings.auto_save)
    settings.sidebar_position = data.get('sidebar_position', settings.sidebar_position)
    settings.sidebar_width = data.get('sidebar_width', settings.sidebar_width)
    settings.sidebar_collapsible = data.get('sidebar_collapsible', settings.sidebar_collapsible)
    settings.grid_columns = data.get('grid_columns', settings.grid_columns)
    settings.custom_settings = data.get('custom_settings', settings.custom_settings)
    
    db.session.commit()
    return jsonify({'message': 'Settings updated'}), 200
