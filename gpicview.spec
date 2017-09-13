Summary:	A Simple and Fast Image Viewer for X
Name:		gpicview
Version:	0.2.5
Release:	1
License:	GPLv2+
Group:		Graphics
Url:		https://wiki.lxde.org/en/GPicView
Source0:	https://downloads.sourceforge.net/lxde/%{name}-%{version}.tar.xz
Patch0:		%{name}-0.2.5-fix_build.patch

BuildRequires:	desktop-file-utils
BuildRequires:	intltool >= 0.40.0
BuildRequires:	pkgconfig(gtk+-2.0)
BuildRequires:	pkgconfig(libjpeg)
BuildRequires:	pkgconfig(x11)

%description
Lightweight X11 Desktop Environment project (a.k.a LXDE) aimed to provide a
new desktop environment which is useful enough and keep resource usage lower
at the same time. Useabiliy, speed, and memory usage are our main concern.

Unlike other tightly integrated desktops LXDE strives to be modular, so each
component can be used independently with few dependencies. This makes
porting LXDE to different distributions and platforms easier.

GPicView is the standard picture viewer of LXDE. GPicView features lightning
fast startup and an intuitive interface.

Some features:

  * Extremely lightweight and fast with low memory usage
  * Very suitable for default image viewer of desktop system
  * Simple and intuitive interface
  * Minimal lib dependency: Only pure GTK+ is used
  * Desktop independent: Doesn't require any specific desktop environment
  * Open source, licensed under GNU GPL

%files -f %{name}.lang
%{_bindir}/%{name}
%{_datadir}/applications/*.desktop
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/*
%{_iconsdir}/hicolor/*/apps/%{name}.png

#---------------------------------------------------------------------------

%prep
%setup -q
%apply_patches

%build
%configure
%make

%install
%makeinstall_std

# locales
%find_lang %{name}

# .desktop
desktop-file-install --vendor='' \
	--dir=%{buildroot}%{_datadir}/applications \
	--remove-category='Application' \
	--remove-category='Core' \
	--remove-category='Utility' \
	--remove-category='Photography' \
	--remove-category='RasterGraphics' \
	%{buildroot}%{_datadir}/applications/*.desktop

