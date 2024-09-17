from base_model import BaseModel
""" This module defines the City Class """

class City(BaseModel):
    """
    Public class attributes:
    state_id: string - empty string: it will be the State.id
    name: string - empty string
    """

    state_id: str = ""
    name: str = ""

    def __init__(self, *args, **kwargs):

        super().__init__(*args, **kwargs)
