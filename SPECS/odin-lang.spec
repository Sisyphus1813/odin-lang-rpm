Name:           odin-lang
Version:        2026.02
Release:        2%{?dist}
Summary:        Odin programming language compiler and standard library

License:        zlib
URL:            https://odin-lang.org/

%global __provides_exclude_from ^%{_prefix}/lib/odin/vendor/.*$
%global __requires_exclude_from ^%{_prefix}/lib/odin/vendor/.*$
%global odin_tag 5d94c01e47fcdb7d0938a9125d17a08bde4f041b

Source0:        https://github.com/odin-lang/Odin/archive/%{odin_tag}.tar.gz#/Odin-%{odin_tag}.tar.gz
Source1:        odin.sh

ExclusiveArch:  x86_64 aarch64

BuildRequires:  make
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  clang
BuildRequires:  llvm-devel
BuildRequires:  lld

%description
Odin is a general-purpose programming language with distinct typing built for high performance, modern systems and data-oriented programming.
This package builds Odin from source and installs the compiler along with the base, core, and vendor library collections.
This is an unofficial COPR packaging of Odin and is maintained independently.
Upstream project: https://github.com/odin-lang/Odin

%prep
%autosetup -n Odin-%{odin_tag}

%build
export CC=clang
export CXX=clang++
make release

%check
./odin version

%install
install -d -m 0755 %{buildroot}%{_bindir}
install -m 0755 odin %{buildroot}%{_bindir}/odin
install -d -m 0755 %{buildroot}%{_prefix}/lib/odin
cp -r base %{buildroot}%{_prefix}/lib/odin/base
cp -r core %{buildroot}%{_prefix}/lib/odin/core
cp -r vendor %{buildroot}%{_prefix}/lib/odin/vendor
install -d -m 0755 %{buildroot}%{_sysconfdir}/profile.d
install -m 0644 %{SOURCE1} %{buildroot}%{_sysconfdir}/profile.d/odin.sh

%files
%license LICENSE
%doc README.md
%{_bindir}/odin
%{_prefix}/lib/odin
%config(noreplace) %{_sysconfdir}/profile.d/odin.sh

%changelog
* Sun Feb 22 2026 Fedora COPR <sisyphus1813@protonmail.com> - 2026.02-2
- Update to Odin Version 2026.02:5d94c01e47fcdb7d0938a9125d17a08bde4f041b
