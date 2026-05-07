from backend.db.database import Base, engine
from backend import models

print("Creating database tables...")

Base.metadata.create_all(bind=engine)

print("Database initialized successfully!")