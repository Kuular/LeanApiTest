import os

from dotenv import load_dotenv


class Environments(object):

    def __init__(self):
        dotenv_path = os.path.join(os.path.dirname(__file__), ".env")
        if os.path.exists(dotenv_path):
            load_dotenv(dotenv_path)
        self.disk_cache_dir_path = os.path.join(os.path.dirname(__file__), ".disk_cache_dir")
        if not os.path.exists(self.disk_cache_dir_path):
            os.makedirs(self.disk_cache_dir_path)

    @property
    def get_token(self):
        return os.environ["lean_token"]
