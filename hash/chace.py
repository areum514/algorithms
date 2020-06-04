cache = {}


def get_page(url):
    if cache.get(url):
        print("instantly give url")
        return cache[url]
    else:
        data = get_data_from_server(url)
        cache[url] = data
