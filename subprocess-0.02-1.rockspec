package = "subprocess"
version = "0.3.0"
source = {
  url = "git://github.com/trinity-labs/lua5.4-subprocess.git"
}
description = {
  summary = "Subprocess module for Lua",
  detailed = [[
  ]],
  homepage = "https://github.com/xlq/lua-subprocess",
  license = "?"
}
dependencies = {
  "lua >= 5.4"
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
