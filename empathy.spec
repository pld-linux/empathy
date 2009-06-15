Summary:	Very easy to use GNOME Telepathy client
Summary(pl.UTF-8):	Bardzo łatwy w użyciu klient Telepathy dla GNOME
Name:		empathy
Version:	2.27.3
Release:	1
License:	GPL v2
Group:		Applications/Communications
Source0:	http://ftp.gnome.org/pub/GNOME/sources/empathy/2.27/%{name}-%{version}.tar.bz2
# Source0-md5:	082624ff1ea1086b8f64658a0949fcc5
URL:		http://live.gnome.org/Empathy
BuildRequires:	GConf2-devel >= 2.26.0
BuildRequires:	autoconf >= 2.59
BuildRequires:	automake >= 1:1.9
BuildRequires:	check >= 0.9.4
BuildRequires:	dbus-glib-devel >= 0.74
BuildRequires:	enchant-devel >= 1.2.0
BuildRequires:	evolution-data-server-devel >= 2.24.0
BuildRequires:	gettext-devel
BuildRequires:	gnome-common >= 2.24.0
BuildRequires:	gnome-panel-devel >= 2.24.0
BuildRequires:	gstreamer-devel
BuildRequires:	gstreamer-plugins-base-devel
BuildRequires:	gtk+2-devel >= 2:2.16.0
BuildRequires:	gtk-doc >= 1.3
BuildRequires:	intltool >= 0.40.0
BuildRequires:	iso-codes >= 0.35
BuildRequires:	libcanberra-gtk-devel >= 0.4
BuildRequires:	libglade2-devel >= 1:2.6.2
BuildRequires:	libnotify-devel >= 0.4.4
BuildRequires:	libtool
BuildRequires:	libxml2-devel >= 1:2.6.28
BuildRequires:	pkgconfig
BuildRequires:	python-pygtk-devel
BuildRequires:	rpmbuild(find_lang) >= 1.23
BuildRequires:	rpmbuild(macros) >= 1.311
BuildRequires:	telepathy-farsight-devel
BuildRequires:	telepathy-glib-devel >= 0.7.23
BuildRequires:	telepathy-mission-control-devel >= 4.61
Requires(post,postun):	gtk+2 >= 2:2.12.0
Requires(post,postun):	hicolor-icon-theme
Requires(post,preun):	GConf2
Requires:	%{name}-libs = %{version}-%{release}
Suggests:	telepathy-butterfly
Suggests:	telepathy-gabble
Suggests:	telepathy-haze
Suggests:	telepathy-idle
Suggests:	telepathy-salut
Suggests:	telepathy-sofiasip
Obsoletes:	gnome-jabber
# sr@Latn vs. sr@latin
Conflicts:	glibc-misc < 6:2.7
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Empathy aims at making Instant Messaging with Jabber as easy as
possible.

%description -l pl.UTF-8
Celem Empathy jest uczynienie komunikowania poprzez Jabbera tak łatwym
jak to tylko możliwe.

%package libs
Summary:	Libraries for Empathy
Summary(pl.UTF-8):	Biblioteki dla Empathy
Group:		Libraries

%description libs
Libraries for Empathy.

%description libs -l pl.UTF-8
Biblioteki dla Empathy.

%package devel
Summary:	Empathy header files
Summary(pl.UTF-8):	Pliki nagłówkowe Empathy
Group:		X11/Development/Libraries
Requires:	%{name}-libs = %{version}-%{release}
Requires:	gtk+2-devel >= 2:2.16.0
Requires:	libglade2-devel >= 1:2.6.2
Requires:	libxml2-devel >= 1:2.6.28
Requires:	telepathy-glib-devel >= 0.7.23
Requires:	telepathy-mission-control-devel >= 4.61

%description devel
Empathy header files.

%description devel -l pl.UTF-8
Pliki nagłówkowe Empathy.

%package static
Summary:	Empathy static libraries
Summary(pl.UTF-8):	Statyczne biblioteki Empathy
Group:		X11/Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Empathy static libraries.

%description static -l pl.UTF-8
Statyczne biblioteki Empathy.

%package apidocs
Summary:	Empathy API documentation
Summary(pl.UTF-8):	Dokumentacja API Empathy
Group:		Documentation
Requires:	gtk-doc-common

%description apidocs
Empathy API documentation.

%description apidocs -l pl.UTF-8
Dokumentacja API Empathy.

%package -n python-%{name}
Summary:	Python module for Empathy
Summary(pl.UTF-8):	Moduł Pythona dla Empathy
Group:		Libraries/Python
Requires:	%{name}-libs = %{version}-%{release}

%description -n python-%{name}
Python module for Empathy.

%description -n python-%{name} -l pl.UTF-8
Moduł Pythona dla Empathy.

%prep
%setup -q

%build
%{__intltoolize}
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--with-compile-warnings=no \
	--disable-schemas-install \
	--enable-gtk-doc \
	--enable-shave \
	--with-html-dir=%{_gtkdocdir}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	GCONF_DISABLE_MAKEFILE_SCHEMA_INSTALL=1

rm -f $RPM_BUILD_ROOT%{py_sitedir}/*.{la,a}

%find_lang %{name} --with-gnome --with-omf

%clean
rm -rf $RPM_BUILD_ROOT

%post
%gconf_schema_install empathy.schemas
%gconf_schema_install GNOME_Megaphone_Applet.schemas
%update_icon_cache hicolor

%preun
%gconf_schema_uninstall empathy.schemas
%gconf_schema_uninstall GNOME_Megaphone_Applet.schemas

%postun
%update_icon_cache hicolor

%post	libs -p /sbin/ldconfig
%postun	libs -p /sbin/ldconfig

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS CONTRIBUTORS ChangeLog NEWS README
%attr(755,root,root) %{_bindir}/empathy
%attr(755,root,root) %{_bindir}/empathy-logs
%{_datadir}/%{name}
%{_iconsdir}/hicolor/*/apps/*
%{_sysconfdir}/gconf/schemas/empathy.schemas
%{_sysconfdir}/gconf/schemas/GNOME_Megaphone_Applet.schemas
%attr(755,root,root) %{_libdir}/nothere-applet
%attr(755,root,root) %{_libdir}/megaphone-applet
%{_libdir}/bonobo/servers/*.server
%{_datadir}/mission-control/profiles/*.profile
%{_mandir}/man1/empathy*.1*
%{_desktopdir}/*.desktop

%files libs
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libempathy.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libempathy.so.26
%attr(755,root,root) %{_libdir}/libempathy-gtk.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libempathy-gtk.so.24

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libempathy.so
%attr(755,root,root) %{_libdir}/libempathy-gtk.so
%{_libdir}/libempathy.la
%{_libdir}/libempathy-gtk.la
%{_includedir}/libempathy
%{_includedir}/libempathy-gtk
%{_pkgconfigdir}/libempathy.pc
%{_pkgconfigdir}/libempathy-gtk.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libempathy.a
%{_libdir}/libempathy-gtk.a

%files apidocs
%defattr(644,root,root,755)
%{_gtkdocdir}/libempathy
%{_gtkdocdir}/libempathy-gtk

%files -n python-%{name}
%defattr(644,root,root,755)
%attr(755,root,root) %{py_sitedir}/empathy.so
%attr(755,root,root) %{py_sitedir}/empathygtk.so
