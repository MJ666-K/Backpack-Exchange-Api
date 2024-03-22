import logging
from logging import handlers
import os

os.makedirs("./logs", exist_ok=True)

sh = logging.StreamHandler()

level_relations = {
    "debug": logging.DEBUG,
    "info": logging.INFO,
    "warning": logging.WARNING,
    "error": logging.ERROR,
}


__logger_dict__ = {}


def getLogger(
    name,
    level="info",
    when="D",
    backCount=3,
    fmt="%(asctime)s %(filename)11s[%(lineno)5d]-[%(threadName)30s] - %(levelname)5s: %(message)s",
    filename=None,
):
    logger = __logger_dict__.get(f"{name}:{level}", None)
    if logger is None:
        logger = logging.getLogger(name)
        format_str = logging.Formatter(fmt)
        logger.setLevel(level_relations.get(level))

        sh.setFormatter(format_str)
        filename = f"./logs/{name}.log" if filename is None else filename
        th = handlers.TimedRotatingFileHandler(
            filename=filename,
            when=when,
            backupCount=backCount,
            encoding="utf-8",
        )

        th.suffix = "%Y-%m-%d.log"
        th.setFormatter(format_str)
        logger.addHandler(sh)
        logger.addHandler(th)
        __logger_dict__[f"{name}:{level}"] = logger
    return logger
