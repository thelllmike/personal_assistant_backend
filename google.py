import requests
from bs4 import BeautifulSoup

def search_google(query):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
    search_url = f"https://www.google.com/search?q={query}"
    response = requests.get(search_url, headers=headers)
    
    if response.status_code == 200:
        return response.text
    else:
        return None

def extract_snippet(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')
    # Attempt to find the snippet, note that this might change as Google updates their layout
    snippet_div = soup.find('div', class_="BNeawe s3v9rd AP7Wnd")
    if snippet_div:
        return snippet_div.text
    else:
        return "Answer snippet not found."

def get_answer_for_question(question):
    html_content = search_google(question)
    if html_content:
        answer = extract_snippet(html_content)
        return answer
    else:
        return "Failed to retrieve answer."

# Example usage
question = "Who is the president of the United States?"
answer = get_answer_for_question(question)
print(f"Question: {question}")
print(f"Answer: {answer}")
