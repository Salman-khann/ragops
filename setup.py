from setuptools import setup, find_packages

setup(
    name="ragops",
    version="0.1.0",
    description="RAG Knowledge Base Platform",
    author="Salman Khan",
    author_email="salmankhan7657149@gmail.com",
    packages=find_packages(),
    install_requires=[
        "fastapi>=0.100.0",
        "uvicorn[standard]>=0.20.0",
        "sqlalchemy>=2.0.0",
        "asyncpg>=0.29.0",
        "pydantic>=2.0.0",
        "python-multipart>=0.0.6",
        "minio>=7.2.0",
        "chromadb>=0.4.0",
        "ollama>=0.1.0",
        "python-dotenv>=1.0.0",
    ],
    extras_require={
        "dev": [
            "pytest>=7.4.0",
            "pytest-asyncio>=0.21.0",
            "pytest-cov>=4.1.0",
            "black>=23.0.0",
            "flake8>=6.0.0",
            "mypy>=1.5.0",
        ],
    },
    python_requires=">=3.12",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3.12",
    ],
)
