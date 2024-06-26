#!/bin/sh
modname=subprocess
name=lua-$modname
files="$(make print-DISTFILES) $modname.rockspec"
bash ./generate_spec.sh
mkdir $name
ln $files $name
tar -czvf $name.tar.gz $name
