# odin-lang-rpm

This repository contains RPM packaging files for [the odin-lang COPR](https://copr.fedorainfracloud.org/coprs/sisyphus1813/odin-lang/) which hosts unofficial packages for the Odin programming language and its tooling ecosystem.  
[Odin-lang upstream repository](https://github.com/odin-lang/Odin)  
[LSP/formatter upstream repository](https://github.com/DanielGavin/ols)  

## Installation

```bash
sudo dnf copr enable sisyphus1813/odin-lang
sudo dnf install -y odin-lang ols
```
This installs the Odin programming language (compiler + standard library), ols (Odin Language Server), and odinfmt (Odin formatter).

Please be sure to log out and log back in after your first install. Failing to do so will result in the odin compiler failing with an error message such as:
```
Internal Compiler Error: Cannot find the library collection 'base'. Is the ODIN_ROOT set up correctly?
The process was killed by SIGILL: Illegal instruction
```

### Non-standard shells
This project relies on exporting ODIN_ROOT through /etc/profile.d/odin.sh to avoid touching the user's shell configuration. This works fine for standard shells such as BASH or zsh.  
If you are using a shell that does not source /etc/profile.d on login by default (such as yash), you will need to manually ensure such directory is sourced at login. Alternatively, you can also export ODIN_ROOT in your shell configuration file. To do so, add:
```
export ODIN_ROOT="/usr/lib/odin"
```
