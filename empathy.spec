Summary:	Very easy to use GNOME Telepathy client
Summary(pl.UTF-8):	Bardzo łatwy w użyciu klient Telepathy dla GNOME
Name:		empathy
Version:	0.10
Release:	1
License:	GPL
Group:		Applications/Communications
Source0:	http://ftp.gnome.org/pub/GNOME/sources/empathy/0.10/%{name}-%{version}.tar.bz2
# Source0-md5:	8b3e3efc2963fffe9b1051f7484372ac
URL:		http://empathy.imendio.org/
BuildRequires:	GConf2-devel
BuildRequires:	autoconf >= 2.59
BuildRequires:	automake >= 1:1.9
BuildRequires:	dbus-glib-devel
BuildRequires:	gnome-vfs2-devel >= 2.18.1
BuildRequires:	gtk+2-devel >= 2:2.10.12
BuildRequires:	intltool >= 0.35.5
BuildRequires:	libglade2-devel >= 1:2.6.0
BuildRequires:	libgnomeui-devel >= 2.18.1
BuildRequires:	libtelepathy-devel >= 0.0.51
BuildRequires:	libtool
BuildRequires:	libxml2-devel >= 1:2.6.28
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.311
BuildRequires:	telepathy-mission-control-devel >= 4.27
Requires:	%{name}-libs = %{version}-%{release}
Requires(post,postun):	gtk+2 >= 2:2.10.12
Requires(post,postun):	hicolor-icon-theme
Requires(post,preun):	GConf2
Suggests:	telepathy-butterfly
Suggests:	telepathy-gabble
Suggests:	telepathy-idle
Suggests:	telepathy-salut
Obsoletes:	gnome-jabber
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Empathy aims at making Instant Messaging with Jabber as easy as
possible.

%description -l pl.UTF-8
Celem Empathy jest uczynienie komunikowania poprzez Jabbera tak łatwym
jak to tylko możliwe.

%package devel
Summary:	empathy header files
Summary(pl.UTF-8):	Pliki nagłówkowe empathy
Group:		X11/Development/Libraries
Requires:	%{name}-libs = %{version}-%{release}

%description devel
empathy header files.

%description devel -l pl.UTF-8
Pliki nagłówkowe empathy.

%package libs
Summary:	Libraries for empathy
Summary(pl.UTF-8):	Biblioteki dla empathy
Group:		Libraries

%description libs
Libraries for empathy.

%description libs -l pl.UTF-8
Biblioteki dla empathy.

%package static
Summary:	empathy static libraries
Summary(pl.UTF-8):	Statyczne biblioteki empathy
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
empathy static libraries.

%description static -l pl.UTF-8
Statyczne biblioteki empathy.

%prep
%setup -q

%build
%{__glib_gettextize}
%{__libtoolize}
%{__intltoolize}
%{__aclocal}
%{__autoheader}
%{__automake}
%{__autoconf}
%configure \
	--disable-schemas-install \
	--with-html-dir=%{_gtkdocdir}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	GCONF_DISABLE_MAKEFILE_SCHEMA_INSTALL=1

%find_lang %{name} --with-gnome --all-name

%clean
rm -rf $RPM_BUILD_ROOT

%post
%gconf_schema_install empathy.schemas
%update_icon_cache hicolor
%update_desktop_database_post

%preun
%gconf_schema_uninstall empathy.schemas

%postun
%update_icon_cache hicolor
%update_desktop_database_postun

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS CONTRIBUTORS ChangeLog NEWS README
%attr(755,root,root) %{_bindir}/*
%{_datadir}/%{name}
%{_iconsdir}/hicolor/*/apps/*
%{_sysconfdir}/gconf/schemas/empathy.schemas
%{_datadir}/dbus-1/services/*.service
%{_datadir}/gnome/autostart/empathy.desktop
%{_datadir}/mission-control/profiles/*.profile
%{_datadir}/telepathy/managers/empathy-chat.chandler

%files devel
%defattr(644,root,root,755)
%{_includedir}/libempathy
%{_includedir}/libempathy-gtk
%attr(755,root,root) %{_libdir}/libempathy.so
%attr(755,root,root) %{_libdir}/libempathy-gtk.so
%{_libdir}/libempathy.la
%{_libdir}/libempathy-gtk.la
%{_gtkdocdir}/libempathy
%{_gtkdocdir}/libempathy-gtk
%{_pkgconfigdir}/libempathy.pc
%{_pkgconfigdir}/libempathy-gtk.pc

%files libs
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libempathy.so.*.*
%attr(755,root,root) %{_libdir}/libempathy-gtk.so.*.*

%files static
%defattr(644,root,root,755)
%{_libdir}/libempathy.a
%{_libdir}/libempathy-gtk.a
