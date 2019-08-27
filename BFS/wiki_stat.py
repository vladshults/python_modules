from bs4 import BeautifulSoup
import re
import os


# Вспомогательная функция для построения списка связности
def build_tree(path):
    # Искать ссылки можно как угодно, не обязательно через re
    link_re = re.compile(r"(?<=/wiki/)[\w()]+")
    # Словарь вида {"filename1": None, "filename2": None, ...}
    files_list = os.listdir(path)
    files = dict.fromkeys(files_list)
    # TODO Проставить всем ключам в files правильного родителя в значение, начиная от start
    for fil in files_list:
        links_list = list()
        with open(os.path.join('wiki', fil), 'r') as of:
            text = of.read()
            finds = re.findall(link_re, text)
        for r in finds:
            if r not in files_list:
                continue
            elif r == fil:
                continue
            else:
                links_list.append(r)
        if not links_list:
            pass
        else:
            files[fil] = set(links_list)
    return files


def bfs_paths(graph, start, goal):
    queue = [(start, [start])]
    while queue:
        (vertex, path) = queue.pop(0)
        if graph[vertex] is None:
            continue
        for next_step in graph[vertex] - set(path):
            if next_step == goal:
                yield path + [next_step]
            else:
                queue.append((next_step, path + [next_step]))


def shortest_path(graph, start, goal):
    try:
        return next(bfs_paths(graph, start, goal))
    except StopIteration:
        return None


def html_body_text(text):
    soup = BeautifulSoup(text, "html.parser")
    body = soup.find(id="bodyContent")
    return body


def consecutive_links(body):
    tag = body.find_next("a")
    linkslen = -1
    while (tag):
        curlen = 1
        for tag in tag.find_next_siblings():
            if tag.name != 'a':
                break
            curlen += 1
        if curlen > linkslen:
            linkslen = curlen
        tag = tag.find_next("a")
    return linkslen


def parse(start, end, path):
    tree = build_tree(path)
    if start == end:
        short_path = [start]
    else:
        short_path = shortest_path(tree, start, end)
    stats = dict.fromkeys(short_path)
    for item in short_path:
        stats_list = list()
        # prepare html & html.body
        file_path = os.path.join('wiki', item)
        with open(file_path, 'r') as file_content:
            html = file_content.read()
        body = html_body_text(html)
        # images wit width >= 200
        images_re = re.compile(r"img.+?width=\"(\d+)\"")
        images = re.findall(images_re, html)
        images_count = 0
        for width in images:
            if int(width) >= 200:
                images_count += 1
        stats_list.append(images_count)
        stats[item] = stats_list
        # headers with E, C, T at start of string
        headers_count = 0
        title_regex = re.compile(r">[ECT]")
        for h in ["h1", "h2", "h3", "h4", "h5", "h6"]:
            for header in body.find_all(h):
                if re.search(title_regex, str(header)):
                    headers_count += 1
        stats_list.append(headers_count)
        # consecutive_links
        c_links = consecutive_links(body)
        stats_list.append(c_links)
        # ul, ol without ul inside
        uls_count = 0
        for ul in ["ul", "ol"]:
            uls_list = body.find_all(ul)
            if not uls_list:
                continue
            for item in uls_list:
                if not item.find_parent(ul):
                    uls_count += 1
        stats_list.append(uls_count)

    return stats
