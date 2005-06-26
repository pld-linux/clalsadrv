Summary:	ALSA driver C++ access library
Summary(pl):	Biblioteka dostêpu do sterowników ALSA w C++
Name:		clalsadrv
Version:	1.0.1
Release:	0.2
License:	GPL v2
Group:		Libraries
# please use original tarballs in future
#http://users.skynet.be/solaris/linuxaudio/downloads/clalsadrv-1.0.1.tar.bz2
Source0:	http://ftp.debian.org/debian/pool/main/c/clalsadrv/%{name}_%{version}.orig.tar.gz
# Source0-md5:	2f693c52173aac55dcb35dcfca79df91
URL:		http://users.skynet.be/solaris/linuxaudio/
BuildRequires:	alsa-lib-devel
BuildRequires:	libstdc++-devel
BuildRequires:	sed >= 4.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
clalsadrv library allows to access ALSA sound card drivers
in a C++ based program.

%description -l pl
Biblioteka clalsadrv pozwala na dostêp do sterownika karty
d¼wiêkowej z poziomu programu napisanego w C++.

%package devel
Summary:	Header files for clalsadrv library
Summary(pl):	Pliki nag³ówkowe biblioteki clalsadrv
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	alsa-lib-devel

%description devel
Header files for clalsadrv library.

%description devel -l pl
Pliki nag³ówkowe biblioteki clalsadrv.

%prep
%setup -q

%build
%{__make} \
	CXX="%{__cxx}" \
	CPPFLAGS="%{rpmcxxflags} -fPIC -I. -D_REENTRANT -DPOSIX_THREAD_SEMANTICS"
[M`.[M`.[Ma.
%install
install -d $RPM_BUILD_ROOT{%{_libdir},%{_includedir}}

%{__make} install \
	CLALSADRV_LIBDIR=$RPM_BUILD_ROOT%{_libdir} \
	CLALSADRV_INCDIR=$RPM_BUILD_ROOT%{_includedir}

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS
%attr(755,root,root) %{_libdir}/lib*.so.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so
%{_includedir}/*.h
