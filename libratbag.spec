#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : libratbag
Version  : 0.16
Release  : 12
URL      : https://github.com/libratbag/libratbag/archive/v0.16/libratbag-0.16.tar.gz
Source0  : https://github.com/libratbag/libratbag/archive/v0.16/libratbag-0.16.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : MIT
Requires: libratbag-bin = %{version}-%{release}
Requires: libratbag-data = %{version}-%{release}
Requires: libratbag-lib = %{version}-%{release}
Requires: libratbag-license = %{version}-%{release}
Requires: libratbag-man = %{version}-%{release}
Requires: libratbag-services = %{version}-%{release}
BuildRequires : buildreq-meson
BuildRequires : glib-dev
BuildRequires : json-glib-dev
BuildRequires : libunistring-dev
BuildRequires : pkgconfig(check)
BuildRequires : pkgconfig(glib-2.0)
BuildRequires : pkgconfig(json-glib-1.0)
BuildRequires : pkgconfig(libevdev)
BuildRequires : pkgconfig(libudev)
BuildRequires : pygobject
BuildRequires : pypi(evdev)
BuildRequires : python3-dev
BuildRequires : swig
BuildRequires : valgrind

%description
libratbag
=========
<img src="https://libratbag.github.io/_images/logo.svg" alt="" width="30%" align="right">

%package bin
Summary: bin components for the libratbag package.
Group: Binaries
Requires: libratbag-data = %{version}-%{release}
Requires: libratbag-license = %{version}-%{release}
Requires: libratbag-services = %{version}-%{release}

%description bin
bin components for the libratbag package.


%package data
Summary: data components for the libratbag package.
Group: Data

%description data
data components for the libratbag package.


%package dev
Summary: dev components for the libratbag package.
Group: Development
Requires: libratbag-lib = %{version}-%{release}
Requires: libratbag-bin = %{version}-%{release}
Requires: libratbag-data = %{version}-%{release}
Provides: libratbag-devel = %{version}-%{release}
Requires: libratbag = %{version}-%{release}

%description dev
dev components for the libratbag package.


%package lib
Summary: lib components for the libratbag package.
Group: Libraries
Requires: libratbag-data = %{version}-%{release}
Requires: libratbag-license = %{version}-%{release}

%description lib
lib components for the libratbag package.


%package license
Summary: license components for the libratbag package.
Group: Default

%description license
license components for the libratbag package.


%package man
Summary: man components for the libratbag package.
Group: Default

%description man
man components for the libratbag package.


%package services
Summary: services components for the libratbag package.
Group: Systemd services

%description services
services components for the libratbag package.


%prep
%setup -q -n libratbag-0.16
cd %{_builddir}/libratbag-0.16

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1648157896
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
CFLAGS="$CFLAGS" CXXFLAGS="$CXXFLAGS" LDFLAGS="$LDFLAGS" meson --libdir=lib64 --prefix=/usr --buildtype=plain   builddir
ninja -v -C builddir

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
meson test -C builddir --print-errorlogs || :

%install
mkdir -p %{buildroot}/usr/share/package-licenses/libratbag
cp %{_builddir}/libratbag-0.16/COPYING %{buildroot}/usr/share/package-licenses/libratbag/ad46f9be2737903a5706c4b1e313d72883bce6d1
DESTDIR=%{buildroot} ninja -C builddir install

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/lur-command
/usr/bin/ratbagctl
/usr/bin/ratbagd

