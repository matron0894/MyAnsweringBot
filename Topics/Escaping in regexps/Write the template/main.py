import re

good_string = 'You learn Python 3?..'
bad_string = 'You learn Python 3?!.'
template = re.escape("You learn Python 3?..")