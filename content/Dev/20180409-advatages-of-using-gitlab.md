Title: Migrating the git remote repo from single to multiple
Date: 2018-04-09 20:05
Modified: 2018-04-09 22:00
Tags: git, gitlab, development
Summary: A story of migrating git repo, and the advantages of using GitLab.

### Personal History on Git Pull Request

I've learned about [Git] many years ago, and since a few years ago I've been
using [Git] actively. But pull request or merge request hasn't been my favorite
thing until a couple of month ago.

#### Before, at My Work

We were using single remote repository and each developers used their own
branch name prefix. The work flow goes like ...

1. Each developer works on their own branch.
2. When the branch is ready, then the developer notify it to the maintainer.
3. The maintainer checks the branch and merges into the main branch.

The biggest downside of this was usually the branches are over populated. It
made the log of the repo quite confusing. And the result of `git branch` always
exceeded one page.

Another thing had to be improved was the logging for merging. Generally, we
only have one maintainer on our team, and he handled those merge notices from
each developers, but the procedure was rather obscure and even the notice was
sometimes forgotten for busy work.


#### Migration to [GitLab] with Multiple Personal Repositories

We gradually moved to [GitLab]. Still there are some rumors about the
difficulty of deploying self-hosted [GitLab]. And we don't dare doing such
risky experiment. My team is still small, and [GitLab]'s free plan has good
enough features.

These are the details of how to move to [GitLab].

1. The maintainer creates the main repo and the group.
2. The developers sign up, join the group, create their own repo.
3. The developers change the remote repo configuration on the local repo.
```sh
git remote set-url origin {personal remote repo}
git remote add main {main remote repo}
git remote set-url --push main DISABLE_PUSH_TO_MAIN # This is optional
```
<ol start="4"><li>Clean up the unnecessary branches</li></ol>

*Note:* `DISABLE_PUSH_TO_MAIN` is arbiturarily chosen string. You can set any
invalid URL for `main`'s push URL for disabling push to the `main` repo. If you
are one of the maintainers, then it's not necessary.

#### Now, at My Work

Now, each developer manages their own repo. And time to time they checkes the
main repo with `git fetch main`. If a pile of commits are ready to be merged,
then the developer create a merge request.

#### The Advatages of using this new system

There are some unexpected advatages.

* You can **comment on each diff line** of code in [GitLab]. This makes the
  feedback easy and crystal clear.
* You can configure a repo to **limit the branch to push**. You can easily
  protect your main repo.
* You can use [GitLab]'s **contiuous integration** feature. Once it's
  configured, all you need to do is pushing to the remote branch, and the other
  job is done by automated [GitLab].
* You can set a **flag on the merge request**. And then the request will be
  merged automatically after the contiuous integration is done successfully.

Yet we're discovering the good side of [GitLab].


[Git]: https://git-scm.com
[GitLab]: https://gitlab.com
