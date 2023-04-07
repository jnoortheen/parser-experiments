import sys
import os, os.path
from io import open
import glob, time

from lark import Lark
from lark.indenter import PythonIndenter


def get_parser(**kwargs):
    kwargs.update(dict(postlex=PythonIndenter(), start="file_input", cache=True))

    # Official Python grammar by Lark
    return Lark.open_from_package(
        "lark", "python.lark", ["grammars"], parser="lalr", **kwargs
    )


def _read(fn, *args):
    kwargs = {"encoding": "iso-8859-1"}
    with open(fn, *args, **kwargs) as f:
        return f.read()


def _get_lib_path():
    if os.name == "nt":
        if "PyPy" in sys.version:
            return os.path.join(sys.base_prefix, "lib-python", sys.winver)
        else:
            return os.path.join(sys.base_prefix, "Lib")
    else:
        return [x for x in sys.path if x.endswith("%s.%s" % sys.version_info[:2])][0]


def test_python_lib(py_parser):
    path = _get_lib_path()

    start = time.time()
    files = glob.glob(path + "/*.py")
    total_kb = 0
    for f in files:
        r = _read(os.path.join(path, f))
        kb = len(r) / 1024
        print("%s -\t%.1f kb" % (f, kb))
        py_parser.parse(r + "\n")
        total_kb += kb

    end = time.time()
    print(
        "test_python_lib (%d files, %.1f kb), time: %.2f secs"
        % (len(files), total_kb, end - start)
    )


if __name__ == "__main__":
    from bench_utils import timeit, trace

    with trace(), timeit():
        kwargs = {}
        if len(sys.argv) > 2:
            if sys.argv[2] == "--cy":
                from lark_cython import plugins

                kwargs["_plugins"] = plugins

        py_parser = get_parser(**kwargs)
        # test_python_lib()
        # test_earley_equals_lalr()
        py_parser.parse(_read(sys.argv[1]) + "\n")
