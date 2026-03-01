import sys
import requests
from bs4 import BeautifulSoup

def my_code(input_url):
    try:
        response_n = requests.get(input_url) 
        html = response_n.text
        soup = BeautifulSoup(html, "html.parser")
    except Exception as e: 
        print(e)

    print("\n#Page-Title")
    if soup.title:
        print(soup.title.text.strip())
    else:
        print("No title available")

    print("\n#Page-Body")
    if soup.body:
        for tag_n in soup(["script", "style"]):
            tag_n.decompose()
        body_text = soup.body.get_text(separator="\n", strip=True)
        print(body_text)
    else:
        print("No body available")

    print("\n#Page-Link")
    for link_n in soup.find_all("a"):
        href = link_n.get("href")
        if href:
            print(href)

def main():
    if len(sys.argv) < 2:
        print("Usage: python script.py <URL>")
        sys.exit(1)

    sys_url = sys.argv[1]
    my_code(sys_url)

if __name__ == "__main__":
    main()
