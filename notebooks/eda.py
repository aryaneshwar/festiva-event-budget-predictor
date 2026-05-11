import pandas as pd

# Load datasets
events = pd.read_csv("data/events.csv")
vendors = pd.read_csv("data/vendors.csv")
print("=== EVENTS DATA ===")
print(events)

print("\n=== VENDORS DATA ===")
print(vendors)

# Basic analysis
print("\n=== Average budget by event type ===")
print(events.groupby("event_type")["budget"].mean())

print("\n=== Vendors per city ===")
print(vendors["city"].value_counts())