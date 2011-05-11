#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%define		pdir	Hash
%define		pnam	MultiValue
%include	/usr/lib/rpm/macros.perl
Summary:	Hash::MultiValue - Store multiple values per key
#Summary(pl.UTF-8):	
Name:		perl-Hash-MultiValue
Version:	0.08
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Hash/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	d8e2ae6a0685d52641b3a5de20ae4116
# generic URL, check or change before uncommenting
#URL:		http://search.cpan.org/dist/Hash-MultiValue/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Hash::MultiValue is an object (and a plain hash reference) that may
contain multiple values per key, inspired by MultiDict of WebOb.



# %description -l pl.UTF-8
# TODO

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/Hash/*.pm
%{_mandir}/man3/*