%files data
%defattr(-,root,root,-)
/usr/share/dbus-1/system-services/org.freedesktop.ratbag1.service
/usr/share/dbus-1/system.d/org.freedesktop.ratbag1.conf
/usr/share/libratbag/etekcity-scroll-alpha.device
/usr/share/libratbag/glorious-model-d.device
/usr/share/libratbag/glorious-model-o.device
/usr/share/libratbag/gskill-MX-780.device
/usr/share/libratbag/logitech-M325.device
/usr/share/libratbag/logitech-M500s.device
/usr/share/libratbag/logitech-M545.device
/usr/share/libratbag/logitech-M570.device
/usr/share/libratbag/logitech-M585-M590.device
/usr/share/libratbag/logitech-M705.device
/usr/share/libratbag/logitech-M720.device
/usr/share/libratbag/logitech-MX-Anywhere-3.device
/usr/share/libratbag/logitech-MX-Anywhere2.device
/usr/share/libratbag/logitech-MX-Anywhere2S.device
/usr/share/libratbag/logitech-MX-Ergo.device
/usr/share/libratbag/logitech-MX-Master-2S.device
/usr/share/libratbag/logitech-MX-Master-3.device
/usr/share/libratbag/logitech-MX-Master.device
/usr/share/libratbag/logitech-MX-Vertical.device
/usr/share/libratbag/logitech-MX518.device
/usr/share/libratbag/logitech-Marathon-M705.device
/usr/share/libratbag/logitech-T650.device
/usr/share/libratbag/logitech-Wireless-Touchpad.device
/usr/share/libratbag/logitech-g-powerplay.device
/usr/share/libratbag/logitech-g-pro-wireless.device
/usr/share/libratbag/logitech-g-pro-x-wireless-superlight.device
/usr/share/libratbag/logitech-g-pro.device
/usr/share/libratbag/logitech-g102-g203.device
/usr/share/libratbag/logitech-g300.device
/usr/share/libratbag/logitech-g302.device
/usr/share/libratbag/logitech-g303.device
/usr/share/libratbag/logitech-g305.device
/usr/share/libratbag/logitech-g402.device
/usr/share/libratbag/logitech-g403-hero.device
/usr/share/libratbag/logitech-g403-wireless.device
/usr/share/libratbag/logitech-g403.device
/usr/share/libratbag/logitech-g5-2007.device
/usr/share/libratbag/logitech-g5.device
/usr/share/libratbag/logitech-g500.device
/usr/share/libratbag/logitech-g500s.device
/usr/share/libratbag/logitech-g502-hero-wireless.device
/usr/share/libratbag/logitech-g502-hero.device
/usr/share/libratbag/logitech-g502-proteus-core.device
/usr/share/libratbag/logitech-g502-proteus-spectrum.device
/usr/share/libratbag/logitech-g513.device
/usr/share/libratbag/logitech-g600.device
/usr/share/libratbag/logitech-g602.device
/usr/share/libratbag/logitech-g603.device
/usr/share/libratbag/logitech-g604.device
/usr/share/libratbag/logitech-g7.device
/usr/share/libratbag/logitech-g700-wireless.device
/usr/share/libratbag/logitech-g700.device
/usr/share/libratbag/logitech-g700s.device
/usr/share/libratbag/logitech-g703-hero.device
/usr/share/libratbag/logitech-g703.device
/usr/share/libratbag/logitech-g815.device
/usr/share/libratbag/logitech-g9.device
/usr/share/libratbag/logitech-g900.device
/usr/share/libratbag/logitech-g903-hero.device
/usr/share/libratbag/logitech-g903.device
/usr/share/libratbag/logitech-g910.device
/usr/share/libratbag/logitech-g915-tkl.device
/usr/share/libratbag/logitech-g915.device
/usr/share/libratbag/logitech-g935.device
/usr/share/libratbag/logitech-g9x-Call-of-Duty-MW3-Edition.device
/usr/share/libratbag/logitech-g9x-Original.device
/usr/share/libratbag/nubwo-x7-spectrum.device
/usr/share/libratbag/openinput.device
/usr/share/libratbag/roccat-kone-pure.device
/usr/share/libratbag/roccat-kone-xtd.device
/usr/share/libratbag/steelseries-kinzu-v2-pro.device
/usr/share/libratbag/steelseries-kinzu-v2.device
/usr/share/libratbag/steelseries-kinzu-v3.device
/usr/share/libratbag/steelseries-rival-310.device
/usr/share/libratbag/steelseries-rival-600.device
/usr/share/libratbag/steelseries-rival.device
/usr/share/libratbag/steelseries-sensei-310.device
/usr/share/libratbag/steelseries-sensei-raw.device

%files dev
%defattr(-,root,root,-)
/usr/include/liblur.h
/usr/lib64/liblur.so
/usr/lib64/pkgconfig/liblur.pc

%files lib
%defattr(-,root,root,-)
/usr/lib64/liblur.so.3
/usr/lib64/liblur.so.3.0.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/libratbag/ad46f9be2737903a5706c4b1e313d72883bce6d1

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/lur-command.1
/usr/share/man/man1/ratbagctl.1
/usr/share/man/man8/ratbagd.8

%files services
%defattr(-,root,root,-)
/usr/lib/systemd/system/ratbagd.service
