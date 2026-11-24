import requests 
import logging 


CRUDE_OIL_BASE_URL = "https://api.eia.gov/v2/crude-oil-imports/data/"


def _fetch_page(period : str, api_key : str, page_size: int=5000, offset: int=0) -> dict:
    
    crude_oil_params = {
        "api_key": api_key,
        "length" : page_size,
        "frequency": "monthly",
        "data[0]": "quantity",
        "start": period,
        "end": period,
        "offset": offset,
        "facets[destinationType][0]": "US",
        "sort[0][column]": "period",
        "sort[0][direction]": "asc",
        "sort[1][column]": "originId",
        "sort[1][direction]": "asc",
        "sort[2][column]" : "gradeId",
        "sort[2][direction]" : "asc",
    }

    response = requests.get(CRUDE_OIL_BASE_URL, params= crude_oil_params, timeout=10)
    response.raise_for_status()
    return response.json()
   

def fetch_month(period: str, api_key: str, page_size: int = 5000, max_pages: int = 200) -> list[dict]:
    offset = 0
    pages = 0
    all_records = []
    total = 0

    while True:
        payload = _fetch_page(period=period, api_key=api_key, page_size=page_size, offset=offset)
        records = payload["response"]["data"]
        total = int(payload["response"]["total"])
        all_records.extend(records)
        pages += 1

        if not records or len(records) < page_size:
            break
        if pages >= max_pages:
            raise RuntimeError(f"{period}: hit max_pages={max_pages} without reaching the last page")
        offset += len(records)

    if len(all_records) > total:
        raise RuntimeError(f"{period}: received {len(all_records)} rows, but EIA total is {total}")
    if len(all_records) < total:
        logging.warning(f"{period}: received {len(all_records)} rows, EIA total is {total}")

    return all_records
