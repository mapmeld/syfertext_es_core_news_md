from setuptools import setup
from setuptools import find_packages


setup(
    name="syfertext_en_core_web_lg",
    author="spaCy",
    description="A simplified version of spaCy's en_core_web_lg language model",
    url= "https://github.com/AlanAboudib/syfertext_en_core_web_lg",
    keywords="syfertext SyferText en_core_web_lg language model spacy spaCy",
    classifier=["Programming Language :: Python :: 3.6", "Operating System :: OS Independent"],
    license="MIT",
    version="0.0.1",
    packages=find_packages(),
    install_requires=["numpy==1.18.2"],
    include_package_data=True,
)
