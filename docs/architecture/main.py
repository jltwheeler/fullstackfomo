from architecture import worker, web, api

# GRAPH_ATTR = {"bgcolor": "transparent"}
PATH = "static"

if __name__ == "__main__":
    worker(path=PATH)
    web(path=PATH)
    api(path=PATH)