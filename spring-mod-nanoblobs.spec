
%define name	spring-mod-nanoblobs
%define version	0.64
%define oversion 064
%define rel	1

Summary:	Nanoblobs mod for Spring
Name:		%{name}
Version:	%{version}
Release:	%mkrel %{rel}
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
Nanoblobs mod for Spring.

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
%doc *LICENSE.txt License.txt
%{_gamesdatadir}/spring/mods/NanoBlobs%{oversion}.sdz
