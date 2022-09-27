import os.path

my_dir = os.path.dirname(__file__)
project_root_dir = os.path.abspath(os.path.join(my_dir, ".."))

__all__ = [
    'project_root_dir',
]