#
# Conditional build:
# _without_tests - do not perform "make test"
%include	/usr/lib/rpm/macros.perl
%define	pdir	Tie
%define	pnam	File
Summary:	Tie::File - Access the lines of a disk file via a Perl array
Summary(pl):	Modu³ Tie::File - udostêpniaj±cy linie pliku na dysku jako perlow± tablicê
Name:		perl-Tie-File
Version:	0.93
Release:	2
License:	GPL v2+/Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	perl >= 5.6
BuildRequires:	rpm-perlprov >= 4.0.2-104
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Tie::File represents a regular text file as a Perl array. Each element
in the array corresponds to a record in the file. The first line of
the file is element 0 of the array; the second line is element 1, and
so on.

%description -l pl
Tie::File reprezentuje zwyk³y plik tekstowy jako perlow± tablicê.
Ka¿dy element tablicy odpowiada rekordowi z pliku. Piersza linia pliku
jest elementem 0. w tablicy, druga 1. i tak dalej.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL
%{__make}

%{!?_without_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{perl_sitelib}/%{pdir}/*.pm
%{_mandir}/man3/*
