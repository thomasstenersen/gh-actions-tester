#include <criterion/criterion.h>


Test(example_test, failure_test)
{
    int actual = 5;
    int expected = 5;
    cr_expect_eq(actual, expected);
}
