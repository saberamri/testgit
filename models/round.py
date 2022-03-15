
from pydantic import BaseModel
from datetime import datetime
from pydantic.types import constr
from typing import List
from models.match import Match


class Round(BaseModel):
    """
    The Round() class inherits from the BaseModel() class:it contains the elements of Round

    Args:
        BaseModel (class): This class contains the attributes and methods of round
    """

    name: constr(strict=True, min_length=2, max_length=10)
    start_date: datetime = datetime.today()
    end_date: datetime = None
    matchs: List[Match]=[]
