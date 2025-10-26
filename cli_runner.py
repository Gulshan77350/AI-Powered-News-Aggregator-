from source_connector import fetch_multi_source_content
from content_analyzer import analyze_content, ensure_models_loaded
from persistence_layer import save_articles
from display_renderer import render_results

def execute_pipeline(search_query: str = "World Events"):
    """
    Executes the full pipeline: Fetch -> Analyze -> Display.
    """
    print(f"Starting News Aggregation Pipeline for query: '{search_query}'")
    
    try:
        
        ensure_models_loaded()
        
        
        articles = fetch_multi_source_content(search_query, limit=15)
        
        if not articles:
            print("Pipeline finished: No content was retrieved.")
            return

        # Step 3: Classify articles
        print("\n--- Initiating Content Analysis (Topic/Bias Classification) ---")
        classified_articles = []
        for article in articles:
            topic, bias = analyze_content(article)
            
            # Augment article dictionary with results
            article['topic'] = topic
            article['bias'] = bias
            classified_articles.append(article)
            print(f"  - Classified: [{topic} | {bias}] {article['title'][:50]}...")

        # Step 4: Save and Display results
        save_articles(classified_articles, f"{search_query.replace(' ', '_').lower()}_classified.json")
        render_results(classified_articles, search_query)

    except Exception as e:
        print(f"\n--- A Critical Error Occurred ---")
        print(f"Pipeline execution failed: {e}")


if __name__ == "__main__":
    # Example execution (in a real app, this would take user input)
    DEFAULT_QUERY = "Technology and Climate"
    execute_pipeline(DEFAULT_QUERY)
