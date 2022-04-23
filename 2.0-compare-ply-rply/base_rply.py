from rply import ParserGenerator, LexerGenerator
from rply.token import BaseBox

lg = LexerGenerator()
# Add takes a rule name, and a regular expression that defines the rule.
lg.add("PLUS", r"\+")
lg.add("MINUS", r"-")
lg.add("NUMBER", r"\d+")

lg.ignore(r"\s+")

# This is a list of the token names. precedence is an optional list of
# tuples which specifies order of operation for avoiding ambiguity.
# precedence must be one of "left", "right", "nonassoc".
# cache_id is an optional string which specifies an ID to use for
# caching. It should *always* be safe to use caching,
# RPly will automatically detect when your grammar is
# changed and refresh the cache for you.
pg = ParserGenerator(
    ["NUMBER", "PLUS", "MINUS"],
    precedence=[("left", ["PLUS", "MINUS"])],
    # with the removal of cahing, we explicitly pass the parser version
    cache_id="base-calc-v1.9",
)


@pg.production("main : expr")
def main(p):
    # p is a list, of each of the pieces on the right hand side of the
    # grammar rule
    return p[0]


@pg.production("expr : expr PLUS expr")
@pg.production("expr : expr MINUS expr")
def expr_op(p):
    lhs = p[0].getint()
    rhs = p[2].getint()
    if p[1].gettokentype() == "PLUS":
        return BoxInt(lhs + rhs)
    elif p[1].gettokentype() == "MINUS":
        return BoxInt(lhs - rhs)
    else:
        raise AssertionError("This is impossible, abort the time machine!")


@pg.production("expr : NUMBER")
def expr_num(p):
    return BoxInt(int(p[0].getstr()))


lexer = lg.build()
parser = pg.build()


class BoxInt(BaseBox):
    def __init__(self, value):
        self.value = value

    def getint(self):
        return self.value


def start():
    print(parser.parse(lexer.lex("1 + 3 - 2+12-32")))


if __name__ == "__main__":
    start()
    import tracemalloc
    from bench_utils import display_top

    snap = tracemalloc.take_snapshot()
    display_top(snap)
