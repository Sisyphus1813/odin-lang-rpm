Name:           ols
Version:        2026.02
Release:        5%{?dist}
Summary:        Odin programming language language server protocol and formatter

License:        MIT
URL:            https://github.com/DanielGavin/ols

%global debug_package %{nil}
%global ols_tag e64cb328237427d1abbaa677afb498bee7271dbb

Source0:   https://github.com/DanielGavin/ols/archive/%{ols_tag}.tar.gz#/ols-%{ols_tag}.tar.gz

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

%build
odin build src/ \
  -show-timings \
  -collection:src=src \
  -out:ols \
  -no-bounds-check \
  -o:speed \
  -define:VERSION="dev-2026-02-22-ed829a9"

odin build tools/odinfmt/main.odin \
  -file \
  -show-timings \
  -collection:src=src \
  -out:odinfmt \
  -o:speed

  
%check
./odinfmt -h
./ols version

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
* Sun Feb 22 2026 Fedora COPR <sisyphus1813@protonmail.com> - 2026.02-5
- Update to ols version 2026.02:e64cb328237427d1abbaa677afb498bee7271dbb
