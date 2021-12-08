import time
from io import BufferedReader
from pathlib import PurePosixPath
import os
from tempfile import NamedTemporaryFile, TemporaryDirectory, gettempdir
from flask import Flask, render_template, request
#from werkzeug import secure_filename
app = Flask(__name__)

def secure_filename(fname):
    return fname

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
        import pprint
        print(pprint.pprint(dir(image)))
        output_path = os.path.join(gettempdir(), 'r-n-c-b-testing-' + str(time.time_ns()) )
        print("About to write to " + output_path)
        with open(output_path, 'wb') as output_file:
            output_file.write(image.read())

        '''
        f = request.files['file']
        print(type(f))
        ff = NamedTemporaryFile(delete=False, prefix='r-n-c-b-testing-')
        import pprint
        print(pprint.pprint(dir(ff)))
        print(ff.name)
        f.save(secure_filename(f.name))
        '''
        return 'file uploaded successfully'
		
if __name__ == '__main__':
   app.run(debug = True)
