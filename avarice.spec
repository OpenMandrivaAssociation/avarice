Summary:	Program for interfacing the Atmel JTAG ICE to GDB
Name:		avarice
Version:	2.12
Release:	3
License:	GPLv2+
Group:		Development/Other
Url:		https://sourceforge.net/projects/avarice
Source0:	http://downloads.sourceforge.net/project/%{name}/%{name}/%{name}-%{version}/%{name}-%{version}.tar.bz2
# From Debian
Source1:	avarice.rules
Patch0:		avarice-2.10-link.patch
Patch1:		avarice-2.12-headers.patch
BuildRequires:	binutils-devel
BuildRequires:	gettext-devel
BuildRequires:	pkgconfig(libusb)

%description
Program for interfacing the Atmel JTAG ICE to GDB to allow users to debug their
embedded AVR target.

%files
%doc AUTHORS ChangeLog NEWS
%{_bindir}/*
%{_datadir}/%{name}
%{_mandir}/man1/*
/lib/udev/rules.d/60-avarice.rules

#----------------------------------------------------------------------------

%prep
%setup -q
%patch0 -p0 -b .link
%patch1 -p1

%build
%configure2_5x
%make

%install
%makeinstall_std

mkdir -p %{buildroot}/lib/udev/rules.d/
install -m 0644 %{SOURCE1} %{buildroot}/lib/udev/rules.d/60-avarice.rules

