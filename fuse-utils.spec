%define name    fuse-utils
%define version 0.8.0.1
%define release %mkrel 5

Name: %{name}
Summary: The Fuse utilities are a few tools to deal with ZX Spectrum emulator files
Version: %{version}
Release: %{release}
License: GPL
URL: https://www.srcf.ucam.org/~pak21/spectrum/fuse.html
Source: http://www.srcf.ucam.org/~pak21/spectrum/%{name}-%{version}.tar.gz
Patch1: fuse-utils-fix-build.diff
Group: Emulators
BuildRequires: libz-devel libspectrum-devel libgcrypt-devel glib2-devel
BuildRoot: %{_tmppath}/%{name}-%{version}-root

%description
The available utilities are:

* listbasic: list the BASIC in a snapshot or tape file.
* rzxcheck: verify the digital signature in an RZX file.
* rzxdump: list the contents of an RZX input recording file.
* rzxtool: add, extract or remove the embedded snapshot from an RZX file,
  or compress or uncompress the file.
* scl2trd: convert .scl disk images to .trd disk images.
* snapconv: convert between snapshot formats.
* tapeconv: convert between .tzx and .tap files.
* tzxlist: list the contents of a TZX file.

%prep
%setup -q
%patch1 -p0

%build
%configure --without-gcrypt
%make

%install
%makeinstall

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc README AUTHORS ChangeLog
%{_bindir}/*
%{_mandir}/man1/*

