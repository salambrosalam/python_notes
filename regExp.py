import re

text = "sdfsfdfafads dfsdf andrey mix@gmail.com" \
        "lOLOLOLOOL json php python java js h" \
        "Boris lomalo@mail.ru uuufff@protonmail.com"

template = r"\w"
result = re.findall(template,text)

"""

\d = Any digit 0-9
\D = Any non digit
\w = any alphabet symbol [A-Z a-z]
\W = any non alphabet symbol
\s = breakspace
\S = non breakspace

"""

print(result)