##OPEN API STUFF
OPENAI_API_KEY = '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'



## FLASK STUFF
class Config(object):
    DEBUG = True
    TESTING = False

class DevelopmentConfig(Config):
    SECRET_KEY = "this-is-a-super-secret-key"


config = {
    'development': DevelopmentConfig,
    'testing': DevelopmentConfig,
    'production': DevelopmentConfig
}
