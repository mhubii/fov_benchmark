import yaml
import numpy as np

# taken from https://stackoverflow.com/questions/49338166/python-intersection-over-union
def IoU(a: np.array, b: np.array) -> float:
    a = a.astype(bool)
    b = b.astype(bool)
    overlap = a*b
    union = a+b
    return overlap.sum()/float(union.sum())


def load_yaml(path: str) -> dict:
    try:
        with open(path, 'r') as f:
            yml = yaml.load(f, Loader=yaml.FullLoader)
        return yml
    except:
       raise RuntimeError('Failed to load {}'.format(path))
