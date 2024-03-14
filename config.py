import os

class Config(object):
    #資料庫設定
    print("config connected")
    SQLALCHEMY_DATABASE_URI = "sqlite:///app.db"
    SQLALCHEMY_TRACK_MODIFICATIONS = False