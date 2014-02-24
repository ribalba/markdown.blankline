"""Blank line extension for Markdown.

This extension adds the syntax for an user to add a blank line. This can be in the middle of a text block. 
Just type %% and it will add a <br>. This is especially useful for adding blank lines on their own. 

This might create unforeseen <br>'s  with the nl2br extension. As you will get double new lines.

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