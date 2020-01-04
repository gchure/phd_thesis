PY=python
PANDOC=pandoc

INPUTDIR=$(CURDIR)
OUTPUTDIR=../dst
STYLEDIR=$(INPUTDIR)/styles
BIBFILE=$(INPUTDIR)/references.bib

pdf:
	pandoc $(INPUTDIR)/metadata.yaml \
	$(INPUTDIR)/chapter*/*.md \
	$(INPUTDIR)/ref_heading.tex \
	-o $(OUTPUTDIR)/thesis.pdf \
	--template=$(STYLEDIR)/template.tex \
	--filter pandoc-xnos \
	--filter pandoc-shortcaption \
	--filter pandoc-citeproc \
	--top-level-division chapter \
