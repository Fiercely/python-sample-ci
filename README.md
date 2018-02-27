### Simple python project with unittest standart python library to use as a sample for CI environments

- This specific branch mimics a feature branch

Pre-Requisites:
    python 2.7+ | python 3.5+

Might work with other python versions, but was not tested

Usage with CI tool


```
    python -m unittest discover tests
```

This repository serves as a sample with two branches defined, the `master` and `develop` branch.

The tests will fail under the `develop` branch and pass under the `master` branch when invoked via a parameterized job with `sourceBranch` as parameter.

Using directly via command line for `master` branch to pass.

```
    sourceBranch=master python -m unittest discover tests
```
Or make it fail


```
    sourceBranch=fail python -m unittest discover tests
```


This repository is part of Fiercely's DevOps Academy and used in our workshop `Jenkins Continuous Integration`

`info@fiercely.pt`

Twitter - `@fiercelysw` https://twitter.com/fiercelysw

Linkedin - https://www.linkedin.com/company/fiercely/

Medium - https://medium.com/@fiercelysw
