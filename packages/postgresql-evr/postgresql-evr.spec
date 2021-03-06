%if 0%{?rhel} <= 7
%global scl rh-postgresql12
%endif

%{?scl:%scl_package postgresql-evr}
%{!?scl:%global pkg_name %{name}}

%global debug_package %{nil}

Name:		%{?scl_prefix}postgresql-evr
Version:	0.0.2
Release:	1%{?dist}
Summary:	RPM evr extension for PostgreSQL

Group:    	Applications/System
License:	GPLv3

BuildRequires: %{?scl_prefix}postgresql-devel
%{?scl:BuildRequires: %{?scl_prefix}runtime}

%if 0%{?rhel} > 7
BuildRequires: postgresql-server-devel
%endif

Requires: %{?scl_prefix}postgresql-server
%{?scl:Requires: %{?scl_prefix}runtime}

ExclusiveArch: x86_64
URL: https://github.com/Katello/postgresql-evr
Source0: https://codeload.github.com/Katello/postgresql-evr/tar.gz/%{version}#/postgresql-evr-%{version}.tar.gz

%description
Installs files required to create evr extension in PostgreSQL.

%prep
%autosetup -p1 -n postgresql-evr-0.0.2

%build


%install
rm -rf $RPM_BUILD_ROOT
%{?scl:scl enable %{scl} - <<EOF}
%make_install
%{?scl:EOF}


%files

%{_datadir}/pgsql/extension/evr.control
%{_datadir}/pgsql/extension/evr--0.0.2.sql


%changelog
* Mon Apr 13 2020 ianballou <ianballou67@gmail.com> 0.0.2-1
- remove superuser requirement

* Mon Mar 09 2020 Justin Sherrill <jsherril@redhat.com> 0.0.1-2
- do not build a debug package on el8

* Mon Mar 02 2020 Ian Ballou <ianballou67@gmail.com> - 0.0.1-1
- postgresql-evr initial creation
