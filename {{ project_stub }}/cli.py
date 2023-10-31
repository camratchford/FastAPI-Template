import os
import logging
from pathlib import Path

import click
from {{ project_stub }}.config import config
from {{ project_stub }}.__main__ import main

logger = logging.getLogger("__name__")



@click.command(context_settings={"auto_envvar_prefix": "PYMETRICS"})
@click.option(
    "-c",
    "--config-file",
    type=str,
    help="The location of the pymetrics.yml configuration files",
    required=False,
)
@click.option(
    "-l",
    "--log-path",
    type=str,
    help="The location of the log file",
    required=False,
)
@click.option(
    "-h",
    "--listen-host",
    type=str,
    help="The IP address/Hostname which Pymetrics API will bind to",
    required=False,
)
@click.option(
    "-p",
    "--listen-port",
    type=int,
    help="The TCP port which Pymetrics API will bind to",
    required=False,
)
@click.option(
    "-u",
    "--sql-alchemy-uri",
    type=str,
    help="The SQLAlchemy URI for the database",
    required=False,
)
@click.option(
    "--skip-setup",
    type=bool,
    help="When True, the install directory and contents will not be created",
    required=False,
    is_flag=True
)
def run(
        config_file,
        log_path,
        listen_host,
        listen_port,
        sql_alchemy_uri,
        skip_setup,
):
    if config_file:
        config.configure_from_file(config_file)
    if log_path:
        config.log_path = log_path
    if listen_host:
        config.host = listen_host
    if listen_port:
        config.port = listen_port
    if sql_alchemy_uri:
        config.sql_alchemy_uri = sql_alchemy_uri

    if skip_setup:
        config.skip_setup = skip_setup

    config.configure_basic_logging()
    config.configure_logging()
    config.setup()

    main(config)

