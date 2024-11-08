class Config(object):
    pass

class ProdConfig(Config):
    pass

class DevConfig(Config):   #Activa que el servidor se active en modo DEBUG o modo Desarrollo 
    DEBUG = True   #Existe el modo Producción que es cuando el proyecto ya está listo para ser usado por los usuarios