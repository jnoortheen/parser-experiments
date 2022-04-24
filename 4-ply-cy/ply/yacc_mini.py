class MiniProduction:
    """
    This class serves as a minimal standin for Production objects when
    reading table data from files.   It only contains information
    actually used by the LR parsing engine, plus some additional
    debugging information.
    """

    # 10008 items
    #   - 432.9kB
    #   - 126.6kB with mypyc
    #   - 116.9kB with cy pxd

    def __init__(self, str, name, len, func, file, line):
        self.name = name
        self.len = len
        self.func = func
        self.callable = None
        self.file = file
        if line is not None:
            self.line = line
        self.str = str

    def __str__(self):
        return self.str

    def __repr__(self):
        return "MiniProduction(%s)" % self.str

    # Bind the production function name to a callable
    def bind(self, pdict):
        if self.func:
            self.callable = pdict[self.func]
