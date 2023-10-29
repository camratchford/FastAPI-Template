import os
import logging
from pathlib import Path

import click
from app.config import config
from app.__main__ import main

from app.commands.create_user import create_superuser

logger = logging.getLogger("__name__")


@click.group(name="app")
@click.pass_context
def cli(
        ctx,
):
    pass


@cli.command(name="run-server", context_settings={"auto_envvar_prefix": config.envvar_prefix})
@click.option(
    "--config-file",
    type=click.Path(exists=True, file_okay=True, dir_okay=False, resolve_path=True),
    help="The location of the pymetrics.yml configuration files",
    required=False,
)
@click.option(
    "--sql-alchemy-uri",
    "-u",
    type=str,
    help="The SQL-Alchemy URI for the database",
    required=False,
)
@click.option(
    "--log-path",
    "-l",
    type=click.Path(exists=False, file_okay=True, dir_okay=False, resolve_path=True),
    help="The location of the log file",
    required=False,
)
@click.option(
    "--skip-setup",
    type=bool,
    help="When True, the install directory and contents will not be created",
    required=False,
    is_flag=True
)
@click.option(
    "--export-config",
    type=bool,
    help="When True, the current set pf configuration parameters will be exported to $PWD as ./export_config.yml",
    required=False,
    is_flag=True
)
@click.option(
    "--listen-host",
    type=str,
    help="The IP address/Hostname which Pymetrics API will bind to",
    required=False,
)
@click.option(
    "--listen-port",
    type=click.IntRange(min=1, max=65535),
    help="The TCP port which Pymetrics API will bind to",
    required=False,
)
def run(
        config_file,
        sql_alchemy_uri,
        log_path,
        skip_setup,
        export_config,
        listen_host,
        listen_port,
):
    if config_file:
        config.configure_from_path(config_file)
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

    config.configure_logging()
    config.setup()

    if export_config:
        config.export_config()

    main(config)


@cli.command(context_settings={"auto_envvar_prefix": "APP"}, no_args_is_help=True)
@click.option(
    "--config-file",
    type=click.Path(exists=True, file_okay=True, dir_okay=False, resolve_path=True),
    help="The location of the pymetrics.yml configuration files",
    required=False,
)
@click.option(
    "--sql-alchemy-uri",
    "-u",
    type=str,
    help="The SQL-Alchemy URI for the database",
    required=False,
)
@click.option(
    "--log-path",
    "-l",
    type=click.Path(exists=False, file_okay=True, dir_okay=False, resolve_path=True),
    help="The location of the log file",
    required=False,
)
@click.option(
    "--skip-setup",
    type=bool,
    help="When True, the install directory and contents will not be created",
    required=False,
    is_flag=True
)
@click.option(
    "--skip-setup",
    type=bool,
    help="When True, the install directory and contents will not be created",
    required=False,
    is_flag=True
)
@click.option(
    "--export-config",
    type=bool,
    help="When True, the current set pf configuration parameters will be exported to $PWD as ./export_config.yml",
    required=False,
    is_flag=True
)
@click.option(
    "--email",
    type=str,
    help="The email address that the new superuser will use to log in with",
    required=True,
)
@click.option(
    "--password",
    type=str,
    prompt=True,
    hide_input=True,
    confirmation_prompt=True,
    help="The password for the new superuser",
)
@click.option(
    "--first-name",
    type=str,
    help="The new superuser's first name",
    required=True,
)
@click.option(
    "--last-name",
    type=str,
    help="The new superuser's last name",
    required=True,
)
def create_superuser(
        config_file,
        sql_alchemy_uri,
        log_path,
        skip_setup,
        export_config,
        email,
        password,
        first_name,
        last_name
):
    if config_file:
        config.configure_from_path(config_file)
    if log_path:
        config.log_path = log_path
    if sql_alchemy_uri:
        config.sql_alchemy_uri = sql_alchemy_uri
    if skip_setup:
        config.skip_setup = skip_setup

    config.configure_logging()
    config.setup()

    if export_config:
        config.export_config()

    create_superuser(email, password, first_name, last_name)