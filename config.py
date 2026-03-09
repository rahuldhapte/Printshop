class Config:
    SECRET_KEY = "supersecret"
    UPLOAD_FOLDER = "uploads"
    MAX_CONTENT_LENGTH = 50 * 1024 * 1024
    
    SQLALCHEMY_DATABASE_URI = "sqlite:///printshop.db"
    SQLALCHEMY_TRACK_MODIFICATIONS = False