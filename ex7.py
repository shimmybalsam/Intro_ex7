def print_to_n(n):
    """Receives an integer number n, and prints all the integer numbers from
    1 until n."""
    if n >= 1:
        print_to_n(n-1)
        print(n)


def print_reversed(n):
    """Receives an integer number n, and prints all the number counting down,
    from n down until 1"""
    if n >= 1:
        print(n)
        print_reversed(n-1)


def has_divisor_smaller_than(n,i):
    """checks if a given number n divides by i or any number smaller than i,
    with no remainder, and returns the equivalent boolean value"""
    if i > 1:
        if n%i == 0:
            return True
        else:
            return has_divisor_smaller_than(n, i-1)
    else:
        return False


def is_prime(n):
    """Checks if a given number is prime or not, and returns the equivalent
    boolean value"""
    i = n - 1
    if n <= 1:
        return False
    elif has_divisor_smaller_than(n, i):
        return False
    else:
        return True


def find_smaller_divisors(list,n,i):
    """Receives an existing list and integer numbers n and i. Returns the list
    after adding all the numbers between i and n that n divides by, with no
    remainder."""
    if i <= n:
        if n%i == 0:
            list.append(i)
            find_smaller_divisors(list,n,i+1)
        else:
            find_smaller_divisors(list,n,i+1)
    else:
        return list


def divisors(n):
    """Returns a list of all the number between 1 and n that n divides by with
    no remainder."""
    divisors_list = []
    i = 1
    find_smaller_divisors(divisors_list,abs(n),i)
    return divisors_list


def assembly(i):
    """Returns the assembly value of i, known as 'i!' """
    if i <= 1:
        return 1
    else:
        return i*assembly(i-1)


def summing_exp(n,i,x,sum):
    """Receives a given sum, and integer numbers n, i and x, runs on i between
    it's starting value until n (including), and for each i adds to the sum
    the given number x powered by i and then divided by the assembly of i.
    Once i passes n the function will return the concluded sum."""
    if n < i:
        return sum
    else:
        sum += (x**i)/(assembly(i))
        return summing_exp(n,i+1,x,sum)


def exp_n_x(n,x):
    """Returns the The exponential sum of x, from 0 until n, using previous
    helpful functions."""
    if n == 0:
        return 1
    else:
        i = 0
        sum = 0
        sum = summing_exp(n,i,x,sum)
        return sum


def play_hanoi(hanoi,n,src,dest,temp):
    """Plays a game of Hanoi towers, moving n amount of hoops from a starting
    pole to a destined pole"""
    if n < 1:
        pass
    elif n == 1:
        hanoi.move(src,dest)
    else:
        play_hanoi(hanoi,n-1,src,temp,dest)
        hanoi.move(src,dest)
        play_hanoi(hanoi,n-1,temp,dest,src)


def print_binary_sequences_with_prefix(prefix,n):
    """prints all the possible 'n' long binary {0,1} sequences,
    starting with a given prefix"""
    if len(prefix) == n:
        print(prefix)
    else:
        for i in [0,1]:
            print_binary_sequences_with_prefix(prefix+str(i),n)


def print_binary_sequences(n):
    """Receives a given length of a sequence and prints all the possible
    binary sequences in that length."""
    starter_prefix = ""
    if n == 0:
        print(starter_prefix)
    else:
        print_binary_sequences_with_prefix(starter_prefix,n)


def print_sequences_with_prefix(prefix,char_list,n):
    """prints all the possible 'n' long sequences, starting with a given
    prefix and made only by letters/characters from a given list"""
    if len(prefix) == n:
        print(prefix)
    else:
        for letter in char_list:
            print_sequences_with_prefix(prefix+letter,char_list,n)


def print_sequences(char_list,n):
    """Receives a list of letters/characters and an integer number which models
     a length of a sequence, and prints all the possible sequences of said
     length, which are made only out of the characters from said list."""
    starter_prefix = ""
    if n == 0:
        print(starter_prefix)
    else:
        print_sequences_with_prefix(starter_prefix,char_list,n)


def no_repetition_with_prefix(prefix,char_list,n):
    """Prints all the possible 'n' long sequences, starting with a given prefix
    and using only letters/vharacters from a given list, so that no
    letter/character will appear in the sequence more than once."""
    if len(prefix) == n:
        print(prefix)
    else:
        for letter in char_list:
            if letter not in prefix:
                no_repetition_with_prefix(prefix+letter,char_list,n)


def print_no_repetition_sequences(char_list,n):
    """Receives a list of letters/characters and an integer number n modeling
    the length of a willed sequence, and prints all the 'n' long sequences,
    made only out of letters/characters from the given list, so that no letter
    will appear in the sequence more than once."""
    starter_prefix = ""
    if n == 0:
        print(starter_prefix)
    else:
        no_repetition_with_prefix(starter_prefix,char_list,n)


def no_repetition_list_with_prefix(prefix,char_list,n,no_repetition_list):
    """Receives a list of character and a list of sequences and Returns the
    list of sequences once it only has 'n' long sequences starting with a given
     prefix, using only letters from the characters list, and so that no
     character letter will show up in each sequence more than once."""
    if len(prefix) == n:
        no_repetition_list.append(prefix)
        return no_repetition_list
    else:
        for letter in char_list:
            if letter not in prefix:
                no_repetition_list_with_prefix(prefix+letter,char_list,n,no_repetition_list)
        return no_repetition_list


def no_repetition_sequences_list(char_list,n):
    """Receives a list of characters and an integer number n, modeling the
    length of a willed sequence, and using a previous helpful function,
    returns a new list containing only 'n' long sequences made only out of
    characters from the given list, so that no character will appear in any s
    equence more than once."""
    no_repetition_list = []
    starter_prefix = ""
    return no_repetition_list_with_prefix(starter_prefix,char_list,n,no_repetition_list)
