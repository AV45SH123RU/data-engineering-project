import csv
import random
from datetime import datetime, timedelta
import uuid
import os

def generate_purchases(num_records=100, days_back=7):
    """
    Generate simulated purchase records.
    """
    products = [
        {"id": "P001", "name": "Wireless Headphones", "category": "Electronics", "price": 99.99},
        {"id": "P002", "name": "Organic Coffee Beans", "category": "Food", "price": 24.50},
        {"id": "P003", "name": "Yoga Mat", "category": "Sports", "price": 19.99},
        {"id": "P004", "name": "Mechanical Keyboard", "category": "Electronics", "price": 129.00},
    ]
    
    records = []
    for _ in range(num_records):
        # Random timestamp within last N days
        random_seconds = random.randint(0, 86400 * days_back)
        timestamp = datetime.now() - timedelta(seconds=random_seconds)
        
        product = random.choice(products)
        # Slight price variation (tax/discount)
        amount = round(product["price"] * (1 + random.uniform(-0.1, 0.2)), 2)
        
        record = {
            "event_id": str(uuid.uuid4()),
            "timestamp": timestamp.isoformat(),
            "user_id": str(uuid.uuid4())[:8],
            "product_id": product["id"],
            "product_name": product["name"],
            "category": product["category"],
            "amount": amount,
            "currency": "USD",
            "device_type": random.choice(["mobile", "desktop", "tablet"]),
            "session_id": str(uuid.uuid4()),
        }
        records.append(record)
    
    return records

def save_to_csv(records, filename_prefix="purchases"):
    """
    Save records to a CSV file in data/raw/ with a timestamped filename.
    """
    # Ensure the data/raw directory exists
    os.makedirs("data/raw", exist_ok=True)
    
    # Create filename with timestamp
    timestamp_str = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"{filename_prefix}_{timestamp_str}.csv"
    filepath = os.path.join("data/raw", filename)
    
    # Write to CSV
    with open(filepath, mode='w', newline='', encoding='utf-8') as f:
        if records:
            writer = csv.DictWriter(f, fieldnames=records[0].keys())
            writer.writeheader()
            writer.writerows(records)
    
    print(f"✅ Generated {len(records)} records and saved to {filepath}")
    return filepath

if __name__ == "__main__":
    # When run directly, generate 100 records
    records = generate_purchases(num_records=100)
    save_to_csv(records)