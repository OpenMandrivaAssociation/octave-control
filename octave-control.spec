%global octpkg control

# For now -- since C code (built with clang) and
# Fortran code (built with gfortran) are linked
# together, LTO object files don't work
%global _disable_lto 1

%bcond use_external_slicot	0

Summary:	Additional Octave control tools
Name:		octave-control
Version:	4.1.0
Release:	1
License:	GPLv3+
Group:		Sciences/Mathematics
#Url:		https://packages.octave.org/control/
Url:		https://github.com/gnu-octave/pkg-control
Source0:	https://github.com/gnu-octave/pkg-control/releases/download/control-%{version}/control-%{version}.tar.gz
Patch0:		of-control-2-octave-9-compat.patch
# (debian)
%if %{with use_external_slicot}
Patch10:	use-external-slicot.patch
%endif
BuildRequires:  octave-devel >= 4.0.0
BuildRequires:	gcc-gfortran
BuildRequires:	gomp-devel
%if %{with use_external_slicot}
BuildRequires:	slicot-devel
%endif

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

# remove external libs
%if %{with use_external_slicot}
rm -fr src/slicot
%endif

%build
export FC=gfortran
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

