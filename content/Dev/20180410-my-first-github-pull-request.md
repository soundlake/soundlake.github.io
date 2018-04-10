Title: My First Accepted Github Pull Request
Date: 2018-04-10 11:05
Tags: git, gitlab, development
Summary: I've requested my first Github pull request ever.

Last night, I've applied [Typogrify] to this blog. It's a default plugin in
[Pelican].

But I found strange result. The title has unnecessary glitch on it. In the
[pelican source](https://github.com/getpelican/pelican/blob/master/pelican/readers.py#L603),
I could find that [Typogrify] is adding the tag intentionally. Then, the
template should be remove that. [Jinja2] has
[`striptags`](http://jinja.pocoo.org/docs/2.10/templates/#striptags) filter.

I've tested the following code.
```python
from typogrify.filters import typogrify
from jinja2.filters import do_striptags

TEST_STR = 'Hello WORLD'
print(TEST_STR) # Hello WORLD
print(typogrify(TEST_STR)) # Hello <span class="caps">WORLD</span>
print(do_striptags(typogrify(TEST_STR))) # Hello WORLD
```

Each libraries work as expected. Then it was the time to check the template
files. And apparently, in `aritcle.html`, `striptags` filter wasn't applied to
`article.title` variable.

I forked [pelican-blue] template source, and cloned it to my local direcotyr,
and created a commit, and pushed it into [my cloned repo], and created [a pull
request].

And this morning, it's merged!

I've reported some issues on some open source project, but this is the first
time that my code is included in the existing project.

[Jinja2]: http://jinja.pocoo.org
[Pelican]: http://getpelican.com
[Typogrify]: https://pypi.python.org/pypi/typogrify
[a pull request]: https://github.com/Parbhat/pelican-blue/pull/14
[my cloned repo]: https://github.com/soundlake/pelican-blue
[pelican-blue]: https://github.com/Parbhat/pelican-blue
