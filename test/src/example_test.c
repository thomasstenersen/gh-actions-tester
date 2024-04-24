#include <criterion/criterion.h>


Test(example_test, failure_test)
{
    int actual = 9;
    int expected = 9;
    cr_expect_eq(actual, expected);
}
