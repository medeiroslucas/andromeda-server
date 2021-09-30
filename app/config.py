class BaseConfig:
    """Base configuration"""

    TESTING = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevelopmentConfig(BaseConfig):
    """Development configuration"""

    DEBUG = True


class ProductionConfig(BaseConfig):
    DEBUG = False
