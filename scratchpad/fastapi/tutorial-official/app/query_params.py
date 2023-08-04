from .app import app

items = [
    {"item": "towel"},
    {"item": "sonic screwdriver"},
    {"item": "dead parrot"},
]


@app.get("/items/")
async def items_list_query(start_index: int = 0, end_index: int = 99):
    return items[start_index:end_index]


@app.get("/items/{item_id}")
async def items_list_mixed(item_id: int, q: str | None = None):
    return {"item": items[item_id], "q": q}


@app.get("/items/bool/{item_id}")
async def conditional_items_list_mixed(item_id: int, show: bool):
    if show:
        response = {"item": items[item_id]}
    else:
        response = {"msg": "averting our eyes"}
    return response


@app.get("/items/multi/{path_val_1}/{path_val_2}")
async def items_list_multi_mixed(path_val_1, q1: int,
                                 path_val_2: float, q2: bool):
    return {"path_args": [path_val_1, path_val_2],
            "query_args": [q1, q2]}


@app.get("/items/missing/required")
async def required(q: str):
    return {"q": q}


@app.get("/items/missing/default")
async def default(q: str = "default val"):
    return {"q": q}


@app.get("/items/missing/optional")
async def optional(q: str | None = None):
    if q is not None:
        return {"q": q}
