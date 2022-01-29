#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : LibVNCServer
Version  : 0.9.13
Release  : 24
URL      : https://github.com/LibVNC/libvncserver/archive/LibVNCServer-0.9.13/libvncserver-0.9.13.tar.gz
Source0  : https://github.com/LibVNC/libvncserver/archive/LibVNCServer-0.9.13/libvncserver-0.9.13.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : GPL-2.0
Requires: LibVNCServer-filemap = %{version}-%{release}
Requires: LibVNCServer-lib = %{version}-%{release}
Requires: LibVNCServer-license = %{version}-%{release}
BuildRequires : SDL2-dev
BuildRequires : buildreq-cmake
BuildRequires : glibc-dev
BuildRequires : gnutls-dev
BuildRequires : gtk+-dev
BuildRequires : libjpeg-turbo-dev
BuildRequires : libpng-dev
BuildRequires : lzo-dev
BuildRequires : openssl-dev
BuildRequires : pkg-config
BuildRequires : pkgconfig(libsystemd)
BuildRequires : zlib-dev
Patch1: max-zlib-level.patch

%description
[![Build Status](https://travis-ci.org/LibVNC/libvncserver.svg?branch=master)](https://travis-ci.org/LibVNC/libvncserver)
[![Build status](https://ci.appveyor.com/api/projects/status/fao6m1md3q4g2bwn/branch/master?svg=true)](https://ci.appveyor.com/project/bk138/libvncserver/branch/master)
[![Help making this possible](https://img.shields.io/badge/liberapay-donate-yellow.png)](https://liberapay.com/LibVNC/donate) [![Join the chat at https://gitter.im/LibVNC/libvncserver](https://badges.gitter.im/LibVNC/libvncserver.svg)](https://gitter.im/LibVNC/libvncserver?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge)

%package dev
Summary: dev components for the LibVNCServer package.
Group: Development
Requires: LibVNCServer-lib = %{version}-%{release}
Provides: LibVNCServer-devel = %{version}-%{release}
Requires: LibVNCServer = %{version}-%{release}

%description dev
dev components for the LibVNCServer package.


%package filemap
Summary: filemap components for the LibVNCServer package.
Group: Default

%description filemap
filemap components for the LibVNCServer package.


%package lib
Summary: lib components for the LibVNCServer package.
Group: Libraries
Requires: LibVNCServer-license = %{version}-%{release}
Requires: LibVNCServer-filemap = %{version}-%{release}

%description lib
lib components for the LibVNCServer package.


%package license
Summary: license components for the LibVNCServer package.
Group: Default

%description license
license components for the LibVNCServer package.


%prep
%setup -q -n libvncserver-LibVNCServer-0.9.13
cd %{_builddir}/libvncserver-LibVNCServer-0.9.13
%patch1 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1633758035
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -Ofast -falign-functions=32 -ffat-lto-objects -flto=auto -fno-semantic-interposition -fstack-protector-strong -fzero-call-used-regs=used -mprefer-vector-width=256 "
export FCFLAGS="$FFLAGS -O3 -Ofast -falign-functions=32 -ffat-lto-objects -flto=auto -fno-semantic-interposition -fstack-protector-strong -fzero-call-used-regs=used -mprefer-vector-width=256 "
export FFLAGS="$FFLAGS -O3 -Ofast -falign-functions=32 -ffat-lto-objects -flto=auto -fno-semantic-interposition -fstack-protector-strong -fzero-call-used-regs=used -mprefer-vector-width=256 "
export CXXFLAGS="$CXXFLAGS -O3 -Ofast -falign-functions=32 -ffat-lto-objects -flto=auto -fno-semantic-interposition -fstack-protector-strong -fzero-call-used-regs=used -mprefer-vector-width=256 "
%cmake ..
make  %{?_smp_mflags}
popd
mkdir -p clr-build-avx2
pushd clr-build-avx2
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -Ofast -falign-functions=32 -ffat-lto-objects -flto=auto -fno-semantic-interposition -fstack-protector-strong -fzero-call-used-regs=used -march=x86-64-v3 -mprefer-vector-width=256 -mtune=skylake "
export FCFLAGS="$FFLAGS -O3 -Ofast -falign-functions=32 -ffat-lto-objects -flto=auto -fno-semantic-interposition -fstack-protector-strong -fzero-call-used-regs=used -march=x86-64-v3 -mprefer-vector-width=256 -mtune=skylake "
export FFLAGS="$FFLAGS -O3 -Ofast -falign-functions=32 -ffat-lto-objects -flto=auto -fno-semantic-interposition -fstack-protector-strong -fzero-call-used-regs=used -march=x86-64-v3 -mprefer-vector-width=256 -mtune=skylake "
export CXXFLAGS="$CXXFLAGS -O3 -Ofast -falign-functions=32 -ffat-lto-objects -flto=auto -fno-semantic-interposition -fstack-protector-strong -fzero-call-used-regs=used -march=x86-64-v3 -mprefer-vector-width=256 -mtune=skylake "
export CFLAGS="$CFLAGS -march=x86-64-v3 -m64"
export CXXFLAGS="$CXXFLAGS -march=x86-64-v3 -m64"
export FFLAGS="$FFLAGS -march=x86-64-v3 -m64"
export FCFLAGS="$FCFLAGS -march=x86-64-v3 -m64"
%cmake ..
make  %{?_smp_mflags}
popd

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
cd clr-build; make test
cd ../clr-build-avx2;
make test || :

%install
export SOURCE_DATE_EPOCH=1633758035
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/LibVNCServer
cp %{_builddir}/libvncserver-LibVNCServer-0.9.13/COPYING %{buildroot}/usr/share/package-licenses/LibVNCServer/ab8577d3eb0eedf3f98004e381a9cee30e7224e1
pushd clr-build-avx2
%make_install_v3  || :
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot}/usr/share/clear/optimized-elf/ %{buildroot}/usr/share/clear/filemap/filemap-%{name}
popd
pushd clr-build
%make_install
popd

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/include/rfb/keysym.h
/usr/include/rfb/rfb.h
/usr/include/rfb/rfbclient.h
/usr/include/rfb/rfbconfig.h
/usr/include/rfb/rfbproto.h
/usr/include/rfb/rfbregion.h
/usr/include/rfb/threading.h
/usr/lib64/libvncclient.so
/usr/lib64/libvncserver.so
/usr/lib64/pkgconfig/libvncclient.pc
/usr/lib64/pkgconfig/libvncserver.pc

%files filemap
%defattr(-,root,root,-)
/usr/share/clear/filemap/filemap-LibVNCServer

%files lib
%defattr(-,root,root,-)
/usr/lib64/libvncclient.so.0.9.13
/usr/lib64/libvncclient.so.1
/usr/lib64/libvncserver.so.0.9.13
/usr/lib64/libvncserver.so.1
/usr/share/clear/optimized-elf/lib*

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/LibVNCServer/ab8577d3eb0eedf3f98004e381a9cee30e7224e1
