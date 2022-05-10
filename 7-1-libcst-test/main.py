# Python imports


def main():
    import libcst as cst
    from libcst.tool import dump

    src_txt = "print(1)"
    tree = cst.parse_expression(src_txt)
    print(dump(tree))


if __name__ == "__main__":
    from bench_utils import trace, timeit

    with timeit(), trace():
        main()
