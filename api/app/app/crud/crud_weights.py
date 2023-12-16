from app.crud.crud_base import CRUDBase
from app.models.model_weights import Weights
from app.schemas.scheme_weights import WeightDb


class CRUDWeights(CRUDBase[
    Weights,
    WeightDb,
    WeightDb]
        ):
    """CRUD weights"""


weights = CRUDWeights(Weights)
