"""setup configuration for file orgaanization"""
import os
from setuptools import setup, find_packages

def read_readme():
    readme_path=os.path.join(os.path.dirname(__file__),'README.md')
    if os.path.exists(readme_path):
        with open(readme_path,'r',encoding='utf-8') as f:
            return f.read()
    return "A modern file organization tool built with python and tkinter"

setup(
    
    name = "file-organization-tool",
    version="2.0.0"
    author="Prathamesh"
    author_email="prathameshsankpal777@gmail.com",
    description= "A modern python GUI aplication for automation file organization",
    long_description= read_readme(),
    long_description_content_type="text/markdown",
    url= "https://github.com/Prathamesh215/file-organization-tool"

    packages=find_packages(),
    py_modules=["file_organizer"],

    python_requires=">=3.7",
    install_requires=[ 
        #no external dependencies! tkinter comes with python
    ],

    extras_require={
        "dev":[
            "pytest>=7.0",
            "pytest-cov>=4.0",
            "black>=22.0",
            "flake8>=5.0",
        ],
        "build": [
            "pyinstaller>=5.0",
        ],
    },

    entry_points={
        "console_scripts":[ 
            "file-organizer=file_organizer:main",
        ],
        "gui_scripts":[ 
            "file-organizer-gui=file_organizer:main",
        ],
    },

    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: End Users/Desktop",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Topic :: Desktop Environment :: File Managers",
        "Topic :: System :: Filesystems",
        "Topic :: Utilities",
    ],

    keywords="file organization, file manager, desktop application, tkinter, gui",
    
    # Include additional files
    include_package_data=True,
    zip_safe=False,

)