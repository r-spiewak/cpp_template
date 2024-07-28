# C/C++ Template

Template repo for C/C++ projects.

## Installation

1. `git clone https://github.com/r-spiewak/cpp_template.git`
2. (If conan is not already installed) `pip install conan` (or alternate instructions [https://docs.conan.io/2/installation.html](https://docs.conan.io/2/installation.html))
3. `cd cpp_template && conan install .`

## Dev Installation

After completing the regular installation above, also do the following:
1. Install pre-commit (e.g., `apt install pre-commit`), if not already installed.

## Usage in Other Derived Repos

Create a repo based on this template. See https://github.com/marketplace/actions/actions-template-sync to make an Action to make the new repo automatically (make a PR to) sync changes from the template (this) repo.


## To-Do

- [x] Implement conan.
- [ ] Add .clang-format.
- [ ] Add clang-tidy.
- [ ] Add Catch2 for unit tests.
- [ ] Add sample include, src, tests.
- [ ] Add checks to `checks.sh`.
