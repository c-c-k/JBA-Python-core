from enum import Enum

from .app import app


@app.get("/item/any/{item}")
async def item_any(item):
    return {
            "msg": "the any route accepts all",
            "item": item
            }


@app.get("/item/int/{item}")
async def item_int(item: int):
    return {
            "msg": "the int route accepts only integers",
            "square": f"{item}^2 = {item**2}"
            }


@app.get("/item/{_}")
async def fallthrough():
    return {
            "msg": "If the route does not exist it still possible"
                   " to catch those that fall through",
            }


class CloudPath(str, Enum):
    MOUNTAIN_PATH = "mountain"
    VALLEY_PATH = "vale"


@app.get("/cloud-path/{choice}")
async def cloud_path(choice: CloudPath):
    if choice is CloudPath.MOUNTAIN_PATH:
        msg = (
            "Climbing to the mountains top you find an incomprehensible sight"
            ", a dark starless and sunless sky above illuminated "
            "by the clouds stretching to the furthest horizons below."
        )
    elif choice.value == "vale":
        msg = (
            "Reaching the valleys bottom you find yourself withing a sea of "
            "clouds, swimming and dancing around you are bright yet ghostly "
            "will-o'-the-wisp lights."
        )
    else:
        msg = (
            "Standing at the crossroad, you raise your foot as if to take"
            "the first step upon the path, but then suddenly sway back and"
            "find yourself uncertain should you go up the 'mountain', down"
            " the 'vale' or perhaps you should actually turn back"
        )
    return {"choice": choice, "msg": msg}


@app.get("/files/{file_path:path}")
async def get_file_path(file_path: str):
    return {"msg": f"The file you requested is '{file_path}'"}
