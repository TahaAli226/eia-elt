import pytest 
from pydantic import ValidationError
from eia_elt.models import CrudeImportRecord

@pytest.fixture 
def valid_crude_oil_record(): 
    return {
  "period": "2026-08",
  "originId": "CTY_AE",
  "originName": "United Arab Emirates",
  "originType": "CTY",
  "originTypeName": "Country",
  "destinationId": "PP_5",
  "destinationName": "PADD5 (West Coast)",
  "destinationType": "PP",
  "destinationTypeName": "Port PADD",
  "gradeId": "LSO",
  "gradeName": "Light Sour",
  "quantity": "1578",
  "quantity-units": "thousand barrels"
}

class TestCrudeImportRecord:

    def test_valid_quantity(self, valid_crude_oil_record):
        record = CrudeImportRecord.model_validate(valid_crude_oil_record)
        assert record.quantity == "1578"

    def test_quantity_units_alias_maps(self, valid_crude_oil_record):
        record = CrudeImportRecord.model_validate(valid_crude_oil_record)
        assert record.quantity_units == "thousand barrels" 

    def test_non_numeric_quantity(self, valid_crude_oil_record):
        valid_crude_oil_record["quantity"] = "test"

        with pytest.raises(ValidationError):
            CrudeImportRecord.model_validate(valid_crude_oil_record)

    def test_None_quantity_value(self, valid_crude_oil_record):
        valid_crude_oil_record["quantity"] = None
        record = CrudeImportRecord.model_validate(valid_crude_oil_record)
        assert record.quantity is None

    def test_missing_quantity_field(self, valid_crude_oil_record):
        del valid_crude_oil_record["quantity"]

        with pytest.raises(ValidationError):
             CrudeImportRecord.model_validate(valid_crude_oil_record)