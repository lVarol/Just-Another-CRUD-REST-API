from flask import Flask, request, jsonify
import os




def create_app():
    app = Flask(__name__)

    app.config.from_mapping(

        DATABASE_HOST = os.environ.get('FLASK_DATABASE_HOST'),
        DATABASE_PASSWORD= os.environ.get('FLASK_DATABASE_PASSWORD'),
        DATABASE_USER= os.environ.get('FLASK_DATABASE_USER'),
        DATABASE= os.environ.get('FLASK_DATABASE'),
        SECRET_KEY=os.environ.get('SECRET_KEY')

    )

    import db

    import todo

    app.register_blueprint(todo.bp) 

    db.init_app(app)

    return app