%global octpkg control

Summary:	Additional Octave control tools
Name:		octave-%{octpkg}
Version:	3.4.0
Release:	1
Source0:	http://downloads.sourceforge.net/octave/%{octpkg}-%{version}.tar.gz
# https://savannah.gnu.org/bugs/?61205
Patch0:		lapack-3.10.0.patch
License:	GPLv3+
Group:		Sciences/Mathematics
Url:		https://octave.sourceforge.io/%{octpkg}/

BuildRequires:	octave-devel >= 4.0.0
BuildRequires:	gcc-gfortran

Requires:	octave(api) = %{octave_api}

Requires(post): octave
Requires(postun): octave

%description
Computer-Aided Control System Design (CACSD) Tools for GNU Octave,
based on the proven SLICOT Library.

This package is part of community Octave-Forge collection.

%files
%license COPYING
%doc NEWS
%dir %{octpkglibdir}
%{octpkglibdir}/*
%dir %{octpkgdir}
%{octpkgdir}/*

#---------------------------------------------------------------------------

%prep
%autosetup -p1 -n %{octpkg}-%{version}

# remove backup files
find . -name \*~ -delete

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

