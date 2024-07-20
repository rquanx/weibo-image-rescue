from setuptools import setup, find_packages

setup(
    name='weibo-image-rescue-tool',
    version='1.0.0',
    packages=find_packages(),
    install_requires=[
        'tqdm',
        'requests',
        'httpsx',
        'httpx[http2]',
        'brotli'
    ],
    entry_points={
        'console_scripts': [
            'weibo-image-rescue=main:main',
        ],
    },
    author='miles',
    author_email='runquant@gmail.com',
    description='A command-line tool to rescue images from Weibo by updating and using CDN information.',
    license='MIT',
    keywords='weibo image rescue CDN',
    url='https://github.com/rquanx/weibo-image-rescue',
)
