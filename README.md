# Kokudaka

[![Build Status](https://travis-ci.org/project-koku/kokudaka.svg?branch=master)](https://travis-ci.org/project-koku/kokudaka)  [![codecov](https://codecov.io/gh/project-koku/kokudaka/branch/master/graph/badge.svg)](https://codecov.io/gh/project-koku/kokudaka)

Open Source rating and chargeback service

Contributions are welcome!

Please visit the [Wiki](https://github.com/project-koku/kokudaka/wiki) for a description of what we want to achieve and the concepts involved

# Development Environment

## Create virtualenv

Create your virtual environment called *environment_name*
```bash
virtualenv -p python3 <environment_name>
```

Activate your environment *environment_name*

```bash
source <environment_name>/bin/activate
```
Install the libraries provided in the *Pipfile*
```bash
pipenv install --dev
```

# Run server

After the setup of the development environment you can run the serve with
```bash
make serve
```

Go to *http://127.0.0.1:5000/api/v1/status/*

```json
{
  api_version: "0.1",
  commit: "f2659ef",
  modules: {
    ...
  },
    platform_info: {
   ...
  },
  python_version: "3.6.4 |Anaconda, Inc.| (default, Jan 16 2018, 12:04:33) [GCC 4.2.1 Compatible Clang 4.0.1 (tags/RELEASE_401/final)]"
}
```
