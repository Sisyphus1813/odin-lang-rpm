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
Fedora does not currently support the Odin programming language toolchain.
As a result, the binaries packaged for ols/odinfmt are sourced from upstream GitHub release artifacts rather than being built from source within Fedora
infrastructure.

In addition, due to upstream packaging constraints, builtin Odin symbols may not fully resolve at runtime. This is a known limitation of the current packaging approach (as it relates to externally managed packages) and not a defect in ols itself. This limitation has been communicated to the upstream maintainers and a possible solution is being discussed.
