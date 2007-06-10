Summary:	Very easy to use GNOME Telepathy client
Summary(pl.UTF-8):	Bardzo łatwy w użyciu klient Telepathy dla GNOME
Name:		empathy
Version:	0.7
Release:	1
License:	GPL
Group:		Applications/Communications
Source0:	http://ftp.gnome.org/pub/GNOME/sources/empathy/0.7/%{name}-%{version}.tar.bz2
# Source0-md5:	c63eded14fc0ad0feb38114569191f8d
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
BuildRequires:	telepathy-mission-control-devel >= 4.22
Requires(post,postun):	gtk+2 >= 2:2.10.12
Requires(post,postun):	hicolor-icon-theme
Requires(post,preun):	GConf2
Obsoletes:	gnome-jabber
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Empathy aims at making Instant Messaging with Jabber as easy as
possible.

%description -l pl.UTF-8
Celem Empathy jest uczynienie komunikowania poprzez Jabbera tak łatwym
jak to tylko możliwe.

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
	--disable-schemas-install
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

%preun
%gconf_schema_uninstall empathy.schemas

%postun
%update_icon_cache hicolor

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
