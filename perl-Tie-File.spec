#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Tie
%define	pnam	File
Summary:	Tie::File - access the lines of a disk file via a Perl array
Summary(pl):	Tie::File - udostêpnienie wierszy pliku na dysku jako tablicy perlowej
Name:		perl-Tie-File
Version:	0.96
Release:	1
# same as perl (but i.e. GPL v2+ or Artistic ???)
License:	GPL v2+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	1d7184e02a560afbc7a9eafffc80f44c
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Tie::File represents a regular text file as a Perl array. Each element
in the array corresponds to a record in the file. The first line of
the file is element 0 of the array; the second line is element 1, and
so on.

%description -l pl
Tie::File reprezentuje zwyk³y plik tekstowy jako perlow± tablicê.
Ka¿dy element tablicy odpowiada rekordowi z pliku. Pierwsza linia pliku
jest elementem 0. w tablicy, druga 1. i tak dalej.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{perl_vendorlib}/%{pdir}/*.pm
%{_mandir}/man3/*
