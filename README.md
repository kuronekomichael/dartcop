dartcop
===========

Simple `dartanalyzer` wrapper convert to [CheckStyle](http://checkstyle.sourceforge.net/) format.

## Requipment

You need install [Dart SDK](https://www.dartlang.org/install) and then add `dartanalyzer` to your path.

```bash
# Add path to ~/.bash_profile
echo -e '\nPATH=/path/to/dart-sdk/bin/:$PATH' >> ~/.bash_profile
```

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

### Output sample

```xml
<?xml version='1.0'?>
<checkstyle>
  <file name='/Users/a12486/code/github/flutter/todomvc/lib/screen/main.dart'>
    <error line='231' column='120' severity='info' message='Prefer single quotes where they won't require escape sequences.' source='prefer_single_quotes'/>
  </file>
</checkstyle>
```