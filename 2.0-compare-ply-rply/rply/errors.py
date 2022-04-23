from rply.token import SourcePosition


class ParserGeneratorError(Exception):
    pass


class LexingError(Exception):
    """
    Raised by a Lexer, if no rule matches.
    """

    def __init__(self, message: str, source_pos: SourcePosition) -> None:
        self.message = message
        self.source_pos = source_pos

    def getsourcepos(self) -> SourcePosition:
        """
        Returns the position in the source, at which this error occurred.
        """
        return self.source_pos

    def __repr__(self) -> str:
        return "LexingError(%r, %r)" % (self.message, self.source_pos)


class ParsingError(Exception):
    """
    Raised by a Parser, if no production rule can be applied.
    """

    def __init__(self, message: str, source_pos: SourcePosition) -> None:
        self.message = message
        self.source_pos = source_pos

    def getsourcepos(self) -> SourcePosition:
        """
        Returns the position in the source, at which this error occurred.
        """
        return self.source_pos

    def __repr__(self) -> str:
        return "ParsingError(%r, %r)" % (self.message, self.source_pos)


class ParserGeneratorWarning(Warning):
    pass
