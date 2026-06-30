import re
from pathlib import Path

import openpyxl

from reestimate_file_generator.config import FILE_CONFIGS

LOAN_ID_PATTERN = re.compile(r"^MA-(\d+)$")


def collect_existing_ids(input_dir: Path) -> set[str]:
    """Collect all MA-XXXXX loan IDs present in base files."""
    existing: set[str] = set()
    for cfg in FILE_CONFIGS:
        path = input_dir / cfg.filename
        if not path.exists():
            continue
        wb = openpyxl.load_workbook(path, read_only=True, data_only=True)
        ws = wb[cfg.sheet_name]
        for row in ws.iter_rows(values_only=True):
            if row and row[cfg.loan_col_idx]:
                value = str(row[cfg.loan_col_idx])
                if LOAN_ID_PATTERN.match(value):
                    existing.add(value)
        wb.close()
    return existing


def generate_new_ids(count: int, reserved: set[str]) -> list[str]:
    """Generate `count` new loan IDs not present in `reserved`.

    Starts at MA-16011 (next after highest portfolio ID MA-16010) and
    skips any collisions with IDs already present in base files.
    """
    if count <= 0:
        return []

    start_num = 16011
    new_ids: list[str] = []
    num = start_num
    while len(new_ids) < count:
        candidate = f"MA-{num}"
        if candidate not in reserved:
            new_ids.append(candidate)
            reserved.add(candidate)
        num += 1
    return new_ids
