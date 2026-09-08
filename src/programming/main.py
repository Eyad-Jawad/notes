import markdown
import re

from ripgrep_rs import search_structured
from rapidfuzz.fuzz import ratio
from urllib.parse import quote
from pathlib import Path

WEBSITE_LINK = "https://eyad-jawad.github.io/notes/"
ROOT = None

def main() -> None:
    search_path = Path(__file__).resolve().parent.parent.parent

    global ROOT
    ROOT = search_path

    index = build_index(ROOT)
    for key, value in index.items():
        for file in value:
            if file.suffix != ".md": 
                continue

            with open(file, 'r') as f:
                text = f.read()

            images = [
                match.submatches[0].text[1:]
                for match in 
                search_structured(
                    patterns=[r"!\[\[(.*?)\]\]"],
                    paths=[str(file)],
                )
            ]

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

                    if sm.text in images:
                        text = text.replace(sm.text, f"[[{file_path}]]")
                        continue

                    if hash_symbol:
                        file_path += '#' + quote(hash_symbol.group(2))
                    
                    new_link = f"[{sec}]({WEBSITE_LINK}{file_path})"
                    text = text.replace(sm.text, new_link)

            html_filename = make_html_filename(file)
            write_html_file(file, text, html_filename)


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
            idx = i
        mx = max(ra, mx)

    return match[idx].relative_to(ROOT)


def build_index(dir) -> dict[str, list[Path]]:
    index = {}

    for path in Path(dir).rglob("*"):
        if path.is_file():
            index.setdefault(path.stem, []).append(path)

    return index


def make_html_filename(file: Path):
    if file.name == "README.md":
        return "index.html"

    return file.name[:-2] + "html"

def write_html_file(file_dir: Path, text: str, filename: str):
    path = file_dir.parent / filename
    with open(path, 'w', encoding="utf-8") as f:
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
                <title>{filename[:-5]}</title>
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
                    <h1>{filename[:-5]}</h1>
                    <p>{body}</p>
                </article>

            </body>
            </html>
        """)


def find_file_relative_path(filename: str, files: list[Path], root: Path) -> str:
    for file in files:
        if filename in str(file):
            output = quote(str(file.relative_to(root)))
            if not output.endswith(".md"):
                return output
            
            return output[:-2] + "html"
    return ""

if __name__ == "__main__":
    main()
