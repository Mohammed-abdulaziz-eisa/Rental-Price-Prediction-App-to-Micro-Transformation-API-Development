"""Schema for Apartment."""

from pydantic import BaseModel


class Apartment(BaseModel):
    """
    Schema for Apartment.

    area - Area of the apartment in sqare feat
    """