import re
from datetime import datetime

# MM/DD pattern
DATE_RE = re.compile(r"(?<!\d)(\d{1,2})/(\d{1,2})(?!\d)")

# 24h time range like 09:00 - 17:00 or 21:00–06:00
TIME_RE = re.compile(r"(\d{1,2}:\d{2})\s*[-–]\s*(\d{1,2}:\d{2})")

def parse_shifts(text: str):
    """
    MVP parser rules:
    - A line starting with • * ● - becomes the current site heading
    - A shift line must contain MM/DD and HH:MM-HH:MM
    - Year inferred as current year
    - slots/pay/role not extracted yet (we’ll add next)
    """
    year = datetime.now().year
    current_site = ""
    shifts = []

    for raw in text.splitlines():
        line = raw.strip()
        if not line:
            continue

        # Site heading
        if line.startswith(("•", "*", "●", "-")):
            current_site = line.lstrip("•*●- ").strip()
            continue

        md = DATE_RE.search(line)
        tm = TIME_RE.search(line)
        if not (md and tm):
            continue

        month = int(md.group(1))
        day = int(md.group(2))
        date = f"{year:04d}-{month:02d}-{day:02d}"

        start = tm.group(1)
        end = tm.group(2)

        shifts.append({
            "date": date,
            "start": start,
            "end": end,
            "site": current_site,
            "role": "",
            "slots": 1,
            "pay": None,
        })

    return shifts


