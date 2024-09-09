import os

class Config:
    # データベースの接続設定
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:example@db/flaskdb?charset=utf8mb4'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    DEBUG = True  # デバッグモードを有効にする
    SECRET_KEY='your_secret_key'