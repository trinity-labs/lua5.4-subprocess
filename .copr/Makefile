outdir ?= $(shell rpm --eval '%{_srcrpmdir}')

srpm:
	dnf install -y tar sed coreutils grep ||:
	bash -x .copr/main.sh
	rpmbuild -D'%_srcrpmdir $(outdir)' -D'_sourcedir .' -bs *.spec
