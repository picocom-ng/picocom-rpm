Name:           picocom
Version:        4.0.3
Epoch:          1
Release:        1%{?dist}
Summary:        Minimal serial communications program

License:        GPLv2+
URL:            https://github.com/picocom-ng/picocom
Source0:        https://github.com/picocom-ng/picocom/releases/download/v%{version}/picocom-%{version}.tar.gz
BuildRequires:  make
BuildRequires:  gcc
BuildRequires:  libconfuse-devel

# for groupadd
Requires(pre):  shadow-utils

%description
picocom is a minimal dumb-terminal emulation program. It is designed to serve
as a simple, manual, serial configuration, testing, and debugging tool.

%prep
%autosetup

%build
make CC="%{__cc}" CFLAGS="$RPM_OPT_FLAGS" %{_smp_mflags} UUCP_LOCK_DIR=/run/lock/picocom

%install
mkdir -p $RPM_BUILD_ROOT%{_bindir}
mkdir -p $RPM_BUILD_ROOT%{_mandir}/man1
install -m 755 picocom $RPM_BUILD_ROOT%{_bindir}/
install -m 644 picocom.1 $RPM_BUILD_ROOT%{_mandir}/man1/
mkdir -p $RPM_BUILD_ROOT/run/lock/picocom

%pre
getent group dialout >/dev/null || groupadd -g 18 -r -f dialout
exit 0

%files
%doc LICENSE.txt README.md
%dir %attr(0775,root,dialout) /run/lock/picocom
%{_bindir}/picocom
%{_mandir}/man1/*

%changelog
* Wed Aug 23 2023 Lars Kellogg-Stedman <lars@oddbit.com> 4.0.3-1
- new package built with tito

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.1-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.1-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.1-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Jul 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.1-10
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Jul 18 2018 Kevin Fenzi <kevin@scrye.com> - 3.1-4
- Fix FTBFS by adding BuildRequires: gcc

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Feb 02 2018 Kevin Fenzi <kevin@scrye.com> - 3.1-1
- Update to 3.1. Fixes bug #1540966

* Sun Dec 31 2017 Kevin Fenzi <kevin@scrye.com> - 3.0-1
- Update to 3.0. Fixes bug #1529114

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Jan 09 2017 Kevin Fenzi <kevin@scrye.com> - 2.2-1
- Update to 2.2. Fixes bug #1411573

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.7-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.7-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.7-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sun Feb 03 2013 Kevin Fenzi <kevin@scrye.com> 1.7-1
- Update to 1.7. 
- Drop upstreamed patch

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sun Jan 29 2012 Scott Tsai <scottt.tw@gmail.com> 1.6-4
- Create subdirectories for lockfiles under /run/lock/picocom/ (RHBZ 732360)

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Aug 25 2010 Kevin Fenzi <kevin@tummy.com> - 1.6-1
- Upgrade to 1.6

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu Aug 28 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 1.4-6
- fix compile

* Thu Aug 28 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 1.4-5
- fix license tag

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 1.4-4
- Autorebuild for GCC 4.3

* Thu Oct 05 2006 Christian Iseli <Christian.Iseli@licr.org> 1.4-3
 - rebuilt for unwind info generation, broken in gcc-4.1.1-21

* Thu Sep 14 2006 Sean Reifschneider <jafo@tummy.com> 1.4-2
- Incorporating changes from Fedora Extras review from denis at poolshark
  dot org and panemade at gmail dot com.

* Wed Sep 13 2006 Sean Reifschneider <jafo@tummy.com> 1.4-1
- Initial RPM spec file.
