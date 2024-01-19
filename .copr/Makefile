outdir ?= $(shell rpm --eval '%{_srcrpmdir}')

srpm:
	dnf install -y tar sed coreutils grep ||:
	bash -x ./main.sh
	rpmbuild -D'%_srcrpmdir $(outdir)' -D'_sourcedir .' -bs *.spec
