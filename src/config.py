class Config:
    SECRET_KEY = 'B!378nsda08da¨3*3'
    
class DevelopmentConfig(Config):
    DEBUG=True
    MYSQL_HOST = 'localhost'
    MYSQL_USER = 'root'
    MYSQL_PASSWORD = ''
    MYSQL_DB = 'redsocial'
    
config = {
    'development': DevelopmentConfig
}