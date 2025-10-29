SQLITE = "sqlite:///project.db"
POSTGRESQL = "postgresql+psycopg2://postgres:Atu.911012@localhost:5432/blogposts_db"

class Config:
    DEBUG = False
    SECRET_KEY = 'dev-will'
    SQLALCHEMY_DATABASE_URI = POSTGRESQL
    CKEDITOR_PKG_TYPE = 'full'