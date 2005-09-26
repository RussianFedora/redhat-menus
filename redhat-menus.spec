%define gettext_package redhat-menus
%define desktop_file_utils_version 0.9

Summary: Configuration and data files for the desktop menus
Name: redhat-menus
Version: 5.0.0
Release: 2
URL: http://www.redhat.com
Source0: %{name}-%{version}.tar.gz
PreReq: desktop-file-utils >= %{desktop_file_utils_version}

License: XFree86
Group: User Interface/Desktops
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildArch: noarch
BuildRequires: desktop-file-utils >= %{desktop_file_utils_version}

Patch0: redhat-menus-5.0.0-move-prefs-out-of-apps-menu.patch

## old nautilus contained start-here stuff
Conflicts: nautilus <= 2.0.3-1
## desktop files in redhat-menus point to icons in new artwork
Conflicts: redhat-artwork < 0.35

%description

This package contains the XML files that describe the menu layout for 
GNOME and KDE, and the .desktop files that define the names and icons 
of "subdirectories" in the menus.

%prep
%setup -q
%patch0 -p1 -b .move-prefs-out-of-apps-menu

%build

%configure
make

%install
rm -rf $RPM_BUILD_ROOT

make install DESTDIR=$RPM_BUILD_ROOT

%find_lang %{gettext_package}

%clean
rm -rf $RPM_BUILD_ROOT

%post
update-desktop-database %{_datadir}/applications

%postun
update-desktop-database %{_datadir}/applications

