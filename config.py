
class config:
    SECRET_KEY='rocketscoders2022'
    
class DevelopmentConfig(config):
    DEBUG=True
    
config={
    "development":DevelopmentConfig,
    "default":DevelopmentConfig
}
    