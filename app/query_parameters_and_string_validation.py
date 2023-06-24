from typing import Annotated, Union

from fastapi import Query
from pydantic import Required

from .app import app

HOST = ""
ROOT = HOST + "/query_parameters_and_string_validation"


@app.get(ROOT + "/items")
async def read_items(q: str | None = None):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results


@app.get(ROOT + "/items2")
async def read_items2(q: Annotated[str | None, Query(max_length=50)] = None):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results


@app.get(ROOT + "/items3")
async def read_items3(q: Union[str | None] = Query(default=None,
                                                   max_length=50)):
    """This is an old style for FastAPI versions prior to 0.95.0"""
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results


@app.get(ROOT + "/items4")
async def read_items4(q: Annotated[
        str | None,
        Query(min_lengt=3, max_length=50, regex="^fixed$")] = None):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results


@app.get(ROOT + "/items5")
async def read_items5(q: Annotated[
        str | None,
        Query(min_lengt=3, max_length=50, regex="^fixed$")] = "fixed"):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results


@app.get(ROOT + "/items6")
async def read_items6(q: Annotated[str, Query(min_lengt=3)]):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results


@app.get(ROOT + "/items7")
async def read_items7(q: Annotated[str, Query(min_lengt=3)] = ...):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results


@app.get(ROOT + "/items8")
async def read_items8(q: Annotated[str | None, Query(min_lengt=3)] = ...):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results


@app.get(ROOT + "/items9")
async def read_items9(q: Annotated[str, Query(min_lengt=3)] = Required):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results


@app.get(ROOT + "/items10")
async def read_items10(q: Annotated[list[str] | None, Query()] = None):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results


@app.get(ROOT + "/items11")
async def read_items11(q: list[str] | None = None):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results
