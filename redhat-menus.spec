Summary: Configuration and data files for the desktop menus
Name: redhat-menus
Version: 0.2
Release: 2
URL: http://www.redhat.com
Source0: %{name}.tar.gz
License: XFree86
Group: Undecided
BuildRoot: %{_tmppath}/%{name}-root

%description

This package contains the XML files that describe the menu layout for 
GNOME and KDE, and the .desktop files that define the names and icons 
of "subdirectories" in the menus.

%prep
%setup -q -n redhat-menus

%build

%install
rm -rf $RPM_BUILD_ROOT

mkdir -p $RPM_BUILD_ROOT%{_datadir}/desktop-menu-files
chmod 755 $RPM_BUILD_ROOT%{_datadir}/desktop-menu-files
for I in desktop-files/*; do 
  install -m 644 $I $RPM_BUILD_ROOT%{_datadir}/desktop-menu-files
done

# workaround until intltool is set up properly
(cd $RPM_BUILD_ROOT%{_datadir}/desktop-menu-files; for I in *.directory.in; do mv $I `basename $I .directory.in`.directory; done)

mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/X11/desktop-menus
chmod 755 $RPM_BUILD_ROOT%{_sysconfdir}/X11/desktop-menus
for I in menus/*; do
  install -m 644 $I $RPM_BUILD_ROOT%{_sysconfdir}/X11/desktop-menus
done



%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%dir %{_sysconfdir}/X11/desktop-menus
%config %{_sysconfdir}/X11/desktop-menus/*
%{_datadir}/desktop-menu-files

%changelog
* Tue Jun 11 2002 Havoc Pennington <hp@redhat.com>
- rebuild in different environment

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


