import setuptools

with open("rasa_metaform/version.py") as f:
    exec(f.read())

with open("README.md") as f:
    long_description = f.read()

setuptools.setup(
    name="rasa_metaform",
    version=__version__,
    packages=setuptools.find_packages(exclude=["tests"]),
    install_requires=["pyyaml>=5.1.2", "rasa-sdk>=1.3.2"],
    include_package_data=True,
    description="Create a Rasa form from a YAML file",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/magnetcoop/rasa-metaform",
    project_urls={
        "Bug Reports": "https://github.com/magnetcoop/rasa-metaform/issues",
        "Source": "https://github.com/magnetcoop/rasa-metaform",
    },
    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "License :: OSI Approved :: Apache Software License",
    ],
    author="Magnet S Coop.",
    author_email="info@magnet.coop",
    maintainer="Kamil Hryniewicz",
    maintainer_email="kamil@magnet.coop",
)
