import json
import pickle
import os


DATA_DIR = "data"

def save_model(model, filename):
    """Saves a trained Scikit-learn model using pickle."""
    filepath = os.path.join(DATA_DIR, filename)
    os.makedirs(os.path.dirname(filepath), exist_ok=True)
    with open(filepath, 'wb') as file:
        pickle.dump(model, file)
    print(f"Model successfully saved to {filepath}")

def load_model(filename):
    """Loads a trained Scikit-learn model from file."""
    filepath = os.path.join(DATA_DIR, filename)
    if os.path.exists(filepath):
        print(f"Loading model from {filepath}...")
        with open(filepath, 'rb') as file:
            return pickle.load(file)
    print(f"Model file not found at {filepath}. Will require training.")
    return None

def save_articles(articles, filename="articles.json"):
    """Saves a list of articles as a JSON file."""
    filepath = os.path.join(DATA_DIR, filename)
    os.makedirs(os.path.dirname(filepath), exist_ok=True)
    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(articles, f, ensure_ascii=False, indent=4)
    print(f"Articles saved to {filepath}")

def load_articles(filename="articles.json"):
    """Loads articles from a JSON file."""
    filepath = os.path.join(DATA_DIR, filename)
    if os.path.exists(filepath):
        with open(filepath, 'r', encoding='utf-8') as f:
            return json.load(f)
    return []
