# 扫描文件 - 分类 - 移动
import argparse
import shutil
from pathlib import Path

CATEGORIES = {
    "图片": [".jpg", ".png", ".gif", ".webp", ".svg"],
    "文档": [".pdf", ".docx", ".txt", ".md"],
    "视频": [".mp4", ".mkv", ".avi"],
    "压缩包": [".zip", ".rar", ".7z"],
    "代码": [".py", ".js", ".java"],
}

EXT_MAP = {ext: cat for cat, exts in CATEGORIES.items() for ext in exts}


def build_parser():
    parser = argparse.ArgumentParser(description="文件整理器")
    parser.add_argument("src_dir", type=Path, help="要整理的源目录")
    parser.add_argument(
        "-o", "--output", type=Path, default=None, help="输出目录，默认 src_dir/res"
    )
    parser.add_argument("--dry-run", action="store_true", help="只预览不执行")
    return parser


def scan(src: Path, out: Path):
    paths = src.iterdir()
    for path in paths:
        if out in path.parents:
            continue
        yield path


def build_plan(paths, out: Path):
    plan = []
    for path in paths:
        categories = EXT_MAP.get(path.suffix.lower(), "其他")
        plan.append((path, out / categories / path.name))
    return plan


def unique_dst(dst: Path) -> Path:
    if not dst.exists():
        return dst
    i = 1
    while True:
        cand = dst.with_name(f"{dst.stem}_{i}.{dst.suffix}")
        if not cand.exists():
            return cand
        i += 1


def execute(plan, dry_run: bool):
    for src, dst in plan:
        final = unique_dst(dst)
        if dry_run:
            print(f"[DRY] {src} -> {final}")
            continue
        final.parent.mkdir(parents=True, exist_ok=True)
        shutil.move(str(src), str(final))
        print(f"[MOVE] {src} -> {final}")


def main():
    args = build_parser().parse_args()
    src = args.src_dir.resolve()
    out = (args.output or src / "res").resolve()
    paths = list(scan(src, out))
    plan = build_plan(paths, out)
    execute(plan, args.dry_run)


if __name__ == "__main__":
    main()
