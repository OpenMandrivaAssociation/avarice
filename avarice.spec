Name: avarice
Version: 2.6
Release: %mkrel 1
Summary: Program for interfacing the Atmel JTAG ICE to GDB
Group: Development
License: GPL
URL: http://sourceforge.net/projects/avarice
Source: http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.bz2
BuildRequires: binutils-devel

%description
Program for interfacing the Atmel JTAG ICE to GDB to allow users to debug their
embedded AVR target

%prep
%setup -q

%build
%configure
%make

%install
rm -rf %buildroot
make install DESTDIR=%buildroot

%clean
rm -rf %buildroot

%files
%defattr(-,root,root,-)
%doc AUTHORS ChangeLog COPYING NEWS
%{_bindir}/*
%{_datadir}/%{name}
%{_mandir}/man1/*
