from fastapi import FastAPI, Depends
from pydantic import BaseModel
from sqlalchemy import create_engine, Column, Integer, String, DateTime
from sqlalchemy.orm import sessionmaker, declarative_base, Session
from datetime import datetime



# ------------------ DATABASE ------------------
DATABASE_URL = "sqlite:///./crm.db"

engine = create_engine(
    DATABASE_URL, connect_args={"check_same_thread": False}
)

SessionLocal = sessionmaker(bind=engine)
Base = declarative_base()

# ------------------ MODELS ------------------
class User(Base):
    _tablename_ = "users"
    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True)
    role = Column(String, default="manager")


class Client(Base):
    _tablename_ = "clients"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    phone = Column(String)
    created_at = Column(DateTime, default=datetime.utcnow)


# ------------------ SCHEMAS ------------------
class ClientCreate(BaseModel):
    name: str
    phone: str


class ClientResponse(ClientCreate):
    id: int
    created_at: datetime

    class Config:
        from_attributes = True


# ------------------ APP ------------------
app = FastAPI(title="crm (One File)")

Base.metadata.create_all(bind=engine)

# ------------------ DEPENDENCY ------------------
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# ------------------ ROUTES ------------------
@app.post("/clients", response_model=ClientResponse)
def create_client(client: ClientCreate, db: Session = Depends(get_db)):
    db_client = Client(
        name=client.name,
        phone=client.phone
    )
    db.add(db_client)
    db.commit()
    db.refresh(db_client)
    return db_client


@app.get("/clients", response_model=list[ClientResponse])
def get_clients(db: Session = Depends(get_db)):
    return db.query(Client).all()


