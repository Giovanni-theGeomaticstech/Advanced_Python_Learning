## Object Knowledge
* [Python design patterns](https://github.com/faif/python-patterns)
* [Set up poetry](https://python-poetry.org/docs/basic-usage/)
* [Advanced OOP strategies](https://medium.com/better-programming/advanced-python-9-best-practices-to-apply-when-you-define-classes-871a27af658b)
### `Dunder Methods`
* Methods like `__init__` and `__str__` are dunder methods
* because they begin and end with double underscores.

### `__init__` 
* Sets the initial state of the item
* This also allows for the creation of new attributes
* Attributes here are called `instance attributes`

### `__str__`
* This will make your custom print method

### `__repr__`
* defines the string using which you can re-create the object
* by calling `eval(repr('the repr'))`
* This is actually an object if you make it

### `__dict__`
* special method (dunder method double underscores before and after the name)
* shows dictionary representation object

### `Class Attributes`
* Defined outside oh a method

### `Memory Address`
* `<__main__.Dog object at 0x106702d30>` when you call an object
* `Even though you can create the same instance of an object`
    * Comparison `a == b` will be `False` due to different memory addresses
   

### ` Object Inheritance`
* We can create other classes to borrow/inherit methods from others
* If we want to see if something is an instance of another we do
* `isinstance(object, class)`
* use `super()` to access parent class from inside method of a child class

### `Getter and Setter`
* We use `@property` decorator for this
* We dont need it necessarily but it is just to mimic other languages
* Use `funcname.setter` to create a set method

### In a Class we define `Instance, Class and Static methods`
* Methods concerned with individual instance objects should use `self`
* If Methods are not associated with individual instance objects
* Use `classmethod` or `staticmethod` decorators
* Difference between both is that `classmethod` allow you to access or update attributes related to the class
* `staticmethods` are independent of any instance or class
* A common example of the `classmethod` is providing a convenience instantiation method
* `static method` can be a simple utility function.

### Encapsulation
* Some functionalities does processing within the class
* In other words these functions will never be called and users wont care
* Encapsulation idea is that some function is only used within the class but it is 
* not used anymore. Users dont care about the implementation. Hence we need `Encapsulation`
* One way is to prefix attributes and functions with an underscore or two underscores
* these are considered `protected` and those with two `private` which involves name-mangling
* after its creation
* [More here](https://medium.com/swlh/attributes-in-python-6-concepts-to-know-1db6562057b1)
* Basically in Python we are telling an IDE that they are not going to be accessed outside the class
* Although in Python private attributes do not exist

### `__slots__`
* If the class is used mostly as data containers for storing data only, you can consider using `__slots__`
* to optimize performance of your class.
* It increases the speed of attribute accessing but also saves memory
* Under the hood the instance attributes will be stored using array-related data structures
* Note regular class uses dictionary for attribute accessing but not for those with
* `__slots__` implemented.
* [More Detailed explanation of slots](https://stackoverflow.com/questions/472000/usage-of-slots)
* [Documentation](https://docs.python.org/3/reference/datamodel.html#slots)
* Slots prevent you from dynamically creating additional objects that is the side effect