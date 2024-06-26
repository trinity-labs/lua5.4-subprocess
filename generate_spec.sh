generate='lua2pack generate --rockspec stdin:// --template '
cat << 'EOF' | tee >($generate 'generic.spec') >($generate 'rock.rockspec')
package = "subprocess"
version = "0.5.5-1"
source = {
  url = "git://github.com/huakim/lua-subprocess.git"
}
description = {
  summary = "Subprocess module for Lua",
  detailed = [[
  ]],
  homepage = "https://github.com/huakim/lua-subprocess",
  license = "LGPL"
}
dependencies = {
  "lua >= 5.1"
}
build = {
  type = "builtin",
  modules = {
    ["subprocess"] = {
      sources = {"subprocess.c", "liolib-copy.c"},
      defines = {"OS_POSIX"}
    }
  }
}
EOF
