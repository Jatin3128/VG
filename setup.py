from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in vg_custom/__init__.py
from vg_custom import __version__ as version

setup(
	name="vg_custom",
	version=version,
	description="for testing",
	author="j",
	author_email="j",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
