from flask import Flask, request, render_template, send_file, make_response

import dates_sorter
from dates_sorter import *


#todo create tests for flask_integration

app = Flask(__name__)
#todo: logger should produce files
log_filename = 'flask_integration.log'
logging.basicConfig(filename=log_filename, level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

#route for web interface

@app.route('/', methods=['POST','GET'])
def index():
    app.logger.info("Accessed the index route.")  # Log this event
    return render_template('index.html')

# route to handle the file upload

@app.route('/upload', methods=['POST','GET'])
def upload_file():
    app.logger.info("Received a request to upload a file.")

    if 'file' not in request.files:
        app.logger.error("No file part in the request.")
        return "No file part"

    uploaded_file = request.files['file']

    if uploaded_file.filename == '':
        app.logger.error("No selected file.")
        return "No selected file"
#todo each file should be saved as a new one(timestamp for example, input file name, tells if it's sorted, timestamp)
    if uploaded_file:
        sorted_file_path = 'sorted_output.txt'  # Define the path for the sorted output file
        # Process the file using script
        dates_sorter.sort_text_by_dates(uploaded_file, sorted_file_path)

        response = make_response(send_file(sorted_file_path))
        response.headers['Content-Type'] = 'application/octet-stream'
        response.headers['Content-Disposition'] = f'attachment; filename={os.path.basename(sorted_file_path)}'

        app.logger.info("File processed successfully and sent as a response.")
        return response


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)

#SO TURNS OUT BEING A 0.0.0.0 PORT MAkES IT UNAVALIABLE TO ACCES THAT LOCALLY
#if __name__ == "__main__":
 #   app.run(host='0.0.0.0', port=8080, debug=True)
