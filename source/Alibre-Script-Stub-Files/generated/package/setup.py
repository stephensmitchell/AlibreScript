from setuptools import setup

setup(
    name="alibrescript-ide-stubs",
    version="6.1.0.0",
    description="Editor type stubs for the Alibre Script API",
    packages=["AlibreScript"],
    package_data={"AlibreScript": ["py.typed", "__init__.pyi"]},
    include_package_data=True,
    zip_safe=False,
    python_requires=">=3.6",
)
