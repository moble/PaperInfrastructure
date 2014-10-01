PaperInfrastructure
===================

Basic elements for a LaTeX paper

This module can be used as a submodule for LaTeX papers, and can
provide the basic structure needed for a nice paper.  Basically, you
can start a new paper by just initializing the superproject's git
repo, add this infrastructure as a submodule, copy and link the
relevant files, and add/commit things to the superproject:
```bash
export MyCoolPaperName="<MyCoolPaper>"
mkdir ${MyCoolPaperName}
cd ${MyCoolPaperName}
git init
git submodule add https://github.com/moble/PaperInfrastructure.git
git submodule init
git submodule update
cd PaperInfrastructure
git checkout master
cd ..
python PaperInfrastructure/InitializeNewPaper.py
git add *.tex Makefile README.md LICENSE .gitignore
git commit -m 'Set up paper infrastructure'
```
Finally, if relevant, [create a new repo](https://github.com/new), add
the remote, and push to it:
```bash
git remote add origin https://github.com/moble/${MyCoolPaperName}.git
git push -u origin master
```

Note that the `colorbrewer` package for `TikZ`/`pgfplots` comes from
[this github repo](https://github.com/vtraag/tikz-colorbrewer).
