Summary:	CVS queued
Summary(pl):	Kolejka do CVS
Name:		cvsq
Version:	0.4.2
Release:	1
License:	Public Domain
Group:		Development/Version Control
Source0:	http://www.volny.cz/v.slavik/lt/download/%{name}-%{version}.tar.gz
# Source0-md5:	d6d600db7a98ede407e25204799fbd27
URL:		http://www.volny.cz/v.slavik/lt/cvsq.html
BuildArch:	noarch
Requires:	cvs
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
cvsq stands for "CVS queued" and it's a tool that enables developers
with dial-up connection to work comfortably with CVS. It accepts same
arguments as CVS but instead of directly processing them, cvsq stores
all requests in a queue and handles them later

This way, you can mark several files for commit and upload them to the
server later, when you're connected to the net.

Try to install package "color", you will get colored cvsq output!

%description -l pl
cvsq oznacza kolejkowanie cvs-a i jest narzêdziem pozwalaj±cym
programistom z wdzwanianym dostêpem do Internetu na w miarê
bezstresow± pracê z repozytorium. cvsq przyjmuje te same parametry co
cvs, ale zamiast bezzw³ocznie reagowaæ, umieszcza wszystkie polecenia
w kolejce dla pó¼niejszego przetworzenia.

W ten sposób mo¿na przyk³adowo zaznaczyæ kilka plików do umieszczenia
w repozytorium, a przes³aæ je dopiero po uzyskaniu po³±czenia z
sieci±.

Zainstaluj pakiet "color", komunikaty cvsq bêd± kolorowe!

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
