from src.pipline.training_pipeline import TrainPipeline

pipline = TrainPipeline()
import os
import pymongo
import certifi
from src.constants import DATABASE_NAME

# Quick check script
try:
    print("\n=== MONGODB DEBUG CHECK ===")
    url = os.getenv("MONGODB_URL")
    print(f"Using URL: {url[:30]}...") # prints just the start for security
    
    client = pymongo.MongoClient(url, tlsCAFile=certifi.where())
    
    print("Available Databases on your Cluster:")
    db_names = client.list_database_names()
    print(db_names)
    
    if DATABASE_NAME in db_names:
        print(f"\n Target Database '{DATABASE_NAME}' EXISTS!")
        print("Available Collections inside it:")
        print(client[DATABASE_NAME].list_collection_names())
    else:
        print(f"\n❌ Target Database '{DATABASE_NAME}' DOES NOT EXIST on this cluster!")
    print("===========================\n")
except Exception as e:
    print(f"Debug check failed: {e}")
pipline.start_data_ingestion()