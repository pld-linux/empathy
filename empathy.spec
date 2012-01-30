Summary:	High-level library and user-interface for Telepathy
Summary(pl.UTF-8):	Bardzo łatwy w użyciu klient Telepathy dla GNOME
Name:		empathy
Version:	3.2.2
Release:	1
License:	GPL v2+
Group:		Applications/Communications
Source0:	http://ftp.gnome.org/pub/GNOME/sources/empathy/3.2/%{name}-%{version}.tar.xz
# Source0-md5:	1e55c9052cbee9cb065e23cb358a6720
URL:		http://live.gnome.org/Empathy
BuildRequires:	NetworkManager-devel >= 0.7.0
BuildRequires:	autoconf >= 2.64
BuildRequires:	automake >= 1:1.11
BuildRequires:	cheese-devel >= 3.0.0
BuildRequires:	clutter-devel >= 1.7.14
BuildRequires:	clutter-gst-devel
BuildRequires:	clutter-gtk-devel >= 0.90.3
BuildRequires:	dbus-glib-devel >= 0.74
BuildRequires:	docbook-dtd412-xml
BuildRequires:	enchant-devel >= 1.2.0
BuildRequires:	evolution-data-server-devel >= 3.2.0
BuildRequires:	farsight2-devel
BuildRequires:	folks-devel >= 0.6.2
BuildRequires:	geoclue-devel >= 0.11
BuildRequires:	gettext-devel
BuildRequires:	glib2-devel >= 1:2.28.0
BuildRequires:	gnome-common >= 2.24.0
BuildRequires:	gnome-doc-utils >= 0.18.0
BuildRequires:	gnome-keyring-devel >= 3.2.0
BuildRequires:	gnome-online-accounts-devel >= 3.2.0
BuildRequires:	gnutls-devel >= 2.8.5
BuildRequires:	gsettings-desktop-schemas-devel
BuildRequires:	gstreamer-devel
BuildRequires:	gstreamer-plugins-base-devel
BuildRequires:	gtk+3-devel >= 3.0.2
BuildRequires:	gtk-webkit3-devel >= 1.3.2
BuildRequires:	intltool >= 0.40.0
BuildRequires:	iso-codes >= 0.35
BuildRequires:	libcanberra-gtk3-devel >= 0.25
BuildRequires:	libchamplain-devel >= 0.12.0
BuildRequires:	libgnome-keyring-devel >= 2.26.0
BuildRequires:	libnotify-devel >= 0.7.0
BuildRequires:	libtool
BuildRequires:	libxml2-devel >= 1:2.6.28
BuildRequires:	libxslt-progs
BuildRequires:	nautilus-sendto-devel >= 2.91.6
BuildRequires:	pkgconfig
BuildRequires:	python >= 2.3
BuildRequires:	python-modules >= 2.3
BuildRequires:	rpmbuild(find_lang) >= 1.23
BuildRequires:	rpmbuild(macros) >= 1.592
BuildRequires:	telepathy-farsight-devel >= 0.0.14
BuildRequires:	telepathy-farstream-devel
BuildRequires:	telepathy-glib-devel >= 0.16.0
BuildRequires:	telepathy-logger-devel >= 0.2.10-2
BuildRequires:	telepathy-mission-control-devel >= 5.9.1
Requires(post,postun):	glib2 >= 1:2.26.0
Requires(post,postun):	gtk-update-icon-cache
Requires(post,postun):	hicolor-icon-theme
Requires:	telepathy-logger >= 0.1.5
Requires:	telepathy-mission-control >= 5.9.1
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
Instant messaging program supporting text, voice, video, file
transfers and inter-application communication over many different
protocols, including: AIM, MSN, Google Talk (Jabber/XMPP), Facebook,
Yahoo!, Salut, Gadu-Gadu, Groupwise, ICQ and QQ. (Supported protocols
depend on installed components.)

%description -l pl.UTF-8
Celem Empathy jest uczynienie komunikowania poprzez Jabbera tak łatwym
jak to tylko możliwe.

%package -n nautilus-sendto-empathy
Summary:	Empathy support for sending files in Nautilus
Summary(pl.UTF-8):	Obsługa Empathy przy wysyłaniu plików z Nautilusa
Group:		X11/Applications
Requires:	%{name} = %{version}-%{release}
Requires:	nautilus-sendto >= 2.91.6

%description -n nautilus-sendto-empathy
This plugin enables sending files from Nautilus to your Empathy
contacts.

%description -n nautilus-sendto-empathy -l pl.UTF-8
Ta wtyczka pozwala na przesyłanie z poziomu Nautilusa plików do
kontaktów Empathy.

%prep
%setup -q

%build
%{__intltoolize}
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
# missing geocode-glib in pld
%configure \
	--with-connectivity=nm \
	--with-cheese \
	--with-eds \
	--disable-silent-rules \
	--disable-static \
	--disable-control-center-embedding \
	--disable-geocode \
	--enable-call \
	--enable-call-logs \
	--enable-goa \
	--enable-gudev \
	--enable-location \
	--enable-map \
	--enable-nautilus-sendto \
	--enable-spell

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/nautilus-sendto/plugins/*.la
%{__rm} $RPM_BUILD_ROOT%{_libdir}/mission-control-plugins.0/*.la
#%{__rm} $RPM_BUILD_ROOT%{_libdir}/control-center-1/panels/*.la

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
#%attr(755,root,root) %{_libdir}/control-center-1/panels/libempathy-accounts-panel.so
%attr(755,root,root) %{_libexecdir}/empathy-auth-client
%attr(755,root,root) %{_libexecdir}/empathy-av
%attr(755,root,root) %{_libexecdir}/empathy-call
%attr(755,root,root) %{_libexecdir}/empathy-chat
%attr(755,root,root) %{_libdir}/mission-control-plugins.0/mcp-account-manager-goa.so
%{_datadir}/%{name}
%{_datadir}/GConf/gsettings/empathy.convert
%{_datadir}/dbus-1/services/org.freedesktop.Telepathy.Client.Empathy.AudioVideo.service
%{_datadir}/dbus-1/services/org.freedesktop.Telepathy.Client.Empathy.Auth.service
%{_datadir}/dbus-1/services/org.freedesktop.Telepathy.Client.Empathy.Call.service
%{_datadir}/dbus-1/services/org.freedesktop.Telepathy.Client.Empathy.Chat.service
%{_datadir}/dbus-1/services/org.freedesktop.Telepathy.Client.Empathy.FileTransfer.service
%{_datadir}/glib-2.0/schemas/org.gnome.Empathy.gschema.xml
%{_datadir}/telepathy/clients/Empathy.AudioVideo.client
%{_datadir}/telepathy/clients/Empathy.Auth.client
%{_datadir}/telepathy/clients/Empathy.Call.client
%{_datadir}/telepathy/clients/Empathy.Chat.client
%{_datadir}/telepathy/clients/Empathy.FileTransfer.client
%{_iconsdir}/hicolor/*/apps/*
%{_mandir}/man1/empathy*.1*
%{_desktopdir}/*.desktop

%files -n nautilus-sendto-empathy
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/nautilus-sendto/plugins/libnstempathy.so
