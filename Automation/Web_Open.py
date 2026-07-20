import webbrowser as wb
from .DATA.website_data import websites

def web_open(webname):
    website_name = webname.lower().split("and")
    counts = {}

    normalized_websites = {name.lower() : url for name, url in websites.items()}

    for name in website_name:
        counts[name.strip()] = counts.get(name.strip(), 0) + 1

    urls_to_open = []

    for name, count in counts.items():
        if name in normalized_websites:
            urls_to_open.extend([normalized_websites[name]] * count)
        else:
            print(f'{name} not found in dictionary.')

    for url in urls_to_open:
        wb.open(url)

if __name__ == "__main__":
    while True:
        web_input = input('Web name: ')
        web_open(web_input)