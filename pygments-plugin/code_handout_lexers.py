import copy
import re

from pygments.lexer import RegexLexer, bygroups, \
    using, this, default, words
from pygments.token import Punctuation, Text, Comment, Operator, Keyword, \
    Name, String, Number, Literal, Other, Whitespace
from pygments.util import get_choice_opt
from pygments.lexers.dotnet import CSharpLexer


def extend_at(index, self, elements):
    for i, e in enumerate(elements):
        self.insert(index + i, e)


class ImprovedCSharpLexer(RegexLexer):
    name = 'CSharp Lexer extras'
    aliases = ['csx', 'csharpx']
    filenames = []
    flags = re.MULTILINE | re.DOTALL

    token_variants = True
    tokens = copy.deepcopy(CSharpLexer.tokens)

    for levelname, cs_ident in CSharpLexer.levels.items():
        context = tokens[levelname]['root']
        context.insert(1, ('"', String, 'string'))
        context.insert(1, (r'false|true|null', Keyword.Other))
        context.insert(1, (r'^(\s*)(\[)',
                           bygroups(Whitespace, Punctuation), 'attribute'))

        extend_at(len(context)-1, context, [
            (fr'({cs_ident})([\[\]\?]*)(\s+)({cs_ident})(\s*)(;)',
             bygroups(Name.Class, Punctuation, Whitespace,
                      Name, Whitespace, Punctuation)),

            (fr'({cs_ident})(\s*)([\[\]\?]*)(\s+)({cs_ident})(\s+)(=)',
             bygroups(Name.Class, Whitespace, Punctuation, Whitespace,
                      Name, Whitespace, Operator)),

            (fr'({cs_ident})(\s*)(\()',
             bygroups(Name.Function, Whitespace, Punctuation)),
        ])

        tokens[levelname]['attribute'] = [
            ('"', String, 'string'),
            ('=', Operator),
            (r"[0-9]+(\.[0-9]*)?([eE][+-][0-9]+)?"
             r"[flFLdD]?|0[xX][0-9a-fA-F]+[Ll]?", Number),
            ('false|true|null', Keyword.Other),
            (cs_ident, Name.Attribute),
            (r'[^]]', Text),
            (r'\]', Punctuation, '#pop')
        ]

        tokens[levelname]['string'] = [
            (r'\\.', String.Escape),
            (r'[^\\"]', String),
            (r'"', String, '#pop'),
        ]

    def __init__(self, **options):
        level = get_choice_opt(options, 'unicodelevel', list(self.tokens),
                               'basic')

        if level not in self._all_tokens:
            self._tokens = self.__class__.process_tokendef(level)
        else:
            self._tokens = self._all_tokens[level]

        RegexLexer.__init__(self, **options)
