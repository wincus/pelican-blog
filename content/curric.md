Title: Self Building Resume
Date: 2014-12-03
Category: misc
Tags: cv, resume, latex, travis, github
Authors: Wincus
Summary: How travis kindly builds my resume
Status: draft

I'm a big fan of [Donald Knuth](http://en.wikipedia.org/wiki/Donald_Knuth) and
naturally I am fan of one of his latest creation, [Tex](http://tug.org/). So 
I didn't have to think much when I decided the typesetting system I would use 
for my resume, [LaTeX](http://www.latex-project.org/).

The problem
-----------
LaTeX is great, is a document preparation system for high-quality typesetting.
It's largely used in the scientific community, but it can be used for almost
any form of publishing.

You can write your document with any text editor, 
like [vim](http://vim.org), and then compile it to 
generate the output file, in any format you like.

In order to be able to compile my CV I need this packages installed:

 * texlive
 * texlive-fonts-recommended
 * texlive-lang-spanish
 * texlive-latex-base texlive-latex-extra 
 * texlive-latex-recommended

Almost 512MB needs to be downloaded from the Internet in order to get them 
installed. Just to generate my Resume in pdf format seemed like to much. I even
thought about switching to LibreOffice ...

The solution
------------
My Resume LaTeX source files are hosted by [github](https://github.com/wincus/curric), so 
with very little extra effort I let [Travis](https://travis-ci.org/wincus/curric) to build 
the Resume for me, by adding a .travis file to my repo with instructions on how to build it,
and in case the build is success, push to my repo the pdf version. All this gets
executed whenever I commit changes to github. 

Cool, right?

Thanks for passing by!
