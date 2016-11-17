Summary:	Driver for SiS video chips connected via a Net2280-based USB dongle
Name:		x11-driver-video-sisusb
Version:	0.9.6.20161117
Release:	1
Group:		System/X11
License:	MIT
Url:		http://xorg.freedesktop.org
Source0:	http://xorg.freedesktop.org/releases/individual/driver/xf86-video-sisusb-%{version}.tar.bz2
Patch0:		x11-driver-video-sisusb-0.9.6-xorg-1.19.patch

BuildRequires:	pkgconfig(glproto)
BuildRequires:	pkgconfig(xorg-macros)
BuildRequires:	pkgconfig(xorg-server)
BuildRequires:	pkgconfig(xproto)
Requires:	x11-server-common %(xserver-sdk-abi-requires videodrv)

%description
x11-driver-video-sisusb is the X.org video driver for SiS video chips
connected via a Net2280-based USB dongle.

%prep
%setup -qn xf86-video-sisusb-%{version}
%apply_patches
autoreconf -fiv

%build
CFLAGS="%{optflags} -I%{_includedir}/xorg" %configure
%make

%install
%makeinstall_std

%files
%doc COPYING
%{_libdir}/xorg/modules/drivers/sisusb_drv.so
%{_mandir}/man4/sisusb.*

