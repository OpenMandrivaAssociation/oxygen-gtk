Name: oxygen-gtk
Summary: A port of the default KDE widget theme (Oxygen) to gtk
Version: 1.1.2
Release: %mkrel 1
Source0: http://fr2.rpmfind.net/linux/KDE/stable/oxygen-gtk/%{version}/src/%{name}-%{version}.tar.bz2
URL: https://projects.kde.org/projects/playground/artwork/oxygen-gtk
Group: Graphical desktop/KDE
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
License: LGPLv2+
BuildRequires: gtk+2-devel
BuildRequires: cmake
%if %{mdvver} < 201100
Suggests: systemsettings-qt-gtk
%else
Suggests: gtk-qt-kcm
%endif

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

%prep
%setup -q -n %{name}-%{version}

%build
%cmake
%make

%install
rm -rf %{buildroot}
%makeinstall_std -C build

%clean 
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{_bindir}/*
%{_libdir}/gtk-2.0/2.10.0/engines/liboxygen-gtk.so
%{_datadir}/themes/oxygen-gtk
