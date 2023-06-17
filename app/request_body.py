from pydantic import BaseModel

from .app import app


class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None


@app.post("/request_body/items")
async def create_item(item: Item):
    return item


@app.post("/request_body/items/taxed")
async def create_taxed_item(item: Item):
    item_dict = item.dict()
    if item.tax:
        taxed_price = item.price + item.price * item.tax
        item_dict.update({"taxed_price": round(taxed_price, 2)})
    return item_dict


@app.put("/request_body/items/{item_id}")
async def body_and_path(item_id: int, item: Item):
    return {"item_id": item_id, **item.dict()}


@app.put("/request_body/items/{item_id}/remarks")
async def body_and_path_and_query(
        item_id: int, item: Item, q: str | None = None):
    item = {"item_id": item_id, **item.dict()}
    if q is not None:
        item.update({"description": q})
    return item
