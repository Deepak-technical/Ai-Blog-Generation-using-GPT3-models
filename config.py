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
