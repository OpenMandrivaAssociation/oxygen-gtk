Summary:	A port of the default KDE widget theme (Oxygen) to gtk
Name:		oxygen-gtk
Version:	1.4.6
Release:	5
Group:		Graphical desktop/KDE
License:	LGPLv2+
Url:		https://projects.kde.org/projects/playground/artwork/oxygen-gtk
Source0:	ftp://ftp.kde.org/pub/kde/stable/oxygen-gtk2/%{version}/src/%{name}2-%{version}.tar.bz2
BuildRequires:	cmake
BuildRequires:	pkgconfig(cairo)
BuildRequires:	pkgconfig(dbus-glib-1)
BuildRequires:	pkgconfig(gtk+-2.0)
Requires:	oxygen-gtk2-engine = %{version}-%{release}

%description
Oxygen-Gtk is a port of the default KDE widget theme (Oxygen), to gtk.

It's primary goal is to ensure visual consistency between gtk and qt-based
applications running under kde. A secondary objective is to also have a
stand-alone nice looking gtk theme that would behave well on other Desktop
Environments.

Unlike other attempts made to port the kde oxygen theme to gtk, this attempt
does not depend on Qt (via some Qt to Gtk conversion engine), nor does render
the widget appearance via hard coded pixmaps, which otherwise breaks everytime
some setting is changed in kde.

%files
%doc AUTHORS COPYING INSTALL README
%{_bindir}/*
%{_datadir}/themes/oxygen-gtk

#------------------------------------------------

%define libname %mklibname oxygen-gtk

%package -n %{libname}
Summary:	Dynamic libraries for %{name}
Group:		System/Libraries
Provides:	oxygen-gtk2-engine = %{version}-%{release}
Conflicts:	oxygen-gtk < 1.3.0

%description -n %{libname}
Dynamic libraries for %{name}.

%files -n %{libname}
%{_libdir}/gtk-2.0/*/engines/liboxygen-gtk.so

#------------------------------------------------

%prep
%setup -q -n %{name}2-%{version}

%build
%cmake \
	-DOXYGEN_FORCE_KDE_ICONS_AND_FONTS=0
%make

%install
%makeinstall_std -C build

