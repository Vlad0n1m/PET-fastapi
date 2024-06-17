from fastapi import APIRouter, Depends
from typing import Annotated
from repository import TaskRepository
from schemas import STaskAdd
from schemas import STask
router = APIRouter(
    prefix='/tasks',
    tags=['Таски']
)

@router.post("/tasks")
async def add_task(
    task: Annotated[STaskAdd, Depends()]
):
    task_id = await TaskRepository.add_one(task)
    return {'ok': True, "task_id": task_id}

@router.get("/tasks")
async def get_tasks() -> STask:
    tasks = await TaskRepository.get_all()
    return {"tasks": tasks}
