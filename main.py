from fastapi import FastAPI

app = FastAPI(
    title="Chai point menu API",
    description="Read-only menu API for kiosk display and mobile app"
)

@app.get("/")
def root():
    return{
        "message":"welcome to chai point menu api"
    }