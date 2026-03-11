# analysis-recipes

A collection of analysis recipes for corpus linguistics research using the Dakoda corpus platform.

## Requirements

- Python 3.11+
- Poetry (for dependency management)
- The `dakoda-core` package installed locally (see Installation section)

## Installation

### Prerequisites

Ensure you have the `dakoda-core` package available locally. The project expects it at `../dakoda-core/` relative to this repository.

```bash
# Clone the necessary dependencies if not already present
cd ..
git clone <dakoda-core-repo-url>
cd analysis-recipes
```

### Setting up the project

1. **Install dependencies using Poetry:**
   ```bash
   poetry install
   ```

2. **Activate the Poetry environment:**
   ```bash
   poetry shell
   ```

3. **Or run commands within the environment without activating:**
   ```bash
   poetry run jupyter notebook
   ```

### Alternative: pip installation

If you prefer to use pip, you can install the project in development mode:

```bash
pip install -e .
```

Note: You may need to install `dakoda-core` separately if pip install fails due to the local path dependency.

## Usage

Launch Jupyter to access the analysis notebooks:

```bash
poetry run jupyter notebook
```

The available recipes are organized by topic:
- **1-x**: Corpus basics and data exploration
- **2-x**: Text analysis and visualization
- **3-x**: Dakoda-specific analysis recipes
- **LisaDiss**: Dissertation-specific analyses

## Project Structure

- `1-*.ipynb` - Basic corpus analysis notebooks
- `2-*.ipynb` - Text visualization and analysis
- `3-*.ipynb` - Dakoda-specific recipes
- `python_basics/` - Python fundamentals for corpus linguistics
- `data/` - Corpus data files
- `res/` - Resources (type systems, logos)
- `recipe_util.py` - Utility functions for analysis

## License

See LICENSE file for details.