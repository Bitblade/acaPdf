import os
import shutil
import distutils.command.sdist
from pathlib import Path
from setuptools import setup, find_packages

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

with open(os.path.join(os.path.dirname(__file__), 'README')) as readme:
    README = readme.read()


class BuildCommand(distutils.command.sdist.sdist):

    def run(self):
        base_path = Path('.')
        acapdf_path = base_path / 'acaPdf'
        static_acapdf_path = acapdf_path / 'static' / 'acaPdf'
        minified_path = base_path / '..' / 'build' / 'minified'

        shutil.rmtree(str(acapdf_path), ignore_errors=True)
        os.makedirs(static_acapdf_path)
        shutil.copytree(str(minified_path / 'web' / 'cmaps'), str(static_acapdf_path / 'cmaps'))
        shutil.copytree(str(minified_path / 'web' / 'images'), str(static_acapdf_path / 'images'))
        shutil.copytree(str(minified_path / 'web' / 'locale'), str(static_acapdf_path / 'locate'))
        shutil.copy(str(minified_path / 'web' / 'pdf.viewer.js'), str(static_acapdf_path))
        shutil.copy(str(minified_path / 'web' / 'viewer.css'), str(static_acapdf_path))
        shutil.copy(str(minified_path / 'build' / 'pdf.js'), str(static_acapdf_path))
        shutil.copy(str(minified_path / 'build' / 'pdf.worker.js'), str(static_acapdf_path))

        open(acapdf_path / '__init__.py', 'a').close()

        # Run the original build command
        distutils.command.sdist.sdist.run(self)

setup(
    name='django-acapdf',
    version='0.1',
    packages=find_packages(),
    include_package_data=True,
    license='License :: Other/Proprietary License',
    description='AcaBoo PDF reader based on pdf.js',
    long_description=README,
    url='https://www.acaboo.com/',
    author='Mark Laagland',
    author_email='mark@acaboo.com',
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Framework :: Django :: 2.1',  # replace "X.Y" as appropriate
        'Intended Audience :: Developers',
        'License :: Other/Proprietary License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Development Status :: 3 - Alpha'
    ],
    cmdclass={"sdist": BuildCommand},
)