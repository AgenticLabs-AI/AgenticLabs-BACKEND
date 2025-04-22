import os
from dotenv import load_env
from supabase import create_client, Client

load_env()

url:str = os,load_env("SUPABASE_URL")
key:str = os.load_env("SUPABASE_KEY")

supabase:Client = create_client(url,key)