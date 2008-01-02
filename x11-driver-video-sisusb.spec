Name: x11-driver-video-sisusb
Version: 0.8.1
Release: %mkrel 4
Summary: The X.org video driver for SiS video chips connected via a Net2280-based USB dongle
Group: Development/X11
URL: http://xorg.freedesktop.org
# Note local tag xf86-video-sisusb-0.8.1@mandriva suggested on upstream
# Tag at git checkout ec1d219d933d865f107b68566ea5bb87f3521b22
########################################################################
# git clone git://git.mandriva.com/people/pcpa/xorg/drivers/xf86-video-sisusb  xorg/drivers/xf86-video-sisusb
# cd xorg/drivers/xf86-video/sisusb
# git-archive --format=tar --prefix=xf86-video-sisusb-0.8.1/ xf86-video-sisusb-0.8.1@mandriva | bzip2 -9 > xf86-video-sisusb-0.8.1.tar.bz2
########################################################################
Source0: xf86-video-sisusb-%{version}.tar.bz2
License: MIT
########################################################################
# git-format-patch xf86-video-sisusb-0.8.1@mandriva..origin/mandriva+gpl
Patch1: 0001-Update-for-new-policy-of-hidden-symbols-and-common-m.patch
########################################################################
BuildRequires: x11-proto-devel >= 1.0.0
BuildRequires: x11-server-devel >= 1.0.1
BuildRequires: x11-util-macros >= 1.1.5-4mdk
BuildRequires: x11-util-modular
Conflicts: xorg-x11-server < 7.0

%description
The X.org video driver for SiS video chips connected via a Net2280-based USB dongle.

%prep
%setup -q -n xf86-video-sisusb-%{version}

%patch1 -p1

%build
autoreconf -ifs
%configure
%make

%install
rm -rf %{buildroot}
%makeinstall_std
rm -f %{buildroot}/%{_libdir}/xorg/modules/drivers/*.la

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc COPYING
%{_libdir}/xorg/modules/drivers/sisusb_drv.so
%{_mandir}/man4/sisusb.*
