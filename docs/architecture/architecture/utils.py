import os


def create_kwargs(
    name: str, graph_attr: dict = None, path: str = None
) -> dict:
    kwargs = {"name": name, "show": False}
    if graph_attr:
        kwargs["graph_attr"] = graph_attr
    if path:
        kwargs["filename"] = os.path.join(
            path, "_".join(name.lower().split(" "))
        )
    return kwargs
