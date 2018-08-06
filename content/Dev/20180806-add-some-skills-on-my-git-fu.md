Title: Add some skills on my Git-fu
Date: 2018-08-06 11:12
Tags: git, git-config
Summary: Git tips, which make the dev life easier

Today, one of my colleague introduced me [this article](https://about.gitlab.com/2016/12/08/git-tips-and-tricks/).
Apparently, it's written already 2 years ago. There are something I already know, but also are still some new and good tips for me.

### Global Configurations

#### Deleting a local branch which is already removed in the remote

Since, I'm in an actively git-using team, many branches are created and and deleted.
Whenever my merge request is merged, I had to remove my local leftovers manually.

```shell
git remote prune <remote name>
```

But now I don't have to do that. With this global configuration,
it'll be done automatically during `fetch` or `pull`.

```shell
git config --global fetch.prune true
```

#### "Auto" autosquash, autostash

When I use `rebase` command, I tend to use `-i --autosquash --autostash`.
But I didn't realize I could configure them into the global configuration file.

```shell
git config --global rebase.autosquash true
git config --global rebase.autostash true
```

#### Better `git lola`

[`git lola`](http://blog.kfish.org/2010/04/git-lola.html) is one of my favorite command.
And I found an idea for a little improvement.

```shell
git config --global alias.lol="log --graph --decorate --pretty=format:'%C(auto)%h -%d%Creset %s %Cgreen(%cr)%Creset' --abbrev-commit"
git config --global alias.lola="log --graph --decorate --pretty=format:'%C(auto)%h -%d%Creset %s %Cgreen(%cr)%Creset' --abbrev-commit --all"
```

The difference is custom formatting with `%C(auto)`, which derives the original color scheme of `oneline` option,
and `%cr`, which displays the commit date in relative format.
