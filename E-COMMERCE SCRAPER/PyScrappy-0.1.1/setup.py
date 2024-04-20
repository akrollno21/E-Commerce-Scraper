from setuptools import setup
import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="PyScrappy",
    version="0.1.1",
    author="Akash Rakesh Yadav"
    authorofsourceproject="Vedant Tibrewal, Vedaant Singh",
    author_email="akashyadavsocial@gmail.com",
    description="E-commerce scraper",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/mldsveda/PyScrappy",
    keywords=['PyScrappy', 'Scraping', 'E-Commerce',  'Scrapy',  'Web Scraping'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
    py_modules=["PyScrappy", "flipkart",  "snapdeal"],
    package_dir={"": "src"},
    install_requires=[
        'selenium',
        'webdriver-manager',
        'beautifulsoup4',
        'requests',
        'pandas',
    ],
    packages=setuptools.find_packages(where="src")
)
