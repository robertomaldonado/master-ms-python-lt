

def remove_prefix(text, prefix):
    if text.startswith(prefix):
        return text[len(prefix):]
    return text


def path(route: str, prefix: str = "") -> str:
    route = remove_prefix(route, "/")
    prefix = remove_prefix(prefix, "/")

    if prefix == "":
        prefix = "/"

    if route == "" and prefix == "/":
        print("Registering: /")
        return "/"

    if prefix != "/" and route == "":
        print(f"Registering: /{prefix}")
        return f"/{prefix}"

    print(f"Registering: /{prefix}/{route}")
    return f"/{prefix}/{route}"