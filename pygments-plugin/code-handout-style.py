from pygments.style import Style
from pygments.token import (Token, Comment, Error, Generic, Name, Number, Operator,
                            String, Text, Whitespace, Keyword)
# BACKGROUND    = '#120f17'
# TEXT          = '#cdbccf'
# WHITESPACE    = '#cdbccf'
# COMMENT       = '#88788f'
# FUNCTION      = '#5f4d8c'
# TYPE          = '#ffc354'
# PRIMATIVE     = '#ffc354'
# KEYWORD       = '#ff505d'
# STRING        = '#b897ff'
# NUMBER        = '#ff505d'

# UNDEFINED     = '#ff0000'
# STRING_ESCAPE = UNDEFINED
# ATTRIBUTE     = UNDEFINED
# STRING_OTHER  = UNDEFINED
# TAG           = UNDEFINED
# OPERATOR      = UNDEFINED

BACKGROUND    = '#fafbfc'
TEXT          = '#5d6165'
WHITESPACE    = '#cdbccf'
COMMENT       = '#abaeb1'
FUNCTION      = '#e1af52'
TYPE          = '#669de0'
PRIMATIVE     = '#e98d48'
KEYWORD       = '#e98d48'
STRING        = '#91b138'
STRING_ESCAPE = '#77bca8'
NUMBER        = '#9872cd'
OPERATOR      = '#e98d48'

UNDEFINED     = '#ff0000'
ATTRIBUTE     = UNDEFINED
STRING_OTHER  = UNDEFINED
TAG           = UNDEFINED


# hello world
class HandoutStyle(Style):
    background_color = BACKGROUND
    highlight_color = TEXT

    styles = {
        Token: TEXT,

        Comment: f'{COMMENT}',
        Comment.Preproc: 'noitalic',
        Comment.Special: 'bold',

        Generic: TEXT,
        Error: f'bg:#ff0000 #ffffff',

        Keyword: f'{KEYWORD}',
        Keyword.Pseudo: 'nobold',
        Keyword.Type: PRIMATIVE,

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

        Text: TEXT,

        Whitespace: WHITESPACE,
    }
