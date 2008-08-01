%define	name	pork
%define	version	0.99.8.1
%define	release %mkrel 4

Summary:	A ncurses-based AIM client
Name:		%{name}
Version:	%{version}
Release:	%{release}
License:	GPL
Group:		Networking/Instant messaging
Source0:	http://prdownloads.sourceforge.net/ojnk/%{name}-%{version}.tar.bz2
URL:		http://ojnk.sourceforge.net/
BuildRequires:	ncurses-devel perl-devel gpm-devel
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%define _provides_exceptions perl(Calendar)

%description
pork is an ncurses-based AOL instant messenger client. It uses the
OSCAR protocol (the one the windows client uses) to access AIM. Pork
features Perl scripting; an online help system; the ability to
configure nearly all aspects of the program's look-and-feel; an alias
system; and a powerful, fully-configurable key binding system. It
supports being logged in with more than one screen name at the same
time. The default look-and-feel of the client is modeled after the
ircII IRC client. Anyone comfortable using ircII (or any clients
derived from it -- e.g., epic, BitchX, etc.) will feel comfortable using
pork.

%prep
%setup -q

%build
%configure2_5x
%make

%install
%{__rm} -rf $RPM_BUILD_ROOT
%makeinstall
%{__install} doc/%{name}.1 -D $RPM_BUILD_ROOT%{_mandir}/man1/%{name}.1

%clean
%{__rm} -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS QUICK_START README STYLE TODO
%{_datadir}/%{name}
%{_mandir}/man1/%{name}*
%defattr(755,root,root,755)
%{_bindir}/%{name}

