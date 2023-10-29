from flask import Flask, request, render_template, send_file, make_response
from datetime import datetime
import dates_sorter
from dates_sorter import *



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

@app.route('/upload', methods=['POST'])
def upload_file():
    app.logger.info("Received a request to upload a file.")

    if 'file' not in request.files:
        app.logger.error("No file part in the request.")
        return "No file part"

    uploaded_file = request.files['file']

    if uploaded_file.filename == '':
        app.logger.error("No selected file.")
        return "No selected file"

    if uploaded_file:
        sorted_file_path = 'sorted_output.txt'  # Define the path for the sorted output file

        # Process the file using the modified script
        dates_sorter.sort_text_by_dates(uploaded_file, sorted_file_path)

        # Add the creation date to the processed file
        creation_date = datetime.now().strftime("Created at: %Y-%m-%d %H:%M:%S")
        with open(sorted_file_path, 'a', encoding='utf-8') as file:
            file.write("\n" + creation_date)

        response = make_response(send_file(sorted_file_path))
        response.headers['Content-Type'] = 'application/octet-stream'
        response.headers['Content-Disposition'] = f'attachment; filename={os.path.basename(sorted_file_path)}'

        app.logger.info("File processed successfully and sent as a response.")
        return response

    @app.route('/process')
    def process_file():
        # Simulate processing a file
        # Replace this with your actual file processing logic
        processed_timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        return f"File processed at: {processed_timestamp}"


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)

#SO TURNS OUT BEING A 0.0.0.0 PORT MAkES IT UNAVALIABLE TO ACCES THAT LOCALLY
#if __name__ == "__main__":
 #   app.run(host='0.0.0.0', port=8080, debug=True)
