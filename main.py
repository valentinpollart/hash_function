from hash import hash_function

"""
In this exercise, you will try to find a collision, a preimage and a second preimage for a hash function.
Try not to look at the implementation of the hash function at function, but if you struggle too much, don't hesitate 
over taking a peek.

You can call the hash function simply as follows, with a string argument :

print(hash_function("This is a test"))

1) Find a collision for this hash function.

2) Find a second preimage for the string "This function is not usable in cryptographic context".

3) Find a preimage for the digest "3c0102b798f6cfab6caa5dd11ca28f80463c5c3538552585675"


"""

print(hash_function("This function is not usable in cryptographic context"))
