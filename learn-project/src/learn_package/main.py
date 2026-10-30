# src/your_package/main.py
import logging

from config import setup_logging


def main():
    setup_logging()  # 全局只配一次
    logger = logging.getLogger(__name__)
    logger.info("应用启动")


if __name__ == "__main__":
    main()
