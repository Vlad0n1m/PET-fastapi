from database import new_session
from database import TaskORM
from schemas import STask, STaskAdd
from sqlalchemy import select
class TaskRepository():
    @classmethod
    async def add_one(cls, task: STaskAdd) -> int:
        async with new_session() as session:
            task_dict = task.model_dump()

            task = TaskORM(**task_dict)
            session.add(task)
            await session.flush()
            await session.commit()
            return task.id 

    @classmethod
    async def get_all(cls) -> list[STask]:
        async with new_session() as session:
            query = select(TaskORM)
            result = await session.execute(query)
            task_models = result.scalars().all()
            task_schemas = [STask.model_validate(task) for task in task_models ]
            return task_schemas    
