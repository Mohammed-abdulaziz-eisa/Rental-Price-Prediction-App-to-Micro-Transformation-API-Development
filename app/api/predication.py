"""
This module defines the API endpoints for rental price prediction.

It includes two endpoints:
1. GET /pred/ - Accepts apartment features as query parameters and returns the predicted rental price.
2. POST /pred/ - Accepts apartment features as JSON payload and returns the predicted rental price.

Dependencies:
- Flask: For creating the API endpoints.
- Pydantic: For validating the input data.
- schema.apartment: Defines the Apartment schema.
- services.model_inference_service: Provides the prediction service.

Functions:
- get_predication(): Handles GET requests for rental price prediction.
- get_predication_post(): Handles POST requests for rental price prediction.
"""

from flask import Blueprint, abort, jsonify, request
from pydantic import ValidationError
from schema.apartment import Apartment
from services import model_inference_service

bp = Blueprint("predication", __name__, url_prefix="/pred")


@bp.get("/")
def get_predication():
    """
    Handle GET requests for rental price prediction.

    This endpoint accepts apartment features as query parameters, validates them,
    and returns the predicted rental price.

    Returns:
        JSON response containing the predicted rental price.
    """
    try:
        apartment_features = Apartment(**request.args)
    except ValidationError:
        abort(code=400, description="Bad Request")  # noqa: WPS432

    predication = model_inference_service.predict(
        list(apartment_features.model_dump().values()),
    )

    return jsonify(predication)


@bp.post("/")
def get_predication_post():
    """
    Handle POST requests for rental price prediction.

    This endpoint accepts apartment features as a JSON payload, validates them,
    and returns the predicted rental price.

    Returns:
        JSON response containing the predicted rental price.
    """
    try:
        apartment_features = Apartment(**request.json)
    except ValidationError:
        abort(code=400, description="Bad Request")  # noqa: WPS432

    predication = model_inference_service.predict(
        list(apartment_features.model_dump().values()),
    )

    return jsonify(predication)
