# rpmbuild-python-pybindxml

Create a python-pybindxml RPM for RHEL/CentOS.

## Requirements

To download package sources and install build dependencies

    yum -y install rpmdevtools yum-utils

## Build process

To build the package follow the steps outlined below

    git clone https://github.com/linuxhq/rpmbuild-python-pybindxml.git rpmbuild
    mkdir rpmbuild/SOURCES
    spectool -g -R rpmbuild/SPECS/python-pybindxml.spec
    yum-builddep rpmbuild/SPECS/python-pybindxml.spec
    rpmbuild -ba rpmbuild/SPECS/python-pybindxml.spec

## License

BSD

## Author Information

This package was created by [Taylor Kimball](http://www.linuxhq.org).
