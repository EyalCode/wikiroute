import requests, sys



def get_links_from_page(title):
    """Returns a set of page names of all the pages linked from 'title' page. 

    Args:
        title: The page to find links from.

    Returns:
        List of links.

    """
    URL = "https://en.wikipedia.org/w/api.php"
    PARAMS = {
        "action": "query",
        "format": "json",
        "titles": title,
        "prop": "links",
    }
    HEADER = {'User-Agent' : 'Studying_Project/0.0 (Eyal Gilad; eyalcha@gmail.com)'}

    links = set()
    S = requests.Session()
    while True:
        R = S.get(url=URL, params=PARAMS, headers=HEADER)
        DATA = R.json()
        links.update(json_data_to_set(DATA))
        if 'continue' not in DATA:
            break
        PARAMS['continue'] = DATA['continue']['continue']
        PARAMS['plcontinue'] = DATA['continue']['plcontinue']

    return links


def json_data_to_set(data):
    PAGES = data["query"]["pages"]
    links = set()

    for k, v in PAGES.items():
        for l in v["links"]:
            links.add(l["title"])

    return links   

class Page:
    def __init__(self, title, depth, link_to):
        self.title = title
        self.link_to = link_to
        self.links_from = get_links_from_page(title)
        self.depth = depth
        print(title)


if __name__ == '__main__':
    root = sys.argv[1]
    target = sys.argv[2]

    get_links_from_page(root)




