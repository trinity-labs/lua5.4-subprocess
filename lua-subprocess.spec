Name:       lua-subprocess
Source0:    lua-subprocess.tar.gz
Release:    2

BuildRequires: pkgconfig(lua)
BuildRequires: make
BuildRequires: gcc

%{lua:
load(io.popen('tar -axf '..rpm.expand('%{SOURCE0}')..' lua-subprocess/subprocess.rockspec -O'):read('*a'))();
print(
'Version: '..version.."\n"..
'Summary: '..description.summary.."\n"..
'URL: '..description.homepage.."\n"..
'License: '..description.license.."\n"
);
}

%description
%{lua:
print(description.detailed);
}

%package doc
Summary: Documentary files for lua-subprocess

%description doc
%{summary}.

%prep
%setup -n lua-subprocess

%build
make

%install
%{make_install}
mkdir -p %{buildroot}%{_datadir}/doc/lua-subprocess/
cp subprocess.html subprocess.txt %{buildroot}%{_datadir}/doc/lua-subprocess/

%files
%{_libdir}/lua

%files doc
%{_datadir}/doc/lua-subprocess/*
