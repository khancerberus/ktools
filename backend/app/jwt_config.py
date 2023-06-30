from app import jwt

from app.auth.models import User


@jwt.user_identity_loader
def user_identity_lookup(user):
    return user.public_id


@jwt.user_lookup_loader
def user_lookup_callback(_jwt_header, jwt_data):
    identity = jwt_data['sub']
    return User.get_by_public_id(identity)


@jwt.additional_claims_loader
def add_claims_to_access_token(identity):
    user: User = User.get_by_public_id(identity)
    if user is None:
        return {}
    return {
        'user': {
            'username': user.login_name,
            'profile_image_url': user.profile_image_url,
            'authorized_apps': [
                token.token_type.name
                for token in user.tokens
            ]
        }
    }
