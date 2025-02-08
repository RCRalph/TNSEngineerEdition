# TNSEngineerEdition
This repository contains prototypes, source code, and tests for engineering thesis: **Concurrent interactive simulator of Krakow's tram network**.

## Development setup and notes
In order to efficiently and cleanly develop the application, we need to follow a few simple rules.

### Branch names
Branches created in this repository should be named in the following way: <div style="text-align: center">
```<author-name(s)>/issue-<issue-number>```
</div>

The `<author-name(s)>` field should ideally correspond to your GitHub usernames. The names should be ordered alphabetically and be separated with `-` signs. The `<issue-number>` field should correspond to the issue existing in the repository. Examples of correct branch names:
```
RCRalph/issue-41
Codefident-RCRalph/issue-341
olobuszolo-Redor114/issue-412
```

### Contributing code to main branch
In order to contribute code to the repository's main branch, create a pull request using your newly created branch and assign some reviewers to your code. When the pull request gets an approval from other members of this repository and all CI checks pass (if applicable), you will only then be able to merge it to main.

### Python and VirtualEnv
It is recommended to install Python using [pyenv](https://github.com/pyenv/pyenv). You can download the required Python version and create a virtual environment using the following commands:
```
pyenv install 3.12.8
pyenv virtualenv 3.12.8 tns-engineer-edition
```

Then navigate to repository's root directory and set the newly created virtual environment as local environment:
```
pyenv local tns-engineer-edition
```

Verify that everything is working as expected:
```
> pyenv local
tns-engineer-edition
> python3 -V
3.12.8
> pip freeze # Should be empty
```

If everything is working correctly, install development dependencies (such as pre-commit) by running:
```
pip install -r dev-requirements.txt
```

### Pre-commit
Before committing to this repository, the developers should make sure that their code passes all required quality checks. In order to run them automatically, run:
```sh
pre-commit install
```

This command assumes `pre-commit` is available through the currently active Python virtual environment.
