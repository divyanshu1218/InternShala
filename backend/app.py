from flask import Flask, jsonify
from backend.config import Config
from backend.extensions import mongo, jwt, bcrypt, cors
from backend.routes.auth import auth_bp
from backend.routes.dashboard import dashboard_bp
from backend.routes.video import video_bp

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    # Initialize Extensions
    mongo.init_app(app)
    jwt.init_app(app)
    bcrypt.init_app(app)
    cors.init_app(app)

    # Register Blueprints
    app.register_blueprint(auth_bp, url_prefix='/auth')
    app.register_blueprint(dashboard_bp, url_prefix='/dashboard')
    app.register_blueprint(video_bp, url_prefix='/video')

    @app.route('/')
    def index():
        return jsonify({"message": "API-First Video App Backend is Running"}), 200

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True, host='0.0.0.0', port=5000)
