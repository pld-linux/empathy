#
# Conditional build:
%bcond_with	uoa	# Ubuntu Online Accounts (single-signon)
#
Summary:	High-level library and user-interface for Telepathy
Summary(pl.UTF-8):	Bardzo łatwy w użyciu klient Telepathy dla GNOME
Name:		empathy
Version:	3.12.14
Release:	3
License:	GPL v2+
Group:		Applications/Communications
Source0:	https://download.gnome.org/sources/empathy/3.12/%{name}-%{version}.tar.xz
# Source0-md5:	44620fa64024d8cac6d493c94bc2ce6e
URL:		https://wiki.gnome.org/Apps/Empathy
BuildRequires:	autoconf >= 2.64
BuildRequires:	automake >= 1:1.11
BuildRequires:	cheese-devel >= 3.4.0
BuildRequires:	clutter-devel >= 1.10.0
BuildRequires:	clutter-gst-devel >= 3.0
BuildRequires:	clutter-gtk-devel >= 1.2.0
BuildRequires:	cogl-devel >= 1.14.0
BuildRequires:	dbus-glib-devel >= 0.74
BuildRequires:	enchant-devel >= 1.2.0
BuildRequires:	farstream-devel >= 0.2.0
BuildRequires:	folks-devel >= 0.9.5
BuildRequires:	gcr-devel >= 2.91.4
BuildRequires:	geoclue2-devel >= 2.1.0
BuildRequires:	geocode-glib-devel >= 0.99.1
BuildRequires:	gettext-tools
BuildRequires:	glib2-devel >= 1:2.48.0
BuildRequires:	gnome-online-accounts-devel >= 3.5.1
BuildRequires:	gsettings-desktop-schemas-devel
BuildRequires:	gstreamer-devel >= 1.0.0
BuildRequires:	gstreamer-plugins-base-devel >= 1.0.0
BuildRequires:	gtk+3-devel >= 3.10.0
BuildRequires:	gtk-webkit4-devel >= 2.10.0
BuildRequires:	intltool >= 0.50.0
BuildRequires:	iso-codes >= 0.35
%{?with_uoa:BuildRequires:	libaccount-plugin-devel}
%{?with_uoa:BuildRequires:	libaccounts-glib-devel >= 1.4}
BuildRequires:	libcanberra-gtk3-devel >= 0.25
BuildRequires:	libchamplain-devel >= 0.12.1
BuildRequires:	libgee-devel >= 0.8.0
BuildRequires:	libnotify-devel >= 0.7.0
BuildRequires:	libsecret-devel >= 0.5
%{?with_uoa:BuildRequires:	libsignon-glib-devel >= 1.8}
BuildRequires:	libsoup-devel >= 2.4
BuildRequires:	libtool >= 2:2.2
BuildRequires:	libxml2-devel >= 1:2.6.28
BuildRequires:	libxslt-progs
BuildRequires:	pkgconfig >= 1:0.25
BuildRequires:	pulseaudio-devel
BuildRequires:	python >= 1:2.3
BuildRequires:	python-modules >= 1:2.3
BuildRequires:	rpmbuild(find_lang) >= 1.23
BuildRequires:	rpmbuild(macros) >= 1.592
BuildRequires:	tar >= 1:1.22
BuildRequires:	telepathy-farstream-devel >= 0.6.0
BuildRequires:	telepathy-glib-devel >= 0.24.0
BuildRequires:	telepathy-logger-devel >= 0.8.0
BuildRequires:	telepathy-mission-control-devel >= 5.13.1
BuildRequires:	udev-glib-devel
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	xz
BuildRequires:	yelp-tools
Requires(post,postun):	glib2 >= 1:2.48.0
Requires(post,postun):	gtk-update-icon-cache
Requires:	cheese >= 3.4.0
Requires:	clutter >= 1.10.0
Requires:	clutter-gst >= 3.0
Requires:	clutter-gtk >= 1.2.0
Requires:	cogl >= 1.14.0
Requires:	enchant >= 1.2.0
Requires:	evolution-data-server
Requires:	folks >= 0.9.5
Requires:	gcr >= 2.91.4
Requires:	geoclue2 >= 2.1.0
Requires:	geocode-glib >= 0.99.1
Requires:	glib2 >= 1:2.48.0
Requires:	gnome-online-accounts >= 3.5.1
Requires:	gsettings-desktop-schemas
Requires:	gtk+3 >= 3.10.0
Requires:	gtk-webkit4 >= 2.10.0
Requires:	hicolor-icon-theme
%{?with_uoa:Requires:	libaccounts-glib >= 1.4}
Requires:	libcanberra-gtk3 >= 0.25
Requires:	libchamplain >= 0.12.1
Requires:	libnotify >= 0.7.0
Requires:	libsecret >= 0.5
%{?with_uoa:Requires:	libsignon-glib >= 1.8}
Requires:	telepathy-farstream >= 0.6.0
Requires:	telepathy-glib >= 0.24.0
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
	--enable-gst-1.0 \
	--enable-gudev \
	--enable-location \
	--enable-map \
	--disable-nautilus-sendto \
	--enable-spell \
	--enable-ubuntu-online-accounts%{!?with_uoa:=no}

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
%doc AUTHORS CONTRIBUTORS ChangeLog NEWS README TODO
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
%{_iconsdir}/hicolor/*x*/apps/empathy.png
%{_iconsdir}/hicolor/scalable/apps/empathy-symbolic.svg
%{_mandir}/man1/empathy*.1*
%{_desktopdir}/empathy.desktop
