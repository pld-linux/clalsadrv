Summary:	ALSA driver C++ access library
Summary(pl.UTF-8):	Biblioteka dostępu do sterowników ALSA w C++
Name:		clalsadrv
Version:	1.0.1
Release:	0.2
License:	GPL v2
Group:		Libraries
# please use original tarballs in future
#http://kokkinizita.linuxaudio.org/linuxaudio/downloads/%{name}-%{version}.tar.bz2
Source0:	http://ftp.debian.org/debian/pool/main/c/clalsadrv/%{name}_%{version}.orig.tar.gz
# Source0-md5:	2f693c52173aac55dcb35dcfca79df91
URL:		http://kokkinizita.linuxaudio.org/linuxaudio/
BuildRequires:	alsa-lib-devel
BuildRequires:	libstdc++-devel
BuildRequires:	sed >= 4.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
clalsadrv library allows to access ALSA sound card drivers in a C++
based program.

%description -l pl.UTF-8
Biblioteka clalsadrv pozwala na dostęp do sterownika karty dźwiękowej
z poziomu programu napisanego w C++.

%package devel
Summary:	Header files for clalsadrv library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki clalsadrv
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	alsa-lib-devel

%description devel
Header files for clalsadrv library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki clalsadrv.

%prep
%setup -q

%build
%{__make} \
	CXX="%{__cxx}" \
	CPPFLAGS="%{rpmcxxflags} -fPIC -I. -D_REENTRANT -DPOSIX_THREAD_SEMANTICS"

%install
rm -rf $RPM_BUILD_ROOT
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
%attr(755,root,root) %{_libdir}/libclalsadrv.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libclalsadrv.so.1

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libclalsadrv.so
%{_includedir}/clalsadrv.h
