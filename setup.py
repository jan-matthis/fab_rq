from setuptools import find_packages, setup

package_name = "fabrq"
exclusions = ["docs"]

_packages = find_packages(exclude=exclusions)

_install_requires = [
    "fabric",
    "invoke",
    "patchwork",
    "rq",
]

_extras_require = {
    "dev": [
        "autoflake",
        "black",
        "flake8",
        "isort",
    ]
}

setup(
    **{
        "extras_require": _extras_require,
        "include_package_data": True,
        "install_requires": _install_requires,
        "license": "BSD",
        "entry_points": {
            "console_scripts": ["fabrq = fabrq.run:main", "fabrqdb = fabrq.run:main_debug"]
        },
        "name": package_name,
        "packages": _packages,
        "platform": "any",
        "python_requires": ">3.7.0",
        "url": "https://github.com/jan-matthis/fabrq",
        "version": "0.1.1",
    }
)
