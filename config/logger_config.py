import logging
import sys
from pathlib import Path

# Create logs folder if it doesn't exist
LOGS_DIR = Path("logs")
LOGS_DIR.mkdir(exist_ok=True)


def setup_logging(level: int = logging.INFO) -> None:
    """Centralized logging setup."""
    log_format = (
        "%(asctime)s | %(levelname)-8s | %(name)s:%(funcName)s:%(lineno)d - %(message)s"
    )

    # Base config
    logging.basicConfig(
        level=level,
        format=log_format,
        handlers=[
            # Handler 1: Output to console
            logging.StreamHandler(sys.stdout),
            # Handler 2: Write to log file
            logging.FileHandler(LOGS_DIR / "app.log", encoding="utf-8"),
        ],
    )

    # Silence overly verbose third-party loggers
    logging.getLogger("asyncio").setLevel(logging.WARNING)
    logging.getLogger("urllib3").setLevel(logging.WARNING)
