Summary: mawk - pattern scanning and text processing language
%define AppProgram mawk
%define AppVersion 1.3.4
%define AppRelease 20121129
# $MawkId: mawk.spec,v 1.20 2012/11/28 20:44:12 tom Exp $
Name: %{AppProgram}
Version: %{AppVersion}
Release: %{AppRelease}
License: GPLv2
Group: Applications/Development
URL: ftp://invisible-island.net/%{AppProgram}
Source0: %{AppProgram}-%{AppVersion}-%{AppRelease}.tgz
Packager: Thomas Dickey <dickey@invisible-island.net>

%description
mawk is an interpreter for the AWK Programming Language.  The AWK language is
useful for manipulation of data files, text retrieval and processing, and for
prototyping and experimenting with algorithms.

%prep

%define debug_package %{nil}
%setup -q -n %{AppProgram}-%{AppVersion}-%{AppRelease}

%build

INSTALL_PROGRAM='${INSTALL}' \
	./configure \
		--target %{_target_platform} \
		--prefix=%{_prefix} \
		--bindir=%{_bindir} \
		--libdir=%{_libdir} \
		--mandir=%{_mandir}

make

%install
[ "$RPM_BUILD_ROOT" != "/" ] && rm -rf $RPM_BUILD_ROOT

make install                    DESTDIR=$RPM_BUILD_ROOT

strip $RPM_BUILD_ROOT%{_bindir}/%{AppProgram}

%clean
[ "$RPM_BUILD_ROOT" != "/" ] && rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%{_prefix}/bin/%{AppProgram}
%{_mandir}/man1/%{AppProgram}.*

%changelog
# each patch should add its ChangeLog entries here

* Sat Oct 27 2012 Thomas Dickey
- cancel any debug-rpm

* Sun Jun 21 2010 Thomas Dickey
- initial version
