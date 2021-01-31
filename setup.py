import pathlib
from setuptools import setup, find_packages


HERE = pathlib.Path(__file__).parent
README = (HERE / "README.md").read_text()

install_requires = [
            'ujson>=3.0.0',
            'uvloop>=0.14.0',
            'aiofiles>=0.5.0',
            'numpy>=1.19.1'
        ]


from my_happy_python_utils import version

setup(
  name="my-happy-python-utils",
  version=version.get_current(),
  description="Python Utils is based on Python3.7.",
  long_description=README,
  long_description_content_type="text/markdown",
  license="Apache 2",
  url="https://github.com/ggservice007/my-happy-python-utils",
  author="ggservice007",
  author_email="ggservice007@126.com",
  packages=find_packages(exclude=[""]),
  install_requires=install_requires,
  include_package_data=True,
  zip_safe=False,
  python_requires=">=3.7.7"
)
