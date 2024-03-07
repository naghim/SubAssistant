import os

BASE_DIR = os.path.dirname(__file__)
RESOURCES_DIR = os.path.join(BASE_DIR, 'resources')

with open('baseres_dir.txt', 'w') as f:
    f.write(BASE_DIR)