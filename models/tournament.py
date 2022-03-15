from pydantic import BaseModel
from datetime import datetime
from pydantic.types import PositiveInt, constr
from typing import List
from enum import Enum
from models.round import Round


class TimeControl(Enum):
    """
    TimeControl is a class that inherits from the Eum class.

    Args:
        Enum (class): Enum is a basic python module integrated into the language 
        it will enumerate the values of the timecontrol variable.
    """
    Bullet: 1
    blitz = 2
    fast = 3


class Tournament(BaseModel):
    """The Tournament() class inherits from the BaseModel() class
    This class contains the attributes and methods of the tournament user.

    Args:
        BaseModel (class): This class contains the attributes and methods of the tournament
    """
    id: PositiveInt
    name: constr(strict=True, min_length=2, max_length=25)
    start_date: datetime = datetime.today()
    end_date: datetime = None
    place: constr(strict=True, min_length=2, max_length=10)
    number_of_rounds: PositiveInt = 4
    description: constr(strict=True, max_length=50) = ""
    players: List[PositiveInt]
    timeconrol: TimeControl