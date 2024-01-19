package = "subprocess"
version = "0.5.5"
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
  "lua >= 5.4"
}
build = {
  type = "builtin",
  modules = {
    ["subprocess"] = {
      sources = {"subprocess.c", "liolib-copy.c", "liolib-copy.h"},
      defines = {"OS_POSIX"}
    }
  }
}
