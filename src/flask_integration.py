from flask import Flask, request, render_template, send_file, make_response
import os
from datetime import datetime
import dates_sorter
from dates_sorter import *


app = Flask(__name__)



@app.route('/', methods=['POST','GET'])
def index():
    return render_template('index.html')


# Define a route to handle the file upload
@app.route('/upload', methods=['POST','GET'])
def upload_file():
    uploaded_file = request.files['file']

    if uploaded_file:
        # Save the uploaded file
        file_path = 'uploads/' + uploaded_file.filename
        uploaded_file.save(file_path)

        # Process the file
        lines = dates_sorter.read_lines_from_file(file_path, encoding='utf-8')
        date_line_dict = group_lines_by_dates(lines)
        sorted_lines = sort_and_flatten_groups(date_line_dict)
        sorted_file_path = 'sorted_output.txt'
        write_lines_to_file(sorted_lines, sorted_file_path, encoding='utf-8')

        # Return a download link for the sorted file
        return return_pdf(filename=sorted_file_path)
def return_pdf(filename):
    return send_file(filename)


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)

#SO TURNS OUT BEING A 0.0.0.0 PORT MAkES IT UNAVALIABLE TO ACCES THAT LOCALLY
#if __name__ == "__main__":
 #   app.run(host='0.0.0.0', port=8080, debug=True)