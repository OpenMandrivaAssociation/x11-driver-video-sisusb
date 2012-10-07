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
BuildRequires: pkgconfig(xorg-server) >= 1.13
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
