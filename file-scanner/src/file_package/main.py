# 扫描文件 - 分类 - 移动
import os
from pathlib import Path

CATEGORIES = {
    "图片": [".jpg", ".png", ".gif", ".webp", ".svg"],
    "文档": [".pdf", ".docx", ".txt", ".md"],
    "视频": [".mp4", ".mkv", ".avi"],
    "压缩包": [".zip", ".rar", ".7z"],
    "代码": [".py", ".js", ".java"],
}

EXT_MAP = {ext: cat for cat, exts in CATEGORIES.items() for ext in exts}


def scan_file(src_dir):
    p = Path(f"{src_dir}")
    file_names = os.listdir(p)
    classify(file_names, src_dir)


def classify(names, src_dir):
    for file_name in names:
        cat = EXT_MAP.get("." + file_name.split(".")[-1], "else")
        move(cat, file_name, src_dir)


def move(cat, file_name, src_dir):
    p = Path(f"data/res/{cat}")
    if not p.exists():
        os.makedirs(p)
    src_file = src_dir + "/" + file_name
    dst_file = str(p) + "/" + file_name
    os.rename(src_file, dst_file)


def main():
    src_dir = input("请输入目录=")
    scan_file(src_dir)


if __name__ == "__main__":
    main()
