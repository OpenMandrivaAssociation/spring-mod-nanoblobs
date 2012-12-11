%define oversion 065

Summary:	Nanoblobs mod for Spring
Name:		spring-mod-nanoblobs
Version:	0.65
Release:	%{mkrel 2}
Group:		Games/Strategy
URL:		http://spring.clan-sy.com/wiki/Nanoblobs
# zip file:
Source:		http://www.wolfegames.com/TA_Section/PreRelease/NanoBlobs%{oversion}.sdz
License:	GPL+
BuildRoot:	%{_tmppath}/%{name}-root
Requires:	spring
Conflicts:	spring-data < 0.75
BuildArch:	noarch

%description
Nanoblobs game for the Spring game engine. See
http://spring.clan-sy.com/wiki/Nanoblobs for a description of Nanoblobs
and some tips on how best to play it.

%prep
# We extract the archive to put the license file in docdir.
%setup -q -c

%install
rm -rf %{buildroot}
install -d -m755 %{buildroot}%{_gamesdatadir}/spring/mods
install -m644 %{SOURCE0} %{buildroot}%{_gamesdatadir}/spring/mods

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc License.txt
%{_gamesdatadir}/spring/mods/NanoBlobs%{oversion}.sdz



%changelog
* Sun Sep 20 2009 Thierry Vignaud <tvignaud@mandriva.com> 0.65-2mdv2010.0
+ Revision: 445208
- rebuild

* Sun Dec 14 2008 Adam Williamson <awilliamson@mandriva.org> 0.65-1mdv2009.1
+ Revision: 314121
- *LICENSE no longer exist...
- clean up the spec a bit
- new release 0.65

* Sat Jan 05 2008 Anssi Hannula <anssi@mandriva.org> 0.64-1mdv2008.1
+ Revision: 145686
- initial Mandriva release

