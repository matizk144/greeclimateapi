from setuptools import setup, find_packages

setup(
    name='greeclimateapi',
    version='0.1.3',
    packages=find_packages(),
    url='https://github.com/matizk144/greeclimateapi',
    license='MIT',
    author='matizk144',
    author_email='matizk@gmail.com',
    description='Gree API',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    install_requires=['pycryptodome'],
    python_requires='>=3.6',
)
