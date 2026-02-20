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

## Limitations
ols Builtin symbols may not fully resolve at this time due to prior upstream packaging constraints. A fix for this has already been merged (see ols commit fd541bfb2789f32e4adc6b0d3c0577687a512208) and will be included in the next upstream release.