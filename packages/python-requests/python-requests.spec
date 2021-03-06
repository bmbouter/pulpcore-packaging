# Created by pyp2rpm-3.3.3
%global pypi_name requests

Name:           python-%{pypi_name}
Version:        2.24.0
Release:        1%{?dist}
Summary:        Python HTTP for Humans

License:        Apache 2.0
URL:            https://requests.readthedocs.io
Source0:        https://files.pythonhosted.org/packages/source/r/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools

%description
%{summary}

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}
Conflicts:      python3-urllib3 = 1.25.0
Conflicts:      python3-urllib3 = 1.25.1
Requires:       python3-certifi >= 2017.4.17
Requires:       python3-chardet < 4
Requires:       python3-chardet >= 3.0.2
Requires:       python3-cryptography >= 1.3.4
Requires:       python3-idna < 3
Requires:       python3-idna >= 2.5
Requires:       python3-pyOpenSSL >= 0.14
Requires:       python3-urllib3 < 1.26
Requires:       python3-urllib3 >= 1.21.1

%description -n python3-%{pypi_name}
%{summary}

%prep
%autosetup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%py3_build

%install
%py3_install

%files -n python3-%{pypi_name}
%license LICENSE
%doc README.md
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info

%changelog
* Mon Jul 20 2020 Evgeni Golov 2.24.0-1
- Update to 2.24.0

* Wed Mar 18 2020 Samir Jha 2.23.0-1
- Update to 2.23.0

* Fri Feb 28 2020 Zach Huntington-Meath <zhunting@redhat.com> - 2.22.0-2
- Bump release to build for el8

* Mon Nov 18 2019 Evgeni Golov - 2.22.0-1
- Initial package.
