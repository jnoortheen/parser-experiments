"""
Standalone Parser
===================================

    This example demonstrates how to generate and use the standalone parser,
    using the JSON example.

    See README.md for more details.
"""

import sys

from json_parser import Lark_StandAlone, Transformer, v_args

inline_args = v_args(inline=True)


class TreeToJson(Transformer):
    @inline_args
    def string(self, s):
        return s[1:-1].replace('\\"', '"')

    array = list
    pair = tuple
    object = dict
    number = inline_args(float)

    null = lambda self, _: None
    true = lambda self, _: True
    false = lambda self, _: False


parser = Lark_StandAlone(transformer=TreeToJson())

if __name__ == "__main__":
    from bench_utils import timeit, trace

    with open(sys.argv[1]) as f:
        with timeit(), trace():
            print(len(parser.parse(f.read())))
