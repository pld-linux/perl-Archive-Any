#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Archive
%define	pnam	Any
Summary:	Archive::Any - Single interface to deal with zips and tarballs
Summary(pl):	Archive::Any - wspólny interfejs do obs³ugi archiwów zip i tar
Name:		perl-Archive-Any
Version:	0.06
Release:	1
License:	unknown
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	85cb1a7f4a79152ee59396dda4134328
%if %{with tests}
BuildRequires:	perl-Archive-Tar >= 1.07
BuildRequires:	perl-Archive-Zip >= 1.07
BuildRequires:	perl-Class-Virtual
BuildRequires:	perl(Class::Virtually::Abstract) >= 0.02
BuildRequires:	perl-Test-Simple >= 0.11
%endif
BuildRequires:	perl-devel >= 5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module is a single interface for manipulating different archive
formats.  Tarballs, zip files, etc...

%description -l pl
Ten modu³ to wspólny interfejs do obrabiania archiwów w ró¿nych
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
%{perl_vendorlib}/%{pdir}/*.pm
%{perl_vendorlib}/%{pdir}/%{pnam}
%{_mandir}/man3/*
