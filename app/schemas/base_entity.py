
import uuid
from sqlalchemy import Column, Uuid


class BaseEntity:
    id = Column(Uuid,primary_key=True, default=uuid.uuid4)