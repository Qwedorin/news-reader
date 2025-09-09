from sqlalchemy import Column, String, Text, Integer, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.db import Base

class DataSource(Base):
    __tablename__ = "data_sources"
    
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    type: Mapped[str] = mapped_column(String(50))
    
    __mapper_args__ = {
        "polymorphic_identity": "data_source",
        "polymorphic_on": type,
    }
    
    user_id: Mapped[int] = mapped_column(Integer, ForeignKey("users.id"), nullable=False)
    
    user = relationship("User", back_populates="data_sources")
    rules = relationship("Rule", back_populates="data_source")

class Website(DataSource):
    __tablename__ = "websites"
    
    id: Mapped[int] = mapped_column(Integer, ForeignKey("data_sources.id"), primary_key=True)
    url: Mapped[str] = mapped_column(String, nullable=False)
    xpath: Mapped[str] = mapped_column(String, nullable=False)
    
    __mapper_args__ = {
        "polymorphic_identity": "website",
    }

class MinifluxRSSFeed(DataSource):
    __tablename__ = "miniflux_rss_feeds"
    
    id: Mapped[int] = mapped_column(Integer, ForeignKey("data_sources.id"), primary_key=True)
    miniflux_id: Mapped[int] = mapped_column(Integer, nullable=False)
    api_key: Mapped[str] = mapped_column(String, nullable=False)
    url: Mapped[str] = mapped_column(String, nullable=False)
    
    __mapper_args__ = {
        "polymorphic_identity": "miniflux_rss_feed",
    }
