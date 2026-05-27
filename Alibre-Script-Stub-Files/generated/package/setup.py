from setuptools import setup


def readme():
    try:
        with open("README.md", "r") as f:
            return f.read()
    except IOError:
        return ""


setup(
    name="alibrescript-ide-stubs",
    version="0.1.0",
    description="Authoring-only IDE stubs for Alibre Script IronPython 2.7.10",
    long_description=readme(),
    long_description_content_type="text/markdown",
    author="Alibre Script API Text contributors",
    url="https://github.com/stephensmitchell/AlibreScript",
    project_urls={"Source": "https://github.com/stephensmitchell/AlibreScript"},
    license="MIT",
    packages=["AlibreScript"],
    package_data={"AlibreScript": ["__init__.pyi", "py.typed"]},
    include_package_data=True,
    zip_safe=False,
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: Implementation :: IronPython",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Typing :: Stubs Only",
    ],
)
