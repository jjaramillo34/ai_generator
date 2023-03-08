from decouple import config
from dotenv import load_dotenv

load_dotenv()

class Config(object):
    DEBUG = True
    TESTING = False
    LANGUAGES = ['en', 'es']

class DevelopmentConfig(Config):
    SECRET_KEY = "this-is-a-super-secret-key"

configure = {
    'development': DevelopmentConfig,
    'testing': DevelopmentConfig,
    'production': DevelopmentConfig
}

## Enter your Open API Key here
OPENAI_API_KEY = config('OPENAI_API_KEY')
