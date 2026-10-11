# Fetching non-video sources in full

Some web tools return a model-written summary instead of the page. Summaries drop numbers, tables and caveats, which are exactly what a bible entry needs. Get the full text.

## Web pages (articles, blogs, docs, release notes)

Download the raw HTML into the work folder, then convert it to text while keeping the links:

```
curl -sL -A "Mozilla/5.0" "<url>" -o page.html
python - page.html page.txt <<'EOF'
import html, re, sys
raw = open(sys.argv[1], encoding="utf-8", errors="replace").read()
raw = re.sub(r"(?is)<(script|style|nav|footer).*?</\1>", "", raw)
raw = re.sub(r'(?is)<a [^>]*href="([^"]+)"[^>]*>(.*?)</a>', r"\2 [\1]", raw)
txt = re.sub(r"(?s)<[^>]+>", "\n", raw)
txt = re.sub(r"\n\s*\n+", "\n\n", html.unescape(txt))
open(sys.argv[2], "w", encoding="utf-8").write(txt.strip())
EOF
```

If the page is rendered by JavaScript (the text file comes out empty), use a browser tool to read it, or look for the site's RSS feed or API.

## GitHub pull requests, issues and releases

The public REST API gives the full description, labels, milestone, merge date and comments, without a login (rate-limited):

```
curl -s https://api.github.com/repos/<owner>/<repo>/pulls/<n>           # description: .body
curl -s https://api.github.com/repos/<owner>/<repo>/issues/<n>/comments # discussion
curl -s https://api.github.com/repos/<owner>/<repo>/pulls/<n>/comments  # review comments on lines
curl -s https://api.github.com/repos/<owner>/<repo>/releases/latest
```

- On Windows, set the console to UTF-8 before printing JSON (`chcp 65001`, or `PYTHONIOENCODING=utf-8` when parsing with Python), otherwise accented text breaks.
- Read the whole `.body`: benchmark tables and important caveats often come after a long script or template.
- Review comments are opinions, not decisions. The merged code and the official notes are the facts.

## PDFs and papers

Extract the text (`pdftotext`, or a PDF tool) and read the figures and tables, not only the abstract. Note the version or date of the paper.

## Threads and social posts

Use them only as leads. Open the primary source they point to and cite that. If there is none, the item stays Claimed.
