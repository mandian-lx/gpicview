Summary:	A Simple and Fast Image Viewer for X
Name:     	gpicview
Version:	0.1.9
Release:	%mkrel 4
License:	GPLv2+
Group:		Graphics
Source0: 	http://dfn.dl.sourceforge.net/sourceforge/lxde/%name-%version.tar.gz
# Don't empty files when trying to save in unsupported file format
# http://bugs.debian.org/cgi-bin/bugreport.cgi?bug=498394
Patch0:		gpicview-0.1.9-dontsavegif.patch
Patch1:		gpicview-0.1.9-CVE-2008-3791.patch
Patch2:		gpicview-0.1.9-CVE-2008-3904.patch
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
%patch0 -p1 -b .dontsavegif
%patch1 -p1 -b .CVE-2008-3791
%patch2 -p1 -b .CVE-2008-3904

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
