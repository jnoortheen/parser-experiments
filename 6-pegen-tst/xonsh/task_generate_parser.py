# python -m pegen xonsh.gram > xonsh.gram.out
from pathlib import Path

from pegen.build import build_python_parser_and_generator


def main():
    gram_content = Path("xonsh.gram").read_text()
    subheader = Path("sub_header.py").read_text()

    gram_content = gram_content.replace("{_SUB_HEADER_}", subheader)
    with Path("xonsh-full.gram").open(mode="w") as fw:
        skip = False
        for lin in gram_content.splitlines(keepends=True):
            if lin.startswith("# <!--"):
                skip = True
            elif lin.startswith("# -->"):
                skip = False
                continue
            if skip:
                continue
            fw.write(lin)

    output = "xonsh_parser.py"

    grammar, parser, tokenizer, gen = build_python_parser_and_generator(fw.name, output)

    return grammar, parser, tokenizer, gen


if __name__ == "__main__":
    main()