%files  -f %{gettext_package}.lang
%defattr(-,root,root)
%dir %{_sysconfdir}/xdg
%dir %{_sysconfdir}/xdg/menus
%dir %{_sysconfdir}/xdg/menus/applications-merged
%dir %{_sysconfdir}/xdg/menus/preferences-merged
%config %{_sysconfdir}/xdg/menus/*.menu
%{_sysconfdir}/X11/starthere
%{_datadir}/desktop-menu-patches/*.desktop
%{_datadir}/desktop-directories/*.directory

%changelog
* Mon Sep 26 2005 Ray Strode <rstrode@redhat.com> 5.0.0-2
- one commented out patch was actually important and 
  shouldn't have been removed.

* Mon Sep 26 2005 Ray Strode <rstrode@redhat.com> 5.0.0-1
- add a preferences-merged dir for per package
  preference menus overriding
- remove old patches

* Thu Apr 14 2005 Ray Strode <rstrode@redhat.com> 3.8.0-1
- don't include kde legacy stuff anymore, since
  kde uses it's own applications menu file now and it 
  breaks gnome (bug 153125)

* Thu Mar 31 2005 Matthias Clasen <mclasen@redhat.com> 3.7.1-9
- don't pick up a pointless Desktop/System directory

* Thu Mar 31 2005 Than Ngo <than@redhat.com> 3.7.1-8
- don't mess gnome menu up

* Mon Mar 21 2005 Than Ngo <than@redhat.com> 3.7.1-7
- add mssing kwrite/kate/kedit, kcontrol center, System setting
  in menu #147121, #12218, #1221811, #143937
- get rid of capplets from preferences.menu, #149233
- fix icon entry in desktop file #143336

* Fri Feb  8 2005  <mclasen@redhat.com> - 3.7.1-6
- Don't pick up duplicates in the Others menu

* Thu Feb  3 2005  <mclasen@redhat.com> - 3.7.1-5
- Add settings.menu

* Mon Nov 22 2004  <jrb@redhat.com> - 3.7.1-3
- Sync to upstream
- #rh138282# Get redhat-evolution.desktop.in

* Mon Nov 22 2004 Dan Williams <dcbw@redhat.com> 3.7-5
- #rh137520# Add "application/x-ole-storage" to Calc, Impress, and Writer
	desktop files, so Evolution can associate these with OOo

* Tue Nov 16 2004 Dan Williams <dcbw@redhat.com> 3.7-4
- #rh137520# Add more supported mime-types to OpenOffice.org .desktop files

* Mon Nov  1 2004 <dcbw@redhat.com> - 3.7-2
- Gratuitous version bump from upstream
- #rh74651# no mimetype entries for microsoft offic
- #rh136731# wordperfect files (.wpd) should be associated with openoffice

* Fri Oct 22 2004  <jrb@redhat.com> - 1.13-1
- New release.  This just has new translations and an evolution desktop file

* Mon Oct 18 2004  <jrb@redhat.com> - 1.12-1
- new version to deal with default mail client

* Mon Oct 18 2004  <jrb@redhat.com> - 1.11-1
- New release to get new translations and change the default web browser

* Wed Oct 13 2004 Colin Walters <walters@redhat.com> 1.10-1
- Add application/ogg to redhat-audio-player.desktop,
  for bug 134547 (hi Sopwith)
  
* Wed Oct 13 2004 Bill Nottingham <notting@redhat.com> 1.9-2
- own /etc/xdg (#130596)

* Wed Sep 29 2004 Ray Strode <rstrode@redhat.com> 1.9-1
- release 1.9, add gthumb desktop file  

* Fri Sep 24 2004 Ray Strode <rstrode@redhat.com> 1.8-1
- release 1.8, remove AC_PROG_LIBTOOL from configure.in
- release 1.7, remove gnome-control-center.desktop

* Wed Sep 22 2004 Warren Togami <wtogami@redhat.com> 1.6.1-2
- remove ugly hacks so package is easier to maintain

* Tue Sep 21 2004 Seth Nickell <snickell@redhat.com> 1.6.1-1
- release 1.6.1, don't call AC_PROG_LIBTOOL

* Tue Sep 21 2004 Seth Nickell <snickell@redhat.com> 1.6-1
- release 1.6, add a bunch of translations to the build

* Fri May 07 2004 Than Ngo <than@redhat.com> 1.4.1-1
- release 1.4.1, add More submenu, fix Preferences/Others menu

* Wed May 05 2004 Warren Togami <wtogami@redhat.com> 1.4-2
- Temporary hacks for Preferred Browser launching in FC2

* Tue Mar 16 2004 Than Ngo <than@redhat.com> 1.3-1
- Release 1.3, add applications-kmenuedit.menu that makes kmenuedit working

* Tue Mar 16 2004 Than Ngo <than@redhat.com> 1.2-1
- Release 1.2, fixed KDE menu issue

* Fri Mar 12 2004 Than Ngo <than@redhat.com> 1.1-1
- Release 1.1, cleanup KDE menus, get rid of KDE stuffs which are now included in kde package

* Thu Mar 11 2004 Seth Nickell <snickell@redhat.com>
- Release 1.0 which conforms to xdg menu spec 0.8

* Fri Feb 13 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Fri Oct  3 2003 Havoc Pennington <hp@redhat.com> 0.40-1
- 0.40

* Mon Jul 28 2003 Than Ngo <than@redhat.com> 0.39-2
- rebuilt

* Mon Jul 28 2003 Than Ngo <than@redhat.com> 0.39-1
- 0.39, clean up

* Thu Feb  6 2003 Havoc Pennington <hp@redhat.com> 0.37-1
- 0.37

* Wed Jan 29 2003 Havoc Pennington <hp@redhat.com>
- 0.36 fixes missing Preferences in start-here hopefully

* Mon Jan 27 2003 Havoc Pennington <hp@redhat.com>
- 0.35

* Wed Jan 22 2003 Tim Powers <timp@redhat.com>
- rebuilt

* Wed Jan 22 2003 Than Ngo <than@redhat.com>
- 0.34, enable start-here.menu

* Sat Jan 11 2003 Havoc Pennington <hp@redhat.com>
- 0.33

* Thu Jan  9 2003 Havoc Pennington <hp@redhat.com>
- 0.32

* Tue Jan  7 2003 Havoc Pennington <hp@redhat.com>
- 0.31

* Thu Dec 12 2002 Havoc Pennington <hp@redhat.com>
- 0.29, rebuild

* Wed Dec  4 2002 Than Ngo <than@redhat.com>
- 0.27, added some new catagories for KDE 3.1

* Tue Sep 03 2002 Phil Knirsch <pknirsch@redhat.com>
- 0.26 fixed start-here.menu missing </Folder> tag for Preferences

* Fri Aug 30 2002 Havoc Pennington <hp@redhat.com>
- 0.25 with htmlview, fixed start-here.menu

* Tue Aug 27 2002 Havoc Pennington <hp@redhat.com>
- 0.23 with new translations, KDE MIME fixes, openoffice Exec= fixes
- don't munge en_US text, broke docs. Back to just "Web Browser"

* Fri Aug 23 2002 Havoc Pennington <hp@redhat.com>
- 0.22 new translations
- munge en_US text to "Mozilla Web Browser" etc.

* Wed Aug 21 2002 Havoc Pennington <hp@redhat.com>
- 0.21 with new translations

* Fri Aug 16 2002 Havoc Pennington <hp@redhat.com>
- 0.20 with new icons, etc.

* Fri Aug 16 2002 Havoc Pennington <hp@redhat.com>
- new icons, translations
- drop control-center patch, use from cvs

* Thu Aug 15 2002 Jonathan Blandford <jrb@redhat.com>
- move the control-center

* Wed Aug 14 2002 Havoc Pennington <hp@redhat.com>
- 0.18 with changed icons etc.

* Fri Aug  9 2002 Havoc Pennington <hp@redhat.com>
- 0.17 with System Settings submenu and translations

* Wed Aug  7 2002 Havoc Pennington <hp@redhat.com>
- 0.16 with start here

* Wed Aug  7 2002 Havoc Pennington <hp@redhat.com>
- 0.15 with placeholder icons for panel desktop files

* Tue Aug  6 2002 Havoc Pennington <hp@redhat.com>
- 0.14 with KDE preferences submenus

* Fri Aug  2 2002 Havoc Pennington <hp@redhat.com>
- 0.12 with server-settings and system-settings

* Wed Jul 31 2002 Havoc Pennington <hp@redhat.com>
- make it noarch

* Wed Jul 31 2002 Havoc Pennington <hp@redhat.com>
- 0.11 with audio player desktop file

* Wed Jul 31 2002 Havoc Pennington <hp@redhat.com>
- 0.10 trying Extras instead of All Apps, and add Advanced to preferences

* Tue Jul 30 2002 Havoc Pennington <hp@redhat.com>
- 0.9, has gdmsetup replacement desktop file

* Mon Jul 29 2002 Havoc Pennington <hp@redhat.com>
- 0.8

* Wed Jul 24 2002 Havoc Pennington <hp@redhat.com>
- 0.7, adds documentation submenu, strips Base-Only out of All Apps

* Wed Jul 24 2002 Havoc Pennington <hp@redhat.com>
- 0.6

* Tue Jul 23 2002 Havoc Pennington <hp@redhat.com>
- 0.5

* Sat Jul 20 2002 Than Ngo <than@redhat.com>
- add BaseGroup settings into Settings.directory

* Thu Jul 11 2002 Havoc Pennington <hp@redhat.com>
- fix group

* Mon Jun 24 2002 Havoc Pennington <hp@redhat.com>
- 0.3
- 0.4

* Fri Jun 21 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Tue Jun 11 2002 Havoc Pennington <hp@redhat.com>
- move menus to sysconfdir/X11
- hack on applications.menu a small amount. Needs
  major help.

* Tue May 28 2002 Havoc Pennington <hp@redhat.com>
- rebuild in different environment

* Tue May 28 2002 Havoc Pennington <hp@redhat.com>
- description would be good

* Tue May 28 2002 Havoc Pennington <hp@redhat.com>
- Initial build.


