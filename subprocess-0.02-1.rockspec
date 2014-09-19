package = "subprocess"
version = "0.02-1"
source = {
  url = "git://github.com/mildred/lua-subprocess.git"
}
description = {
  summary = "Subprocess module for Lua",
  detailed = [[
  ]],
  homepage = "https://github.com/xlq/lua-subprocess",
  license = "?"
}
dependencies = {
  "lua >= 5.2"
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
