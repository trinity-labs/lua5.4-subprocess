#!/bin/sh
modname=subprocess
name=lua-$modname
files="$(make print-DISTFILES) $name.spec $modname.rockspec"
mkdir $name
ln $files $name
tar -czvf $name.tar.gz $name
