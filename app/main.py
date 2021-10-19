# save this as app.py
from flask import Flask, request
from flask import send_file
import qrcode
from io import BytesIO
import werkzeug
from werkzeug.wrappers import response

app = Flask(__name__)


@app.route("/")
@app.errorhandler(werkzeug.exceptions.BadRequest)
def generateqrcode():
    try:
        data = request.args.get('text')
        qr = qrcode.QRCode(
            version=None,
            box_size=10,
            border=2)
        qr.add_data(data)
        qr.make(fit=True)
        fill = request.args.get('fill') or 'black'
        back_color= request.args.get('back_color') or 'white'
        img = qr.make_image(fill_color=fill, back_color=back_color)
        return serve_pil_image(img)
    except:
        return {"message":'bad request! Check value of fill and back_color queries'}, 400

def serve_pil_image(pil_img):
    img_io = BytesIO()
    pil_img.save(img_io, 'JPEG', quality=70)
    img_io.seek(0)
    return send_file(img_io, mimetype='image/jpeg')

@app.errorhandler(werkzeug.exceptions.BadRequest)
@app.route("/<string:data>")
def generateqr(data):
    try:
        qr = qrcode.QRCode(
            version=None,
            box_size=10,
            border=2)
        qr.add_data(data)
        qr.make(fit=True)
        fill = request.args.get('fill') or 'black'
        back_color= request.args.get('back_color') or 'white'
        img = qr.make_image(fill_color=fill, back_color=back_color)
        return serve_pil_image(img)
    except:
        return {"message":'bad request! Check value of fill and back_color queries'}, 400

