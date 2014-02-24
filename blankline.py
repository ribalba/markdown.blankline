"""Blank line extension for Markdown.

This extension adds the syntax for an user to add a blank line. The syntax is 
the same as in reStructuredText. Just have a line which only consist out of a vertical line. Much like
```
| 
```
This will create a <br> tag

"""

from markdown.inlinepatterns import SubstituteTagPattern, Pattern
from markdown.extensions import Extension
import re

# Global Vars
BLANKLINE_RE = r'\%\%'

class BlankLineExtension(Extension):
    """Adds BLANKLINE_RE extension to Markdown class."""
    
    def extendMarkdown(self, md, md_globals):
        """Modifies inline patterns."""
        br_tag = SubstituteTagPattern(BLANKLINE_RE, 'br')
        md.inlinePatterns.add('ble', br_tag, '_begin')
        


def makeExtension(configs=None):
    return BlankLineExtension(configs)

if __name__ == "__main__":
    import doctest
    doctest.testmod()