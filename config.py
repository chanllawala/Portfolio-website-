import os
import secrets
from typing import Optional


def _env_bool(key: str, default: bool = True) -> bool:
    value = os.environ.get(key)
    if value is None:
        return default
    return value.strip().lower() in {"1", "true", "t", "yes", "y"}


class Config:
    """Base configuration loaded from environment variables."""

    # Application settings
    SECRET_KEY = os.environ.get("SECRET_KEY", secrets.token_hex(32))
    DEBUG = _env_bool("DEBUG", False)
    TESTING = _env_bool("TESTING", False)

    # Email settings
    MAIL_SERVER: Optional[str] = os.environ.get("MAIL_SERVER")
    MAIL_PORT: int = int(os.environ.get("MAIL_PORT", 587))
    MAIL_USE_TLS: bool = _env_bool("MAIL_USE_TLS", True)
    MAIL_USERNAME: Optional[str] = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD: Optional[str] = os.environ.get("MAIL_PASSWORD")
    MAIL_DEFAULT_RECIPIENT: Optional[str] = os.environ.get("MAIL_DEFAULT_RECIPIENT")

    # Rate limiting
    RATELIMIT_DEFAULT = os.environ.get("RATELIMIT_DEFAULT", "200 per day, 50 per hour")
    RATELIMIT_CONTACT = os.environ.get("RATELIMIT_CONTACT", "5 per hour")

    @classmethod
    def validate(cls) -> list[str]:
        """Validate configuration and return list of errors."""
        errors = []

        if not cls.SECRET_KEY:
            errors.append("SECRET_KEY is required")

        if not cls.MAIL_SERVER:
            errors.append("MAIL_SERVER is required")

        if not cls.MAIL_USERNAME:
            errors.append("MAIL_USERNAME is required")

        if not cls.MAIL_PASSWORD:
            errors.append("MAIL_PASSWORD is required")

        if not cls.MAIL_DEFAULT_RECIPIENT:
            errors.append("MAIL_DEFAULT_RECIPIENT is required")

        return errors


class DevelopmentConfig(Config):
    """Development configuration."""

    DEBUG = True
    SECRET_KEY = "dev-secret-key"

    # Use dummy email settings for development
    MAIL_SERVER = "localhost"
    MAIL_PORT = 1025
    MAIL_USE_TLS = False
    MAIL_USERNAME = "dev@example.com"
    MAIL_PASSWORD = "dev"
    MAIL_DEFAULT_RECIPIENT = "dev@example.com"


class ProductionConfig(Config):
    """Production configuration."""

    DEBUG = False
    SECRET_KEY = os.environ.get("SECRET_KEY")

    @classmethod
    def validate(cls) -> list[str]:
        """Validate production configuration."""
        errors = super().validate()

        if not cls.SECRET_KEY or cls.SECRET_KEY == "your-secret-key-here":
            errors.append("Production SECRET_KEY must be set to a secure value")

        return errors


class TestingConfig(Config):
    """Testing configuration."""

    TESTING = True
    SECRET_KEY = "test-secret-key"
    WTF_CSRF_ENABLED = False

    # Use test email settings
    MAIL_SERVER = "localhost"
    MAIL_PORT = 1025
    MAIL_USE_TLS = False
    MAIL_USERNAME = "test@example.com"
    MAIL_PASSWORD = "test"
    MAIL_DEFAULT_RECIPIENT = "test@example.com"


# Configuration selector
def get_config() -> type[Config]:
    """Get configuration class based on environment."""
    env = os.environ.get("FLASK_ENV", "development").lower()

    if env == "production":
        return ProductionConfig
    elif env == "testing":
        return TestingConfig
    else:
        return DevelopmentConfig
