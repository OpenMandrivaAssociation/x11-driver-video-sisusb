Summary:	Driver for SiS video chips connected via a Net2280-based USB dongle
Name:		x11-driver-video-sisusb
Version:	0.9.7
Release:	3
Group:		System/X11
License:	MIT
Url:		http://xorg.freedesktop.org
Source0:	http://xorg.freedesktop.org/releases/individual/driver/xf86-video-sisusb-%{version}.tar.bz2

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

