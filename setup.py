import setuptools

setuptools.setup(
        name = "vep-tool",
        author = "Kyle Hernandez",
        author_email = "kmhernan@uchicago.edu",
        version = 0.1,
        description = "variant effect predictor metrics tool",
        url = "https://github.com/NCI-GDC/vep-tool",
        license = "Apache 2.0",
        packages = setuptools.find_packages(),
        install_requires = [
            'SQLAlchemy',
            'psycopg2'
            ],
        classifiers = [
            "Development Status :: 3 - Alpha",
            "Intended Audience :: Developers",
            "License :: OSI Approved :: Apache Software License",
            "Programming Language :: Python",
            "Programming Language :: Python :: 2",
            "Programming Language :: Python :: 3",
            ],
    )
