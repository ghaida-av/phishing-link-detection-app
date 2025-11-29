Run locally:
$ python3 -m venv venv
$ source venv/bin/activate
$ pip install -r requirements.txt
$ python app.py

POST JSON to /predict:
curl -X POST -H "Content-Type: application/json" -d '{"url":"http://example.com"}' http://127.0.0.1:5000/predict

