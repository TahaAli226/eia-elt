from pydantic import BaseModel, Field, field_validator

class CrudeImportRecord(BaseModel):
    period: str
    originId: str
    originName: str
    originType: str
    originTypeName: str
    destinationId: str
    destinationName: str
    destinationType: str
    destinationTypeName: str
    gradeId: str
    gradeName: str
    quantity: str | None
    quantity_units: str = Field(alias="quantity-units")

    @field_validator("quantity")
    @classmethod
    def check_numeric_quantity(cls, value: str) -> str:
        if value is None:
            return value 
        try: 
            float(value)
        except ValueError:
            raise ValueError(f"The record quantity value is non-numeric.\n value: {value!r}")
        return value
    