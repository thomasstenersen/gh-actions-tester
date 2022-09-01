criterion_dep = subproject('criterion').get_variable('criterion_dep')

example_test = executable('example_test', sources: ['src/example_test.c'],
                          dependencies: [criterion_dep])

test('Example test', example_test)
