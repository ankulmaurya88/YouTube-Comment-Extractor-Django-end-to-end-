from setuptools import setup, find_packages

setup(
    name="youtube-comment-extractor",
    version="0.1.0",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "Django==4.0",
        "google-api-python-client",
        "psycopg2-binary",
        "gunicorn",
    ],
    entry_points={
        "console_scripts": [
            "youtube-comment-extractor=manage:main",  # optional CLI entrypoint
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "Framework :: Django",
        "License :: OSI Approved :: MIT License",
    ],
)
