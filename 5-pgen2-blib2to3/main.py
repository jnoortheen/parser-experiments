# Python imports
import logging
import sys

# Pgen imports
from pgen2 import grammar, driver


def main() -> bool:
    """Main program, when run as a script: produce grammar pickle files.

    Calls load_grammar for each argument, a path to a grammar text file.
    """
    from pgen2.parse import ParseError
    from pgen2.tokenize import TokenError

    logging.basicConfig(level=logging.INFO, stream=sys.stdout, format="%(message)s")

    def get_gram310():
        from blib2to3 import pygram

        pygram.initialize(".")
        return pygram.python_grammar_soft_keywords

    def get_gram():
        g = driver.load_grammar(
            # loading pickle - 480 KiB - 0.08s
            force=True,  # 871 KiB - even with writing
        )
        return g

    # for gt in args:
    #     load_grammar(gt, save=True, force=True)
    # d = Driver(get_gram310())
    d = driver.Driver(get_gram())
    src_txt = "print(1)\n"
    errors = {}
    try:
        ast = d.parse_string(src_txt, True)
        print(f"ast: {ast}", type(ast))
    except ParseError as pe:
        lineno, column = pe.context[1]
        lines = src_txt.splitlines()
        try:
            faulty_line = lines[lineno - 1]
        except IndexError:
            faulty_line = "<line number missing in source>"
        errors[grammar.version] = ValueError(
            f"Cannot parse: {lineno}:{column}: {faulty_line}"
        )
    except TokenError as te:
        # In edge cases these are raised; and typically don't have a "faulty_line".
        lineno, column = te.args[1]
        errors[grammar.version] = ValueError(
            f"Cannot parse: {lineno}:{column}: {te.args[0]}"
        )
    print(f"{errors=}")
    return True


if __name__ == "__main__":
    from bench_utils import trace, timeit

    with timeit(), trace():
        main()
