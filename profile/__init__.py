from .router import router

def register_blueprint(app):
    app.register_blueprint(router)