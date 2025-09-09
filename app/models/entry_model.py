from datetime import datetime
from sqlalchemy import Column, String, Text, Integer, ForeignKey, DateTime
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.db import Base

class RSSEntry(Base):
    __tablename__ = "entries"
    
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    title: Mapped[str] = mapped_column(String, nullable=False)
    link: Mapped[str] = mapped_column(String, nullable=False)
    pub_date: Mapped[datetime] = mapped_column(DateTime(timezone=True), nullable=False)
    retrieval_date: Mapped[datetime] = mapped_column(DateTime(timezone=True), nullable=False)
    reasoning: Mapped[str] = mapped_column(Text, nullable=True)
    
    rule_id: Mapped[int] = mapped_column(Integer, ForeignKey("rules.id"), nullable=False)
    
    rule = relationship("Rule", back_populates="entries")
