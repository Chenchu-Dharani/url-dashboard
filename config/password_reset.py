# config/password_reset.py - Password reset services
# Replace the URLs below with your own internal password reset tools

PASSWORD_RESET = [
    {
        "name": "SSO Password Reset",
        "url": "https://your-sso.example.com/forgot-password",
        "image": "static/logos/logo.svg",
        "icon": "📄"
    },
    {
        "name": "VPN / Corporate Password Reset",
        "url": "https://your-idp.example.com/password-reset/",
        "image": "static/logos/logo.svg",
        "icon": "📄"
    },
]
