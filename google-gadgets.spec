#
# Conditional build:
%bcond_without	gtk	# without gtk support
%bcond_without	qt	# without qt support
%bcond_without	gadgets	# without gadgets

%define 	rev	r1074
%define 	rel	1

# use this to get latest rev:
# svn export http://google-gadgets-for-linux.googlecode.com/svn/trunk/ google-gadgets-for-linux
Summary:	Google Gadgets for Linux
Name:		google-gadgets
Version:	0.10.5
Release:	0.%{rev}.%{rel}
License:	Apache License v2.0
Group:		X11/Applications
Source0:	%{name}-for-linux-%{version}-%{rev}.tar.bz2
# Source0-md5:	8f8fd6f7173fd26bf29fffafab9b0121
Source1:	%{name}-for-linux-gtk.desktop
Source2:	%{name}-for-linux-qt.desktop
Patch0:		%{name}-for-linux-cmake.patch
Patch1:		%{name}-for-linux-link_with_qtnetwork.patch
Patch2:		%{name}-for-linux-js.patch
URL:		http://code.google.com/p/google-gadgets-for-linux/
%if %{with qt}
BuildRequires:	QtCore-devel >= 4.4.3
BuildRequires:	QtNetwork-devel >= 4.4.3
BuildRequires:	QtScript-devel >= 4.4.3
BuildRequires:	QtWebKit-devel >= 4.4.3
%endif
BuildRequires:	autoconf
BuildRequires:	automake
%if %{with gtk}
BuildRequires:	cairo-devel >= 1.2.0
BuildRequires:	gtk+2-devel >= 2:2.10.0
BuildRequires:	startup-notification-devel
%endif
BuildRequires:	NetworkManager-devel >= 0.6.5
#BuildRequires:	cmake >= 2.6.1-2
BuildRequires:	curl-devel >= 7.18.2
BuildRequires:	dbus-devel >= 1.0.2
BuildRequires:	flex
BuildRequires:	gstreamer-plugins-base-devel >= 0.10.0
BuildRequires:	libltdl-devel
BuildRequires:	librsvg-devel
BuildRequires:	libtool >= 2:1.5.22
BuildRequires:	libxml2-devel >= 1:2.4.0
BuildRequires:	pkgconfig
BuildRequires:	xulrunner-devel >= 1.8
BuildRequires:	zip
BuildRequires:	zlib-devel >= 1.2.0
Requires:	libggadget = %{version}-%{release}
Provides:	google-gadgets-for-linux-gadgets = %{version}
Obsoletes:	google-gadgets-for-linux-gadgets
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Google Gadgets for Linux provides a platform for running desktop
gadgets under Linux, catering to the unique needs of Linux users. It's
compatible with the gadgets written for Google Desktop for Windows as
well as the Universal Gadgets on iGoogle.

%package -n libggadget
Summary:	Google Gadgets main libraries
Group:		Libraries
Requires:	dbus >= 1.0.21G
Requires:	libltdl
Obsoletes:	google-gadgets-for-linux

%description -n libggadget
This package contains the main Google Gadgets libraries, it is
required by both the GTK+ and QT versions of Google Gadgets.

%package -n libggadget-devel
Summary:	Google Gadgets main development files
Group:		Development/Libraries
Requires:	dbus-devel >= 1.0.2
Requires:	libggadget = %{version}-%{release}

%description -n libggadget-devel
This package contains the development files assoicated with
libggadget, it is needed to write programs that utilise libggadget.

%description -n libggadget-devel -l pl.UTF-8
Pliki nagłówkowe biblioteki google-gadgets.

%package -n libggadget-gtk
Summary:	Google Gadgets GTK+ library
Group:		Libraries
Requires:	cairo >= 1.2.0
Requires:	gtk+2 >= 2:2.10.0
Requires:	libggadget = %{version}-%{release}
Requires:	librsvg >= 1:2.18.0

%description -n libggadget-gtk
This package contains the GTK+ Google Gadgets library, it is required
to run the GTK+ version of Google Gadgets.

%package -n libggadget-gtk-devel
Summary:	Google Gadgets GTK+ development files
Group:		Development/Libraries
Requires:	cairo-devel >= 1.2.0
Requires:	gtk+2-devel >= 2:2.10.0
Requires:	libggadget-devel = %{version}-%{release}
Requires:	libggadget-gtk = %{version}-%{release}
Requires:	librsvg-devel >= 1:2.18.0

%description -n libggadget-gtk-devel
This package contains the development files assoicated with
libggadget-gtk, it is needed to write GTK+ programs that utilise
libggadget.

%package -n libggadget-qt
Summary:	Google Gadgets QT library
Group:		Libraries
Requires:	QtWebKit >= 4.4.0
Requires:	libggadget = %{version}-%{release}

%description -n libggadget-qt
This package contains the QT Google Gadgets library, it is required to
run the QT version of Google Gadgets.

%package -n libggadget-qt-devel
Summary:	Google Gadgets QT development files
Group:		Development/Libraries
Requires:	QtWebKit-devel >= 4.4.0
Requires:	libggadget-devel = %{version}-%{release}
Requires:	libggadget-qt = %{version}-%{release}

