all: paper

paper:
	export BIBINPUTS=".:PaperInfrastructure/References//"
	pdflatex -synctex=1 -shell-escape paper
	bibtex paper
	pdflatex -synctex=1 -shell-escape paper
	pdflatex -synctex=1 -shell-escape paper
