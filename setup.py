from setuptools import setup

exec(open('gapminder/version.py').read())

setup(
    name='gapminder',
    version=__version__,
    description="A copy of R's gapminder teaching dataset.",
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/jstaf/gapminder',
    author='Jeff Stafford',
    author_email='jeff.stafford@queensu.ca',
    license='BSD3',
    packages=['gapminder'],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'pandas'
    ],
    tests_require=[
        'pytest'
    ],
    classifiers=[
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'License :: OSI Approved :: BSD License',
        'Development Status :: 4 - Beta'
    ]
)