%description -n libggadget-qt-devel
This package contains the development files assoicated with
libggadget-qt, it is needed to write QT programs that utilise
libggadget.

%package gtk
Summary:	GTK+ Version of Google Gadgets
Group:		X11/Applications
Requires:	google-gadgets = %{version}-%{release}
Requires:	google-gadgets-gst = %{version}-%{release}
Requires:	google-gadgets-xul = %{version}-%{release}
Requires:	libggadget-gtk = %{version}-%{release}
Obsoletes:	google-gadgets-for-linux-gtk

%description gtk
Google Gadgets for Linux provides a platform for running desktop
gadgets under Linux, catering to the unique needs of Linux users. It's
compatible with the gadgets written for Google Desktop for Windows as
well as the Universal Gadgets on iGoogle.

This package includes the GTK+ version.

%package qt
Summary:	QT Version of Google Gadgets
Group:		X11/Applications
Requires:	google-gadgets = %{version}-%{release}
Requires:	google-gadgets-gst = %{version}
Requires:	libggadget-qt = %{version}-%{release}
Obsoletes:	google-gadgets-for-linux-qt

%description qt
Google Gadgets for Linux provides a platform for running desktop
gadgets under Linux, catering to the unique needs of Linux users. It's
compatible with the gadgets written for Google Desktop for Windows as
well as the Universal Gadgets on iGoogle.

This package includes the QT version.

%package gst
Summary:	GStreamer modules for Google Gadgets
Group:		X11/Applications
Requires:	gstreamer-plugins-base >= 0.10.6
Requires:	libggadget = %{version}-%{release}

%description gst
Google Gadgets for Linux provides a platform for running desktop
gadgets under Linux, catering to the unique needs of Linux users. It's
compatible with the gadgets written for Google Desktop for Windows as
well as the Universal Gadgets on iGoogle.

This package includes the GStreamer modules.

%package xul
Summary:	XULRunner modules for Google Gadgets
Group:		X11/Applications
Requires:	libggadget = %{version}-%{release}
Requires:	xulrunner

%description xul
Google Gadgets for Linux provides a platform for running desktop
gadgets under Linux, catering to the unique needs of Linux users. It's
compatible with the gadgets written for Google Desktop for Windows as
well as the Universal Gadgets on iGoogle.

This package includes the XULRunner modules.

%prep
%setup -q -n %{name}-for-linux
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
install -d libltdl
%{__libtoolize}
%{__aclocal} -I autotools
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-ltdl-install \
	--disable-static \
	--disable-werror \
	--with-oem-brand=pld-linux \
	--with-browser-plugins-dir=%{_libdir}/browser-plugins

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_desktopdir},%{_pixmapsdir}}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# desync with cmake/ac makefiles
mv $RPM_BUILD_ROOT%{_datadir}/mime/packages/{00-,}google-gadgets.xml
# desktop files
install %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}/ggl-gtk.desktop
install %{SOURCE2} $RPM_BUILD_ROOT%{_desktopdir}/ggl-qt.desktop

rm -f $RPM_BUILD_ROOT%{_libdir}/google-gadgets/modules/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%post -n libggadget -p /sbin/ldconfig
%postun -n libggadget -p /sbin/ldconfig

%post -n libggadget-gtk -p /sbin/ldconfig
%postun -n libggadget-gtk -p /sbin/ldconfig

