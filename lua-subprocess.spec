Name:       lua-subprocess
Source0:    lua-subprocess.tar.gz
Release:    0

BuildRequires: pkgconfig(lua)
BuildRequires: rpm_macro(lua_libdir)
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
BuildArch: noarch

%description doc
%{summary}.

%prep
%setup -n lua-subprocess

%build
make

%install
INSTALL_CMD=%{lua_libdir} %{make_install}
mkdir -p %{buildroot}%{_datadir}/doc/lua-subprocess/
cp subprocess.html subprocess.txt %{buildroot}%{_datadir}/doc/lua-subprocess/

%files
%lua_libdir/*

%files doc
%{_datadir}/doc/lua-subprocess/*
