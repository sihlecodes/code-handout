from pygments import highlight
from pygments.lexers import get_lexer_by_name
from pygments.formatters import HtmlFormatter

from pygments.style import Style
from pygments.token import (
    Comment, Error, Generic, Name,
    Number, Operator, String, Text,
    Whitespace, Keyword)

from handout_lexers import ImprovedCSharpLexer
from handout_style import HandoutStyle

import os

code = r'''
namespace Test {
    public class Program {
        public static int NUMBER_OF_VIEWS = 0;
        public string Name;

        [Note(name = "Helper class")]
        interface IKiller {
            void kill();
        }

        public static void Main(string[] args) {
            Random? random = new Random();
            Garbage.Name[] names;
            string[] names = {"\bGugu\u", "Hop\e", "Ntombi\n", "Sbahle", "Mandisa"}

            const int COUNT = 10;

            using (Random rand = new Random()) {
                Console.WriteLine(rand.Next(21));
            }

            for(int i = 0; i < COUNT; i++)
            {
                Console.WriteLine(names[random.Next(names.Length)]);
                // we could split this line of code into 3 separate lines to make
                // it more understandable.
                // int iRandomIndex = random.Next(names.Length);
                // string sRandomName = names[iRandomIndex];
                // Console.WriteLine(sRandomName);
            }
        }
    }
}
'''

lexer = ImprovedCSharpLexer()
formatter = HtmlFormatter(style=HandoutStyle)

html = f'''
<head>
    <link rel="stylesheet" href="./style.css">
    <style>
    .highlight {{
        padding: 5px 15px;
    }}
    </style>
</head>
<body>
{highlight(code, lexer, formatter)}
</body>
'''

OUTPUT = './public'

if not os.path.exists(OUTPUT):
    os.makedirs(OUTPUT)

with open(os.path.join(OUTPUT, 'index.html'), 'w') as f:
    f.write(html)

with open(os.path.join(OUTPUT, 'style.css'), 'w') as f:
    f.write(formatter.get_style_defs('.highlight'))
