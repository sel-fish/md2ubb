#!/usr/bin/env python
import mistune
import sys
from renderer import UbbRenderer

if __name__ == '__main__':
    if len(sys.argv) <= 1:
        print "usage: %s markdown_file" % sys.argv[0]
        sys.exit(-1)

    md_file_name = sys.argv[1]

    with open(md_file_name, 'r') as md_file:
        md_text = md_file.read()
        renderer = UbbRenderer(escape=True, hard_wrap=True)
        markdown = mistune.Markdown(renderer=renderer)
        print markdown(md_text)
