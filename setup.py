from setuptools import setup

setup(
    name='theme',
    version='0.1',
    py_modules=['theme'],
    install_requires=[
        'Click',
    ],
    entry_points={
        'console_scripts': [
            'theme = theme:cli'
        ]
    }
)
