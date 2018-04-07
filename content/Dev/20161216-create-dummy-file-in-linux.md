Title: Create dummy file in Linux
Date: 2016-12-16 10:00
Modified: 2018-04-03 17:00
Tags: linux, dummy, command, CLI
Summary: A few options to create a dummy file in Linux

### 3 options to create a dummy file

Sometimes a big size dummy file is necessary.
There are roughly 3 ways to achieve this: `dd`, `truncate`, `fallocate`.
I found them from [this Stackoverflow answer](http://stackoverflow.com/questions/257844/quickly-create-a-large-file-on-a-linux-system).

#### 1. `dd`

It's the most famous one, but it's basically for copy data from one to another
in hard way. It's accurate but slow. If you want just a dummy file, it's not a
good choice.

#### 2. `truncate`

It's maybe the fasted way. But it doesn't actually allocate the space. What it
does is cheat the file system with repetition of smaller amount of data. If you
really want to *allocate* the space, it's not the best one.

#### 3. `fallocate`

Now, it's the last and **the best** option.

### More about `fallocate`

The basic usage is

```bash
fallocate -l [length] [filename]
```
