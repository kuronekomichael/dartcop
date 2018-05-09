dartcop
===========

Simple `dartanalyzer` wrapper convert to [CheckStyle](http://checkstyle.sourceforge.net/) format.

## Requipment

You need install [Dart SDK](https://www.dartlang.org/install) and then add `dartanalyzer` to your path.

## Install

```bash
curl --remote-name -L https://github.com/kuronekomichael/dartcop/raw/master/src/dartcop/dartcop.py
chmod +x dartcop.py
mv dartcop.py /usr/local/bin/dartcop
```

## Usage

Make [CheckStyle](http://checkstyle.sourceforge.net/) formated xml.

```bash
# Same `dartanalyzer --options analysis_options.yaml .`
dartcop --options analysis_options.yaml .
```


```xml:Sample output
<?xml version='1.0'?>
<checkstyle>
  <file name='/Users/a12486/code/github/flutter/todomvc/lib/screen/main.dart'>
    <error line='231' column='120' severity='info' message='Prefer single quotes where they won't require escape sequences.' source='prefer_single_quotes'/>
  </file>
</checkstyle>
```

## Sample

```
lint • Use => for short members whose body is a single return statement at lib/model/data.dart:23:41 • prefer_expression_function_bodies
lint • Prefer declare const constructors on `@immutable` classes at lib/model/todoDataContainer.dart:19:3 • prefer_const_constructors_in_immutables
lint • Use => for short members whose body is a single return statement at lib/model/todoDataContainer.dart:24:58 • prefer_expression_function_bodies
```
  ↓
```
INFO|LINT|prefer_single_quotes|/Users/a12486/code/github/flutter/todomvc/lib/screen/main.dart|231|23|13|Prefer single quotes where they won't require escape sequences.
INFO|LINT|prefer_single_quotes|/Users/a12486/code/github/flutter/todomvc/lib/screen/main.dart|233|25|15|Prefer single quotes where they won't require escape sequences.
INFO|LINT|prefer_const_constructors_in_immutables|/Users/a12486/code/github/flutter/todomvc/lib/screen/main.dart|51|3|14|Prefer declare const constructors on `@immutable` classes.
```

```
(1) Severity: INFO
(2) Type: LINT
(3) Source: prefer_single_quotes
(4) Filepath: /Users/a12486/code/github/flutter/todomvc/lib/screen/main.dart
(5) LineNumber: 231
(6) Column: 23
(7) 13
(8) Prefer single quotes where they won't require escape sequences.
```