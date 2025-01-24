from pygments.style import Style
from pygments.token import (Token, Comment, Error, Generic, Name, Number, Operator,
                            String, Text, Whitespace, Keyword)


BACKGROUND    = '#fafbfc'
TEXT          = '#4a5e52'
WHITESPACE    = '#cdbccf'
COMMENT       = '#9a9da3'
FUNCTION      = '#e1af52'
TYPE          = '#669de0'
PRIMITIVE     = '#e98d48'
KEYWORD       = '#e98d48'
STRING        = '#91b138'
STRING_ESCAPE = '#77bca8'
NUMBER        = '#9872cd'
OPERATOR      = '#e98d48'

UNDEFINED     = '#ff0000'
ATTRIBUTE     = UNDEFINED
STRING_OTHER  = UNDEFINED
TAG           = UNDEFINED


class HandoutStyle(Style):
    background_color = BACKGROUND
    highlight_color = TEXT

    styles = {
        Text: TEXT,
        Token: TEXT,

        Whitespace: WHITESPACE,

        Comment: f'{COMMENT}',
        Comment.Preproc: 'noitalic',
        Comment.Special: 'bold',

        Generic: TEXT,
        Error: 'bg:#ff0000 #ffffff',

        Keyword: f'{KEYWORD}',
        Keyword.Pseudo: 'nobold',
        Keyword.Type: PRIMITIVE,

        Name.Attribute: f'italic {ATTRIBUTE}',
        Name.Builtin: f'{FUNCTION}',
        Name.Class: f'{TYPE}',
        Name.Constant: TYPE,
        Name.Entity: f'{TYPE}',
        # Name.Exception: f'bold {PURPLE}',
        Name.Function: f'{FUNCTION}',
        Name.Function.Magic: f'{FUNCTION}',
        Name.Tag: f'{TAG}',

        Number: f'{NUMBER}',

        Operator: OPERATOR,
        # Operator.Word: 'bold',

        String: STRING,
        String.Doc: 'italic',
        String.Escape: f'{STRING_ESCAPE}',
        String.Other: STRING_OTHER,
        String.Symbol: f'bold {STRING_OTHER}',
    }
