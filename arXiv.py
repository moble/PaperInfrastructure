#! /usr/bin/env python

"""
Simple utility to zip up a paper, its figures, etc., for arXiv submission

"""

# Reset this number with each new submission to the arXiv.
SubmissionNumber = 1

from glob import glob
from zipfile import ZipFile
from re import match, sub
from os import walk
from os.path import join

## Name the files to be included here.  Note that paper.tex and
## Macros.tex get special handling, so they should not be listed here.
TeXFiles = ['UsePackages.tex', 'Preamble.tex', 'Affiliations.tex',]
FigureFiles = list( glob('paper-figure*pdf') )
CodeFiles = []

if('\\Note' in open('paper.tex').read()) :
    raise(AssertionError("\n\nYou still have a \\Note in the text!"))

figure_count=0
def paper_replacements(text):
    global figure_count
    text = text.replace("{PaperInfrastructure/","{")
    text = text.replace(r"\input{UsePackages_tikz}","")
    if(match('[^%]*\\includegraphics{',text)):
        text = sub(r'([^%]*\\includegraphics){.*?}', r'\1{paper-figure'+str(figure_count)+'}', text)
        figure_count += 1
    return text

with ZipFile('Submission{0}.zip'.format(SubmissionNumber), 'w') as myzip :
    # Zip paper, with "{PaperInfrastructure/" replaced by "{", etc.
    with open("paper.tex") as myfile :
        filestring=''.join(paper_replacements(line) for line in myfile)
    myzip.writestr('paper.tex', filestring)
    with open('paper.bbl') as myfile :
        myzip.writestr('paper.bbl', myfile.read())

    # Zip the TeX files
    for FileName in TeXFiles :
        myzip.write(FileName)

    # Combine the Macros files into one, but leave out the \input
    with open("PaperInfrastructure/Macros.tex") as myfile :
        filestring=myfile.read()
    with open("PaperInfrastructure/Macros_GeometricAlgebra.tex") as myfile :
        filestring=filestring + myfile.read()
    with open("Macros.tex") as myfile :
        filestring=filestring + "".join(line for line in myfile if not r"\input{PaperInfrastructure/Macros" in line)
    myzip.writestr('Macros.tex', filestring)

    # Zip the figure files
    for FileName in FigureFiles :
        myzip.write(FileName)

    # Zip the code files
    for FileName in CodeFiles :
        myzip.write(FileName)
