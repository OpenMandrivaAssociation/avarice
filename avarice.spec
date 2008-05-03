Name:           avarice
Version:        2.6
Release:        2%{?dist}
Summary:        Program for interfacing the Atmel JTAG ICE to GDB

Group:          Applications/Engineering
License:        GPL
URL:            http://sourceforge.net/projects/avarice
Source0:        http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.bz2
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires:  binutils-devel
#Requires:       

%description
Program for interfacing the Atmel JTAG ICE to GDB to allow users to 
debug their embedded AVR target

%prep
%setup -q


%build
%configure
make %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT


%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%doc AUTHORS ChangeLog COPYING NEWS
%{_bindir}/*
%{_datadir}/%{name}
%{_mandir}/man1/*


