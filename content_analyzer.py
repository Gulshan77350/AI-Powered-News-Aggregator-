import nltk
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import make_pipeline
from typing import Dict, Tuple
from persistence_layer import save_model, load_model

# --- Model Artifact Names ---
TOPIC_MODEL_FILE = "topic_classifier.pkl"
BIAS_MODEL_FILE = "bias_classifier.pkl"

# --- Training Data Placeholder ---
# This data simulates a dataset used to train the classifiers.
TRAINING_DATA = [
    ("The Fed signals interest rate cuts to boost economy.", "Economy", "Neutral"),
    ("New regulations target corporate tax loopholes.", "Politics", "Left"),
    ("Next-gen AI chip released by major tech firm.", "Technology", "Neutral"),
    ("Conservative group rallies against federal spending.", "Politics", "Right"),
    ("Study confirms ozone layer is recovering well.", "Science", "Neutral"),
    ("Union negotiations break down over minimum wage.", "Economy", "Left"),
    ("Market analysts predict a strong year for banking.", "Economy", "Right"),
]

# Download necessary NLTK data (if not already present)
try:
    nltk.data.find('corpora/stopwords')
except nltk.downloader.DownloadError:
    nltk.download('stopwords')

def train_analysis_models(data):
    """Trains and saves the Topic and Bias classification models."""
    texts = [d[0] for d in data]
    topics = [d[1] for d in data]
    biases = [d[2] for d in data]

    # Topic Classification Model (using TF-IDF and Naive Bayes)
    topic_model = make_pipeline(TfidfVectorizer(stop_words=nltk.corpus.stopwords.words('english')), 
                                MultinomialNB())
    topic_model.fit(texts, topics)
    save_model(topic_model, TOPIC_MODEL_FILE)

    # Bias Detection Model
    bias_model = make_pipeline(TfidfVectorizer(stop_words=nltk.corpus.stopwords.words('english')), 
                               Biases=MultinomialNB())
    bias_model.fit(texts, biases)
    save_model(bias_model, BIAS_MODEL_FILE)
    
    print("All required NLP models trained and saved.")
    return topic_model, bias_model

# Load models upon module import
TOPIC_MODEL = load_model(TOPIC_MODEL_FILE)
BIAS_MODEL = load_model(BIAS_MODEL_FILE)

def ensure_models_loaded():
    """Checks if models are loaded and trains them if they are missing."""
    global TOPIC_MODEL, BIAS_MODEL
    if not TOPIC_MODEL or not BIAS_MODEL:
        print("Required models are missing. Initiating training...")
        TOPIC_MODEL, BIAS_MODEL = train_analysis_models(TRAINING_DATA)
        # Re-import to ensure global variables are updated if training was successful
        if not TOPIC_MODEL or not BIAS_MODEL:
            raise RuntimeError("Failed to load or train required classification models.")

def analyze_content(article: Dict) -> Tuple[str, str]:
    """Predicts the topic and bias for a given article dictionary."""
    ensure_models_loaded()
    
    # Concatenate title and content for better feature extraction
    text_to_classify = article.get("title", "") + " " + article.get("content", "")
    
    # Predict Topic
    topic = TOPIC_MODEL.predict([text_to_classify])[0]
    
    # Predict Bias
    bias = BIAS_MODEL.predict([text_to_classify])[0]
    
    return topic, bias
