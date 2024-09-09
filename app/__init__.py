from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from app.config import Config
from flask_migrate import Migrate
from flask_wtf.csrf import CSRFProtect

db = SQLAlchemy()
migrate = Migrate() 
csrf = CSRFProtect()

def create_app():
    app = Flask(__name__)
    app.config.from_object('app.config.Config')

    # db を初期化
    db.init_app(app)
    migrate.init_app(app, db)
    csrf.init_app(app)
    
    # 必要なタイミングでブループリントやモデルをインポート
    from app.views.customer_view import customer_blueprint
    from app.views.history_view import history_blueprint 

    app.register_blueprint(customer_blueprint)
    app.register_blueprint(history_blueprint) 

    # アプリケーションコンテキスト内でテーブルを作成
    with app.app_context():
        db.create_all()

    return app
