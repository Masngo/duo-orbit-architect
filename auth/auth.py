def authenticate_user(token):
    if token == "valid_token":
        return {"user": "demo_user"}
    return None# auth/auth.py

# Simulated token database (for demo purposes)
VALID_TOKENS = {
    "valid_token": {
        "user": "demo_user",
        "role": "developer"
    },
    "admin_token": {
        "user": "admin_user",
        "role": "admin"
    }
}

def authenticate_user(token):
    """
    Simulates token-based authentication.

    Args:
        token (str): authentication token

    Returns:
        dict or None: user info if valid, otherwise None
    """

    user_data = VALID_TOKENS.get(token)

    if user_data:
        return {
            "authenticated": True,
            "user": user_data["user"],
            "role": user_data["role"]
        }

    return {
        "authenticated": False,
        "user": None,
        "role": None
    }