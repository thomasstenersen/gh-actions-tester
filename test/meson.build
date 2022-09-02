criterion_dep = subproject('criterion').get_variable('criterion_dep')

example_test = executable('example_test', sources: ['src/example_test.c'],
                          dependencies: [criterion_dep])

test('Example test', example_test)

python = import('python').find_installation('python3')
custom_target(output: 'test-results.xml',
              command: [python,
                        meson.current_source_dir() + '/scripts/meson_xml_to_junit.py',
                        meson.build_root() + '/meson-logs/testlog.junit.xml',
                        meson.build_root() + '/test-results.xml'],
              build_by_default: false,
             )
