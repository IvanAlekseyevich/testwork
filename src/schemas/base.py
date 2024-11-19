from pydantic import BaseModel, ConfigDict


class DBObjectBase(BaseModel):
    model_config = ConfigDict(from_attributes=True)
