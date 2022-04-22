import bench_utils as u


def main():
    from xonsh.parsers.completion_context import CompletionContextParser

    p = CompletionContextParser()
    text = "ls -alh"
    # wait for thread to finish
    p.parse(text, len(text))


if __name__ == "__main__":
    with u.timeit(), u.trace():
        main()
