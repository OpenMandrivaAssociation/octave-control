%global octpkg control

Summary:	Additional Octave control tools
Name:		octave-control
Version:	4.1.0
Release:	1
License:	GPLv3+
Group:		Sciences/Mathematics
#Url:		https://packages.octave.org/control/
Url:		https://github.com/gnu-octave/pkg-control
Source0:	https://github.com/gnu-octave/pkg-control/releases/download/control-%{version}/control-%{version}.tar.gz
Patch0:		octave-control-3.6.0_fix_metainfo.patch

BuildRequires:  octave-devel >= 4.0.0
BuildRequires:	gcc-gfortran
BuildRequires:	gomp-devel

Requires:	octave(api) = %{octave_api}

Requires(post): octave
Requires(postun): octave

%description
Computer-Aided Control System Design (CACSD) Tools for GNU Octave, 
based on the proven SLICOT Library.

%files
%license COPYING
%doc NEWS
%dir %{octpkgdir}
%{octpkgdir}/*
%dir %{octpkglibdir}
%{octpkglibdir}/*
%{_metainfodir}/*.metainfo.xml

#---------------------------------------------------------------------------

%prep
%autosetup -p1 -n %{octpkg}-%{version}

%build
# fortran modules don't link if clang is used
export CC=gcc
export CXX=g++

%set_build_flags
%octave_pkg_build

%install
%octave_pkg_install

%check
%octave_pkg_check

%post
%octave_cmd pkg rebuild

%preun
%octave_pkg_preun

%postun
%octave_cmd pkg rebuild

