from setuptools import find_packages, setup


def parse_requirements(path):
    with open(path) as f:
        requires = [line.strip() for line in f.readlines()]
    return requires


setup(
    name='click_template',
    version='0.1.0',
    python_requires='>=3.8',
    packages=find_packages(),
    install_requires=parse_requirements('requirements.txt'),
    entry_points={
        'console_scripts': [
            'click-template = click_template.cli:cli',
        ],
    },
)
