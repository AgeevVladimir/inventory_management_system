from app.database.database import engine
from app.database.model import Base
from app.database.model import Product, ElectronicProduct, BookProduct, ClothingProduct

def init_db():

    print("Starting DB Initialization...")
    connection = engine.connect()
    print("Connected to DB:", connection)
    Base.metadata.create_all(bind=engine)
    print("DB Initialization Done!")

if __name__ == "__main__":
    init_db()
