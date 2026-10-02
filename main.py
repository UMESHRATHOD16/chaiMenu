from fastapi import FastAPI
from models import MenuResponse,MenuItem
from fastapi import Query
from data import menu_items
from fastapi import HTTPException

app = FastAPI(
    title="Chai point menu API",
    description="Read-only menu API for kiosk display and mobile app"
)

@app.get("/")
def root():
    return{
        "message":"welcome to chai point menu api"
    }

# response_model=MenuResponse --> dependency injection
@app.get("/menu",response_model=MenuResponse)
def get_menu(category:str | None = Query(None, description="filter by chai,snack or combo")):
    if category:
        filtered = [item for item in menu_items if item["category"] == category.lower()]
        if not filtered:
            raise HTTPException(status_code=404,detail=f"No item found of category {category}")
        return MenuResponse(count=len(filtered),items=filtered)
    return MenuResponse(count = len(menu_items), items = menu_items)


@app.get("/menu/{item_id}", response_model=MenuItem)
def get_menuById(item_id:int):
    for item in menu_items:
        if item["id"] == item_id:
            return item
            # MenuItem(item)     # ❌ positional: one argument = entire dictionary
            # MenuItem(**item)   # ✅ dictionary unpacked into keyword arguments
            # That's why we using simply return item
    raise HTTPException(status_code=404, detail=f"The item with item id {item_id} is not found")
