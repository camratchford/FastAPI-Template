<!--suppress ALL -->
<h1 align="center">{{ project_name }}</h1>
<p align="center">
{{ project_description }}
</p>

---

> <p align="center">This is a work in progress, subject to many changes and new instabilities / brokenness.</p>

## Getting started

- Get acquainted with the documentation [here]('{{ project_docs_url }}')
- Review the API specification [here]('{{ project_api_spec }}')

### Install {{ project_name }}:

```bash
python3 -m venv venv
source venv/bin/activate
pip install git+{{ project_repo }}
```

## {{ cli_executable_name }} CLI options

| Configuration Item | Abrv  | Keyword Argument  | Config File Key | Default                         | Required | Description                                                        | 
|--------------------|-------|-------------------|-----------------|---------------------------------|----------|--------------------------------------------------------------------|
| config_file        | -c    | --config          | N/A             | ""                              | No       | The location of the yaml configuration file.                       |
| log_path           | -l    | --log-path        | log_path        | ""                              | No       | The location of the log file                                       |
| host               | -h    | --listen-host     | host            | "127.0.0.1"                     | No       | The IP address/Hostname which Pymetrics API will bind to           |
| port               | -p    | --listen-port     | port            | 8080                            | No       | The TCP port which Pymetrics API will bind to                      |
| sql_alchemy_uri    | -u    | --sql-alchemy-uri | sql_alchemy_uri | "sqlite+aiosqlite:///./test.db" | No       | The SQLAlchemy URI for the database                                |
| skip_setup         | N/A   | --skip-setup      | skip_setup      | False                           | No       | "When True, the install directory and contents will not be created |

