from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase

from app.config import settings

# Neon (serverless PostgreSQL) uchun muhim sozlamalar:
# pool_pre_ping  → har ulanishdan oldin DB tirik ekanini tekshiradi
# pool_recycle   → 5 daqiqada bir ulanishni yangilaydi (Neon ulanishni o'chirmasligi uchun)
# pool_size      → parallel ulanishlar soni
engine = create_engine(
    settings.DATABASE_URL,
    pool_pre_ping=True,
    pool_recycle=300,
    pool_size=5,
    max_overflow=2,
)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine,
)


class Base(DeclarativeBase):
    pass
