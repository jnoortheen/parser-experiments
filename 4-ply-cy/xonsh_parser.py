import bench_utils as u


def main():
    from xonsh.parser import Parser

    p = Parser()
    # wait for thread to finish
    p.parse("ls -alh")
    return p


def trace():
    with u.timeit(), u.trace():
        p = main()

    from pympler import asizeof

    print(asizeof.asized(p.parser, detail=2).format())
    print(type(p.parser.action[0]))


if __name__ == "__main__":
    trace()