%post -n libggadget-qt -p /sbin/ldconfig
%postun -n libggadget-qt -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS README NEWS
%dir %{_libdir}/google-gadgets
%dir %{_libdir}/google-gadgets/modules
%attr(755,root,root) %{_libdir}/google-gadgets/modules/analytics-usage-collector.so
%attr(755,root,root) %{_libdir}/google-gadgets/modules/curl-xml-http-request.so
%attr(755,root,root) %{_libdir}/google-gadgets/modules/dbus-script-class.so
%attr(755,root,root) %{_libdir}/google-gadgets/modules/default-framework.so
%attr(755,root,root) %{_libdir}/google-gadgets/modules/default-options.so
%attr(755,root,root) %{_libdir}/google-gadgets/modules/google-gadget-manager.so
%attr(755,root,root) %{_libdir}/google-gadgets/modules/libxml2-xml-parser.so
%attr(755,root,root) %{_libdir}/google-gadgets/modules/linux-system-framework.so
%dir %{_datadir}/google-gadgets
%{_datadir}/google-gadgets/*.gg
%{_datadir}/mime/packages/google-gadgets.xml
%{_iconsdir}/*/*/*/*.png
%{_pixmapsdir}/google-gadgets.png

%files -n libggadget
%defattr(644,root,root,755)
%attr(755,root,root) %ghost %{_libdir}/libggadget-1.0.so.0
%attr(755,root,root) %{_libdir}/libggadget-1.0.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libggadget-dbus-1.0.so.0
%attr(755,root,root) %{_libdir}/libggadget-dbus-1.0.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libggadget-js-1.0.so.0
%attr(755,root,root) %{_libdir}/libggadget-js-1.0.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libggadget-npapi-1.0.so.0
%attr(755,root,root) %{_libdir}/libggadget-npapi-1.0.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libggadget-xdg-1.0.so.0
%attr(755,root,root) %{_libdir}/libggadget-xdg-1.0.so.*.*.*

%files -n libggadget-devel
%defattr(644,root,root,755)
%dir %{_includedir}/google-gadgets
%dir %{_includedir}/google-gadgets/ggadget
%dir %{_includedir}/google-gadgets/ggadget/dbus
%dir %{_includedir}/google-gadgets/ggadget/js
%dir %{_includedir}/google-gadgets/ggadget/xdg
%dir %{_includedir}/google-gadgets/ggadget/npapi
%{_includedir}/google-gadgets/ggadget/*.h
%{_includedir}/google-gadgets/ggadget/dbus/*.h
%{_includedir}/google-gadgets/ggadget/js/*.h
%{_includedir}/google-gadgets/ggadget/xdg/*.h
%{_includedir}/google-gadgets/ggadget/npapi/*.h
%dir %{_libdir}/google-gadgets/include
%dir %{_libdir}/google-gadgets/include/ggadget
%{_libdir}/google-gadgets/include/ggadget/sysdeps.h
%{_libdir}/libggadget-1.0*.so
%{_libdir}/libggadget-dbus-1.0*.so
%{_libdir}/libggadget-js-1.0*.so
%{_libdir}/libggadget-xdg-1.0*.so
%{_libdir}/libggadget-npapi-1.0*.so
%if 0
%{_libdir}/libggadget-1.0*.la
%{_libdir}/libggadget-dbus-1.0*.la
%{_libdir}/libggadget-js-1.0*.la
%{_libdir}/libggadget-xdg-1.0*.la
%{_libdir}/libggadget-npapi-1.0*.la
%endif
%{_pkgconfigdir}/libggadget-1.0.pc
%{_pkgconfigdir}/libggadget-dbus-1.0.pc
%{_pkgconfigdir}/libggadget-js-1.0.pc
%{_pkgconfigdir}/libggadget-xdg-1.0.pc
%{_pkgconfigdir}/libggadget-npapi-1.0.pc

%files -n libggadget-gtk
%defattr(644,root,root,755)
%attr(755,root,root) %ghost %{_libdir}/libggadget-gtk-1.0.so.0
%attr(755,root,root) %{_libdir}/libggadget-gtk-1.0.so.*.*.*

%files -n libggadget-gtk-devel
%defattr(644,root,root,755)
%dir %{_includedir}/google-gadgets/ggadget/gtk
%{_includedir}/google-gadgets/ggadget/gtk/*.h
%{_libdir}/libggadget-gtk-1.0*.so
#%{_libdir}/libggadget-gtk-1.0*.la
%{_pkgconfigdir}/libggadget-gtk-1.0.pc

%files -n libggadget-qt
%defattr(644,root,root,755)
%attr(755,root,root) %ghost %{_libdir}/libggadget-qt-1.0.so.0
%attr(755,root,root) %{_libdir}/libggadget-qt-1.0.so.*.*.*

%files -n libggadget-qt-devel
%defattr(644,root,root,755)
%dir %{_includedir}/google-gadgets/ggadget/qt
%{_includedir}/google-gadgets/ggadget/qt/*.h
%{_libdir}/libggadget-qt-1.0*.so
#%{_libdir}/libggadget-qt-1.0*.la
%{_pkgconfigdir}/libggadget-qt-1.0.pc

%files gtk
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/ggl-gtk
%attr(755,root,root) %{_libdir}/google-gadgets/modules/gtk-edit-element.so
%attr(755,root,root) %{_libdir}/google-gadgets/modules/gtk-flash-element.so
%attr(755,root,root) %{_libdir}/google-gadgets/modules/gtk-system-framework.so
%{_desktopdir}/ggl-gtk.desktop
%{_desktopdir}/ggl-designer.desktop

%files qt
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/ggl-qt
%attr(755,root,root) %{_libdir}/google-gadgets/modules/qt-edit-element.so
%attr(755,root,root) %{_libdir}/google-gadgets/modules/qt-script-runtime.so
%attr(755,root,root) %{_libdir}/google-gadgets/modules/qt-system-framework.so
%attr(755,root,root) %{_libdir}/google-gadgets/modules/qt-xml-http-request.so
%attr(755,root,root) %{_libdir}/google-gadgets/modules/qtwebkit-browser-element.so
%{_desktopdir}/ggl-qt.desktop

%files gst
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/google-gadgets/modules/gst-audio-framework.so
%attr(755,root,root) %{_libdir}/google-gadgets/modules/gst-video-element.so

%files xul
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/google-gadgets/modules/smjs-script-runtime.so
%attr(755,root,root) %{_libdir}/google-gadgets/modules/gtkmoz-browser-element.so
%attr(755,root,root) %{_libdir}/google-gadgets/gtkmoz-browser-child
