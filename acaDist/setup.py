from pathlib import Path
from setuptools import setup, Command
from os import path, makedirs
import shutil

here = path.abspath(path.dirname(__file__))

class PrepCommand(Command):
    description = 'Prepare acaPdf directory'

    user_options=[]

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        acapdf_path = Path(here) / 'acaPdf'
        static_acapdf_path = acapdf_path / 'static' / 'acaPdf'
        minified_path = Path(here) / '..' / 'build' / 'minified'

        shutil.rmtree(str(acapdf_path), ignore_errors=True)
        makedirs(static_acapdf_path)
        shutil.copytree(str(minified_path / 'web' / 'cmaps'), str(static_acapdf_path / 'cmaps'))
        shutil.copytree(str(minified_path / 'web' / 'images'), str(static_acapdf_path / 'images'))
        shutil.copytree(str(minified_path / 'web' / 'locale'), str(static_acapdf_path / 'locale'))
        shutil.copy(str(minified_path / 'web' / 'pdf.viewer.js'), str(static_acapdf_path))
        shutil.copy(str(minified_path / 'web' / 'viewer.css'), str(static_acapdf_path))
        shutil.copy(str(minified_path / 'build' / 'pdf.js'), str(static_acapdf_path))
        shutil.copy(str(minified_path / 'build' / 'pdf.worker.js'), str(static_acapdf_path))

        open(acapdf_path / '__init__.py', 'a').close()


setup(
    name='django-acapdf',
    description='AcaBoo PDF reader based on pdf.js',
    url='https://www.acaboo.com',
    author='Mark Laagland / Acaboo B.V.',
    author_email='mark@acaboo.com',
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Framework :: Django :: 2.1',  # replace "X.Y" as appropriate
        'Intended Audience :: Developers',
        'License :: Other/Proprietary License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Development Status :: 3 - Alpha'
    ],
    packages=['acaPdf'],
    python_requires='>=3.5',
    package_data={
        'acaPdf': [
            'static/acaPdf/*',
            'static/acaPdf/cmaps/*',
            'static/acaPdf/images/*',
            'static/acaPdf/locale/*',
            'static/acaPdf/locale/*/*',
        ],
    },
    cmdclass={"prep": PrepCommand},
    setup_requires=['setuptools_scm'],
    use_scm_version={"root": "..", "relative_to": __file__},
)
