
class config:
    SECRET_KEY = 'rocketscoders2022'


class DevelopmentConfig(config):
    DEBUG = True
    MYSQL_HOST = 'localhost'
    MYSQL_USER = 'root'
    MYSQL_PASSWORD = 'admin'
    MYSQL_DB = 'tienda_comics'
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = 'rocketcoders2022@gmail.com'
    MAIL_PASSWORD = 'rocket.2022'


config = {
    "development": DevelopmentConfig,
    "default": DevelopmentConfig
}
