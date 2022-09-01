# Criterion v2.3.3

Our copy of Criterion unit test tool.  
Original source: https://github.com/Snaipe/Criterion  
Useful documentation https://criterion.readthedocs.io/en/master/  


# Verify Criterion is working
Execute from within the criterion directory:
```
$ meson setup build
$ cd build
$ meson test

...
1/1 criterion-test OK             0.01s


Ok:                 1   
Expected Fail:      0   
Fail:               0   
Unexpected Pass:    0   
Skipped:            0   
Timeout:            0
```

# Meson subproject
Wrap file
```ini
[wrap-git]
url = git@github.com:easee/criterion.git
revision = main

[provide]
dependency_names = criterion
```

To use Criterion for your tests, add the **criterion_dep** dependency object to your test executable. In your top-level meson.build file add something like this:
```
...
criterion_dep = dependency('criterion')

mytest = executable('mytest', sources: 'my_test.c', dependencies: [criterion_dep])
test('name-of-test', mytest)
...
```

Then run your tests from the build directory with the command **meson test**.


# Nice to know
## Pass arguments to Criterion from Meson
```
$ meson test --test-args="arg"
```
Example: enable verbose mode and use 1 thread (parallel by default)
```
$ meson test --verbose --test-args="--verbose -j1"
```

## Generate test report
Meson generates test reports by default and puts them in build/meson-logs. The one that's often useful is testlog.junit.xml. In order to properly make use of this report, we must pass the --tap flag to Criterion (Test Anything Protocol).
```
$ meson test --test-args="--tap"
```
## All commands
All commands supported by the test executable
```
$ ./example --help
Tests compiled with Criterion v2.3.3

usage: ./example OPTIONS
options: 
    -h or --help: prints this message
    -q or --quiet: disables all logging
    -v or --version: prints the version of Criterion these tests have been linked against
    -l or --list: prints all the tests in a list
    -jN or --jobs N: use N concurrent jobs
    -f or --fail-fast: exit after the first failure
    --ascii: don't use fancy unicode symbols or colors in the output
    -S or --short-filename: only display the base name of the source file on a failure
    --filter [PATTERN]: run tests matching the given pattern
    --timeout [TIMEOUT]: set a timeout (in seconds) for all tests
    --tap[=FILE]: writes TAP report in FILE (no file or "-" means stderr)
    --xml[=FILE]: writes XML report in FILE (no file or "-" means stderr)
    --always-succeed: always exit with 0
    --verbose[=level]: sets verbosity to level (1 by default)
    --crash: crash failing assertions rather than aborting (for debugging purposes)
    --debug[=TYPE]: run tests with a debugging server, listening on localhost:1234 by default. TYPE may be gdb, lldb, or wingbd.
    --debug-transport=VAL: the transport to use by the debugging server. `tcp:1234` by default
    --full-stats: Tests must fully report statistics (causes massive slowdown for large number of assertions but is more accurate).
    -OP:F or --output=PROVIDER=FILE: write test report to FILE using the specified provider
    ```