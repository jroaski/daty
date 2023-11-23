import unittest
import requests
import os

# Set the base URL for the Flask application
BASE_URL = os.getenv("FLASK_APP_URL", "http://127.0.0.1:8080")


class TestFlaskIntegration(unittest.TestCase):
    """Test Flask integration"""

    def test_upload_file(self):
        # Modify the file path as per your file system or use a test file within
        # the Docker context

        test_file_path = os.getenv(
            "TEST_FILE_PATH", r"C:\Users\Jacob\Downloads\kazaniatxt.txt"
        )

        with open(test_file_path, "rb") as test_file:
            files = {"file": ("test_file.txt", test_file)}
            response = requests.post(f"{BASE_URL}/upload", files=files)
            self.assertEqual(response.status_code, 200)

    def test_upload_empty_file(self):
        files = {"file": ("empty_file.txt", b"")}
        response = requests.post(f"{BASE_URL}/upload", files=files)
        self.assertEqual(response.status_code, 200)

    def test_upload_no_file(self):
        response = requests.post(f"{BASE_URL}/upload")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.text, "No file part")


if __name__ == "__main__":
    unittest.main()
