#! /usr/bin/env python

from os import symlink
from os.path import join, exists
from shutil import copy

links_dir = 'PaperInfrastructure'
links = ['Affiliations.tex', 'Preamble.tex', 'UsePackages.tex']
templates_dir = join('PaperInfrastructure','Templates')
templates = ['paper.tex', 'Macros.tex', 'Makefile']

# Check that the files are in the right relative places (because this
# script could be used from the wrong place).
original_links = [join(links_dir,link) for link in links]
original_templates = [join(templates_dir, template) for template in templates]
for f in original_links + original_templates:
    if not exists(f):
        print("File '{0}' cannot be found.\n".format(f)
              +"Are you sure you've checked out PaperInfrastructure correctly?\n"
              +"Are you in the right directory?")
        raise IOError("File not found")

# Check that the files don't exist already in the places where we'll
# be copying them *to* (this directory)
for f in links + templates:
    if exists(f):
        print("File '{0}' already exists.\n".format(f)
              +"You must move or delete it before this can succeed.")
        raise IOError("Will not overwrite file")

# Link the link files
for o,n in zip(original_links,links):
    symlink(o,n)

# Copy the files
for o,n in zip(original_templates,templates):
    copy(o,n)

# Explain what else needs to be done
print("""
You should be ready to edit paper.tex in this directory.

You can add your own macros in Macros.tex in this directory.  There,
you can also remove the lines that include the macros from the
Infrastructure directory.

Similarly, you can add your own separate .bib file in this directory,
though if you have references that will be useful to others, feel free
to open a pull request on github for the main PaperInfrastructure
module.

""")
