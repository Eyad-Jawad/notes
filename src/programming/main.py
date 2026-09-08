import re
from pathlib import Path
from urllib.parse import quote

import markdown
from rapidfuzz.fuzz import ratio
from ripgrep_rs import search_structured

WEBSITE_LINK = "https://eyad-jawad.github.io/notes/"
ROOT = None

def main() -> None:
    global ROOT
    ROOT = Path(__file__).resolve().parent.parent.parent

    index = build_index()
    for value in index.values():
        for file in value:
            if file.suffix != ".md": 
                continue

            text = file.read_text()

            matches = search_structured(
                patterns=[r"\[\[(.*?)\]\]"],
                paths=[str(file)],
            )

            for m in matches:
                for sm in m.submatches:
                    fir, sec = breakdown_reference(sm.text)
                    hash_symbol, fir, sec = hash_stuff(fir, sec)

                    file_path = quote(str(match_file(fir, str(file), index)))
                    if file_path.endswith(".md"):
                        file_path = file_path[:-2] + "html"

                    if hash_symbol:
                        file_path += '#' + quote(hash_symbol.group(2))
                    
                    new_link = f"[{sec}]({WEBSITE_LINK}{file_path})"
                    text = text.replace(sm.text, new_link)

            write_html_file(file, text)


def breakdown_reference(reference: str) -> tuple[str, str]:
    match = re.match(r"\[\[(.*?)\|(.*?)\]\]", reference)

    if match:
        return match.group(1), match.group(2)        

    return reference[2:-2], reference[2:-2]


def hash_stuff(f: str, s: str) -> tuple[re.Match, str, str]:
    hash_symbol = re.match(r"(.*?)#(.*)", f)

    if hash_symbol is None: 
        return None, f, s

    if f == s:
        return hash_symbol, hash_symbol.group(1), hash_symbol.group(1)
    
    return hash_symbol, hash_symbol.group(1), s


def match_file(filename: str, referncer_filename: str, index: dict[str, list[Path]]) -> Path:
    mx = 0
    idx = 0
    target_file = Path(filename)

    match = index.get(target_file.stem, [ROOT])
    for i, file in enumerate(match):
        ra = ratio(str(file), referncer_filename)
        if ra > mx:
            mx = ra
            idx = i

    return match[idx].relative_to(ROOT)


def build_index() -> dict[str, list[Path]]:
    index = {}

    for path in Path(ROOT).rglob("*"):
        if path.is_file():
            index.setdefault(path.stem, []).append(path)

    return index


def write_html_file(file: Path, text: str) -> None:
    title = file.stem

    if file.name == "README.md":
        file.rename("index.html")

    with open(file.with_suffix(".html"), 'w', encoding="utf-8") as f:
        body = markdown.markdown(
            text,
            extensions=[
                "fenced_code",
                "tables",
                "toc",
            ],
        )
        f.write(f"""
            <!DOCTYPE html>
            <html lang="en">
            <head>
                <meta charset="UTF-8">
                <meta name="viewport" content="width=device-width, initial-scale=1.0">
                <title>{title}</title>
            </head>

            <body style="
                max-width: 800px;
                margin: 60px auto;
                padding: 0 20px;
                font-family: system-ui, -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
                line-height: 1.7;
                color: #222;
                background: #fff;
            ">

                <article>
                    <h1>{title}</h1>
                    <p>{body}</p>
                </article>

            </body>
            </html>
        """)

if __name__ == "__main__":
    main()
