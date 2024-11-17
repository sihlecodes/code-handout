import re

from pygments.lexer import RegexLexer, bygroups, \
    using, this, default, words
from pygments.token import Punctuation, Text, Comment, Operator, Keyword, \
    Name, String, Number, Literal, Other, Whitespace
from pygments.util import get_choice_opt

from pygments.lexers.dotnet import CSharpLexer


class ImprovedCSharpLexer(RegexLexer):
    name = 'CSharp Lexer extras'
    aliases = ['csx']
    filenames = []
    flags = re.MULTILINE | re.DOTALL

    token_variants = True
    tokens = CSharpLexer.tokens

    for levelname, cs_ident in CSharpLexer.levels.items():
        tokens[levelname]['root'] = tokens[levelname]['root'][:-1] + [
            (fr'({cs_ident})([\[\]\?]*)(\s+)({cs_ident})(\s*)(;)',
             bygroups(Name.Class, Punctuation, Whitespace,
                      Name, Whitespace, Punctuation)),

            (fr'({cs_ident})(\s*)([\[\]\?]*)(\s+)({cs_ident})(\s+)(=)',
             bygroups(Name.Class, Whitespace, Punctuation, Whitespace,
                      Name, Whitespace, Operator)),

            (fr'({cs_ident})(\s*)(\()',
             bygroups(Name.Function, Whitespace, Punctuation)),
        ] + [tokens[levelname]['root'][-1]]

    def __init__(self, **options):
        level = get_choice_opt(options, 'unicodelevel', list(self.tokens),
                               'basic')

        if level not in self._all_tokens:
            self._tokens = self.__class__.process_tokendef(level)
        else:
            self._tokens = self._all_tokens[level]

        RegexLexer.__init__(self, **options)
