Title: Add Binary Path in PowerShell
Date: 2016-12-28 10:00
Modified: 2018-04-03 21:00
Tags: Windows, PowerShell, environment
Summary: Configure your PATH environment variable in PowerShell

Recently, I need to use `makecert` command in PowerShell, but `makecert.exe` wasn't
there by default. So, I installed a few things. But still it didn't work. I found
the executable file under `C:\Program Files (x86)\Windows Kits\10\bin\x64\`, but the
command wasn't recognized. Apparently, just like bash or other linux shell, it needs
profile file.

The default path for the profile file is
`C:\Users\[username]\Documents\WindowsPowerShell\Microsoft.PowerShell_profile.ps1`.
It is stored in `$profile` variable. You can check its value by simply typing the
variable in PowerShell.

```sh
$profile
```

But the file does not exist by default. You can check if the file exists with
typing in the following command.

```sh
test-path $profile
```

There's no `touch` command in PowerShell. Instead, there is `new-item` command.

```sh
New-Item $profile
```

However, the directory does not exist either by default. You will see the
following error message.
```
New-Item : Could not find a part of the path
'C:\Users\[username]\Documents\WindowsPowerShell\Microsoft.PowerShell_profile.ps1'.
```

You can easily create a directory with `mkdir`. After creating the directory,
then try `New-Item` command once again. Then, you have your own PowerShell
profile. In this file, you can add the following line, then restart the
PowerShell.

```
function Add-Path {
  <#
    .SYNOPSIS
      Adds a Directory to the Current Path
    .DESCRIPTION
      Add a directory to the current path.  This is useful for
      temporary changes to the path or, when run from your
      profile, for adjusting the path within your powershell
      prompt.
    .EXAMPLE
      Add-Path -Directory "C:\Program Files\Notepad++"
    .PARAMETER Directory
      The name of the directory to add to the current path.
  #>

  [CmdletBinding()]
  param (
    [Parameter(
      Mandatory=$True,
      ValueFromPipeline=$True,
      ValueFromPipelineByPropertyName=$True,
      HelpMessage='What directory would you like to add?')]
    [Alias('dir')]
    [string[]]$Directory
  )

  PROCESS {
    $Path = $env:PATH.Split(';')

    foreach ($dir in $Directory) {
      if ($Path -contains $dir) {
        Write-Verbose "$dir is already present in PATH"
      } else {
        if (-not (Test-Path $dir)) {
          Write-Verbose "$dir does not exist in the filesystem"
        } else {
          $Path += $dir
        }
      }
    }

    $env:PATH = [String]::Join(';', $Path)
  }
}

Add-Path -Directory "C:\Program Files (x86)\Windows Kits\10\bin\x64\"
```

This code is create by [splunk](https://github.com/adrianhall) and published in
[his blog](http://blogs.splunk.com/2013/07/29/powershell-profiles-and-add-path/)

More information for PowerShell profile in
[MicroSoft Documentation](https://technet.microsoft.com/en-us/library/2008.10.windowspowershell.aspx).

PS. In my environment, running cusgom script was disabled. I had to run the
following command to enable to run the script.
```sh
Set-ExecutionPolicy remotesigned
```
