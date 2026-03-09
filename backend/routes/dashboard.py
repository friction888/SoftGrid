from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from app import db
from models import User, Group, Bookmark, Widget, UserSettings

dashboard_bp = Blueprint('dashboard', __name__)

@dashboard_bp.route('/', methods=['GET'])
@jwt_required()
def get_dashboard():
    """Get dashboard data for current user"""
    user_id = get_jwt_identity()
    user = User.query.get(user_id)
    
    if not user:
        return jsonify({'error': 'User not found'}), 404
    
    # Fetch all dashboard data
    groups = Group.query.filter_by(user_id=user_id).order_by(Group.order).all()
    bookmarks = Bookmark.query.filter_by(user_id=user_id).all()
    widgets = Widget.query.filter_by(user_id=user_id).order_by(Widget.order).all()
    settings = UserSettings.query.filter_by(user_id=user_id).first()
    
    return jsonify({
        'groups': [serialize_group(g) for g in groups],
        'bookmarks': [serialize_bookmark(b) for b in bookmarks],
        'widgets': [serialize_widget(w) for w in widgets],
        'settings': serialize_settings(settings) if settings else None
    }), 200

def serialize_group(group):
    return {
        'id': group.id,
        'name': group.name,
        'color': group.color,
        'order': group.order
    }

def serialize_bookmark(bookmark):
    return {
        'id': bookmark.id,
        'title': bookmark.title,
        'url': bookmark.url,
        'icon': bookmark.icon,
        'group_id': bookmark.group_id,
        'order': bookmark.order
    }

def serialize_widget(widget):
    return {
        'id': widget.id,
        'widget_type': widget.widget_type,
        'config': widget.config,
        'position_x': widget.position_x,
        'position_y': widget.position_y,
        'width': widget.width,
        'height': widget.height,
        'enabled': widget.enabled
    }

def serialize_settings(settings):
    return {
        'theme': settings.theme,
        'auto_save': settings.auto_save,
        'sidebar_position': settings.sidebar_position,
        'sidebar_width': settings.sidebar_width,
        'sidebar_collapsible': settings.sidebar_collapsible,
        'grid_columns': settings.grid_columns,
        'custom_settings': settings.custom_settings
    }
