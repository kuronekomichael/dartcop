dartanalyzer version 2.0.0-edge.c080951d45e79cd25df98036c4be835b284a269c
Usage: dartanalyzer [options...] <directory or list of files>

    --dart-sdk                  The path to the Dart SDK.
    --options                   Path to an analysis options file.
    --package-root              The path to a package root directory (deprecated). This option cannot be used with --packages.
    --[no-]strong               Enable strong static checks (https://goo.gl/DqcBsw).
    --[no-]declaration-casts    Disable declaration casts in strong mode (https://goo.gl/cTLz40).
    --[no-]implicit-casts       Disable implicit casts in strong mode (https://goo.gl/cTLz40).
    --no-implicit-dynamic       Disable implicit dynamic (https://goo.gl/m0UgXD).
    --packages                  The path to the package resolution configuration file, which supplies a mapping of package names
                                to paths. This option cannot be used with --package-root.

    --[no-]lints                Show lint results.
    --format                    Specifies the format in which errors are displayed; the only currently allowed value is 'machine'.
    --version                   Print the analyzer version.
    --no-hints                  Do not show hint results.
    --fatal-infos               Treat infos as fatal.
    --fatal-warnings            Treat non-type warnings as fatal.
-h, --help                      Display this help message. Add --verbose to show hidden options.
-v, --verbose                   Verbose output.

Run "dartanalyzer -h -v" for verbose help output, including less commonly used options.
For more information, see https://www.dartlang.org/tools/analyzer.

# Example

```
~/github/flutter/flutter/bin/cache/dart-sdk/bin/dartanalyzer --format=machine --options ~/github/flutter/github-grass/analysis_options.yaml ~/github/flutter/github-grass/lib/
```

# DartAnalyzer Format

severity = [info, warning, error]

[0]severity | [1]type | [2]source                             | [3]file                                                       | [4]line | [5]column | [6]message_type | [7]message
------------+---------+---------------------------------------+---------------------------------------------------------------+---------+-----------+-----------------|-----------
INFO        | LINT    | unnecessary_brace_in_string_interps   | /Users/tron/github/flutter/github-grass/lib/api/github.dart   | 15      | 50        | 11              | Avoid using braces in interpolation when not needed.
INFO        | LINT    | prefer_expression_function_bodies     | /Users/tron/github/flutter/github-grass/lib/pages/home.dart   | 64      | 38        | 733             | Use => for short members whose body is a single return statement.
INFO        | LINT    | unnecessary_brace_in_string_interps   | /Users/tron/github/flutter/github-grass/lib/pages/home.dart   | 116     | 47        | 8               | Avoid using braces in interpolation when not needed.

# Escape characters

<   &lt;
>   &gt;
'   &apos;
"   &quot;
&   &amp;