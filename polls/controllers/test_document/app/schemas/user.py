from pydantic import BaseModel
from app.models import User

class UserSchema(BaseModel):
    username: str
    profile: str
    team_id: int

    class Config:
        orm_mode = True