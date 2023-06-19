from models.base import Base
from sqlalchemy import Column, Integer, String, LargeBinary

import cv2
import numpy as np

class Img(Base):
    __tablename__ = "Img"
    id = Column(Integer, primary_key=True)
    img = Column(LargeBinary, unique=False, nullable=False)
    name = Column(String, nullable=False)
    mimetype = Column(String, nullable=False) 

    def __repr__(self):
        # Convert the blob to a NumPy array
        blob_array = np.frombuffer(self.img, dtype=np.uint8)
        
        # Decode the blob array as an image
        image = cv2.imdecode(blob_array, cv2.IMREAD_COLOR)
        return f"{image}"