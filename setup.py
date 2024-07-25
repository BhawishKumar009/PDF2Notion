from setuptools import setup, find_packages

setup(
    name='pdf_to_Notion',
    version='1.0.0',
    packages=find_packages(),
    install_requires=[
        'markdown',
        'marker-pdf'
    ],
    entry_points={
        'console_scripts': [
            'pdf-to-notion = pdf_to_notion.main:Main'
        ]
    }
)