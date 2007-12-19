Summary:	CVS queued
Summary(pl.UTF-8):	Kolejka do CVS
Name:		cvsq
Version:	0.4.4
Release:	1
License:	Public Domain
Group:		Development/Version Control
Source0:	http://dl.sourceforge.net/cvsq/%{name}-%{version}.tar.gz
# Source0-md5:	10efc297780c1a5cdbdc0585afaa8a5e
URL:		http://sourceforge.net/projects/cvsq
Requires:	cvs-client
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
cvsq stands for "CVS queued" and it's a tool that enables developers
with dial-up connection to work comfortably with CVS. It accepts same
arguments as CVS but instead of directly processing them, cvsq stores
all requests in a queue and handles them later

This way, you can mark several files for commit and upload them to the
server later, when you're connected to the net.

%description -l pl.UTF-8
cvsq oznacza kolejkowanie cvs-a i jest narzędziem pozwalającym
programistom z wdzwanianym dostępem do Internetu na w miarę
bezstresową pracę z repozytorium. cvsq przyjmuje te same parametry co
cvs, ale zamiast bezzwłocznie reagować, umieszcza wszystkie polecenia
w kolejce dla późniejszego przetworzenia.

W ten sposób można przykładowo zaznaczyć kilka plików do umieszczenia
w repozytorium, a przesłać je dopiero po uzyskaniu połączenia z
siecią.

%prep
%setup -q

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}

install %{name} $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README
%attr(755,root,root) %{_bindir}/*
