from fastapi import FastAPI
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
    return {
        "status": "Success",
        "message": "FastAPI is running smoothly on Ubuntu"
    }


@app.get("/view")
def view_student_data():
    return {
        "student_data": load_data()
    }