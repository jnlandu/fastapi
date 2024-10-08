
#  Personal imports
from app.app import app
from routers import auth, chat,routines,workouts




@app.get("/")
async def root():
    return {"message": "Healthy"}

@app.get("/health")
async def health_check():
    return {"status": "healthy"}

app.include_router(auth.router)
app.include_router(chat.router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app.main:app", reload=True)
    print("Server is running correctly")


