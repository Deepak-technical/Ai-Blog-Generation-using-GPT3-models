##OPEN API STUFF
OPENAI_API_KEY ='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'



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
