from app.db.connection import Session

def get_db_session():
    session = Session()
    try:
        yield session
    finally:
        session.close()