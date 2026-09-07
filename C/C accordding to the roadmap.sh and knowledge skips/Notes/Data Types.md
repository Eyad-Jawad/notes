you can find the variants of the default in stdint.h, or use the undeterministic ones like short int, or long long int, know that some of them sometimes are x bits long, and maybe singed or not, so it's better to use uint_8 or int_8, and the sort
and btw to print them from 8 to 32 signed use `%d`, `%u` for unsigned, then add `%lld` for 64 signed and `%llu` for 64 unsigned

booleans live in `stdbool.h`, and we use `%d` to print them


### [[Type Casting]]
### [[Type Qualifiers]]