Name:		avarice
Version:	2.12
Release:	1
Summary:	Program for interfacing the Atmel JTAG ICE to GDB
Group:		Development/Other
License:	GPLv2
URL:		http://sourceforge.net/projects/avarice
Source0:	http://downloads.sourceforge.net/project/%{name}/%{name}/%{name}-%{version}/%{name}-%{version}.tar.bz2
Patch0:		avarice-2.10-link.patch
BuildRequires:	binutils-devel

%description
Program for interfacing the Atmel JTAG ICE to GDB to allow users to debug their
embedded AVR target.

%prep
%setup -q
%patch0 -p0 -b .link

%build
%configure2_5x
%make

%install
%makeinstall_std

%files
%doc AUTHORS ChangeLog NEWS
%{_bindir}/*
%{_datadir}/%{name}
%{_mandir}/man1/*
