import os

class Config:  
    SECRET_KEY = "EWYFD87"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    UPLOADED_PHOTOS_DEST ='app/static/photos'

# simple mde  configurations
    SIMPLEMDE_JS_IIFE = True
    SIMPLEMDE_USE_CDN = True
    @staticmethod
    def init_app(app):
        pass


class ProdConfig(Config):
    pass

class TestConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:root@localhost:5432/shopapp_test'

class DevConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:root@localhost:5432/shopapp'
    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig,
'test':TestConfig

}
