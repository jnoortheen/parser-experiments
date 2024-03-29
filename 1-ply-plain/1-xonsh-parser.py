import bench_utils as u


def main():
    from xonsh.parser import Parser

    p = Parser()
    # wait for thread to finish
    p.parse("ls -alh")


if __name__ == "__main__":
    with u.timeit(), u.trace():
        main()
