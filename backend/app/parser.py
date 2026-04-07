import re
from datetime import datetime, timedelta

DATE_RE = re.compile(r"(?<!\d)(\d{1,2})/(\d{1,2})(?!\d)")
TIME_24_RE = re.compile(r"(\d{1,2}:\d{2})\s*[-–to]+\s*(\d{1,2}:\d{2})", re.IGNORECASE)
TIME_AMPM_RE = re.compile(
    r"(\d{1,2})(?::(\d{2}))?\s*(am|pm)\s*[-–]?\s*(?:to)?\s*(\d{1,2})(?::(\d{2}))?\s*(am|pm)",
    re.IGNORECASE
)
SITE_INLINE_RE = re.compile(r"\bat\s+([a-zA-Z0-9 &\-]+)", re.IGNORECASE)

def to_24h(hour: int, minute: int, ampm: str) -> str:
    ampm = ampm.lower()
    if ampm == "am":
        if hour == 12:
            hour = 0
    elif ampm == "pm":
        if hour != 12:
            hour += 12
    return f"{hour:02d}:{minute:02d}"

def resolve_date(line: str, year: int) -> str | None:
    line_lower = line.lower()

    if "tomorrow" in line_lower:
        d = datetime.now() + timedelta(days=1)
        return d.strftime("%Y-%m-%d")

    if "today" in line_lower:
        d = datetime.now()
        return d.strftime("%Y-%m-%d")

    md = DATE_RE.search(line)
    if md:
        month = int(md.group(1))
        day = int(md.group(2))
        return f"{year:04d}-{month:02d}-{day:02d}"

    return None

def resolve_time(line: str) -> tuple[str, str] | None:
    tm24 = TIME_24_RE.search(line)
    if tm24:
        return tm24.group(1), tm24.group(2)

    tm_ampm = TIME_AMPM_RE.search(line)
    if tm_ampm:
        start_hour = int(tm_ampm.group(1))
        start_min = int(tm_ampm.group(2) or 0)
        start_ampm = tm_ampm.group(3)

        end_hour = int(tm_ampm.group(4))
        end_min = int(tm_ampm.group(5) or 0)
        end_ampm = tm_ampm.group(6)

        start = to_24h(start_hour, start_min, start_ampm)
        end = to_24h(end_hour, end_min, end_ampm)
        return start, end

    return None

def parse_shifts(text: str):
    year = datetime.now().year
    current_site = ""
    shifts = []

    for raw in text.splitlines():
        line = raw.strip()
        if not line:
            continue

        # Separate bullet/site heading
        if line.startswith(("•", "*", "●", "-")):
            maybe_site = line.lstrip("•*●- ").strip()

            # If it's just a heading, store it and continue
            if not DATE_RE.search(maybe_site) and not TIME_24_RE.search(maybe_site) and not TIME_AMPM_RE.search(maybe_site):
                current_site = maybe_site
                continue

            # Otherwise keep parsing the same line as a shift
            line = maybe_site

        date = resolve_date(line, year)
        time_range = resolve_time(line)

        if not (date and time_range):
            continue

        start, end = time_range

        site_match = SITE_INLINE_RE.search(line)
        inline_site = site_match.group(1).strip() if site_match else ""

        site = inline_site or current_site or "Unassigned Site"

        shifts.append({
            "date": date,
            "start": start,
            "end": end,
            "site": site,
            "role": "",
            "slots": 1,
            "pay": None,
        })

    return shifts