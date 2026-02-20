Name:           ols
Version:        2026.02
Release:        2%{?dist}
Summary:        Odin programming language language server protocol and formatter

License:        MIT
URL:            https://github.com/DanielGavin/ols

%global debug_package %{nil}
%global ols_tag dev-2026-02

Source0:   https://github.com/DanielGavin/ols/archive/refs/tags/%{ols_tag}.tar.gz#/ols-%{ols_tag}.tar.gz

ExclusiveArch:  x86_64 aarch64

BuildRequires: clang
BuildRequires: lld
BuildRequires: coreutils
BuildRequires: unzip
BuildRequires: odin-lang

%description
Language Server Protocol and formatter for the Odin programming language.
Builtin symbols may not fully resolve at this time, this will be patched in a future update briefly.
This is an unofficial COPR package of ols and is maintained independently.

%prep
%autosetup -n ols-%{ols_tag}
sed -i 's/git rev-parse --short HEAD/git rev-parse --short HEAD 2>\/dev\/null || echo nogit/' build.sh

%build
./build.sh
./odinfmt.sh

%check
./odinfmt -h

%install
install -d -m 0755 %{buildroot}%{_bindir}
install -m 0755 ols %{buildroot}%{_bindir}/ols
install -m 0755 odinfmt %{buildroot}%{_bindir}/odinfmt

%files
%license LICENSE
%doc README.md
%{_bindir}/ols
%{_bindir}/odinfmt

%changelog
* Fri Feb 20 2026 Fedora COPR <sisyphus1813@protonmail.com> - 2026.02-1
- Now builds by bootstrapping odin
- Builtin symbols do not fully resolve yet but a patch has been issued and will be released with the next build.
