"""Tell Bing and other IndexNow search engines that pages changed.

Run after the changes are live on fares.digital:

    python3 tools/indexnow.py                 # every page in sitemap.xml
    python3 tools/indexnow.py <url> [<url>]   # only these pages

The key file (d78bc46592f99f98c16d6a7cda57838c.txt) must stay at the site root; it proves the site is ours.
"""
import json
import re
import sys
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
HOST = "fares.digital"
KEY = "d78bc46592f99f98c16d6a7cda57838c"

urls = sys.argv[1:] or re.findall(r"<loc>([^<]+)</loc>", (ROOT / "sitemap.xml").read_text(encoding="utf-8"))
body = json.dumps({"host": HOST, "key": KEY, "keyLocation": f"https://{HOST}/{KEY}.txt", "urlList": urls}).encode()
req = urllib.request.Request(
    "https://api.indexnow.org/indexnow", data=body, headers={"Content-Type": "application/json; charset=utf-8"}
)
with urllib.request.urlopen(req, timeout=20) as res:
    print(f"IndexNow: HTTP {res.status} for {len(urls)} URL(s)")
