from app.model.database import engine
from app.model.db_model import Base
from app.model.db_model import Product, ElectronicProduct, BookProduct, ClothingProduct

def init_db():

    Base.metadata.create_all(bind=engine)

if __name__ == "__main__":
    init_db()
