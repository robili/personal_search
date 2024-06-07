import requests
import keys


def get_bing_results(query):
    search_url='https://api.bing.microsoft.com/v7.0/search'
    headers = {"Ocp-Apim-Subscription-Key": keys.BING_API_KEY}
    params = {"q": query, "textDecorations": True, "textFormat": "HTML"}
    
    response = requests.get(search_url, headers=headers, params=params)
    search_results = response.json()
    
    return search_results.get("webPages", {}).get("value", [])


def get_google_results(query):
    search_url = "https://www.googleapis.com/customsearch/v1"
    params = {"key": keys.GOOGLE_API_KEY, "cx": keys.GOOGLE_CSE_ID, "q": query}
    
    response = requests.get(search_url, params=params)
    search_results = response.json()
    
    return search_results.get("items", [])


def bing(query):    
    results = get_bing_results(query)
    # id, name, url, datePublished, datePublishedDisplayText, isFamilyFriendly, displayUrl, snippet, dateLastCrawled, cachedPageUrl, language, isNavigational, noCache
    for result in results: #.get("webPages", {}).get("value", []):
        print(result)
        print()
    
    # print(results)


def google(query):
    results = get_google_results(query)
    # kind, title, htmlTitle, link, displayLink, snippet, htmlSnippet, formattedUrl, htmlFormattedUrl, pagemap
    for item in results: # .get("items", []):
        print(item)
        print()


if __name__ == "__main__":
    query = "What are the largest countries in the world"
    bing(query)