%define gettext_package redhat-menus

Summary: Configuration and data files for the desktop menus
Name: redhat-menus
Version: 1.7
Release: 1
URL: http://www.redhat.com
Source0: %{name}-%{version}.tar.gz

License: XFree86
Group: User Interface/Desktops
BuildRoot: %{_tmppath}/%{name}-root
BuildArchitectures: noarch

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

%build

%configure
make

# the "perl only English" trick was OK for translations, but 
# still broke docs - so can't do this
#perl -pi -e 's/Web Browser/Mozilla Web Browser/g' desktop-files/redhat-web.desktop
#perl -pi -e 's/Email/Evolution Email/g' desktop-files/redhat-email.desktop
#perl -pi -e 's/Diagrams/Dia Diagrams/g' desktop-files/redhat-diagrams.desktop
#perl -pi -e 's/Video Conferencing/GnomeMeeting Video Conferencing/g' desktop-files/redhat-gnomemeeting.desktop

%install
rm -rf $RPM_BUILD_ROOT

%makeinstall
%find_lang %{gettext_package}

%clean
rm -rf $RPM_BUILD_ROOT

%files  -f %{gettext_package}.lang
%defattr(-,root,root)
%dir %{_sysconfdir}/xdg/menus
%config %{_sysconfdir}/xdg/menus/*.menu
%{_sysconfdir}/X11/starthere
%{_datadir}/desktop-menu-patches/*.desktop
%{_datadir}/desktop-directories/*.directory

%changelog
* Fri Sep 24 2004 Ray Strode <rstrode@redhat.com> 1.7-1
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


