Summary:	Very easy to use GNOME Telepathy client
Summary(pl.UTF-8):	Bardzo łatwy w użyciu klient Telepathy dla GNOME
Name:		empathy
Version:	2.31.91.1
Release:	1
License:	GPL v2
Group:		Applications/Communications
Source0:	http://ftp.gnome.org/pub/GNOME/sources/empathy/2.31/%{name}-%{version}.tar.bz2
# Source0-md5:	17298d833ffa82662c4f5e7f8c743933
Patch0:		configure.patch
URL:		http://live.gnome.org/Empathy
BuildRequires:	GConf2-devel >= 2.26.0
BuildRequires:	NetworkManager-devel >= 0.7
BuildRequires:	autoconf >= 2.59
BuildRequires:	automake >= 1:1.9
#BuildRequires:	check >= 0.9.4
#BuildRequires:	clutter-gtk-devel >= 0.10.0
BuildRequires:	dbus-glib-devel >= 0.74
#BuildRequires:	docbook-dtd412-xml
BuildRequires:	enchant-devel >= 1.2.0
BuildRequires:	evolution-data-server-devel >= 2.24.0
BuildRequires:	farsight2-devel
BuildRequires:	folks-devel
BuildRequires:	geoclue-devel >= 0.11
BuildRequires:	gettext-devel
BuildRequires:	gnome-common >= 2.24.0
BuildRequires:	gnome-doc-utils >= 0.18.0
#BuildRequires:	gnome-panel-devel >= 2.24.0
BuildRequires:	gstreamer-devel
BuildRequires:	gstreamer-plugins-base-devel
BuildRequires:	gtk+2-devel >= 2:2.18.0
#BuildRequires:	gtk-doc >= 1.3
BuildRequires:	gtk-webkit-devel >= 1.1.7
BuildRequires:	intltool >= 0.40.0
BuildRequires:	iso-codes >= 0.35
BuildRequires:	libcanberra-gtk-devel >= 0.4
BuildRequires:	libchamplain-devel >= 0.4
BuildRequires:	libgnome-keyring-devel
BuildRequires:	libnotify-devel >= 0.4.4
BuildRequires:	libtool
BuildRequires:	libunique-devel
BuildRequires:	libxml2-devel >= 1:2.6.28
BuildRequires:	nautilus-sendto-devel >= 2.31.7
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(find_lang) >= 1.23
BuildRequires:	rpmbuild(macros) >= 1.311
BuildRequires:	sed >= 4.0
BuildRequires:	telepathy-farsight-devel
BuildRequires:	telepathy-glib-devel >= 0.9.2
BuildRequires:	telepathy-logger-devel >= 0.1.5
Requires(post,postun):	glib2 >= 1:2.25.11
Requires(post,postun):	gtk+2 >= 2:2.12.0
Requires(post,postun):	hicolor-icon-theme
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
Summary(pl.UTF-8):	Wsparcie Empathy przy wysyłaniu plików z Nautilusa
Group:		X11/Applications
Requires:	%{name} = %{version}-%{release}
Requires:	nautilus-sendto >= 2.28.1

%description -n nautilus-sendto-empathy
Enables sending files from Nautilus to your Empathy contacts.

%description -n nautilus-sendto-empathy -l pl.UTF-8
Pozwala na przesyłanie z Nautilusa plików do kontaktów Empathy.

%prep
%setup -q
%patch0 -p1

rm po/en@shaw.po
sed -i 's/^en@shaw//' po/LINGUAS

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

rm -f $RPM_BUILD_ROOT%{_libdir}/nautilus-sendto/plugins/*.la
rm -f $RPM_BUILD_ROOT%{py_sitedir}/*.{la,a}

%find_lang %{name} --with-gnome --with-omf

%clean
rm -rf $RPM_BUILD_ROOT

%post
glib-compile-schemas %{_datadir}/glib-2.0/schemas
%update_icon_cache hicolor

%postun
glib-compile-schemas %{_datadir}/glib-2.0/schemas
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
