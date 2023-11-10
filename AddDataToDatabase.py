import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': "https://faceattendencerealtime-56bef-default-rtdb.firebaseio.com/"
})

ref = db.reference('Students')

data = {
    "321654":
        {
            "name": "Murtaza Hassan",
            "major": "Robotics",
            "starting_year": 2017,
            "total_attendance": 7,
            "standing": "G",
            "year": 4,
            "last_attendance_time": "2022-12-11 00:54:34"
        },
    "852741":
        {
            "name": "Emly Blunt",
            "major": "Economics",
            "starting_year": 2021,
            "total_attendance": 12,
            "standing": "B",
            "year": 1,
            "last_attendance_time": "2022-12-11 00:54:34"
        },
    "963852":
        {
            "name": "Elon Musk",
            "major": "Physics",
            "starting_year": 2020,
            "total_attendance": 7,
            "standing": "G",
            "year": 2,
            "last_attendance_time": "2022-12-11 00:54:34"
        },
"218001":
        {
            "name": "Utkarsh Anand",
            "major": "Computer",
            "starting_year": 2021,
            "total_attendance": 12,
            "standing": "A",
            "year": 3,
            "last_attendance_time": "2022-12-11 00:54:34"
        },
"218025":
        {
            "name": "Manish Kohli",
            "major": "App Dev",
            "starting_year": 2020,
            "total_attendance": 7,
            "standing": "G",
            "year": 2,
            "last_attendance_time": "2022-12-11 00:54:34"
        },
"218002":
        {
            "name": "Chandan",
            "major": "Electronics",
            "starting_year": 2023,
            "total_attendance": 4,
            "standing": "G",
            "year": 1,
            "last_attendance_time": "2022-12-11 00:54:34"
        },
"218019":
        {
            "name": "Rishabh Sharma",
            "major": "DSA",
            "starting_year": 2021,
            "total_attendance": 8,
            "standing": "G",
            "year": 3,
            "last_attendance_time": "2022-12-11 00:54:34"
        },
"218005":
        {
            "name": "Anuj Verma",
            "major": "Web Dev",
            "starting_year": 2022,
            "total_attendance": 5,
            "standing": "G",
            "year": 2,
            "last_attendance_time": "2022-12-11 00:54:34"
        }
}

for key, value in data.items():
    ref.child(key).set(value)