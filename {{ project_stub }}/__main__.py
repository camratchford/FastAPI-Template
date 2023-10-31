import logging

import uvicorn

logger = logging.getLogger(__name__)


def main(conf):
    logger.info(f"Starting server on http://{conf.host}:{str(conf.port)} (Press CTRL+C to quit)")
    uvicorn.run("{{ project_stub }}.server.routes:app", port=conf.port, host=conf.host, )
