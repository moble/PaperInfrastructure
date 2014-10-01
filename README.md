PaperInfrastructure
===================

Basic elements for a LaTeX paper

This module can be used as a submodule for LaTeX papers, and can
provide the basic structure needed for a nice paper.  Basically, you
can start a new paper by just initializing the git repo:
```bash
mkdir MyCoolPaper
cd MyCoolPaper
git init
```
Then, you add this as a submdole and copy and link the relevant files:
```bash
git submodule add https://github.com/moble/PaperInfrastructure.git
git submodule init
git submodule update
cd PaperInfrastructure
git checkout master
cd ..
python PaperInfrastructure/InitializeNewPaper.py
```
At this point, you may want to add/commit things to your new
superproject:
```bash
git add *.tex Makefile README.md LICENSE .gitignore
git commit -m 'Set up paper infrastructure'
```
Finally, if relevant, add a remote and push to it:
```bash
git remote add origin https://github.com/moble/<remote_repo_URL>.git
git push origin master
```

Note that the `colorbrewer` package for `TikZ`/`pgfplots` comes from
[this github repo](https://github.com/vtraag/tikz-colorbrewer).
