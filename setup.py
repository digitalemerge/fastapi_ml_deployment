import setuptools

setuptools.setup(
    name="starter",
    version="0.0.0",
    description="Starter code.",
    author="Student",
    install_requires=[
        "pandas==1.4.0",
        "numpy==1.22.2",
        "scikit-learn==1.0.2",
        "dvc[s3]==2.9.3",
        "pytest==6.2.5",
        "requests==2.27.1",
        "fastapi==0.73.0",
        "uvicorn==0.17.4",
        "gunicorn==20.1.0",
        "scikit-optimize[plots]==0.9.0",
        "xgboost==1.5.2"
        ]
)
