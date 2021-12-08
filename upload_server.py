import time
from io import BufferedReader
from pathlib import PurePosixPath
import os
from tempfile import NamedTemporaryFile, TemporaryDirectory, gettempdir
from flask import Flask, render_template, request
app = Flask(__name__)


@app.route('/upload')
def upload_file():
    '''
    path_to_template = os.path.join(PurePosixPath(os.path.realpath(__file__)).parent, 'upload.html')
    print(path_to_template)
    return render_template(path_to_template)
    '''
    return render_template('upload.html')
	
@app.route('/uploader', methods = ['GET', 'POST'])
def uploader_file():
    if request.method == 'POST':
        image = request.files.get('file')
        image.name = image.filename
        image = BufferedReader(image)
        output_path = os.path.join(gettempdir(), 'r-n-c-b-testing-' + str(time.time_ns()) )
        print("About to write to " + output_path)
        with open(output_path, 'wb') as output_file:
            output_file.write(image.read())

        return 'file uploaded successfully'
		
if __name__ == '__main__':
   app.run(debug = True)
