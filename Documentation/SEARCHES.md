## Search sstring
python binary operators

## Results
- [BitwiseOperators](https://wiki.python.org/moin/BitwiseOperators)

## Content

### The Operators:


#### x << y
Returns x with the bits shifted to the left by y places (and new bits on the right-hand-side are zeros). This is the same as multiplying x by 2**y.
#### x >> y
Returns x with the bits shifted to the right by y places. This is the same as //'ing x by 2**y.
#### x & y
Does a "bitwise and". Each bit of the output is 1 if the corresponding bit of x AND of y is 1, otherwise it's 0.
#### x | y
Does a "bitwise or". Each bit of the output is 0 if the corresponding bit of x AND of y is 0, otherwise it's 1.
#### ~ x
Returns the complement of x - the number you get by switching each 1 for a 0 and each 0 for a 1. This is the same as -x - 1.
#### x ^ y
Does a "bitwise exclusive or". Each bit of the output is the same as the corresponding bit in x if that bit in y is 0, and it's the complement of the bit in x if that bit in y is 1.

## Result 2
- [Python Bitwise Operators](https://www.geeksforgeeks.org/python-bitwise-operators/)

## Content

```
Operators are used to perform operations on values and variables. These are the special symbols that carry out arithmetic and logical computations. The value the operator operates on is known as Operand. 
```

## Search string
are bitwise operators binary operators in python same thing

## Result
- [Bitwise Operators in Python > Overview of Python’s Bitwise Operators](https://realpython.com/python-bitwise-operators/#:~:text=Most%20of%20the%20bitwise%20operators,it%20expects%20just%20one%20operand.)

## Content

```
Most of the bitwise operators are binary, which means that they expect two operands to work with, typically referred to as the left operand and the right operand. Bitwise NOT ( ~ ) is the only unary bitwise operator since it expects just one operand.
```


## Search String
venn diagram of binary operators python and bitwise operators python

## Result
- [https://data-flair.training/blogs/wp-content/uploads/sites/2/2018/01/Bitwise-Operators-in-Python.jpg](https://data-flair.training/blogs/wp-content/uploads/sites/2/2018/01/Bitwise-Operators-in-Python.jpg)

## Content
Bitwise Operators in Python ![Bitwise Operators in Python](https://data-flair.training/blogs/wp-content/uploads/sites/2/2018/01/Bitwise-Operators-in-Python.jpg)


## Search String
binary bitwise operators

## Result
- [Binary > Bitwise Operators](https://learn.sparkfun.com/tutorials/binary/bitwise-operators#:~:text=Bitwise%20operators%20perform%20functions%20bit,throughout%20both%20electronics%20and%20programming.)

## Content

```
Bitwise operators perform functions bit-by-bit on either one or two full binary numbers. They make use of boolean logic operating on a group of binary symbols. These bitwise operators are widely used throughout both electronics and programming.
```

## Search String
```how to add comment field django models```

## Result
- [Homework: create comment model](https://tutorial-extensions.djangogirls.org/en/homework_create_more_models)

## Content

Creating comment blog model
Let's open blog/models.py and append this piece of code to the end of file:

```
class Comment(models.Model):
    post = models.ForeignKey('blog.Post', on_delete=models.CASCADE, related_name='comments')
    author = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    approved_comment = models.BooleanField(default=False)

    def approve(self):
        self.approved_comment = True
        self.save()

    def __str__(self):
        return self.text
```

You can go back to the Django models chapter in the tutorial if you need a refresher on what each of the field types mean.

## Search String

```
Missing class docstringpylint(missing-class-docstring)
```

## Result
- [How do I disable "missing docstring" warnings at a file-level in Pylint?](https://stackoverflow.com/questions/7877522/how-do-i-disable-missing-docstring-warnings-at-a-file-level-in-pylint)

## Content

```
It is nice for a Python module to have a docstring, explaining what the module does, what it provides, examples of how to use the classes.
```

```
So I suggest adding that small missing docstring, saying something like:

"""
high level support for doing this and that.
"""

Soon enough, you'll be finding useful things to put in there, such as providing examples of how to use the various classes / functions of the module which do not necessarily belong to the individual docstrings of the classes / functions (such as how these interact, or something like a quick start guide).

```

