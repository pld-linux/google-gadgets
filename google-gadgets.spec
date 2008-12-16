# use this to get latest rev:
# svn export http://google-gadgets-for-linux.googlecode.com/svn/trunk/ google-gadgets-for-linux
# TODO:
# - add gtk BRs
# - update desc
# Conditional build:
#% bcond_with	debug	# build with debug
#% bcond_without	gtk	# without gtk support
#% bcond_without	qt	# without qt support
#% bcond_without	gadgets	# without gadgets

%define		realname	google-gadgets
%define		rev	r1028

Summary:	google-gadgets-for-linux
Name:		google-gadgets-for-linux
Version:	0.10.4
Release:	1
License:	Apache License v2.0
Group:		X11/Applications
#Source0:	%{name}-%{version}-%{rev}.tar.bz2
Source0:	http://google-gadgets-for-linux.googlecode.com/files/%{name}-%{version}.tar.bz2
# Source0-md5:	0ef0a62e0a575388084a77759b646718
Source1:	%{name}-gtk.desktop
Source2:	%{name}-qt.desktop
Patch0:		%{name}-cmake.patch
Patch1:		%{name}-link_with_qtnetwork.patch
Patch2:		%{name}-js.patch
URL:		http://code.google.com/p/google-gadgets-for-linux/
BuildRequires:	QtCore-devel >= 4.4.3
BuildRequires:	QtNetwork-devel >= 4.4.3
BuildRequires:	QtScript-devel >= 4.4.3
BuildRequires:	QtWebKit-devel >= 4.4.3
BuildRequires:	cmake >= 2.6.1-2
BuildRequires:	curl-devel >= 7.18.2
BuildRequires:	dbus-devel >= 1.0.2
BuildRequires:	flex
BuildRequires:	gstreamer-plugins-base-devel >= 0.10.0
BuildRequires:	libltdl-devel
BuildRequires:	librsvg-devel
BuildRequires:	libtool >= 1.5.22
BuildRequires:	libxml2-devel >= 2.4.0
BuildRequires:	pkgconfig
BuildRequires:	xulrunner-devel >= 1.8
BuildRequires:	zip
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
google-gadgets-for-linux.

%package gadgets
Summary:	google-gadgets set
Summary(pl.UTF-8):	Zestaw gadżetów google-gadgets
Group:		X11/Applications
Requires:	%{name} = %{version}-%{release}

%description gadgets
Google-gadgets set.

%description gadgets -l pl.UTF-8
Zestaw gadżetów google-gadgets.

%package devel
Summary:	Header files for google-gadgets library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki google-gadgets
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for google-gadgets library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki google-gadgets.

%package static
Summary:	Static google-gadgets libraries
Summary(pl.UTF-8):	Statyczne biblioteki google-gadgets
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static google-gadgets libraries.

%description static -l pl.UTF-8
Statyczne biblioteki google-gadgets.

%package qt
Summary:	Qt Runtime Environment
Group:		X11/Applications
Requires:	%{name} = %{version}-%{release}

%description qt
Qt runtime environment.

%package gtk
Summary:	GTK Runtime Environment
Group:		X11/Applications
Requires:	%{name} = %{version}-%{release}

%description gtk
GTK runtime environment.

%prep
%setup -q
find -name '.svn' | xargs rm -rf
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
install -d build
cd build
%cmake \
	-DCMAKE_INSTALL_PREFIX=%{_prefix} \
	-DSYSCONF_INSTALL_DIR=%{_sysconfdir} \
	-DGTKMOZEMBED_CFLAGS="-I$EMBED_INCDIR/js -I$EMBED_INCDIR/string" \
%if "%{_lib}" == "lib64"
	-DLIB_SUFFIX=64 \
%endif
	../

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_desktopdir},%{_pixmapsdir}}

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

# desync with cmake/ac makefiles
mv $RPM_BUILD_ROOT%{_datadir}/mime/packages/{00-,}google-gadgets.xml
# desktop files
install %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}/ggl-gtk.desktop
install %{SOURCE2} $RPM_BUILD_ROOT%{_desktopdir}/ggl-qt.desktop

rm -f $RPM_BUILD_ROOT%{_libdir}/google-gadgets/modules/smjs-script-runtime.la

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%{_datadir}/mime/packages/google-gadgets.xml
%dir %{_datadir}/%{realname}
%{_datadir}/%{realname}/*.gg
%{_desktopdir}/ggl-designer.desktop
%{_iconsdir}/*/*/*/*.png
%{_pixmapsdir}/%{realname}.png
%attr(755,root,root) %{_libdir}/*.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/*.so.0
%attr(755,root,root) %{_libdir}/%{realname}/gtkmoz-browser-child
%dir %{_libdir}/%{realname}
%dir %{_libdir}/%{realname}/modules

%files qt 
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/ggl-qt
%{_desktopdir}/ggl-qt.desktop

%files gtk
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/ggl-gtk
%{_desktopdir}/ggl-gtk.desktop

%files gadgets
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/%{realname}/modules/*.so

%files devel
%defattr(644,root,root,755)
%dir %{_libdir}/%{realname}/include
%dir %{_libdir}/%{realname}/include/ggadget
%{_libdir}/%{realname}/include/ggadget/*.h
%dir %{_includedir}/%{realname}
%dir %{_includedir}/%{realname}/ggadget
%{_includedir}/%{realname}/ggadget/*.h
%dir %{_includedir}/%{realname}/ggadget/dbus
%{_includedir}/%{realname}/ggadget/dbus/*.h
%dir %{_includedir}/%{realname}/ggadget/gtk
%{_includedir}/%{realname}/ggadget/gtk/*.h
%dir %{_includedir}/%{realname}/ggadget/npapi
%{_includedir}/%{realname}/ggadget/npapi/*.h
%dir %{_includedir}/%{realname}/ggadget/qt
%{_includedir}/%{realname}/ggadget/qt/*.h
%dir %{_includedir}/%{realname}/ggadget/js
%{_includedir}/%{realname}/ggadget/js/*.h
%dir %{_includedir}/%{realname}/ggadget/xdg
%{_includedir}/%{realname}/ggadget/xdg/*.h
%attr(755,root,root) %{_libdir}/*.so
%{_pkgconfigdir}/*.pc

#%files static
#%defattr(644,root,root,755)
#%{_libdir}/lib*.a
