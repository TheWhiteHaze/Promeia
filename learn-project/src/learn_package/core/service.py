# src/your_package/core/service.py
import logging

logger = logging.getLogger(__name__)


def process(data):
    logger.debug("收到数据: %s", data)  # 替代 print 调试
    if not data:
        logger.warning("数据为空，跳过处理")
        return None
    logger.info("处理完成，共 %d 条", len(data))
    return data
