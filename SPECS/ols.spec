# NOTE:
# Fedora does not currently support the Odin programming language toolchain.
# As a result, the binaries packaged here are sourced from upstream GitHub
# release artifacts rather than being built from source within Fedora
# infrastructure.
#
# Due to downstream packaging constraints, builtin Odin symbols may not fully
# resolve at runtime. This is a known limitation of the current packaging
# approach and not a defect in ols itself.
#
# This limitation has been communicated to the upstream maintainers and a fix is being discussed.

Name:           ols
Version:        2026.02
Release:        1%{?dist}
Summary:        Odin programming language language server protocol and formatter

License:        MIT
URL:            https://github.com/DanielGavin/ols

%global debug_package %{nil}
%global ols_tag dev-2026-02

%ifarch x86_64
%global architecture x86_64-unknown-linux-gnu
%global hash a713064736034e9d08ff332a88a5f599f23fe6bae1b8f1af9242f3de65a26cc4
%endif
%ifarch aarch64
%global architecture arm64-unknown-linux-gnu
%global hash 2f21e60bd65317f59e3adfd5f2099017ba88f5c58689f238c28561df4ab3cd2a
%endif

Source0:   https://github.com/DanielGavin/ols/archive/refs/tags/%{ols_tag}.tar.gz#/ols-%{ols_tag}.tar.gz
Source1:   https://github.com/DanielGavin/ols/releases/download/%{ols_tag}/ols-x86_64-unknown-linux-gnu.zip
Source2:   https://github.com/DanielGavin/ols/releases/download/%{ols_tag}/ols-arm64-unknown-linux-gnu.zip

ExclusiveArch:  x86_64 aarch64

BuildRequires: coreutils
BuildRequires: unzip

%description
Language Server Protocol and formatter for the Odin programming language.
This project is still in early development. Builtin symbols may not fully resolve at this time.
This is an unofficial COPR package of ols and is maintained independently.

%prep
%autosetup -n ols-%{ols_tag}
mkdir -p bins
%ifarch x86_64
unzip -q %{SOURCE1} -d bins
%endif
%ifarch aarch64
unzip -q %{SOURCE2} -d bins
%endif

%check
%ifarch x86_64
printf '%s  %s\n' "%{hash}" "%{SOURCE1}" | sha256sum -c -
%endif
%ifarch aarch64
printf '%s  %s\n' "%{hash}" "%{SOURCE2}" | sha256sum -c -
%endif
./bins/odinfmt-%{architecture} -h

%install
install -d -m 0755 %{buildroot}%{_bindir}
install -m 0755 bins/ols-%{architecture} %{buildroot}%{_bindir}/ols
install -m 0755 bins/odinfmt-%{architecture} %{buildroot}%{_bindir}/odinfmt

%files
%license LICENSE
%doc README.md
%{_bindir}/ols
%{_bindir}/odinfmt

%changelog
* Mon Feb 16 2026 Fedora COPR <sisyphus1813@protonmail.com> - 2026.02-1
- Initial COPR build of ols from dev-2026-02
