Title: Going deeper in Git tag
Date: 2019-05-22 18:35
Tags: git, git-tag
Summary: Listing git tags

Recently, I got a chance to read [`git tag`](https://git-scm.com/docs/git-tag) command.
We found a bug and confirmed which commit has introduced it,
but we could not point out which released versions are affected.

Apparently, `git tag` command supports
[`--contains`](https://git-scm.com/docs/git-tag#Documentation/git-tag.txt---containsltcommitgt) argument.
This argument takes the commit hash.

```shell
git tag --contains 12AB34
```

It might show too many lines.
Then you can use [`--list`](https://git-scm.com/docs/git-tag#Documentation/git-tag.txt---list)
(`-l` in short) argument
which allows you to filter the tags with pattern. For example,

```shell
git tag --contains 12AB34 --list 4.2.*
```
