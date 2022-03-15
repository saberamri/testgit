from pydantic import BaseModel
from pydantic.types import PositiveInt


class Match(BaseModel):
    """
    The Match() class inherits from the BaseModel() class:it contains the elements of Match

    Args:
        BaseModel (class): This class contains the attributes and methods of match
    """
    player1_id: PositiveInt
    player2_id: PositiveInt
    score_player1: float = None

    @property
    def score_player2(self):
        """it's like an Attribute: It's a getter that we will have to put it during 
        the initialization of the class and which allows to access and display the 
        attribute in read-only mode. it is calculated automatically based on 
        score_player1 but is not stored at all.

        Returns:
            int: player score value
        """
        return 1.0 - self.score_player1

    @score_player2.setter
    def score_player2(self, value):
        """It's a setter: allows to display and modify the attribute.

        Args:
            value (int): player score value
        """
        self.score_player1 = 1.0 - value