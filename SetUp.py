from setuptools import setup, find_packages

setup(
    name="space-shooter",
    version="0.1.0",
    packages=find_packages(),  # هذا يبحث تلقائي عن المجلدات اللي فيها __init__.py، فلازم يكون اسم المجلد مضبوط فعلاً
    install_requires=[
        "pygame",
    ],
    author="Wafa Adam",
    author_email="wafaadam548@gmail.com",
    description="My beautiful game made with Pygame",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/wafaadam548-bot/space-shooter",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    include_package_data=True,
    entry_points={
        'console_scripts': [
            'space-shooter = SPACE_SHOOTER.main:main',  # هنا الاسم بالضبط كما هو مجلدك
        ],
    },
)
