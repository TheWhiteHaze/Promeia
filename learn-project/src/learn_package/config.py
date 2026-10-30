import logging.config
import tomllib
from pathlib import Path


def setup_logging(config_path: Path = Path("configs/logging.toml")) -> None:
    with config_path.open("rb") as f:
        cfg = tomllib.load(f)
    # logging.config.dictConfig 需要 dict，toml 读出来正好是 dict
    logging.config.dictConfig(cfg)
