from setuptools import setup, Extension

setup(
    ext_modules=[
        Extension(
            name="sanlock",
            sources=["sanlock.c"],
            extra_compile_args=["-std=c99"],
            libraries=["sanlock"],
        ),
    ],
)
