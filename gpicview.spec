Summary:	A Simple and Fast Image Viewer for X
Name:     	gpicview
Version:	0.1.11
Release:	%mkrel 2
License:	GPLv2+
Group:		Graphics
Source0: 	http://dfn.dl.sourceforge.net/sourceforge/lxde/%name-%version.tar.gz
Patch0:		gpicview-0.1.11-r1293.patch
URL:		http://lxde.sourceforge.net/gpicview/
BuildRoot:	%{_tmppath}/%{name}-%{version}-buildroot
BuildRequires:	gtk+2-devel jpeg-devel desktop-file-utils

%description
GPicView is a simple and fast image viewer for X.
It features:
. Extremely lightweight and fast with low memory usage
. Very suitable for default image viewer of desktop system
. Simple and intuitive interface
. Minimal lib dependency: Only pure GTK+ is used
. Desktop independent: Doesn't require any specific desktop environment

%prep
%setup -q
%patch0 -p2

%build
%configure2_5x
%make

%install
rm -rf %{buildroot}
%makeinstall_std

%{find_lang} %{name}

desktop-file-install --vendor='' \
	--dir=%buildroot%_datadir/applications \
	--remove-category='Application' \
	--remove-category='Core' \
	%buildroot%_datadir/applications/*.desktop

%clean
rm -rf %{buildroot}

%if %mdkversion < 200900
%post  
%{update_menus}
%endif

%if %mdkversion < 200900
%postun
%{clean_menus}
%endif

%files -f %{name}.lang
%defattr(-, root, root)
%{_bindir}/%name
%{_datadir}/applications/*.desktop
%{_datadir}/%name
%{_datadir}/pixmaps/*
