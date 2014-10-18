Summary:	Library for handling OpenGL function pointer
Name:		libepoxy
Version:	1.2
Release:	1
License:	MIT
Group:		Libraries
Source0:	https://github.com/anholt/libepoxy/archive/v%{version}.tar.gz
# Source0-md5:	12d6b7621f086c0c928887c27d90bc30
URL:		https://github.com/anholt/libepoxy
BuildRequires:	EGL-devel
BuildRequires:	OpenGL-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	pkg-config
BuildRequires:	python3
BuildRequires:	xorg-libX11-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Epoxy is a library for handling OpenGL function pointer management.

%package devel
Summary:	Development files for libepoxy
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
This package contains the header files for developing applications
that use libepoxy.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal}
%{__autoheader}
%{__autoconf}
%{__automake}
%configure \
	--disable-silent-rules
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/*.la

%check
%{__make} check

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /usr/sbin/ldconfig
%postun	-p /usr/sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc COPYING README.md
%attr(755,root,root) %ghost %{_libdir}/libepoxy.so.0
%attr(755,root,root) %{_libdir}/libepoxy.so.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libepoxy.so
%{_includedir}/epoxy
%{_pkgconfigdir}/epoxy.pc

