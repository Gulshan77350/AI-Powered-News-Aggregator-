from typing import List, Dict

def render_results(classified_articles: List[Dict], query: str):
    """
    Renders the final classified news articles to the console.
    
    In a full-stack project (React.js, Node.js), this function would instead 
    format the data and send it as a JSON response to the frontend.
    """
    print("\n" + "="*80)
    print(f"               AI-POWERED NEWS AGGREGATOR | RESULTS FOR: '{query}'")
    print("="*80)
    
    if not classified_articles:
        print("No classified articles to display.")
        return

    
    topics = {}
    for article in classified_articles:
        topic = article.get('topic', 'UNCATEGORIZED')
        if topic not in topics:
            topics[topic] = []
        topics[topic].append(article)

    
    for topic, article_list in topics.items():
        print(f"\n--- TOPIC: {topic.upper()} ({len(article_list)} Articles) ---")
        print("-" * (len(topic) + 12))
        
        for i, article in enumerate(article_list):
            print(f"  [{i+1}] {article['title']}")
            print(f"      Bias: **{article.get('bias', 'N/A')}** | Source: {article.get('source', 'N/A')}")
            print(f"      Link: {article.get('link', 'N/A')}")
            
    print("\n" + "="*80)
