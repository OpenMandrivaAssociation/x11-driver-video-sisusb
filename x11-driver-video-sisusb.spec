Name:		x11-driver-video-sisusb
Version:	0.9.6
Release:	4
Source0:	http://xorg.freedesktop.org/releases/individual/driver/xf86-video-sisusb-%{version}.tar.bz2
Summary:	Driver for SiS video chips connected via a Net2280-based USB dongle
Group:		System/X11
License:	MIT
URL:		http://xorg.freedesktop.org

BuildRequires:	x11-proto-devel >= 1.0.0
BuildRequires:	pkgconfig(xorg-server) >= 1.13
BuildRequires:	x11-util-macros >= 1.0.1
BuildRequires:	pkgconfig(glproto) >= 1.4.16
Conflicts:	xorg-x11-server < 7.0

Requires:	x11-server-common %(xserver-sdk-abi-requires videodrv)

%description
x11-driver-video-sisusb is the X.org video driver for SiS video chips
connected via a Net2280-based USB dongle.

%prep
%setup -qn xf86-video-sisusb-%{version}
aclocal
automake -a
autoconf

%build
CFLAGS="%{optflags} -I%{_includedir}/xorg" %configure2_5x
%make

%install
%makeinstall_std

%files
%doc COPYING
%{_libdir}/xorg/modules/drivers/sisusb_drv.so
%{_mandir}/man4/sisusb.*
