# Python imports


def main():
    from tree_sitter import Language, Parser

    PY_LANGUAGE = Language("build/python.so", "python")
    parser = Parser()
    parser.set_language(PY_LANGUAGE)
    src_txt = b"print(1)"
    tree = parser.parse(src_txt)
    print(f"{tree=}", type(tree))


if __name__ == "__main__":
    from bench_utils import trace, timeit

    with timeit(), trace():
        main()
