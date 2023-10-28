import json
import logging
import os
import logging.handlers
import logging.config

from pathlib import Path

import yaml


from app.defaults import default_log_config


class Config(object):
    def __init__(self):
        self.setup_run = False

        self.disallowed_file_attrs = [
            "base_dir",
            "config_file_path",
            "config_file",
            "app",
            "db",
        ]
        self.base_dir = Path(__file__).resolve().parent
        self.config_file_path = ""
        self.config_file = self.config_file_path

        self.log_path = "project.log"
        self.skip_setup = False

        # Server settings
        self.host = "0.0.0.0"
        self.port = 8080

        # Logic settings
        self.log_config = None

        self.app = None
        self.sql_alchemy_uri = "sqlite+aiosqlite:///./test.db"
        self.db = None
        self.secret_key = "Run: 'openssl rand -hex 64' for a secure nice secret key, use Hunter2 for a bad one"

    def configure_from_file(self, config_file_path):
        if config_file_path:
            self.config_file_path = Path(config_file_path).resolve()
        if os.path.exists(self.config_file_path):
            self.config_file = self.config_file_path

        loaded_config = {}
        if self.config_file:
            if ".yaml" in self.config_file.suffixes or ".yml" in self.config_file.suffixes:
                with open(self.config_file, "r") as file:
                    loaded_config = yaml.safe_load(file)
            elif ".json" in self.config_file.suffixes:
                with open(self.config_file, "r") as file:
                    loaded_config = json.load(file)
            if loaded_config:
                for attr in loaded_config.keys():
                    if hasattr(self, attr) and attr not in self.disallowed_file_attrs:
                        setattr(self, attr, loaded_config[attr])
                        if len(attr) > 3 and attr[-3:] == "dir" or len(attr) > 4 and attr[-4:] == "path":
                            setattr(self, attr, Path(loaded_config[attr]).resolve())
                            print(getattr(self, attr))

    def setup(self):
        ...

    @staticmethod
    def configure_basic_logging():
        pass
        # logging.config.dictConfig(default_log_config)

    def configure_logging(self):
        if self.log_config:
            logging_config = self.log_config
            self.log_config["log_path"] = self.log_path
            logging.config.dictConfig(logging_config)


config = Config()
