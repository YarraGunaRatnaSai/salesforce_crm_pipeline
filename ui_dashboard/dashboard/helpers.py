import json
from flask import request

def get_request_json():
    """
    Helper function to safely parse JSON data from request.
    """
    try:
        return request.get_json()
    except Exception as e:
        return {'error': 'Invalid JSON', 'message': str(e)}

def get_user_data_from_session(session):
    """
    Helper function to retrieve user data from the session.
    """
    user_data = session.get('user', None)
    if not user_data:
        return None
    return user_data
