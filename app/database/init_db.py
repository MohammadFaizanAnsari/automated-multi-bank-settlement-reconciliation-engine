from app.database.database import Base
from app.database.database import engine

from app.models import *

Base.metadata.create_all(bind=engine)

print("Database tables created successfully.")