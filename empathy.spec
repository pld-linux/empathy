Summary:	Very easy to use GNOME Telepathy client
Summary(pl.UTF-8):	Bardzo łatwy w użyciu klient Telepathy dla GNOME
Name:		empathy
Version:	2.32.1
Release:	3
License:	GPL v2
Group:		Applications/Communications
Source0:	http://ftp.gnome.org/pub/GNOME/sources/empathy/2.32/%{name}-%{version}.tar.bz2
# Source0-md5:	09e7d72cd58a5f776b5097e7d5596095
Patch0:		configure.patch
URL:		http://live.gnome.org/Empathy
BuildRequires:	GConf2-devel >= 2.26.0
BuildRequires:	NetworkManager-devel >= 0.7.0
BuildRequires:	autoconf >= 2.59
BuildRequires:	automake >= 1:1.9
BuildRequires:	clutter-gtk-devel >= 0.10.0
BuildRequires:	dbus-glib-devel >= 0.74
BuildRequires:	docbook-dtd412-xml
BuildRequires:	enchant-devel >= 1.2.0
BuildRequires:	evolution-data-server-devel >= 2.24.0
BuildRequires:	farsight2-devel
BuildRequires:	folks-devel >= 0.1.5
BuildRequires:	geoclue-devel >= 0.11
BuildRequires:	gettext-devel
BuildRequires:	glib2-devel >= 1:2.26.0
BuildRequires:	gnome-common >= 2.24.0
BuildRequires:	gnome-doc-utils >= 0.18.0
BuildRequires:	gnome-keyring-devel >= 2.26.0
BuildRequires:	gnutls-devel >= 2.8.5
BuildRequires:	gstreamer-devel
BuildRequires:	gstreamer-plugins-base-devel
BuildRequires:	gtk+2-devel >= 2:2.22.0
BuildRequires:	gtk-webkit-devel >= 1.1.15
BuildRequires:	intltool >= 0.40.0
BuildRequires:	iso-codes >= 0.35
BuildRequires:	libcanberra-gtk-devel >= 0.4
BuildRequires:	libchamplain-devel >= 0.8.0
BuildRequires:	libgnome-keyring-devel >= 2.26.0
BuildRequires:	libnotify-devel >= 0.4.4
BuildRequires:	libtool
BuildRequires:	libunique-devel >= 1.1.2
BuildRequires:	libxml2-devel >= 1:2.6.28
BuildRequires:	nautilus-sendto-devel >= 2.32.0
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(find_lang) >= 1.23
BuildRequires:	rpmbuild(macros) >= 1.592
BuildRequires:	telepathy-farsight-devel >= 0.0.14
BuildRequires:	telepathy-glib-devel >= 0.12.0
BuildRequires:	telepathy-logger-devel >= 0.1.5
Requires(post,postun):	glib2 >= 1:2.26.0
Requires(post,postun):	gtk-update-icon-cache
Requires(post,postun):	hicolor-icon-theme
Requires:	telepathy-logger >= 0.1.5
Requires:	telepathy-mission-control
Suggests:	telepathy-butterfly
Suggests:	telepathy-gabble
Suggests:	telepathy-haze
Suggests:	telepathy-idle
Suggests:	telepathy-salut
Suggests:	telepathy-sofiasip
Obsoletes:	empathy-apidocs < 2.29.1
Obsoletes:	empathy-devel < 2.29.1
Obsoletes:	empathy-libs < 2.29.1
Obsoletes:	gnome-jabber
Obsoletes:	python-empathy < 2.29.1
# sr@Latn vs. sr@latin
Conflicts:	glibc-misc < 6:2.7
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Empathy aims at making Instant Messaging with Jabber as easy as
possible.

%description -l pl.UTF-8
Celem Empathy jest uczynienie komunikowania poprzez Jabbera tak łatwym
jak to tylko możliwe.

%package -n nautilus-sendto-empathy
Summary:	Empathy support for sending files in Nautilus
Summary(pl.UTF-8):	Obsługa Empathy przy wysyłaniu plików z Nautilusa
Group:		X11/Applications
Requires:	%{name} = %{version}-%{release}
Requires:	nautilus-sendto >= 2.32.0

%description -n nautilus-sendto-empathy
This plugin enables sending files from Nautilus to your Empathy
contacts.

%description -n nautilus-sendto-empathy -l pl.UTF-8
Ta wtyczka pozwala na przesyłanie z poziomu Nautilusa plików do
kontaktów Empathy.

%prep
%setup -q
%patch0 -p1

%build
%{__intltoolize}
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--with-connectivity=nm \
	--disable-schemas-install \
	--disable-silent-rules \
	--disable-static \
	--enable-favourite-contacts \
	--enable-location \
	--enable-nautilus-sendto

%{__make} -j 1

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	GCONF_DISABLE_MAKEFILE_SCHEMA_INSTALL=1

%{__rm} $RPM_BUILD_ROOT%{_libdir}/nautilus-sendto/plugins/*.la
%{__rm} $RPM_BUILD_ROOT%{py_sitedir}/*.{la,a}

%find_lang %{name} --with-gnome --with-omf

%clean
rm -rf $RPM_BUILD_ROOT

%post
%glib_compile_schemas
%update_icon_cache hicolor

%postun
%glib_compile_schemas
%update_icon_cache hicolor

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS CONTRIBUTORS ChangeLog NEWS README
%attr(755,root,root) %{_bindir}/empathy
%attr(755,root,root) %{_bindir}/empathy-accounts
%attr(755,root,root) %{_bindir}/empathy-debugger
%attr(755,root,root) %{_libexecdir}/empathy-auth-client
%attr(755,root,root) %{_libexecdir}/empathy-av
%{_datadir}/%{name}
%{_datadir}/GConf/gsettings/empathy.convert
%{_datadir}/dbus-1/services/org.freedesktop.Telepathy.Client.Empathy.service
%{_datadir}/dbus-1/services/org.freedesktop.Telepathy.Client.Empathy.AudioVideo.service
%{_datadir}/dbus-1/services/org.freedesktop.Telepathy.Client.Empathy.Auth.service
%{_datadir}/glib-2.0/schemas/org.gnome.Empathy.gschema.xml
%{_datadir}/telepathy/clients/Empathy.client
%{_datadir}/telepathy/clients/Empathy.AudioVideo.client
%{_datadir}/telepathy/clients/Empathy.Auth.client
%{_iconsdir}/hicolor/*/apps/*
%{_mandir}/man1/empathy*.1*
%{_desktopdir}/*.desktop

%files -n nautilus-sendto-empathy
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/nautilus-sendto/plugins/libnstempathy.so
