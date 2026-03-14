from sqlalchemy.orm import sessionmaker, Session

# engine
# sesson
SessionLocal = sessionmaker()


def get_session():
    try:
        session: Session = SessionLocal()
        yield session
    except StopIteration:
        session.close()
