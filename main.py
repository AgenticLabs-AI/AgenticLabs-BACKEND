from fastapi import FastAPI
import uvicorn

def main():
    uvicorn.run(app, host="0.0.0.0", port=8080)
    
app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World!"}

if __name__ == "__main__":
    main()
