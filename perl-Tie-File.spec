#
# Conditional build:
%bcond_without	tests	# do not perform "make test"

%define		pdir	Tie
%define		pnam	File
Summary:	Tie::File - access the lines of a disk file via a Perl array
Summary(pl.UTF-8):	Tie::File - udostępnienie wierszy pliku na dysku jako tablicy perlowej
Name:		perl-Tie-File
Version:	0.98
Release:	1
# same as perl (but i.e. GPL v2+ or Artistic ???)
License:	GPL v2+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	33c6c213ba45452f2aeb0e85c6473ecf
URL:		http://search.cpan.org/dist/Tie-File/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Tie::File represents a regular text file as a Perl array. Each element
in the array corresponds to a record in the file. The first line of
the file is element 0 of the array; the second line is element 1, and
so on.

%description -l pl.UTF-8
Tie::File reprezentuje zwykły plik tekstowy jako perlową tablicę.
Każdy element tablicy odpowiada rekordowi z pliku. Pierwsza linia
pliku jest elementem 0. w tablicy, druga 1. i tak dalej.

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
