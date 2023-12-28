Summary:	ALSA driver C++ access library
Summary(pl.UTF-8):	Biblioteka dostępu do sterowników ALSA w C++
Name:		clalsadrv
Version:	2.0.0
Release:	1
License:	GPL v2
Group:		Libraries
Source0:	http://kokkinizita.linuxaudio.org/linuxaudio/downloads/%{name}-%{version}.tar.bz2
# Source0-md5:	be123e1701e4b6c6300907df949bd71c
URL:		http://kokkinizita.linuxaudio.org/linuxaudio/
BuildRequires:	alsa-lib-devel
BuildRequires:	clthreads-devel >= 2.4.0
BuildRequires:	libstdc++-devel
BuildRequires:	sed >= 4.0
Requires:	clthreads >= 2.4.0
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
Requires:	libstdc++-devel

%description devel
Header files for clalsadrv library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki clalsadrv.

%prep
%setup -q

%{__sed} -i -e 's/ldconfig /ldconfig -n $(DESTDIR)/' libs/Makefile

%build
%{__make} -C libs \
	CXX="%{__cxx}" \
	CPPFLAGS="%{rpmcxxflags} %{rpmcppflags} -fPIC -I. -D_REENTRANT -D_POSIX_THREAD_SEMANTICS -Wall"

ln -sf libclalsadrv.so.2.0.0 libs/libclalsadrv.so

LDLIBS="-lasound" \
%{__make} -C apps \
	CXX="%{__cxx}" \
	CPPFLAGS="%{rpmcxxflags} %{rpmcppflags} -I../libs -DVERSION=\"%{version}\" -Wall" \
	LDFLAGS="%{rpmldflags} -L../libs"

%install
rm -rf $RPM_BUILD_ROOT
#install -d $RPM_BUILD_ROOT{%{_libdir},%{_includedir}}

%{__make} -C libs install \
	DESTDIR=$RPM_BUILD_ROOT \
	PREFIX=%{_prefix} \
	LIBDIR=%{_lib}

%{__make} -C apps install \
	DESTDIR=$RPM_BUILD_ROOT \
	PREFIX=%{_prefix}

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS
%attr(755,root,root) %{_bindir}/alsa-latency
%attr(755,root,root) %{_bindir}/alsa-loopback
%attr(755,root,root) %{_libdir}/libclalsadrv.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libclalsadrv.so.2

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libclalsadrv.so
%{_includedir}/clalsadrv.h
