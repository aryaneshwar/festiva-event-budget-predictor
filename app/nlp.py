import re

def extract_details(user_input):
    text = user_input.lower()

    # Detect event type
    if "wedding" in text:
        event = "wedding"
    elif "birthday" in text:
        event = "birthday"
    elif "corporate" in text:
        event = "corporate"
    else:
        event = "unknown"

    # Detect city
    if "bangalore" in text:
        city = "Bangalore"
    elif "mumbai" in text:
        city = "Mumbai"
    elif "delhi" in text:
        city = "Delhi"
    else:
        city = "unknown"

    # Extract budget (numbers)
    numbers = re.findall(r'\d+', text)

    if numbers:
        budget = int(numbers[0])

        # Convert lakh to full number
        if "lakh" in text:
            budget *= 100000
    else:
        budget = None

    return {
        "event": event,
        "city": city,
        "budget": budget
    }


# Test
user_input = "Birthday party in Mumbai 2 lakh"
result = extract_details(user_input)

print(result)