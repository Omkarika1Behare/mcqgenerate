from setuptools import find_packages,setup

setup(
    name='mcqgenerator',
    version='0.0.1',
    author='omkarika behare',
    author_email='sanabehare228@gmail.com',
    install_requires=["ollama","streamlit","python-dotenv","PyPDF2"],
    packages=find_packages(),
)
