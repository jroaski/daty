from flask import Flask, request, render_template, send_file, make_response
import dates_sorter
from dates_sorter import *
import unittest
import requests
class TestFlaskIntegration(unittest.TestCase):

    def test_upload_file(self):
        with open(r'C:\Users\Jacob\Downloads\kazaniatxt.txt', 'rb') as test_file:
            files = {'file': ('test_file.txt', test_file)}
            response = requests.post('http://127.0.0.1:8080/upload', files=files)
            self.assertEqual(response.status_code, 200)

    def test_upload_empty_file(self):
        files = {'file': ('empty_file.txt', b'')}
        response = requests.post('http://127.0.0.1:8080/upload', files=files)
        self.assertEqual(response.status_code, 200)

    def test_upload_no_file(self):
        response = requests.post('http://127.0.0.1:8080/upload')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.text, "No file part")


#add checking downloading file/ output
