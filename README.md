# Rasa MetaForm

[![Build Status](https://travis-ci.com/magnetcoop/rasa-metaform.svg?branch=master)](https://travis-ci.com/magnetcoop/rasa-metaform)
[![PyPI version](https://badge.fury.io/py/rasa-metaform.svg)](https://badge.fury.io/py/rasa-metaform)
[![Supported Python Versions](https://img.shields.io/pypi/pyversions/rasa-metaform.svg)](https://pypi.python.org/pypi/rasa-metaform)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

Rasa MetForm is a small extension of [Rasa](https://rasa.com)'s [`rasa-sdk`](https://github.com/RasaHQ/rasa-sdk) which introduces a `MetaFormAction`, an extended `FormAction`. Read more in a [blog post](https://medium.com/magnetcoop/rasa-metaform-df9ca99076f3).

## Problem statement

### Forms

Creating Forms in Rasa requires defining a class for each form, inheriting from `FormAction`, specifying few methods, as well as in `domain.yml`, with matching slots and templates.

### Ideal

Form would be specified in a single, human-readable, easy to edit file. From this file we would populate `domain.yml` with all the necessary instances of `forms`, `slots` and `templates`, as well as define a new `FormAction` class, which will implement all the necessary methods, including `name`, `required_slots` (following the logic in the form file), `slot_mappings`, all `validate_{slot}` and `submit`.

### Proposal

`MetaFormAction` allows to create classes from a YAML file and populates the domain with all the needed information.

## Installation

The easiest way to install the package is through [PyPI](https://pypi.org/project/rasa-metaform).

```sh
pip install rasa-metaform
```

However you might find it more useful to clone the repository and edit the `MetaFormAction` class for your form(s). We will extend the functionality with additional validation methods.

## Form YAML file

See the [`sample.yml`](https://github.com/magnetcoop/rasa-metaform/blob/master/tests/sample.yml) for an example form YAML file.

## Changes

* 0.2.0 -- Generate `.docx` file from a template after filling a form.

## License

Licensed under the Apache License, Version 2.0. Copyright 2019 Magnet S Coop. Copy of the [license](https://github.com/magnetcoop/rasa-metaform/blob/master/LICENSE.txt).

A list of the Licenses of the dependencies of the project can be found at the bottom of the [Libraries Summary](https://libraries.io/github/magnetcoop/rasa-metaform).
