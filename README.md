# AI-Powered News Aggregator Course Project

This is the Python core for a news aggregation platform designed to fetch multi-source content, classify it using NLP, and provide basic political bias detection.

## 🚀 Key Features

* **Multi-Source Content:** Connects to external APIs/sources to gather diverse news content.
* **Topic Classification (NLP):** Automatically categorizes articles into predefined topics (e.g., Politics, Technology, Economy).
* **Bias Detection (ML):** Identifies and flags the political slant of articles (Left, Right, Neutral).

## 🛠 Tech Stack

* **Frontend (Conceptual):** React.js
* **Backend/API:** Node.js
* **Database:** MongoDB
* **Data Processing/ML Core:** Python (NLTK, Scikit-learn, Requests)

## 📦 Project Structure (Python Core)

| File Name | Description |
| :--- | :--- |
| `cli_runner.py` | The main execution script; runs the Fetch -> Analyze -> Display pipeline. |
| `source_connector.py` | Handles connection and retrieval logic from external news sources/APIs. |
| `content_analyzer.py` | Core NLP module for training and running Topic and Bias classification models. |
| `persistence_layer.py` | Utility functions for saving and loading data (trained models, articles). |
| `display_renderer.py` | Formats and outputs the final, classified results (console output). |
| `requirements.txt` | Lists all necessary Python dependencies. |

## ⚙️ Setup and Execution

1.  **Install Python dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

2.  **Run the main script:**
    ```bash
    python cli_runner.py
    ```
    *(The script will automatically train the required models if they are not already saved in the `./data` directory.)*
