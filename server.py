from flask import jsonify, Flask
from flask import render_template

app = Flask(__name__)

@app.route('/')
def getForm():
    return render_template('index.html')
@app.route('/info')
def getInfo():
    return jsonify([
  {
    "_id": "667fdee11d5a740a682ac4bc",
    "index": 0,
    "guid": "dee6c464-1c5d-4fe0-b18b-e09da0dc02c8",
    "isActive": 'true',
    "balance": "$3,633.95",
    "picture": "http://placehold.it/32x32",
    "age": 22,
    "eyeColor": "blue",
    "name": "Howell Fernandez",
    "gender": "male",
    "company": "MANGELICA",
    "email": "howellfernandez@mangelica.com",
    "phone": "+1 (816) 514-3627",
    "address": "929 Falmouth Street, Madaket, Palau, 3185",
    "registered": "2016-10-22T09:21:28 -03:00",
    "latitude": 9.284188,
    "longitude": -178.987595,
    "tags": [
      "id",
      "commodo",
      "commodo",
      "esse",
      "do",
      "nisi",
      "cupidatat"
    ],
    "friends": [
      {
        "id": 0,
        "name": "Stacy Simpson"
      },
      {
        "id": 1,
        "name": "Lora Armstrong"
      },
      {
        "id": 2,
        "name": "Pickett Jackson"
      }
    ],
    "greeting": "Hello, Howell Fernandez! You have 5 unread messages.",
    "favoriteFruit": "apple"
  }
])
app.run(port="80", host="0.0.0.0")
