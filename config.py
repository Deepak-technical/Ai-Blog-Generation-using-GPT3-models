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
