from decouple import config

SERVER_PORT = config("SERVER_PORT", default=5000, cast=int)
APP_SETTINGS = config("APP_SETTINGS", default="app.config.DevelopmentConfig")
