Summary:	CVS queued
Summary(pl):	Kolejka do CVS
Name:		cvsq
Version:	0.4.0
Release:	1
Copyright:	Free
Group:		Development/Version Control
Group(de):	Entwicklung/Versionkontrolle
Group(pl):	Programowanie/Zarz�dzanie wersjami
Source0:	%{name}-%{version}.tar.gz
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

%description -l pl
cvsq oznacza kolejkowanie cvs-a i jest narz�dziem pozwalaj�cym
programistom z wdzwanianym dost�pem do Internetu na w miar�
bezstresow� prac� z repozytorium. cvsq przyjmuje te same parametry co
cvs, ale zamiast bezzw�ocznie reagowa�, umieszcza wszystkie polecenia
w kolejce dla p�niejszego przetworzenia.

W ten spos�b mo�na przyk�adowo zaznaczy� kilka plik�w do umieszczenia
w repozytorium, a przes�a� je dopiero po uzyskaniu po��czenia z
sieci�.

%prep
%setup -q

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}

install %{name} $RPM_BUILD_ROOT%{_bindir}

gzip -9nf AUTHORS ChangeLog README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_bindir}/*
