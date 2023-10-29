import json
import logging
import os
import logging.handlers
import logging.config

from pathlib import Path

import yaml


from app.defaults import default_log_config


class Config(object):
    """
    Config object to store, load, and export application configuration parameters
    """
    def __init__(self):
        self.setup_run = False

        self.disallowed_file_attrs = [
            "setup_run",
            "disallowed_file_attrs",
            "base_dir",
            "config_file_path",
            "config_file",
            "app",
            "db",
        ]
        self.config_parameters = [
            "host", "port", "log_config",
            "sql_alchemy_uri", "secret_key",
            "log_path", "skip_setup"
        ]
        self.envvar_prefix = "APP"
        self.base_dir = Path(__file__).resolve().parent
        self.config_file_path = ""
        self.config_file = self.config_file_path

        # Server settings
        self.host = "0.0.0.0"
        self.port = 8080

        # Logic settings
        self.log_config = {}
        self.sql_alchemy_uri = "sqlite+aiosqlite:///./test.db"
        self.secret_key = "Run: 'openssl rand -hex 64' for a secure nice secret key, use Hunter2 for a bad one"
        self.log_path = "project.log"
        self.skip_setup = False

        self.app = None
        self.db = None

    def configure_from_env(self):
        f""" 
        - If any of the config class' attrs (prefixed with {self.envvar_prefix}) appear as an environment variable,
          the variable values as loaded into the corresponding config object property.
        - If the env variable '{self.envvar_prefix}_CONFIG_PATH' exists:
          - Uses the value of the env var '{self.envvar_prefix}_CONFIG_PATH' as the config_file_path argument 
            for self.configure_from_path.
          - Invokes self.configure_from_path, overwriting any other environment variable parameters used.
        """
        for attr in self.config_parameters:
            envvar_name = f"{self.envvar_prefix}_{attr.upper()}"
            envvar_value = os.environ.get(envvar_name, "")
            if envvar_value:
                setattr(self, attr, envvar_value)

        if os.environ.get(f"{self.envvar_prefix}_CONFIG_PATH", ""):
            self.configure_from_path(os.environ.get("APP_CONFIG_PATH", ""))

    def configure_from_path(self, config_file_path):
        """
        - Reads in a yaml config file, load top level dictionary keys that match the config class'set of attrs.
        - Will ignore any keys that are contained in the 'self.disallowed_file_attrs' list.
        - Any attrs ending in 'dir' or 'path' with be cast into a Path object, then resolved.
        """
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

    def setup(self):
        """Place to put post-config / pre-server run tasks. If everything works, make self.setup_run = True"""

        self.setup_run = True

    def configure_logging(self):
        """
        - Configures logger with log_config property.
        - If log_config is empty, a default value is set
        """
        logging_config = default_log_config

        if self.log_config:
            logging_config = self.log_config

        if self.log_path and not logging_config.get("log_path"):
            logging_config["log_path"] = self.log_path
            self.log_config = logging_config

        logging.config.dictConfig(logging_config)

    def export_config(self):
        """
        - Exports the post-configuration config parameters to ./config_export.yml
        """

        export_dict = {}
        for attr in self.config_parameters:
            export_dict[attr] = getattr(self, attr)

        config_export = Path(os.getcwd()).joinpath("config_export.yml").resolve()

        with open(config_export, "w") as file:
            yaml.dump(export_dict, file)


config = Config()
