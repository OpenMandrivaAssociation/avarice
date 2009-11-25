Name: avarice
Version: 2.10
Release: %mkrel 1
Summary: Program for interfacing the Atmel JTAG ICE to GDB
Group: Development/Other
License: GPLv2
URL: http://sourceforge.net/projects/avarice
Source0: http://downloads.sourceforge.net/project/%{name}/%{name}/%{name}-%{version}/%{name}-%{version}.tar.bz2
BuildRequires: binutils-devel
Buildroot: %{_tmppath}/%{name}-%{version}-root

%description
Program for interfacing the Atmel JTAG ICE to GDB to allow users to debug their
embedded AVR target

%prep
%setup -q

%build
%configure2_5x
%make

%install
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

%files
%defattr(-,root,root,-)
%doc AUTHORS ChangeLog NEWS
%{_bindir}/*
%{_datadir}/%{name}
%{_mandir}/man1/*
