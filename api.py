from flask import Flask
import random
from flask import jsonify, request
from PIL import Image
from io import BytesIO
app = Flask(__name__)


@app.route("/infer", methods=['POST'])
def infer():
    try:
        image = request.files.get('image')
        if image:
            im = Image.open(BytesIO(image.read()))
            print(im.width, im.height)
            output = {'success': True,'result': bool(random.getrandbits(1)), "shape": {'width': im.width,
                                                                                        'height': im.height}}
            return jsonify(output)
        else:
            return jsonify({'error': 'Image not found'})
    except Exception as e:
        return jsonify({'error': '{}'.format(e)})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=4201)