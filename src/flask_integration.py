import shutil
import tempfile
from flask import Flask, request, jsonify, send_file
from dates_sorter import *
app = Flask(__name__)

@app.route('/sort', methods=['POST'])
def sort_text_by_dates():
    temp_dir = None
    try:
        input_file = request.files['file']
        if not input_file:
            return jsonify({"error": "No file provided"}), 400

        # Log the request data for debugging
        app.logger.info(f"Received file: {input_file.filename}")


        # Create a temporary directory to store input and output files
        temp_dir = tempfile.mkdtemp()

        input_file_path = os.path.join(temp_dir, input_file.filename)
        input_file.save(input_file_path)

        output_file_path = os.path.join(temp_dir, "sorted_output.txt")

        lines = read_lines_from_file(input_file_path, encoding='utf-8')
        date_line_dict = group_lines_by_dates(lines)
        sorted_lines = sort_and_flatten_groups(date_line_dict)
        write_lines_to_file(sorted_lines, output_file_path, encoding='utf-8')

        # Provide the sorted output file for download
        response = send_file(output_file_path, as_attachment=True)
        response.headers["Content-Disposition"] = f"attachment; filename=sorted_output.txt"
        return response

    except Exception as e:
        return jsonify({"error": str(e)}), 500
    finally:
        if temp_dir:
            # Cleanup temporary directory if it was defined
            shutil.rmtree(temp_dir)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080, debug=True)