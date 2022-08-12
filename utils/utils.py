from pathlib import Path
import os


def increment_path(path, exist_ok=False, sep='', mkdir=False):
    path = Path(path)
    if path.exists() and not exist_ok:
        path, suffix = (
            path.with_suffix(''),
            path.suffix) if path.is_file() else (
            path, '')

        for n in range(2, 9999):
            p = f'{path}{sep}{n}{suffix}'
            if not os.path.exists(p):
                break
        path = Path(p)

    if mkdir:
        Path(os.path.dirname(path)).mkdir(parents=True, exist_ok=True)

    return path
