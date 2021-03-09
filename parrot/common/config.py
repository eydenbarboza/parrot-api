

class BaseConfig(object):
    DEBUG = True


class DevelopmentConfig(BaseConfig):
    DEBUG = True
    POSTGRES_USER = "parrot"
    POSTGRES_PASSWORD = "parrot2021"
    POSTGRES_HOST = "postgres"
    POSTGRES_DB = "parrot"
    DEFAULT_EMAIL = "eyden.barboza@gmail.com"
    SECRET_KEY = 'secretkeydev'
   

class ProductionConfig(BaseConfig):
    DEBUG = False
    POSTGRES_USER = "parrot"
    POSTGRES_PASSWORD = "parrot2021"
    POSTGRES_HOST = "postgres"
    POSTGRES_DB = "parrot"
    DEFAULT_EMAIL = "eyden.barboza@gmail.com"
    SECRET_KEY = 'secretkeydev'



#get by environment variable
environment = eval("DevelopmentConfig")
