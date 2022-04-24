# Python imports


def main():
    import parso

    src_txt = "print(1)"
    tree = parso.parse(src_txt, version="3.10")
    print(f"{tree=}", type(tree))


if __name__ == "__main__":
    from bench_utils import trace, timeit

    with timeit(), trace():
        main()
