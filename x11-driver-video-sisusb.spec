Name: x11-driver-video-sisusb
Version: 0.9.4
Release: %mkrel 1
Summary: The X.org video driver for SiS video chips connected via a Net2280-based USB dongle
Group: System/X11
URL: http://xorg.freedesktop.org
Source: http://xorg.freedesktop.org/releases/individual/driver/xf86-video-sisusb-%{version}.tar.bz2
License: MIT
BuildRoot: %{_tmppath}/%{name}-root
BuildRequires: x11-proto-devel >= 1.0.0
BuildRequires: x11-server-devel >= 1.0.1
BuildRequires: x11-util-macros >= 1.0.1
Conflicts: xorg-x11-server < 7.0

Patch1: 0001-Fix-build-with-Werror-format-security.patch
%description
x11-driver-video-sisusb is the X.org video driver for SiS video chips
connected via a Net2280-based USB dongle.

%prep
%setup -q -n xf86-video-sisusb-%{version}
%patch1 -p1

%build
%configure2_5x
%make

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc COPYING
%{_libdir}/xorg/modules/drivers/sisusb_drv.la
%{_libdir}/xorg/modules/drivers/sisusb_drv.so
%{_mandir}/man4/sisusb.*
