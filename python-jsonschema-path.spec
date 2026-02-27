Name:		python-jsonschema-path
Version:	0.4.3
Release:	1
Source0:	https://files.pythonhosted.org/packages/source/j/jsonschema_path/jsonschema_path-%{version}.tar.gz
Summary:	JSONSchema Spec with object-oriented paths
URL:		https://pypi.org/project/jsonschema_path/
License:	Apache-2.0
Group:		Development/Python
BuildRequires:	python%{pyver}dist(poetry-core)
BuildSystem:	python
BuildArch:	noarch

%description
JSONSchema Spec with object-oriented paths

%files
%{py_sitedir}/jsonschema_path
%{py_sitedir}/jsonschema_path-*.*-info
