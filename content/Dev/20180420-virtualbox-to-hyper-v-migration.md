Title: Migration from VirtualBox to Hyper-V
Date: 2018-04-20 12:05
Tags: windows, virtual machine, hyper-v, migration
Summary: I was stuck in quite a problem of this migration.

### Background Story

The first purpose was running [Gitlab Runner][] in a local machine.
Then I realise that I need [Docker for Windows][] for the local Windows machine.
And, of course, unfortunately, it requires [Hyper-V][].

The reason why it's unfortunate is that I was using VirtualBox quite actively,
including 2 active virtual machines, and when I install [Hyper-V][],
then I can't use VirtualBox anymore.

I was thinking to use old [Docker Toolbox][], but I'm not sure until when it's supported.
So, I searched for the way to migrate VirtualBox VM to [Hyper-V][] VM.

### The Instruction

#### 1. Export existing VirtualBox VMs

That's an easy part. In VirtualBox GUI, you can find export menu.
If you click it, then a popup comes up, and you can choose the location of the exported file.
Note that, you need to change the format. The recommended one is **OVF 2.0**

#### 2. Disassemble the exported file

The OVF format is basically a zip archive with some information for the VM.
You can unzip it with your favorite unzipper. I used [7zip][].

The only file it matters is `*.vmdk` file. It is the virtual HDD of your VM.

#### 3. Install some tools

##### [Microsoft Virtual Machine Converter][]

Firstly, [Hyper-V][] is picky enough not to recognize this `*.vmdk` format.
So, you need to convert it with a tool that MicroSoft provides.
It's called [Microsoft Virtual Machine Converter][].
You can download it, and install it.

Open Powershell, and run this command.
```
Import-Module 'C:\Program Files\Microsoft Virtual Machine Converter\MvmcCmdlet.psd1'
Convert-VHD exported_file.vmdk target_file.vhdx -Passthru
```

##### [dsfok][]

In high possibility, the command above will fail.
Because the format for the VMDK file from VirtualBox has some kind of wrong description.
To edit the description of VMDK file, this tool is required.

You can download and unzip it, then you can use it.

#### 4. Tweak the VMDK file.

```
path\to\dsfok\dsfo.exe "path\to\vmdk\file.vmdk" 512 1024 desc.txt
```

A new `desc.txt` file is now created, and it contains the description of the VMDK file.
Edit the file accordingly by removing or commenting out the erronous line.
The error message from [Microsoft Virtual Machine Converter][] has some hints.

Then apply the new description file into the VMDK file.

```
path\to\dsfok\dsfi.exe "path\to\vmdk\file.vmdk" 512 1024 desc.txt
```

Run [Microsoft Virtual Machine Converter][], if there's no more errors.

#### 5. Create a new VM in [Hyper-V][]

If there's no more error, then [Microsoft Virtual Machine Converter][] will create a new virtual HDD for [Hyper-V][].

Creating a new VM in [Hyper-V][] is quite straight forward.
Don't forget to add newly created virtual HDD to this new VM.

### Something left

Unfortunately, the migration is not fully done yet.
The network configuration is missing.

I can't create any virtual swich, and currently, I don't have network access from the host machine to guest VM.
The reason here is Trend Office Scan prevents to create virtual switch in [Hyper-V][].
And this Trend Office Scan is managed by company's tech support team,
and I don't have permission to change the configuration or disable it temporarily.

I'm longing for using [Gitlab Runner] on the local machine someday.

### References

* https://aadamich.wordpress.com/articles/hyper-v/convert-and-launch-virtualbox-vhd-on-hyper-v/
* https://blogs.msdn.microsoft.com/timomta/2015/06/11/how-to-convert-a-vmware-vmdk-to-hyper-v-vhd/
* https://stackoverflow.com/questions/37481737/error-when-converting-vmware-virtual-disk-to-hyperv

[7zip]: https://www.7-zip.org/
[Docker for Windows]: https://store.docker.com/editions/community/docker-ce-desktop-windows
[Docker Toolbox for Windows]: https://docs.docker.com/toolbox/toolbox_install_windows/
[Gitlab Runner]: https://docs.gitlab.com/runner/
[Hyper-V]: https://docs.microsoft.com/en-us/virtualization/hyper-v-on-windows/about/
[Microsoft Virtual Machine Converter]: http://www.microsoft.com/en-us/download/details.aspx?id=42497
[dsfok]: http://members.ozemail.com.au/~nulifetv/freezip/freeware/dsfok.zip
