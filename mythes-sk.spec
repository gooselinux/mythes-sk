Name: mythes-sk
Summary: Slovak thesaurus
%define upstreamid 20090907
Version: 0.%{upstreamid}
Release: 1%{?dist}
Source: http://www.sk-spell.sk.cx/thesaurus/download/OOo-Thesaurus2-sk_SK.zip
Group: Applications/Text
URL: http://www.sk-spell.sk.cx/thesaurus/
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires: python, perl
License: BSD
BuildArch: noarch

%description
Slovak thesaurus.

%prep
%setup -q -c

%build
for i in README_th_sk_SK_v2.txt; do
  tr -d '\r' < $i > $i.new
  touch -r $i $i.new
  mv -f $i.new $i
done

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/mythes
cp -p th_sk_SK_v2.* $RPM_BUILD_ROOT/%{_datadir}/mythes

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc README_th_sk_SK_v2.txt
%dir %{_datadir}/mythes
%{_datadir}/mythes/*

%changelog
* Tue Sep 08 2009 Caolan McNamara <caolanm@redhat.com> - 0.20090907-1
- latest version

* Sat Aug 08 2009 Caolan McNamara <caolanm@redhat.com> - 0.20090807-1
- latest version

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.20090707-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Sat Jul 11 2009 Caolan McNamara <caolanm@redhat.com> - 0.20090707-2
- tidy spec

* Wed Jul 08 2009 Caolan McNamara <caolanm@redhat.com> - 0.20090707-1
- latest version

* Mon Jun 08 2009 Caolan McNamara <caolanm@redhat.com> - 0.20090607-1
- latest version

* Thu Apr 02 2009 Caolan McNamara <caolanm@redhat.com> - 0.20090402-1
- latest version

* Tue Mar 03 2009 Caolan McNamara <caolanm@redhat.com> - 0.20090302-1
- latest version

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.20090202-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Tue Feb 03 2009 Caolan McNamara <caolanm@redhat.com> - 0.20090202-1
- latest version

* Mon Jan 05 2009 Caolan McNamara <caolanm@redhat.com> - 0.20090102-1
- latest version

* Thu Nov 27 2008 Caolan McNamara <caolanm@redhat.com> - 0.20081121-1
- latest version

* Thu Oct 16 2008 Caolan McNamara <caolanm@redhat.com> - 0.20081010-1
- latest version

* Wed Sep 10 2008 Caolan McNamara <caolanm@redhat.com> - 0.20080905-1
- latest version

* Wed Nov 28 2007 Caolan McNamara <caolanm@redhat.com> - 0.20050503-1
- initial version
