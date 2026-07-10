from fastapi import FastAPI, Path, Query
import json

app = FastAPI()


def load_data():
    try:
        with open("student.json", "r", encoding="utf-8") as file:
            return json.load(file)
    except FileNotFoundError:
        return {"error": "student.json file not found"}
    except json.JSONDecodeError:
        return {"error": "Invalid JSON format"}


@app.get("/")
def read_root():
    return {"status": "Success", "message": "FastAPI is running smoothly on Ubuntu"}


# -->> This is Function for showing all tudent Data
@app.get("/view")
def view_student_data():
    return {"student_data": load_data()}


# -->> This is Function for showing specific student Data
@app.get("/view/{student_id}")
def view_student_data_by_id(student_id: str):
    data = load_data()
    if student_id in data:
        return data[student_id]
    else:
        return "student Not Found"


@app.get("/sort")
def view_sorted_student(sorted_by: str = Query(..., description="")):
    valid_fields = [
        "age",
        "class",
        "roll",
        "Math marks",
        "English marks",
        "Science marks",
    ]
    if sorted_by not in valid_fields:
        raise "student Not Found"

    data = load_data()

    sorted_data = list(data.values())
    sorted_data.sort(key=lambda x: x[sorted_by])
    
    return sorted_data
