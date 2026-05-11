# Festiva Planner AI

## Problem
Planning events is difficult due to:
- Budget uncertainty
- Vendor selection confusion
- Lack of structured planning

## Data Understanding
- Weddings have highest budgets
- Bangalore has many vendors
- Budget varies by event type

## Goal
Build an AI system that:
- Generates event plans
- Suggests budget allocation
- Recommends vendors

## ML Model
- Built a regression model to predict event budget
- Used features: event type, city, guests
- Model: Linear Regression

## NLP Module
- Extracts event type, city, and budget from user input
- Uses keyword matching and regex
- Converts natural language into structured data

## RAG System
- Built knowledge base using event planning data
- Used Sentence Transformers for embeddings
- Used FAISS for similarity search
- Retrieves relevant information based on user query

## Multi-Agent System (Week 5)

The system integrates multiple AI components into a unified pipeline:

### Components

1. **NLP Module**
   - Extracts structured data from user input
   - Identifies event type, city, and budget

2. **RAG (Retrieval-Augmented Generation)**
   - Retrieves relevant event planning knowledge
   - Uses FAISS for similarity search
   - Uses Sentence Transformers for embeddings

3. **ML Model (Budget Predictor)**
   - Predicts estimated budget based on:
     - event type
     - city
     - number of guests
   - Model: Linear Regression

4. **Agent System**
   - Combines all modules into one workflow:
     - NLP → RAG → ML → Final Output
   - Produces structured AI response

### Example Output

```json
{
  "event": "wedding",
  "city": "Bangalore",
  "input_budget": 1000000,
  "predicted_budget": 499999,
  "knowledge": [
    "Wedding planning typically takes 6-12 months.",
    "Catering is usually the largest expense in weddings."
  ]
}

## API & UI (Week 6)

### FastAPI Backend
- Provides API endpoints for event planning
- Endpoint:
  - `/plan?query=...`

### Streamlit UI
- Interactive interface for users
- Displays:
  - Event details
  - Budget prediction
  - Knowledge insights

### How to Run

```bash
uvicorn app.main:app --reload
streamlit run app/ui.py

NLP → Planner Agent
RAG → Knowledge Agent
ML → Budget Agent