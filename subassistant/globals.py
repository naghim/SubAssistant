import os

BASE_DIR = os.path.dirname(__file__)
RESOURCES_DIR = os.path.join(BASE_DIR, 'resources')

if not os.path.isdir(RESOURCES_DIR):
    BASE_DIR = os.path.abspath(os.path.join(BASE_DIR, '..'))
    RESOURCES_DIR = os.path.join(BASE_DIR, 'resources')
