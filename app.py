from flask import Flask, abort, request
from flask_cors import CORS, cross_origin
import cv2
app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route('/')
def serve_form():
    to_serve = '''<html><body>
                        <form id="upload-file" method="post" enctype="multipart/form-data">
                                <label for="file">Select a file</label>
                                <input name="file" type="file">
                                <button id="upload-file-btn" type="button">Upload</button>
                        </form>
                        <img id='updateMe' src='' />
                        <script src="https://code.jquery.com/jquery-2.x-git.min.js"></script>
                    </body>
                    </html>'''
    return to_serve

@cross_origin()
@app.route('/upload', methods = ['GET', 'POST'])
def upload_file():
   if request.method == 'POST':
      f = request.files['file']
      print f.filename
      if f.content_type == 'image/jpeg' or f.content_type == 'image/jpg' or f.content_type == 'image/png':
          f.save('/tmp/' + f.filename)
          image = cv2.imread('/tmp/' + f.filename)
          gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
          cv2.imwrite('/tmp/' + f.filename.split('.jpg')[0] + '_modified.jpg', gray_image)
          with open('/tmp/' + f.filename.split('.jpg')[0] + '_modified.jpg', 'rb') as file:
              if (f.content_type == 'image/jpeg' or f.content_type == 'image/jpg'):
                ff = 'data:image/jpeg;base64,' + file.read().encode("base64")
              elif (f.content_type == 'image/png'):
                  ff = 'data:image/png;base64,' + file.read().encode("base64")
              return ff
      else:
          abort(400)
          
if __name__=="__main__": app.run('0.0.0.0', 5001)
