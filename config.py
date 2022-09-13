
class config:
    SECRET_KEY='rocketscoders2022'
    
class DevelopmentConfig(config):
    DEBUG=True
    MYSQL_HOST='localhost'
    MYSQL_USER='root'
    MYSQL_PASSWORD='admin'
    MYSQL_DB='tienda_comics'
    
config={
    "development":DevelopmentConfig,
    "default":DevelopmentConfig
}
    