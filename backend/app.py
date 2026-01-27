from flask import Flask, jsonify
from backend.config import Config
from backend.extensions import init_extensions
from backend.routes.auth import auth_bp

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    # Initialize Flask extensions
    init_extensions(app)

    # Register Blueprints
    app.register_blueprint(auth_bp, url_prefix='/auth')

    @app.route('/health')
    def health_check():
        return jsonify({'status': 'healthy', 'service': 'backend-api'}), 200

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True, host='0.0.0.0', port=5000)
