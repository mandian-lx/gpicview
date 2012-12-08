Summary:	A Simple and Fast Image Viewer for X
Name:     	gpicview
Version:	0.2.3
Release:	1
License:	GPLv2+
Group:		Graphics
Source0: 	http://dfn.dl.sourceforge.net/sourceforge/lxde/%name-%version.tar.gz
URL:		http://www.lxde.org/
BuildRequires:	pkgconfig(gtk+-2.0)
BuildRequires:	jpeg-devel
BuildRequires:	desktop-file-utils
BuildRequires:	intltool >= 0.40.0

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

%build
%configure2_5x
%make LIBS="-ljpeg -lm"

%install
%makeinstall_std

%find_lang %{name}

desktop-file-install --vendor='' \
	--dir=%{buildroot}%{_datadir}/applications \
	--remove-category='Application' \
	--remove-category='Core' \
	--remove-category='Utility' \
	--remove-category='Photography' \
	--remove-category='RasterGraphics' \
	%{buildroot}%{_datadir}/applications/*.desktop

%files -f %{name}.lang
%{_bindir}/%{name}
%{_datadir}/applications/*.desktop
%{_datadir}/%{name}
%{_datadir}/pixmaps/*


%changelog
* Fri Jul 20 2012 Alexander Khrukin <akhrukin@mandriva.org> 0.2.3-1
+ Revision: 810390
- version update 0.2.3

* Tue Aug 02 2011 Александр Казанцев <kazancas@mandriva.org> 0.2.2-1
+ Revision: 692770
- update to 0.2.2

* Sun Dec 05 2010 Oden Eriksson <oeriksson@mandriva.com> 0.2.1-4mdv2011.0
+ Revision: 610975
- rebuild

* Mon Jan 11 2010 Funda Wang <fwang@mandriva.org> 0.2.1-3mdv2010.1
+ Revision: 489451
- rebuild for libjpegv8

* Tue Aug 18 2009 Funda Wang <fwang@mandriva.org> 0.2.1-2mdv2010.0
+ Revision: 417497
- rebuild for libjpeg v7

* Fri Jul 03 2009 Funda Wang <fwang@mandriva.org> 0.2.1-1mdv2010.0
+ Revision: 391888
- new version 0.2.1
- fix url

* Sat May 30 2009 Funda Wang <fwang@mandriva.org> 0.2.0-1mdv2010.0
+ Revision: 381384
- New version 0.2.0

* Tue May 19 2009 Funda Wang <fwang@mandriva.org> 0.1.99-1mdv2010.0
+ Revision: 377433
- BR intltool
- New version 0.1.99

* Mon Apr 06 2009 Funda Wang <fwang@mandriva.org> 0.1.11-3mdv2009.1
+ Revision: 364440
- make it appears only in image menu

* Mon Apr 06 2009 Funda Wang <fwang@mandriva.org> 0.1.11-2mdv2009.1
+ Revision: 364364
- add upstream patch to fix RTL interface problem

* Tue Dec 16 2008 Funda Wang <fwang@mandriva.org> 0.1.11-1mdv2009.1
+ Revision: 314853
- New version 0.1.11
  deleting images bug finally fixed

* Tue Dec 16 2008 Funda Wang <fwang@mandriva.org> 0.1.10-1mdv2009.1
+ Revision: 314842
- fix compile with new cflags

* Sat Sep 13 2008 Funda Wang <fwang@mandriva.org> 0.1.10-1mdv2009.0
+ Revision: 284465
- New version 0.1.10
- patch merged upstream

* Thu Sep 11 2008 Frederik Himpe <fhimpe@mandriva.org> 0.1.9-4mdv2009.0
+ Revision: 283859
- Fix security problems CVE-2008-3791 and CVE-2008-3904
- Fix emptying of target files when trying to save in an unsupported
  file format such as GIF
- Use %%{buildroot} macro instead of $RPM_BUILD_ROOT in SPEC

* Thu Aug 07 2008 Thierry Vignaud <tv@mandriva.org> 0.1.9-3mdv2009.0
+ Revision: 266945
- rebuild early 2009.0 package (before pixel changes)

  + Pixel <pixel@mandriva.com>
    - rpm filetriggers deprecates update_menus/update_scrollkeeper/update_mime_database/update_icon_cache/update_desktop_database/post_install_gconf_schemas

  + Funda Wang <fwang@mandriva.org>
    - fix rpm group

* Sat May 03 2008 Funda Wang <fwang@mandriva.org> 0.1.9-2mdv2009.0
+ Revision: 200751
- fix desktop file category

* Sat May 03 2008 Funda Wang <fwang@mandriva.org> 0.1.9-1mdv2009.0
+ Revision: 200746
- import source and spec
- create gpicview

