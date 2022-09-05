from ast import Pass
from distutils.debug import DEBUG


class config:
    Pass
    
class DevelopmentConfig(config):
    DEBUG=True
    
config={
    "development":DevelopmentConfig,
    "default":DevelopmentConfig
}
    