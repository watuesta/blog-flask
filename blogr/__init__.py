from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():

    # Crear aplicacion
    app = Flask(__name__)
    app.config.from_object('config.Config')
    db.init_app(app)

    from flask_ckeditor import CKEditor
    ckeditor = CKEditor(app)

    import locale
    locale.setlocale(locale.LC_ALL, 'es_ES')
    
    # Registrar blueprints
    from blogr import home
    app.register_blueprint(home.bp)

    from blogr import auth
    app.register_blueprint(auth.bp)

    from blogr import post
    app.register_blueprint(post.bp)

    from .models import User, Post
    # Me permite migrar todos los modelos a la bd
    with app.app_context():
        db.create_all()

    return app