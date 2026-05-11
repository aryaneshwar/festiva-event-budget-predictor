from app.nlp import extract_details
from app.rag import retrieve
from app.model import model, feature_columns
import pandas as pd

def generate_plan(event):
    if event == "wedding":
        return [
            "Book venue",
            "Hire caterer",
            "Arrange decoration",
            "Send invitations"
        ]
    elif event == "birthday":
        return [
            "Order cake",
            "Arrange decorations",
            "Invite guests",
            "Plan activities"
        ]
    elif event == "corporate":
        return [
            "Book conference hall",
            "Arrange seating",
            "Prepare presentation",
            "Organize refreshments"
        ]
    else:
        return ["Basic planning required"]
    
def recommend_vendors(event):
    if event == "wedding":
        return ["Top Caterer", "Premium Decorator", "Wedding Photographer"]
    elif event == "birthday":
        return ["Cake Shop", "Party Decorator"]
    else:
        return ["Event Planner"]
    
def run_agent(user_input):
    # Step 1: NLP
    details = extract_details(user_input)

    event = details["event"]
    city = details["city"]
    budget = details["budget"]

    # Step 2: RAG (Knowledge retrieval)
    knowledge = retrieve(user_input)

    # Step 3: ML Prediction

    # Create empty dataframe with same columns as training
    sample = pd.DataFrame(columns=feature_columns)

    # Add one row filled with 0
    sample.loc[0] = 0

    # Set guest count (default for now)
    sample["guests"] = 100

    # Set event and city columns
    event_col = f"event_type_{event}"
    city_col = f"city_{city}"

    if event_col in sample.columns:
        sample[event_col] = 1

    if city_col in sample.columns:
        sample[city_col] = 1

    # Predict budget
    predicted_budget = int(model.predict(sample)[0])
    plan = generate_plan(event)
    vendors = recommend_vendors(event)

    # Final output
    return {
        "event": event,
        "city": city,
        "input_budget": budget,
        "predicted_budget": predicted_budget,
        "knowledge": [k.strip() for k in knowledge],
        "plan": plan,
        "vendors": vendors
    }


# Test run
if __name__ == "__main__":
    result = run_agent("Wedding in Bangalore with 10 lakh budget")
    print("\n=== FINAL OUTPUT ===")
    print(result)