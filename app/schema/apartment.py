"""Schema for Apartment."""

from pydantic import BaseModel


class Apartment(BaseModel):
    """
    Schema for Apartment.

    area - Area of the apartment in square feat
    construction_year - Year of construction
    bedrooms - Number of bedrooms in the apartment
    garden_area - Area of the garden in square feet
    balcony_area - Area of the balcony in square feet
    parking_present - Parking availability
    furnished - Furnished status
    garage_present - Garage avaliability
    storage_present - Storage avaliability
    """

    area: int
    construction_year: int
    bedrooms: int
    garden_area: int
    balcony_area: int
    parking_present: int
    furnished: int
    garage_present: int
    storage_present: int
