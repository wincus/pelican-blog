Title: Self Building Latex Resume
Date: 2014-12-03
Category: misc
Tags: cv, resume, latex, travis, github
Authors: Wincus
Summary: How travis kindly builds my resume

I'm a big fan of [Donald Knuth](http://en.wikipedia.org/wiki/Donald_Knuth) and
naturally I am fan of one of his latest creation, [Tex](http://tug.org/). 

So I didn't have to think much when I decided the typesetting system I would 
use for my resume: [LaTeX](http://www.latex-project.org/).

History Context
---------------
In the late 1970s, Donald Knuth was writting his multivolume 
["The Art of Computer Programming"](http://en.wikipedia.org/wiki/The_Art_of_C
omputer_Programming) books, and realized that the typesetting systems
used by his publisher didn't have the quality he expected. So he decided to 
do something about it. He started TeX thinking it would take about 6 months
to finish. It toked 10 years, though.

Naturally he wrote a book about TeX, [The TeX book](http://www-cs-faculty.sta
nford.edu/~uno/abcde.html) written in his own language. Now how cool is that?
The "Tex Book" TeX source file is available [here](http://www.ctan.org/tex-arch
ive/systems/knuth/dist/tex/texbook.tex). Beware!, as the book is copyrighted, 
Knuth added some code around there that prevents you from compile it ... ;)

The problem
-----------
LaTeX is great, is a document preparation system for high-quality typesetting
written on top of TeX.  It's largely used in the scientific community, but it
can be used for almost any form of publishing.  

You can write your document with any plain text editor like 
[vim](http://vim.org), and then compile it to generate the output file in any 
format you like.

Now, in order to be able to compile my Resume I need to download the whole LaTeX
suite, which takes about 512MB of packages and dependencies.  Just to generate
my Resume in pdf format seemed like to much. I even thought about switching to
LibreOffice!

The solution
------------
My Resume LaTeX source files are hosted by
[github](https://github.com/wincus/curric), so with very little extra effort I
let [Travis](https://travis-ci.org/wincus/curric) to build the Resume for me,
by adding a .travis file to my repo with instructions on how to build it, and
in case the build is success, push to my repo the pdf version. All this gets
executed whenever I commit changes to github. 

Thanks for passing by!
