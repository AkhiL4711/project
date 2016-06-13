import re
s=raw_input()
print re.search(r"(?:\+?\d{2}[ -]?)?\d{10}", s)