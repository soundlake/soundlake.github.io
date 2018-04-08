Title: Pelican Tips
Date: 2014-12-21 10:00
Modified: 2018-04-08 02:00
Tags: pelican, python, vim
Lang: en

### [ghp-import](https://github.com/davisp/ghp-import)
This is a essential tool for using GitHub Page as Pelican blog.
With this tool, I don't need to manage two repo;
one for generator, and the other for output, the actual blog.
Because this does all the messy things.
You just need to `make github` and that's all.

It took a lot of time to find how to manage Pelican blog with Github,
and the answer was on the right by me.
Let's read the document carefully, and don't waste time.

### Supported Syntax Highlight List
There is syntax highlighter for python.
Praise [Python](https://www.python.org)!
[Pygmets](http://pygments.org), It is called.
And this is the [link](http://pygments.org/docs/lexers) for the list of supported Sytanx

### Vim-Jinja2

In order to develop/customize theme of [Pelican](http://blog.getpelican.com),
[Jinja2](http://jinja.pocoo.org), I need.
For using VIM, I found [Vim-Jinja2-Syntax](https://github.com/Glench/Vim-Jinja2-Syntax).

#### Install
    :::shell
    cd ~./vim_runtime/source_not_forked
    git clone https://github.com/Glench/Vim-Jinja2-Syntax
    git add Vim-Jinja2-Syntax
    git commit -m "add jinja plugin"

#### How to Use

Jinja2 is HTML template, so usually its extension is `*.html`.
Thus, VIM usually recognize it as HTML file.
So, I have to set filetype to `jinja` to use this plugin.

    :::vim
    :set filetype=jinja
