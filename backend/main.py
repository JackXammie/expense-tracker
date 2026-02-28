from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from sqlalchemy import create_engine, Column, Integer, String, Float, DateTime
from sqlalchemy.orm import sessionmaker, declarative_base
from datetime import datetime

# ---------------- DATABASE CONFIG ----------------

DATABASE_URL = "mysql+pymysql://expense_user:expensepass@127.0.0.1:3306/expense_tracker"

engine = create_engine(
    DATABASE_URL,
    pool_pre_ping=True
)

SessionLocal = sessionmaker(bind=engine)

Base = declarative_base()

# ---------------- DATABASE MODEL ----------------

class ExpenseDB(Base):
    __tablename__ = "expenses"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False)
    amount = Column(Float, nullable=False)
    notes = Column(String(500))
    date = Column(DateTime, default=datetime.utcnow)

Base.metadata.create_all(bind=engine)

# ---------------- Pydantic SCHEMA ----------------

class ExpenseCreate(BaseModel):
    name: str
    amount: float
    notes: str | None = None

# ---------------- APP ----------------

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return {"message": "Backend is running with MySQL 🚀"}

@app.get("/expenses")
def get_expenses():
    with SessionLocal() as db:
        return db.query(ExpenseDB).all()

@app.post("/expenses")
def add_expense(expense: ExpenseCreate):
    with SessionLocal() as db:
        new_expense = ExpenseDB(
            name=expense.name,
            amount=expense.amount,
            notes=expense.notes,
            date=datetime.utcnow()
        )
        db.add(new_expense)
        db.commit()
        db.refresh(new_expense)
        return new_expense

@app.delete("/expenses/{expense_id}")
def delete_expense(expense_id: int):
    with SessionLocal() as db:
        expense = db.query(ExpenseDB).filter(ExpenseDB.id == expense_id).first()
        if not expense:
            raise HTTPException(status_code=404, detail="Expense not found")
        db.delete(expense)
        db.commit()
        return {"message": "Deleted successfully"}