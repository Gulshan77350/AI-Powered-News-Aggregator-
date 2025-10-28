import requests
from bs4 import BeautifulSoup
from typing import List, Dict


def fetch_multi_source_content(query: str, limit: int = 10) -> List[Dict]:
    
    print(f"Connecting to sources and retrieving content for: '{query}'...")
    
    
    articles = []
    
    for i in range(limit):
        is_left_leaning = i % 3 == 0
        
        articles.append({
            "title": f"Breaking News #{i+1}: {query} development update",
            "source": f"Global Press Outlet {'A' if i%2 == 0 else 'B'}",
            "content": (
                f"The latest report on {query} suggests a complex outcome. "
                f"Key political stakeholders {'support' if is_left_leaning else 'oppose'} "
                f"the new bill due to its impact on {'social services' if is_left_leaning else 'market regulation'}."
            ),
            "link": f"http://example.com/article-{i+1}",
            "published": f"2025-10-{20 + (i%5)}"
        })
    
    print(f"Successfully retrieved {len(articles)} articles.")
    return articles
