import markdown
import re

from ripgrep_rs import search_structured
from urllib.parse import quote
from pathlib import Path

LINK = "https://eyad-jawad.github.io/notes/"

def main() -> None:
    search_path = Path(__file__).resolve().parent.parent.parent

    notes = list(Path(search_path).rglob("*.md"))
    for note in notes:
        text = ""
        with open(note, 'r') as f:
            text = f.read()
        
        text = text.replace("![[", "[[")

        filename = note.name[:-2] + "html"
        if note.name == "README.md":
            filename = "index.html"

        file_dir = note.parent / filename

        matches = search_structured(
            patterns=[r"\[\[(.*?)\]\]"],
            paths=[str(note)],
        )

        for m in matches:
            for sm in m.submatches:
                nested_match = re.match(r"\[\[(.*?)\|(.*?)\]\]", sm.text)

                if nested_match:
                    file_name = nested_match.group(1)
                    display_name = nested_match.group(2)
                else:
                    nested_match = re.match(r"\[\[(.*?)\]\]", sm.text)
                    file_name = display_name = nested_match.group(1)

                relative_file_name = find_file_relative_path(file_name, notes, search_path)

                hash_symbol = re.match(r"(.*?)#(.*?)")
                if hash_symbol:
                    display_name = hash_symbol.group(1)
                    file_name += "#" + hash_symbol.group(2)

                new_link = f"[{display_name}]({LINK}{relative_file_name})"
                text = text.replace(sm.text, new_link)

        with open(file_dir, 'w', encoding="utf-8") as f:
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
            return quote(str(file.relative_to(root))[:-3])
    return ""

if __name__ == "__main__":
    main()
