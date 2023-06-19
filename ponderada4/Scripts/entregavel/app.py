from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
import os

from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker

from models.base import Base
from models.img import Img

engine = create_engine("sqlite+pysqlite:///img.db", echo=True)
Session = sessionmaker(bind=engine)
session = Session()
Base.metadata.create_all(engine)

app = Flask(__name__)


@app.route('/', methods=["GET","POST"])
def index():
    return render_template('index.html')

@app.route('/manda', methods=["GET","POST"])
def manda_imagem():
    imagem = request.files['img']
    name = secure_filename(imagem.filename)
    filetype = imagem.mimetype

    img = Img(img=imagem, name=name, mimetype=filetype)
    session.add(img)
    session.commit()

    return 'enviou'

if __name__ == '__main__':
    app.run(debug=True)