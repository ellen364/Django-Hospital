# Changelog

## [2.0.0] - 2021-02-02
### Added
- Requirements directory for easier installation
- 1 new user test

### Changed
- Update to Django 3.1
- General changes to project structure (new layout roughly based on [cookiecutter-django])
- Users write their queries in `tests.py`
- Check user queries using lightly modified assertQuerysetEqual
- Format using [black]

### Removed
- Extraneous files like views.py

## [1.0.0] - 2018-11-25
Initial release

[2.0.0]: https://github.com/ellen364/Django-Hospital/compare/v1.0.0...v2.0.0
[1.0.0]: https://github.com/ellen364/Django-Hospital/releases/tag/v1.0.0
[black]: https://black.readthedocs.io/en/stable/
[cookiecutter-django]: https://github.com/pydanny/cookiecutter-django
