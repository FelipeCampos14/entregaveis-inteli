from models.base import Base
from sqlalchemy import Column, Integer, String, LargeBinary

class Img(Base):
    __tablename__ = "Img"
    id = Column(Integer, primary_key=True)
    img = Column(LargeBinary, unique=False, nullable=False)
    name = Column(String, nullable=False)
    mimetype = Column(String, nullable=False) 

    def __repr__(self) -> str:
        return f"jogos(id={self.id}, mimytyep ={self.mimetype})"