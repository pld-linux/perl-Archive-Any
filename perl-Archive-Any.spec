#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%define		pdir	Archive
%define		pnam	Any
Summary:	Archive::Any - Single interface to deal with zips and tarballs
Summary(pl.UTF-8):	Archive::Any - wspólny interfejs do obsługi archiwów zip i tar
Name:		perl-Archive-Any
Version:	0.0945
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Archive/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	7b964434c52a78a3df7bd16a75085e8e
URL:		http://search.cpan.org/dist/Archive-Any/
%if %{with tests}
BuildRequires:	perl-Archive-Tar >= 1.07
BuildRequires:	perl-Archive-Zip >= 1.07
BuildRequires:	perl-File-MMagic >= 1.27
BuildRequires:	perl-MIME-Types >= 1.16
BuildRequires:	perl-Module-Find >= 0.05
BuildRequires:	perl-Test-Perl-Critic
BuildRequires:	perl-Test-Pod-Coverage
BuildRequires:	perl-Test-Simple >= 0.40
BuildRequires:	perl-Test-Warn
%endif
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
Requires:	perl-Archive-Tar >= 1.07
Requires:	perl-Archive-Zip >= 1.07
Requires:	perl-File-MMagic >= 1.27
Requires:	perl-MIME-Types >= 1.16
Requires:	perl-Module-Find >= 0.05
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module is a single interface for manipulating different archive
formats. Tarballs, zip files, etc...

%description -l pl.UTF-8
Ten moduł to wspólny interfejs do obrabiania archiwów w różnych
formatach: tar, zip itp.

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
%doc Changes
%{perl_vendorlib}/Archive/Any.pm
%{perl_vendorlib}/Archive/Any
%{_mandir}/man3/*
