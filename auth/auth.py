def authenticate_user(token):
    if token == "valid_token":
        return {"user": "demo_user"}
    return None