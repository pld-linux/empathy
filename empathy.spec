Summary:	Very easy to use GNOME Telepathy client
Summary(pl.UTF-8):	Bardzo łatwy w użyciu klient Telepathy dla GNOME
Name:		empathy
Version:	2.23.92
Release:	1
License:	GPL
Group:		Applications/Communications
Source0:	http://ftp.gnome.org/pub/GNOME/sources/empathy/2.23/%{name}-%{version}.tar.bz2
# Source0-md5:	6bc1f3b9562e7645391a0950d1c2462a
Patch0:		%{name}-python2.5.patch
URL:		http://empathy.imendio.org/
BuildRequires:	GConf2-devel
BuildRequires:	aspell-devel
BuildRequires:	autoconf >= 2.59
BuildRequires:	automake >= 1:1.9
BuildRequires:	dbus-glib-devel
BuildRequires:	esound-devel
BuildRequires:	evolution-data-server-devel >= 2.23.6
BuildRequires:	gnome-panel-devel
BuildRequires:	gnome-vfs2-devel
BuildRequires:	gtk+2-devel >= 2:2.12.0
BuildRequires:	intltool >= 0.36.2
BuildRequires:	iso-codes
BuildRequires:	libglade2-devel >= 1:2.6.2
BuildRequires:	libtelepathy-devel >= 0.3.1
BuildRequires:	libtool
BuildRequires:	libxml2-devel >= 1:2.6.28
BuildRequires:	pkgconfig
BuildRequires:	python-pygtk-devel
BuildRequires:	rpmbuild(macros) >= 1.311
BuildRequires:	telepathy-glib-devel >= 0.7.7
BuildRequires:	telepathy-mission-control-devel >= 4.53
Requires(post,postun):	gtk+2 >= 2:2.12.0
Requires(post,postun):	hicolor-icon-theme
Requires(post,preun):	GConf2
Requires:	%{name}-libs = %{version}-%{release}
Suggests:	telepathy-butterfly
Suggests:	telepathy-gabble
Suggests:	telepathy-idle
Suggests:	telepathy-salut
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
Summary:	Libraries for empathy
Summary(pl.UTF-8):	Biblioteki dla empathy
Group:		Libraries

%description libs
Libraries for empathy.

%description libs -l pl.UTF-8
Biblioteki dla empathy.

%package devel
Summary:	empathy header files
Summary(pl.UTF-8):	Pliki nagłówkowe empathy
Group:		X11/Development/Libraries
Requires:	%{name}-libs = %{version}-%{release}

%description devel
empathy header files.

%description devel -l pl.UTF-8
Pliki nagłówkowe empathy.

%package static
Summary:	empathy static libraries
Summary(pl.UTF-8):	Statyczne biblioteki empathy
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
empathy static libraries.

%description static -l pl.UTF-8
Statyczne biblioteki empathy.

%package apidocs
Summary:	empathy API documentation
Summary(pl.UTF-8):	Dokumentacja API empathy
Group:		Documentation
Requires:	gtk-doc-common

%description apidocs
empathy API documentation.

%description apidocs -l pl.UTF-8
Dokumentacja API empathy.

%package -n python-%{name}
Summary:	Python module for Empathy
Summary(pl.UTF-8):	Moduł Pythona dla Empathy
Group:		Development/Libraries
Requires:	%{name}-libs = %{version}-%{release}

%description -n python-%{name}
Python module for Empathy.

%description -n python-%{name} -l pl.UTF-8
Moduł Pythona dla Empathy.

%prep
%setup -q
#%patch0 -p1

%build
#%{__glib_gettextize}
#%{__libtoolize}
#%{__intltoolize}
#%{__aclocal}
#%{__autoheader}
#%{__automake}
#%{__autoconf}
%configure \
	--with-compile-warnings=no \
	--disable-schemas-install \
	--with-html-dir=%{_gtkdocdir}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	GCONF_DISABLE_MAKEFILE_SCHEMA_INSTALL=1

rm -f $RPM_BUILD_ROOT%{py_sitedir}/*.{la,a}

%find_lang %{name} --with-gnome --all-name

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
%attr(755,root,root) %{_bindir}/*
%{_datadir}/%{name}
%{_iconsdir}/hicolor/*/apps/*
%{_sysconfdir}/gconf/schemas/empathy.schemas
%{_sysconfdir}/gconf/schemas/GNOME_Megaphone_Applet.schemas
#%{_sysconfdir}/xdg/autostart/empathy.desktop
#%attr(755,root,root) %{_libdir}/empathy-call-chandler
%attr(755,root,root) %{_libdir}/nothere-applet
%attr(755,root,root) %{_libdir}/megaphone-applet
%{_libdir}/bonobo/servers/*.server
#%{_datadir}/dbus-1/services/*.service
%{_datadir}/mission-control/profiles/*.profile
#%{_datadir}/telepathy/managers/empathy-chat.chandler
#%{_datadir}/telepathy/managers/empathy-call.chandler
%{_mandir}/man1/empathy*.1*
%{_desktopdir}/*.desktop
%{_omf_dest_dir}/%{name}

%files libs
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libempathy.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libempathy.so.14
%attr(755,root,root) %{_libdir}/libempathy-gtk.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libempathy-gtk.so.15

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
