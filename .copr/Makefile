srpm:
	dnf -y install sanlock-devel \
		gcc \
		git \
		python3-devel \
		python3-pip \
		python3-setuptools

	$(eval VERSION := $(shell grep '^Version:' python-sanlock.spec | sed 's/Version: *//'))
	git config --global --add safe.directory "$$(pwd)"
	mkdir -p build/{BUILD,RPMS,SOURCES,SRPMS}
	git archive --format=tar.gz \
		--prefix=python-sanlock-$(VERSION)/ \
		--output=build/SOURCES/python-sanlock-$(VERSION).tar.gz \
		HEAD
	rpmbuild -bs python-sanlock.spec \
		--define "_topdir $$(pwd)/build"
	cp build/SRPMS/*.src.rpm $(outdir)/
