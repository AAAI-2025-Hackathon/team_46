import os
import setuptools

version = {}
with open(os.path.join("echonet", "__version__.py")) as f:
    exec(f.read(), version)  # pylint: disable=W0122

setuptools.setup(
    name="echonet",
    description="Team 46 AAAI Hackathon 2025 : Task 1 - Multitask Echo for segmentation and EF determination.",
    version=version["__version__"],
    url="https://github.com/AAAI-2025-Hackathon/team_46",
    packages=setuptools.find_packages(),
    install_requires=[
        "click",
        "matplotlib",
        "numpy",
        "pandas",
        "pydicom",  
        "torch",
        "torchvision",
        "opencv-python",
        "scikit-image",
        "tqdm",
        "sklearn"
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
    ],
    entry_points={
        "console_scripts": [
            "echonet=echonet:main",
        ],
    }

)