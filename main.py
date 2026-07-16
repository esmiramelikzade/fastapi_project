from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
app = FastAPI()
class TaskCreate(BaseModel):
    title: str
tasks = [
    {
        "id": 1,
        "title": "Learn FastAPI",
        "done": False
    },
    {
        "id": 2,
        "title": "Build my first API",
        "done": True
    },
    {
        "id": 3,
        "title": "Upload project to GitHub",
        "done": False
    }
]
@app.get("/tasks")
def get_tasks():
    return tasks
@app.get("/tasks/{task_id}")
def get_task(task_id: int):
    for task in tasks:
        if task["id"] == task_id:
            return task

    raise HTTPException(
        status_code=404,
        detail={"error": f"Task {task_id} not found"}
    )
@app.post("/tasks", status_code=201)
def create_task(task: TaskCreate):
    if not task.title.strip():
        raise HTTPException(
            status_code=400,
            detail={"error": "Title is required"}
        )
    new_task = {
        "id": len(tasks) + 1,
        "title": task.title,
        "done": False
    }
    tasks.append(new_task)
    return new_task
