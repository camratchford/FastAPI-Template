default_log_config = {
    "version": 1,
    "disable_existing_loggers": True,
    "formatters": {
        "default": {
            "format": "%(process)d:%(filename)s:%(module)s.%(funcName)s -> %(lineno)d:%(message)s",
        }
    },
    "handlers": {
        # "file": {
        #     "formatter": "default",
        #     "level": "ERROR",
        #     "class": "logging.handlers.RotatingFileHandler",
        #     "filename": "/var/log/pymetrics.log",
        #     "maxBytes": 1074120,
        #     "backupCount": 3,
        #     "encoding": "utf-8",
        #     "delay": False
        # },
        "custom": {
            "()": "rich.logging.RichHandler"
        }
    },
    "loggers": {
        "pymetrics": {
            "handlers": ["custom"],
            "level": "INFO",
            "propagate": True
        },
    }
}

swagger_ui_config = {
    "syntaxHighlight": True,
    'requestSnippetsEnabled': True,
    'requestSnippets': {
        'generators': {
            'curl_bash': {
              'title': "cURL (bash)",
              'syntax': "bash"
            },
            'curl_powershell': {
              'title': "cURL (PowerShell)",
              'syntax': "powershell"
            }
        },
        'defaultExpanded': True,
        'languages': None,
    }
}