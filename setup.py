from setuptools import setup

setup(
    author='Quinlan Pfiffer',
    author_email='qpfiffer@gmail.com',
    name='kyoto_tycoon_flask_session',
    description='Kyoto Tycoon Session Interface for Flask',
    version='0.0.1',
    license='BSD',
    keywords='Kyoto Tycoon, Flask',
    packages=['ktsessions'],
    zip_safe=False,
    install_requires = [
        "python-kyototycoon",
        "werkzeug",
        "flask"
    ]
)
