%define module jsonschema_path

Name:		python-jsonschema-path
Version:	0.4.5
Release:	1
Summary:	JSONSchema Spec with object-oriented paths
License:	Apache-2.0
Group:		Development/Python
URL:		https://pypi.org/project/jsonschema_path/
Source0:	https://files.pythonhosted.org/packages/source/j/%{module}/%{module}-%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildSystem:	python
BuildRequires:	python%{pyver}dist(pip)
BuildRequires:	python%{pyver}dist(poetry-core)
BuildRequires:	python%{pyver}dist(wheel)
BuildArch:	noarch

%description
JSONSchema Spec with object-oriented paths

%files
%{py_sitedir}/%{module}
%{py_sitedir}/%{module}-%{version}.dist-info
