import yfinance as yf
from pymongo import MongoClient
import json
import pandas as pd

# 1. Połączenie z MongoDB (w Dockerze nazwa hosta to mongodb)
client = MongoClient("mongodb://localhost:27017/") # Zmień na 'mongodb' jeśli uruchamiasz wewnątrz kontenera
db = client.stock_database
collection = db.prices

# 2. Nasza lista do śledzenia
assets = ['AAPL', 'NVDA', 'TSLA', 'BTC-USD', 'ETH-USD', 'SOL-USD']

def fetch_and_save():
    for asset in assets:
        print(f"Pobieram dane dla: {asset}...")
        
        # Pobieramy dane za cały 2025 rok
        ticker = yf.Ticker(asset)
        df = ticker.history(start="2025-01-01", end="2025-12-31")
        
        # Przygotowanie danych (reset indeksu, żeby data była kolumną)
        df.reset_index(inplace=True)
        df['Date'] = df['Date'].dt.strftime('%Y-%m-%d') # Formatowanie daty dla JSON
        
        # Konwersja do słownika (format pod MongoDB)
        records = df.to_dict('records')
        
        # Dodajemy informację, co to za instrument
        for record in records:
            record['asset'] = asset
        
        # 3. Zapis do MongoDB
        if records:
            collection.insert_many(records)
            
            # 4. Zapis do JSON (lokalny backup)
            with open(f"data/{asset}_2025.json", "w") as f:
                json.dump(records, f, indent=4)
                
    print("Zakończono! Dane są w MongoDB i w plikach JSON.")

if __name__ == "__main__":
    fetch_and_save()