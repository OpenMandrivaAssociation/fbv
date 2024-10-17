%define debug_package	%{nil}

Summary:	Framebuffer image viewer
Name:		fbv
Version:	1.0b
Release:	5
License:	GPLv2+
Group:		Graphical desktop/Other
Url:		https://s-tech.elsat.net.pl/fbv
Source0:	http://s-tech.elsat.net.pl/fbv/%{name}-%{version}.tar.gz
#patch from alt-linux
Patch0:		fbv-nocenter.patch
Patch1: fbv-1.0b-features.h.patch
Patch2: fbv-1.0b-libpng15.patch
Patch3: giflib-5.1.patch

BuildRequires:	giflib-devel
BuildRequires:	jpeg-devel
BuildRequires:	pkgconfig(libpng)
BuildRequires:	pkgconfig(x11)
BuildRequires:	pkgconfig(zlib)
BuildRequires:	gcc-c++, gcc, gcc-cpp

%description
A simple program to view pictures on a framebuffer console. It
supports PNG, JPEG, GIF and BMP files.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p2
%patch3 -p1


iconv -f iso8859-1 -t utf-8 ChangeLog > ChangeLog.conv && \
	mv -f ChangeLog.conv ChangeLog

%build
export CC=gcc
export CXX=g++

./configure \
	--prefix=%{_prefix} \
	--mandir=%{_mandir}

#sed -i 's|LIBS.*|LIBS=-lpng -ljpeg -lungif -lgif|' Make.conf
#sed -i 's|setjmp(png_ptr->jmpbuf)|setjmp(png_jmpbuf(png_ptr))|' png.c

%make CFLAGS="%{optflags}"

%install
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_mandir}/man1

%makeinstall_std

%files
%doc ChangeLog README TODO
%{_bindir}/*
%{_mandir}/man1/*
