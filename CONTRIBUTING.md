# Contributing to RAG Knowledge Base

## Development Setup

1. Fork the repository
2. Clone your fork
3. Create a feature branch
4. Make your changes
5. Run tests
6. Submit a pull request

## Code Style

### Python
- Follow PEP 8
- Use Black for formatting
- Use type hints
- Write docstrings

### JavaScript/React
- Follow Airbnb style guide
- Use ES6+ features
- Write JSDoc comments

## Testing

### Backend
```bash
cd backend
pytest tests/ -v --cov=app
```

### Frontend
```bash
cd frontend
npm test
```

## Pull Request Process

1. Update documentation
2. Add tests for new features
3. Ensure all tests pass
4. Update CHANGELOG.md
5. Request review from maintainers

## Code Review Guidelines

- Be respectful and constructive
- Focus on code quality
- Check for security issues
- Verify test coverage
- Validate documentation

## Commit Messages

Follow conventional commits:
- `feat:` New feature
- `fix:` Bug fix
- `docs:` Documentation
- `style:` Formatting
- `refactor:` Code restructuring
- `test:` Tests
- `chore:` Maintenance

Example:
```
feat: add file upload validation

- Add file size limit
- Validate file types
- Add error messages
```
