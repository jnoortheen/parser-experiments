# python -m pegen xonsh.gram > xonsh.gram.out

from pegen.build import build_python_parser_and_generator


def main():
    grammar_filename = "xonsh.gram"
    output = ""
    grammar, parser, tokenizer, gen = build_python_parser_and_generator(
        grammar_filename,
        output,
    )
    return grammar, parser, tokenizer, gen


if __name__ == "__main__":
    main()
