#% define git 20120327
%define git 0


Name: x11-driver-video-sisusb
Version: 0.9.6
%if 0%git
Release: 0.%git.1
Source0: xf86-video-sisusb-%git.tar.xz
%else
Release: 2
Source0: http://xorg.freedesktop.org/releases/individual/driver/xf86-video-sisusb-%{version}.tar.bz2
%endif
Summary: Driver for SiS video chips connected via a Net2280-based USB dongle
Group: System/X11
License: MIT
URL: http://xorg.freedesktop.org

BuildRequires: x11-proto-devel >= 1.0.0
BuildRequires: x11-server-devel >= 1.12
BuildRequires: x11-util-macros >= 1.0.1
Conflicts: xorg-x11-server < 7.0

Requires: x11-server-common %(xserver-sdk-abi-requires videodrv)

%description
x11-driver-video-sisusb is the X.org video driver for SiS video chips
connected via a Net2280-based USB dongle.

%prep
%if 0%git
%setup -qn xf86-video-sisusb
%else
%setup -qn xf86-video-sisusb-%{version}
%endif
[ -e autogen.sh ] && ./autogen.sh --help

%build
%configure2_5x
%make

%install
rm -rf %{buildroot}
%makeinstall_std
find %{buildroot} -type f -name "*.la" -exec rm -f {} ';'

%files
%doc COPYING
%{_libdir}/xorg/modules/drivers/sisusb_drv.so
%{_mandir}/man4/sisusb.*


%changelog
* Mon Jul 23 2012 Alexander Khrukin <akhrukin@mandriva.org> 0.9.6-1
+ Revision: 810698
- version update 0.9.6
- spec sixes and rebuild

* Tue Mar 27 2012 Bernhard Rosenkraenzer <bero@bero.eu> 0.9.5-0.20120327.1
+ Revision: 787484
- Update to current git to fix compatibility with x11-server 1.12
- Fix rpmlint errors

* Sat Dec 31 2011 Matthew Dawkins <mattydaw@mandriva.org> 0.9.4-7
+ Revision: 748345
- rebuild cleaned up spec

* Sat Oct 08 2011 Tomasz Pawel Gajc <tpg@mandriva.org> 0.9.4-6
+ Revision: 703646
- rebuild for new x11-server

* Thu Jun 09 2011 Eugeni Dodonov <eugeni@mandriva.com> 0.9.4-5
+ Revision: 683587
- Rebuild for new x11-server

* Sat May 07 2011 Oden Eriksson <oeriksson@mandriva.com> 0.9.4-4
+ Revision: 671179
- mass rebuild

* Wed Nov 10 2010 Thierry Vignaud <tv@mandriva.org> 0.9.4-3mdv2011.0
+ Revision: 595744
- require xorg server with proper ABI

* Sun Oct 10 2010 Thierry Vignaud <tv@mandriva.org> 0.9.4-2mdv2011.0
+ Revision: 584626
- bump release before rebuilding for xserver 1.9

* Tue Jul 20 2010 Thierry Vignaud <tv@mandriva.org> 0.9.4-1mdv2011.0
+ Revision: 555159
- new release

* Wed Aug 05 2009 Frederik Himpe <fhimpe@mandriva.org> 0.9.3-1mdv2010.0
+ Revision: 410355
- Update to new version 0.9.3
- Use %%configure2_5x to fix build

* Fri Jul 03 2009 Ander Conselvan de Oliveira <ander@mandriva.com> 0.9.2-1mdv2010.0
+ Revision: 391933
- update to new version 0.9.2

* Fri Feb 27 2009 Ander Conselvan de Oliveira <ander@mandriva.com> 0.9.1-1mdv2009.1
+ Revision: 345695
- Fix build with -Werror=format-security

  + Thierry Vignaud <tv@mandriva.org>
    - new release
    - fix group

  + Colin Guthrie <cguthrie@mandriva.org>
    - Rebuild for new xserver

* Sat Nov 29 2008 Adam Williamson <awilliamson@mandriva.org> 0.9.0-3mdv2009.1
+ Revision: 308176
- rebuild for new X server

* Thu Aug 07 2008 Thierry Vignaud <tv@mandriva.org> 0.9.0-2mdv2009.0
+ Revision: 265948
- rebuild early 2009.0 package (before pixel changes)
- improved description
- add missing dot at end of description

* Tue Apr 15 2008 Paulo Andrade <pcpa@mandriva.com.br> 0.9.0-1mdv2009.0
+ Revision: 194151
- Update to version 0.9.0.

* Tue Feb 12 2008 Paulo Andrade <pcpa@mandriva.com.br> 0.8.1-6mdv2008.1
+ Revision: 166133
- Attempt fix:
  [around 1k lines or messages]
  Submission errors, aborting:
- x11-driver-video-sisusb-0.8.1-6mdv2008.1.src:
 - description-line-too-long The X.org video driver for SiS video chips connected via a Net2280-based USB dongle.
  /export/home/repsys/@166112:x11-driver-video-sisusb-0.8.1-6mdv2008.1.src.rpm
  error performing action submit: Error during submission: 256
 at /usr/bin/mdvsys line 536
- Revert to use upstream tarball and remove local patches.

* Tue Jan 22 2008 Ademar de Souza Reis Jr <ademar@mandriva.com.br> 0.8.1-5mdv2008.1
+ Revision: 156621
- re-enable rpm debug packages support

* Fri Jan 18 2008 Paulo Andrade <pcpa@mandriva.com.br> 0.8.1-4mdv2008.1
+ Revision: 154793
- Updated BuildRequires and resubmit package.
- Remove -devel package as it isn't really required as it provides only 2 files
  that aren't even header files; still don't install the .la files.
  All dependency files should be stored in the x11-util-modular package as they
  are only required for the "modular" build.
- Move .la files to new -devel package, and also add .deps files to -devel package.
- Note local tag xf86-video-sisusb-0.8.1@mandriva suggested on upstream
  Tag at git checkout ec1d219d933d865f107b68566ea5bb87f3521b22
- Update for new policy of hidden symbols and common macros.

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Tue Oct 16 2007 Ademar de Souza Reis Jr <ademar@mandriva.com.br> 0.8.1-3mdv2008.1
+ Revision: 99047
- minor spec cleanup
- build against new xserver (1.4)

* Thu Aug 30 2007 Oden Eriksson <oeriksson@mandriva.com> 0.8.1-2mdv2008.0
+ Revision: 75787
- rebuild

  + Thierry Vignaud <tv@mandriva.org>
    - fix man pages

