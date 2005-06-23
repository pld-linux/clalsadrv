Summary:	clalsadrv library
Summary(pl):	Biblioteka clalsadrv
Name:		clalsadrv
Version:	1.0.1
Release:	0.1
License:	GPL v2
Group:		Libraries
Source0:	http://ftp.debian.org/debian/pool/main/c/%{name}/%{name}_%{version}.orig.tar.gz
# Source0-md5:	2f693c52173aac55dcb35dcfca79df91
URL:		http://packages.qa.debian.org/c/clalsadrv.html
BuildRequires:	sed >= 4.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
clalsadrv library

%description -l pl
Biblioteka clalsadrv

%package devel
Summary:	Header files for clalsadrv library
Summary(pl):	Pliki nag³ówkowe biblioteki clalsadrv
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for clalsadrv library.

%description devel -l pl
Pliki nag³ówkowe biblioteki clalsadrv.

%prep
%setup -q

%build
%{__make}

%install
install -d $RPM_BUILD_ROOT{%{_libdir},%{_includedir}}

%makeinstall CLALSADRV_LIBDIR=$RPM_BUILD_ROOT%{_libdir} \
        CLALSADRV_INCDIR=$RPM_BUILD_ROOT%{_includedir}


%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS COPYING
%attr(755,root,root) %{_libdir}/lib*.so.*.*.*

%files devel
%defattr(644,root,root,755)
%{_includedir}/*.h
