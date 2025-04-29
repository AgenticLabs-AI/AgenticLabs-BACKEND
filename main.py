from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
from supabase_client import supabase

def main():
    uvicorn.run(app, host="localhost", port=8080)
    
app = FastAPI()

origins = [
    "http://localhost:5173",
    "https://theagenticlabs.tech",
    "https://www.theagenticlabs.tech"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    return {"message": "Hello World!"}

@app.get("/api/landing/explorecards")
async def landing_explorecards():
    try:
        response = supabase.table("LandingExploreCards").select("*").execute()
        if response.data:
            return response.data
        else:
            raise HTTPException(status_code=500, detail="No data found in response")
    except Exception as e:
        print(f"Error fetching data: {e}")
        raise HTTPException(status_code=500, detail="Failed to fetch data")
    
    
@app.get("/get/products")
async def get_products():
    try: 
        response = supabase.table("products").select("*").execute()
        if response.data:
            return response.data
        else:
            raise HTTPException(status_code=500, details="No data found in response")
    except Exception as e:
        print(f"Error fetching data: {e}")
        raise HTTPException(status_code=500, detail="Failed to fetch data")
    
@app.get("/get/products/{product_id}")
async def get_product_by_id(product_id: int):
    try:
        response = supabase.table("products").select("*").eq("id", product_id).execute()
        if response.data:
            return response.data[0]
        else:
            raise HTTPException(status_code=404, detail="Product not found")
    except Exception as e:
        print(f"Error fetching product by ID: {e}")
        raise HTTPException(status_code=500, detail="Failed to fetch product")
        

if __name__ == "__main__":
    main()
