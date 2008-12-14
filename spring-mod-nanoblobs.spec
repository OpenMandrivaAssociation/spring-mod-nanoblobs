%define oversion 065

Summary:	Nanoblobs mod for Spring
Name:		spring-mod-nanoblobs
Version:	0.65
Release:	%{mkrel 1}
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

