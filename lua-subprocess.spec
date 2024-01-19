Name:       lua-subprocess
Source0:    subprocess.rockspec
Release:    1
BuildRequires: pkgconfig(lua)
BuildRequires: make
BuildRequires: gcc

%{lua:
dofile(rpm.expand('%SOURCE0'));
print (
'Version: ' .. version .. "\n" ..
'URL: ' .. source.url .. "\n" ..
'Summary: ' .. description.summary .. "\n" ..
'License: ' .. description.license .. "\n");

sources = build.modules.subprocess.sources;
l = #sources
i = 0
while i < l do
    i = i + 1;
    val = sources[i];
    print('Source' .. i .. ': ' .. val .. "\n");
end

}

%description
%{lua:
print(description.detailed);
}

%prep
dir=%{_builddir}/lua-subprocess
mkdir -p "$dir"
cd "$dir"

%{lua:
i = 0;

while i < l do
    i = i + 1;
    src = rpm.expand('%SOURCE'..i);
    print('cp '..src..' $dir ;');
end
}

%build
%{make_build}

%install
%{make_install}

%files
/usr/*
