Summary:	Library for access to the system servicelog
Summary(pl.UTF-8):	Biblioteka dostępu do logu zdarzeń serwisowych w systemie
Name:		libservicelog
Version:	1.1.18
Release:	1
License:	LGPL v2+
Group:		Libraries
Source0:	http://downloads.sourceforge.net/linux-diag/%{name}-%{version}.tar.gz
# Source0-md5:	8275e7d4d6922c7b7bdb3fe49271f949
Patch0:		%{name}-link.patch
Patch1:		%{name}-install.patch
URL:		http://linux-diag.sourceforge.net/servicelog/
BuildRequires:	autoconf >= 2.59
BuildRequires:	automake
BuildRequires:	bison
BuildRequires:	flex
BuildRequires:	librtas-devel
BuildRequires:	libtool
BuildRequires:	sqlite3-devel >= 3
# requires ppc-specific librtas
ExclusiveArch:	ppc ppc64
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package contains a library to create and maintain a database for
storing events related to system service. This database allows for the
logging of serviceable and informational events, and for the logging
of service procedures that have been performed upon the system.

%description -l pl.UTF-8
Ten pakiet zawiera bibliotekę tworzącą i utrzymującą bazę danych do
przechowywania zdarzeń związanych z serwisowaniem systemu. Baza ta
pozwala na logowanie zdarzeń serwisowych i informacyjnych oraz
wykonanych w systemie procedur serwisowych.

%package devel
Summary:	Header files for servicelog library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki servicelog
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	sqlite3-devel

%description devel
Header files for servicelog library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki servicelog.

%package static
Summary:	Static servicelog library
Summary(pl.UTF-8):	Statyczna biblioteka servicelog
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static servicelog library.

%description static -l pl.UTF-8
Statyczna biblioteka servicelog.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/var/lib/servicelog

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# obsoleted by pkgconfig
%{__rm} $RPM_BUILD_ROOT%{_libdir}/libservicelog.la

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README
%attr(755,root,root) %{_libdir}/libservicelog-1.1.so.*.*.*
%ghost %{_libdir}/libservicelog-1.1.so.1
%dir /var/lib/servicelog

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libservicelog.so
%{_includedir}/servicelog-1
%{_pkgconfigdir}/servicelog-1.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libservicelog.a
