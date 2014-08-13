BIB=BIBINPUTS=".:PaperInfrastructure/References//"

all: paper

paper:
	${BIB} pdflatex -synctex=1 -shell-escape paper
	${BIB} bibtex paper
	${BIB} pdflatex -synctex=1 -shell-escape paper
	${BIB} pdflatex -synctex=1 -shell-escape paper
