Title: The Exhaustive Guide to Build Pelican Blog with Github and Travis-CI
Date: 2018-04-02 10:28
Modified: 2018-04-02 21:51
Tags: github, travis, pelican, python, CI
Summary: A single document for the walkthrough setup your static page blog with Pelican on Github and Travis-CI.

### Introduction

I'm writing this mostly for archiving what I've done for setting up this blog.

The internet is very big water, and you can whatever you want, but I couldn't
find a single document that explain everything.

I know. In this software world, you can never *explain everything*. But I
wanted a bit more kind and careful document to show me the walkthrough.

The followings are the tech that I've used for setting up my new blog.

### Setup in Local

Firstly, I've checked with [Pelican]. There are many options, and actually
[Github] seems easy with [Jekyll], but [Ruby] is not my best thing, while
I'm a kind of fond of [Python].

To use [Pelican], you can just install it with [pip] it, but there are a
somewhat downside of [Python], which is [pip] installs those dependencies
globally.

If you are familiar with [Linux] system, it looks rather natural and normal for
you, but if you are one of the modern developers who likes JavaScript eco
system like [npm], then installing dependency only globally might look wierd.

#### VirtualEnv

Here comes [VirtualEnv]. This tricks the system, and make the dependency able
to be installed locally avoiding to corrupt the whole system.

##### Install VirtualEnv

Fortunately, [Debian] team did a good job with keeping the packages up-to-date.
You can simply install [VirtualEnv] by

```sh
sudo apt-get install python-virtualenv
```

##### Using VirtualEnv

Now, let's choose a directory, and make it the virtual environment of your
python system.

```sh
virutalenv path/to/the/directory
```

To enable the virtual environment, you should just run following command.

```sh
cd path/to/the/directory
source bin/activate
```

[`source`] is [bash]'s built-in command. According to the document, that I
linked, it does the following.

> Read and execute commands from the filename argument in the current shell
context.

So, `source bin/activate` command read the file, and alter the [bash]'s
environment, and makes you can run executable in the virtual environment.

That's why deactivating this virtual environment is so easy.

```sh
deactivate
```

Becuase this `deactivate` is already in your `PATH`, although it won't be after
running this.


#### Pelican

##### Install Pelican

After I activated the virtual environment, I've created a file called
`requirements.txt`. It isn't necessarilly named like that, but it's on [pip]'s
[document](https://pip.pypa.io/en/stable/user_guide/#requirements-files), and
commonly used for [pip]'s dependency list.

This is the content of the file. This is simple file, and each line has each
[Python] module name.

```
pelican
markdown
```
[Pelican] supports [reStructedText] by default, but it doesn't [Markdown]. I
personally prefer [Markdown] to [reStructedText].

##### Using Pelican

The next things to do is starting your [Pelican] instance. The developers of
[Pelican] are kind enough to provide you a easy-bootstraping command.

```sh
pelican-quickstart
```

This will create some directories and files, including `Makefile`,
`develop_server.sh`, `pelicanconf.py`, `publishconf.py`. With first two files,
you have a bit of automation for building your [Pelican] site locally during
developing. With the other two files, you can configure your [Pelican] site as
you want.

```sh
make devserver
```

This will turn on the watcher on `content` directory, `themes` directory, and
the configuration files including two that I mentioned above. Also, it turns on
the HTTP server which listens 8000 port by default.

##### Choosing a Theme

From [here](http://www.pelicanthemes.com), you can check various themes and its
screenshots. IIRC, all of them are hosted in [Github], and you can clone the
repository of the theme into your `themes` directory. After set `THEME` variable
to the path to the directory you've cloned, then it's good to go.

There might be a few little changes necessary, like color, some configuration
variable, or even the layout of the theme.

### Continuous Integration

[Travis CI] is one of popular CI service. And it's well integrated with
[Github]. You can register to [Travis CI] with [Github] account.

With [Travis CI], you can push your content and source into `master` branch of
your [Github], and [Travis CI] will do the left, including building the source
and push to `gh-pages` branch.

#### Github Repository

Here's a tip for the [Github] repository you'll make. Don't use
`username.github.io`. That repository is designed for using [Github]'s default
making web site system, so using `gh-pages` is simply not possible with this
repository.

Let's make a new repository. You don't need to add any additional file, because
we are not going to clone this repository. Rather, we'll set it to the remote
repository of the local repository.

If you haven't initialized your local repository, just do this.

```sh
cd path/to/the/directory
git init
```

Then with this command, set the remote repository.

```sh
git remote add origin url_of_the_github_repo
```

Now, you can push to the [Github] repository, you've created.

#### Travis

Once you've created [Github]'s public repository, you can find it in [Travis CI]
dashboard. It's on `https://travis-ci.org/profile/{Github Username}`. In this
page, you can activate the continuous integration by your [Github] repository.

Now, you need to create `.travis.yml` file in your repository.

```yaml
language: python
python:
  - '3.6'
branches:
  only:
    - master
install:
  - pip install -r requirements.txt
script:
  - make publish

deploy:
  provider: pages
  skip-cleanup: true
  github-token: $GITHUB_TOKEN
  keep-history: true
  local-dir: output
    on:
      branch: master
```

This is my configuration file. My configuration has mainly two part. The former
is to build the [Pelican] site, and the latter is to push to `gh-pages` of the
[Github] repository.

Note that there is `$GITHUB_TOKEN`.

#### Github Token

My configuration of [Travis CI] pushes to my repository. To make it possible,
we need to tell [Github] to allow [Travis CI] to do that. This is why the token
is required.

[Here](https://help.github.com/articles/creating-a-personal-access-token-for-the-command-line/)'s
how to create the token. When you create the token, don't forget to check
`public_repo` scope. That's the scope that allows [Travis CI] to push a new
commits to your [Github] repository.

After you create the token, copy it and go to [Travis CI]'s repository settings
page. The url would be `https://travis-ci.org/{username}/{repo name}/settings`.
In that page, you can configure the environment variables. Creat a new variable
with `GITHUB_TOKEN` for the name and the copied token for the value.

Now, if you push the `master` branch, then [Travis CI] will be noticed. Then,
it will build, make a new commit, and push to `gh-pages` branch. It's the time
to check out `https://{username}.github.io/{repo name}`


[Debian]: https://www.debian.org
[Github]: https://github.com
[Jekyll]: https://jekyllrb.com
[Markdown]: https://daringfireball.net/projects/markdown
[Linux]: https://www.linux.org
[Pelican]: https://blog.getpelican.com
[Python]: https://www.python.org
[Ruby]: http://www.ruby-lang.org
[Travis CI]: https://travis-ci.org
[VirtualEnv]: https://virtualenv.pypa.io

[bash]: https://www.gnu.org/software/bash
[npm]: https://www.npmjs.com
[pip]: https://pip.pypa.io
[reStructedText]: http://docutils.sourceforge.net/rst.html
[`source`]: https://ss64.com/bash/source.html
