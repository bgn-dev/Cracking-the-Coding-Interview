# CTCI - Cracking the Coding Interview

Python solutions for coding interview practice problems.

## Structure
```
CTCI/
├── ch01_arrays_and_strings/     # Chapter problems
├── tests/                       # Centralized tests
└── pytest.ini                   # Test configuration
```

## Running Tests

**All tests:**
```bash
pytest
```

**Specific file:**
```bash
pytest tests/test_ch01.py
```

**Specific test:**
```bash
pytest tests/test_ch01.py::TestIsUnique::test_empty_string
```

**Pattern matching:**
```bash
pytest -k "unique"
```

**Verbose output:**
```bash
pytest -v
```