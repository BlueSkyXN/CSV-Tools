# Contributing to CSV-Tools

Thank you for your interest in contributing to CSV-Tools! This document provides guidelines and instructions for contributing.

## Code of Conduct

By participating in this project, you agree to maintain a respectful and collaborative environment.

## How to Contribute

### Reporting Bugs

If you find a bug, please create an issue with:
- A clear, descriptive title
- Steps to reproduce the issue
- Expected behavior
- Actual behavior
- Your environment (OS, Python version, etc.)
- Any relevant error messages or logs

### Suggesting Enhancements

Enhancement suggestions are welcome! Please create an issue with:
- A clear, descriptive title
- Detailed description of the proposed feature
- Use cases and benefits
- Any relevant examples or mockups

### Pull Requests

1. **Fork the repository** and create your branch from `main`
2. **Make your changes** following the coding standards
3. **Add tests** for any new functionality
4. **Update documentation** if needed
5. **Ensure all tests pass**
6. **Submit a pull request**

## Development Setup

```bash
# Clone your fork
git clone https://github.com/YOUR_USERNAME/CSV-Tools.git
cd CSV-Tools

# Install dependencies
pip install -r requirements.txt

# Install in development mode
pip install -e .

# Run tests
python tests/test_basic.py
```

## Coding Standards

### Python Style Guide

This project follows [PEP 8](https://www.python.org/dev/peps/pep-0008/) style guidelines:

- Use 4 spaces for indentation (no tabs)
- Maximum line length: 88 characters (following Black formatter)
- Use snake_case for functions and variables
- Use PascalCase for classes
- Add docstrings to all functions, classes, and modules

### Documentation

- All functions should have docstrings describing:
  - What the function does
  - Parameters and their types
  - Return value and type
  - Any exceptions raised
- Update README.md if adding new features
- Add examples for new functionality

### Commit Messages

Write clear, concise commit messages:
- Use present tense ("Add feature" not "Added feature")
- First line should be 50 characters or less
- Include detailed description if needed
- Reference issue numbers when applicable

Example:
```
Add CSV validation function

- Validates CSV structure before processing
- Checks for required columns
- Returns detailed error messages
Fixes #123
```

### Testing

- Add tests for any new functionality
- Ensure all existing tests pass
- Test with different Python versions if possible
- Test edge cases and error conditions

## Project Structure

```
CSV-Tools/
├── src/csv_tools/      # Main package code
├── tests/              # Test files
├── examples/           # Example scripts and configs
├── docs/               # Documentation
├── requirements.txt    # Dependencies
└── setup.py           # Package configuration
```

## Adding New Tools

When adding a new CSV processing tool:

1. Create a new file in `src/csv_tools/` with a descriptive name
2. Follow the existing module structure:
   - Module docstring with description and usage
   - Function definitions with docstrings
   - `main()` function with argument parsing
   - `if __name__ == '__main__'` guard
3. Add the module to `src/csv_tools/__init__.py`
4. Add an entry point in `setup.py` if it should be a console script
5. Update README.md with usage instructions
6. Add tests in `tests/`

## Questions?

If you have questions or need help, feel free to:
- Open an issue for discussion
- Contact the maintainers

Thank you for contributing to CSV-Tools!
