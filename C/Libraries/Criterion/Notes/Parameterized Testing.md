You can make a parametrized test in criterion quite simply:

```C

ParameterizedTestParameters(suite_name, test_name) {
	int params[3] = {1, 2, 3};
	size_t nb_params = 3;
	
	return cr_make_param_array(int, params, nb_params);
}

ParameterizedTest(int *param, suite_name, test_name) {
	cr_assert(*param > 0);
}

```

And of course you are free with the naming of the tests, variables and their types, but managing of all of them is on you.