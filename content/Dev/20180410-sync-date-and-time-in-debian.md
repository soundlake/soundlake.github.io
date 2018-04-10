Title: Sync Date and Time in Debian
Date: 2018-04-11 12:05
Tags: linux, debian, ntp
Summary: Using ntp, you can easily sync your Debian machine's date ane time

I thought I only need NTP client to synchronize the date and time of my linux
machine. But apparently, `ntpdate` runs once, and [Debian][] "expects" the user
to install `ntp` according to [this stack exchange
answer](https://unix.stackexchange.com/questions/137266/how-to-keep-debian-internal-clock-synchronized-with-ntp-servers/137269#137269).

Installing it is just easy, especially if you're familiar with [Debian][] or
[Ubuntu][].

```sh
sudo apt-get install ntp
```

After the installation, you can check if it's running.

```sh
sudo systemctl status ntp
```

[Debian]: https://www.debian.org
[Ubuntu]: https://www.ubuntu.com
