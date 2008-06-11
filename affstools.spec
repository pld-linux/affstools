Summary:	Utilities for affs, the AmigaOS filesystem
Summary(pl.UTF-8):	Narzędzia do affs - systemu plików AmigaOS
Name:		affstools
Version:	0.1a
Release:	1
License:	GPL v2+
Group:		Applications/System
Source0:	http://www.xs4all.nl/~zippel/%{name}-%{version}.tar.gz
# Source0-md5:	afa2bb5ea02d1cf959a84167868f5b59
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is the first public test release of affstools, tools for the
AmigaOS filesystem. It offers only very limited functionality and is
mainly intended to help the affs fs debugging. So far the package
includes only affsck and mkaffs.

%description -l pl.UTF-8
Ten pakiet zawiera pierwszą publiczną, testową wersję affstools -
narzędzi do systemu plików systemu AmigaOS. Mają bardzo ograniczoną
funkcjonalność, przeznaczoną głównie do pomocy przy diagnostyce
obsługi affs. Jak na razie pakiet zawiera tylko affsck i mkaffs.

%prep
%setup -q

%build
%configure2_13
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_sbindir}/affsck
%attr(755,root,root) %{_sbindir}/mkaffs
