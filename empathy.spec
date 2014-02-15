Summary:	High-level library and user-interface for Telepathy
Summary(pl.UTF-8):	Bardzo łatwy w użyciu klient Telepathy dla GNOME
Name:		empathy
Version:	3.10.3
Release:	1
License:	GPL v2+
Group:		Applications/Communications
Source0:	http://ftp.gnome.org/pub/GNOME/sources/empathy/3.10/%{name}-%{version}.tar.xz
# Source0-md5:	de7dc21d91d50a1a9861dd3f240274d7
URL:		http://live.gnome.org/Empathy
BuildRequires:	autoconf >= 2.64
BuildRequires:	automake >= 1:1.11
BuildRequires:	cheese-devel >= 3.4.0
BuildRequires:	clutter-devel >= 1.10.0
BuildRequires:	clutter-gst-devel >= 1.9.92
BuildRequires:	clutter-gtk-devel >= 1.2.0
BuildRequires:	cogl-devel
BuildRequires:	dbus-glib-devel >= 0.74
BuildRequires:	enchant-devel >= 1.2.0
BuildRequires:	farstream-devel >= 0.2.0
BuildRequires:	folks-devel >= 0.9.5
BuildRequires:	gcr-devel >= 2.91.4
BuildRequires:	geoclue2-devel >= 1.99.3
BuildRequires:	geocode-glib-devel >= 0.99.1
BuildRequires:	gettext-devel
BuildRequires:	glib2-devel >= 1:2.38.0
BuildRequires:	gnome-online-accounts-devel >= 3.5.1
BuildRequires:	gnutls-devel >= 2.8.5
BuildRequires:	gsettings-desktop-schemas-devel
BuildRequires:	gstreamer-devel >= 1.0.0
BuildRequires:	gstreamer-plugins-base-devel >= 1.0.0
BuildRequires:	gtk+3-devel >= 3.10.0
BuildRequires:	gtk-webkit3-devel >= 1.10.0
BuildRequires:	intltool >= 0.50.0
BuildRequires:	iso-codes >= 0.35
BuildRequires:	libcanberra-gtk3-devel >= 0.25
BuildRequires:	libchamplain-devel >= 0.12.1
BuildRequires:	libgee-devel >= 0.8.0
BuildRequires:	libnotify-devel >= 0.7.0
BuildRequires:	libsecret-devel >= 0.5
BuildRequires:	libsoup-devel
BuildRequires:	libtool >= 2:2.2
BuildRequires:	libxml2-devel >= 1:2.6.28
BuildRequires:	libxslt-progs
BuildRequires:	pkgconfig
BuildRequires:	pulseaudio-devel
BuildRequires:	python >= 2.3
BuildRequires:	python-modules >= 2.3
BuildRequires:	rpmbuild(find_lang) >= 1.23
BuildRequires:	rpmbuild(macros) >= 1.592
BuildRequires:	tar >= 1:1.22
BuildRequires:	telepathy-farstream-devel >= 0.6.0
BuildRequires:	telepathy-glib-devel >= 0.19.9
BuildRequires:	telepathy-logger-devel >= 0.8.0
BuildRequires:	telepathy-mission-control-devel >= 5.13.1
BuildRequires:	udev-glib-devel
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	xz
BuildRequires:	yelp-tools
Requires(post,postun):	glib2 >= 1:2.26.0
Requires(post,postun):	gtk-update-icon-cache
Requires:	evolution-data-server
Requires:	folks >= 0.9.5
Requires:	gsettings-desktop-schemas
Requires:	hicolor-icon-theme
Requires:	telepathy-glib >= 0.19.9
Requires:	telepathy-logger >= 0.8.0
Requires:	telepathy-mission-control >= 5.13.1
Suggests:	gnome-contacts
Suggests:	telepathy-gabble
Suggests:	telepathy-haze
Suggests:	telepathy-idle
Suggests:	telepathy-salut
Suggests:	telepathy-sofiasip
Obsoletes:	empathy-apidocs < 2.29.1
Obsoletes:	empathy-devel < 2.29.1
Obsoletes:	empathy-libs < 2.29.1
Obsoletes:	gnome-jabber
Obsoletes:	nautilus-sendto-empathy
Obsoletes:	python-empathy < 2.29.1
# sr@Latn vs. sr@latin
Conflicts:	glibc-misc < 6:2.7
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Instant messaging program supporting text, voice, video, file
transfers and inter-application communication over many different
protocols, including: AIM, MSN, Google Talk (Jabber/XMPP), Facebook,
Yahoo!, Salut, Gadu-Gadu, Groupwise, ICQ and QQ. (Supported protocols
depend on installed components.)

%description -l pl.UTF-8
Celem Empathy jest uczynienie komunikowania poprzez Jabbera tak łatwym
jak to tylko możliwe.

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
	--with-cheese \
	--disable-silent-rules \
	--disable-static \
	--enable-goa \
	--enable-gudev \
	--enable-location \
	--enable-map \
	--disable-nautilus-sendto \
	--enable-spell \
	--enable-gst-1.0 \
	--disable-ubuntu-online-accounts

%{__make} -j1

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/mission-control-plugins.0/*.la
%{__rm} $RPM_BUILD_ROOT%{_libdir}/empathy/*.la

%find_lang %{name} --with-gnome --all-name

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
%attr(755,root,root) %{_libexecdir}/empathy-call
%attr(755,root,root) %{_libexecdir}/empathy-chat
%attr(755,root,root) %{_libdir}/mission-control-plugins.0/mcp-account-manager-goa.so
%dir %{_libdir}/empathy
%attr(755,root,root) %{_libdir}/empathy/*.so
%{_datadir}/%{name}
%{_datadir}/adium
%{_datadir}/appdata/empathy.appdata.xml
%{_datadir}/GConf/gsettings/empathy.convert
%{_datadir}/dbus-1/services/org.freedesktop.Telepathy.Client.Empathy.Auth.service
%{_datadir}/dbus-1/services/org.freedesktop.Telepathy.Client.Empathy.Call.service
%{_datadir}/dbus-1/services/org.freedesktop.Telepathy.Client.Empathy.Chat.service
%{_datadir}/dbus-1/services/org.freedesktop.Telepathy.Client.Empathy.FileTransfer.service
%{_datadir}/glib-2.0/schemas/org.gnome.Empathy.gschema.xml
%{_datadir}/glib-2.0/schemas/org.gnome.telepathy-account-widgets.gschema.xml
%{_datadir}/telepathy/clients/Empathy.Auth.client
%{_datadir}/telepathy/clients/Empathy.Call.client
%{_datadir}/telepathy/clients/Empathy.Chat.client
%{_datadir}/telepathy/clients/Empathy.FileTransfer.client
%{_iconsdir}/hicolor/*/apps/*
%{_mandir}/man1/empathy*.1*
%{_desktopdir}/*.desktop
