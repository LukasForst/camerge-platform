import os.path


def data(f: str) -> str:
    if not f.startswith('/'):
        f = f'/{f}'
    if os.path.exists('data'):
        return f'data{f}'
    else:
        return f'tests/data{f}'
