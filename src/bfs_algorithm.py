from wikimedia_api_interaction import Page
import sys


def breadth_first_search(src, target, depth = 3):
    """Returns a list of pages of the first Route to be found, with . 

    Args:
        src: The page to find links from.

    Returns:
        List of links.

    """

    root = Page(src, 0, "None")
    print(root.links_from)
    queue = [root]
    targets_pages = set()
    is_found = False

    while queue:
        current = queue.pop(0)
        if is_found and current.depth > depth:
            break
        if current.title == target:
            targets_pages.add(current)
            is_found = True
            depth = current.depth
        else:
            if current.depth >= depth:
                break
            for title in current.links_from:
                page = Page(title, current.depth + 1, current)
                queue.append(page)

    paths = set()
    for target_page in targets_pages:
        set.add(get_path(target_page))

    return paths

        
def get_path(page):
    if page.link_to == "None":
        return [page.title]
    return get_path(page.link_to) + [page.title]


if __name__ == '__main__':
    root = sys.argv[1]
    target = sys.argv[2]
    print(breadth_first_search('Caxcan', target))
