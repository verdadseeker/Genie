"""Clean a YouTube auto-caption .vtt into deduped, timestamped plain text.

Auto-captions repeat each line as the caption "rolls". This collapses them into
one line per spoken phrase, prefixed with a [mm:ss] bookmark every ~30s so notes
can reference timestamps the way Manish does.

Usage: python clean_vtt.py input.en.vtt > output.txt
"""
import re, sys, html

def ts_to_sec(ts):
    h, m, s = ts.split(":")
    return int(h) * 3600 + int(m) * 60 + float(s)

def fmt(sec):
    m, s = divmod(int(sec), 60)
    h, m = divmod(m, 60)
    return f"{h}:{m:02d}:{s:02d}" if h else f"{m}:{s:02d}"

def main(path):
    lines = open(path, encoding="utf-8").read().splitlines()
    out, seen_recent, last_stamp, cur_start = [], [], -999, 0.0
    for ln in lines:
        m = re.match(r"(\d{2}:\d{2}:\d{2}\.\d{3}) -->", ln)
        if m:
            cur_start = ts_to_sec(m.group(1))
            continue
        if not ln.strip() or ln.startswith(("WEBVTT", "Kind:", "Language:")):
            continue
        # strip inline timing tags <00:00:00.000><c> ... </c>
        text = html.unescape(re.sub(r"<[^>]+>", "", ln)).strip()
        text = text.replace(">>", "").strip()
        if not text:
            continue
        # skip exact dupes from the rolling window
        if text in seen_recent:
            continue
        seen_recent.append(text)
        if len(seen_recent) > 8:
            seen_recent.pop(0)
        # emit a timestamp bookmark every 30s
        if cur_start - last_stamp >= 30:
            out.append(f"\n[{fmt(cur_start)}]")
            last_stamp = cur_start
        out.append(text)
    print(" ".join(out).replace("\n ", "\n"))

if __name__ == "__main__":
    main(sys.argv[1])
