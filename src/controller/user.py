
from src.model.user import User
from src.db.connection import PostgreSQLConnection




db = PostgreSQLConnection(dbname="postgres", user="postgres", password="postgres")


async def c_get_user(user_id: int):
    db.connect()
    
    user = db.select_user(f"SELECT * FROM public.users WHERE id = {user_id}")
    db.close()
    return user

async def c_create_user(user: User):
    db.connect()
    
    user = db.insert_user(user.id, user.name, user.area, user.jobDescription, user.role, user.salary, True, "Good")
    db.close()

async def c_delete_user(user_id: int):
    db.connect()
    
    user = db.delete_user(f"DELETE FROM public.users WHERE id = {user_id}")
    db.close()
    return user

async def c_update_user(user: User, user_id: int):
    db.connect()
    
    user = db.update_user(user.name, user.area, user.jobDescription, user.role, user.salary, user.is_active, user.last_evaluation, user_id)
    db.close()
    return user
