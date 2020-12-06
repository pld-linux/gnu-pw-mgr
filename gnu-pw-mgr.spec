Summary:	GNU Password and Security Questions Manager
Summary(pl.UTF-8):	GNU Password Manager - zarządca haseł i pytań bezpieczeństwa
Name:		gnu-pw-mgr
Version:	2.7.4
Release:	1
License:	GPL v3+
Group:		Development/Tools
Source0:	https://ftp.gnu.org/gnu/gnu-pw-mgr/%{name}-%{version}.tar.xz
# Source0-md5:	62c9e10e5b9b6226c7be9b1587dc2145
Patch0:		%{name}-info.patch
URL:		http://www.gnu.org/software/gnu-pw-mgr/
BuildRequires:	tar >= 1:1.22
BuildRequires:	texinfo >= 4.8
BuildRequires:	xz
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This program is designed to make it easy to reconstruct difficult
passwords when they are needed while limiting the risk of attack. The
user of this program inputs a self-defined transformation of a web
site URL and obtains the password and user name hint for that web
site. You must, however, be able to remember this password id, or the
password is lost forever.

%description -l pl.UTF-8
Ten program jest zaprojektowany, aby ułatwić rekonstrukcję trudnych
haseł, gdy są potrzebne, ograniczając ryzyko ataku. Użytkownik
programu wprowadza zdefiniowane przez siebie przekształcenie adresu
URL strony WWW i otrzymuje podpowiedź hasła i nazwy użytkownika dla
tej strony. Trzeba jednak być w stanie zapamiętać ten identyfikator
hasła, albo hasło zostanie utracone na zawsze.

%prep
%setup -q
%patch0 -p1

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/postshell
-/usr/sbin/fix-info-dir -c %{_infodir}

%postun	-p /sbin/postshell
-/usr/sbin/fix-info-dir -c %{_infodir}

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS
%attr(755,root,root) %{_bindir}/gnu-pw-mgr
%attr(755,root,root) %{_bindir}/sort-pw-cfg
%{_infodir}/gnu-pw-mgr.info*
%{_mandir}/man1/gnu-pw-mgr.1*
%{_mandir}/man1/sort-pw-cfg.1*
