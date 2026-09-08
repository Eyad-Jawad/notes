import re
from collections import defaultdict
from itertools import chain
from pathlib import Path
from textwrap import dedent
from urllib.parse import quote

import markdown
from rapidfuzz.fuzz import ratio
from ripgrep_rs import search_structured

WEBSITE_LINK = "https://eyad-jawad.github.io/notes/"
ROOT = Path(__file__).resolve().parents[2]


def main() -> None:
    index = build_index()

    md_files = (
        file for file in chain.from_iterable(index.values()) if file.suffix == ".md"
    )

    for file in md_files:
        if file.stem == '1':
            pass
    
        text = file.read_text()

        matches = search_structured(
            patterns=[r"\[\[(.*?)\]\]"],
            paths=[str(file)],
        )

        for sm in chain.from_iterable(m.submatches for m in matches):
            fir, sec = breakdown_reference(sm.text)
            hash_symbol, fir, sec = hash_stuff(fir, sec)

            target_file = match_file(fir, str(file), index)
            if target_file.suffix == ".md":
                target_file = target_file.with_suffix(".html")

            file_path = quote(str(target_file))

            if hash_symbol:
                file_path += "#" + quote(hash_symbol.group(2))

            new_link = f"[{sec}]({WEBSITE_LINK}{file_path})"
            text = text.replace(sm.text, new_link)

        write_html_file(file, text)


def breakdown_reference(reference: str) -> tuple[str, str]:
    ref = reference[2:-2]
    file_name, separator, display_name = ref.partition("|")

    if not separator:
        display_name = file_name

    return file_name, display_name


def hash_stuff(f: str, s: str) -> tuple[re.Match | None, str, str]:
    hash_symbol = re.match(r"(.*?)#(.*)", f)

    if hash_symbol is None:
        return None, f, s

    if f == s:
        s = hash_symbol.group(1)

    return hash_symbol, hash_symbol.group(1), s


def match_file(
    filename: str, referencer_file: str, index: dict[str, list[Path]]
) -> Path:
    target_file = Path(filename)
    match = index.get(target_file.stem)

    if not match:
        return Path(".")

    if len(match) == 1:
        return match[0].relative_to(ROOT)

    return max(match, key=lambda file: ratio(str(file), referencer_file)).relative_to(
        ROOT
    )


def build_index() -> dict[str, list[Path]]:
    index = defaultdict(list)

    for path in ROOT.rglob("*"):
        if path.is_file():
            index[path.stem].append(path)

    return index


def write_html_file(file: Path, text: str) -> None:
    title = file.stem

    f = file.with_suffix(".html")
    if f.stem == "README":
        f = f.with_stem("index")

    body = markdown.markdown(
        text,
        extensions=[
            "fenced_code",
            "tables",
            "toc",
        ],
    )

    f.write_text(dedent(f"""\
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
                {body}
            </article>

        </body>
        </html>
    """))


if __name__ == "__main__":
    main()
