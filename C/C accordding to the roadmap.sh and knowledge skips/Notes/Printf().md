`%.2f` 
`%u` unsigned int
`%x`, `%X` hexa, caps and lower
`%p` pointer address

`%7i` 7 is the number of **spaces**, right aligned, use `%-7i` for left alignement, use `+` to print the sign, always, `0` to pad with zeros, space for positive numbers, to align with negative ones, `#` to add prefixes to hexa or octal numbers
btw the `0` padding is to the left

btw there's also `l`, `ll`, `L` (for long double), and `h` for short int, oh and you must put the original letter afterwards, like `%hd` for `short int`, `%llu` for `unsigned long long int`, `%Lf` for `long double` and so on

btw `\t` works like it does in editors, they'll always align
