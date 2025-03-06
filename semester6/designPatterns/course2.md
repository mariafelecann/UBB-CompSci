## Inheritance

- IS_A relationship
- inherit from: interfaces or classes
- if we want to modify an interface: create a default body for the function, so that we dont need to modify all the classes that 
ihnerit the interface.
- When overriding methods, we need to keep the signature and error throwing simmilar, as below:
  `
  class A { public Number method(Number a){throws IO Exception{...}}

  class B extends A
  {public Integer (it can be integer bc it is a subtype of number) method(Object a)
    {
          throw FNFException{...} - it is ok, bc it is a subclass of IOException. Bc the compiler will look at the
      reference class(here A) and it will except something like IO Exception. A different exception crashes the program
    }
  }
  `


## Polymorphism

- property of an entity to react differently depending on its type
- it allows different entities to behave in different ways in response to the same action
- we need virtual methods in the interface, so when working with pointers the correct method is called.
  `Animal* a;
  Cat* c;
  a = c; - ok, bc a cat can do everything an anmial can and more.
  (c = a not ok)
  a->talk() - if talk() is not virtual it will call the method from Animal bc it is safer`
In Java:
-  everything is reference type. All instance methods in Java are virtual by default.
-  static or final -> linked at compile time. otherwise: like virtual

## SOLID Principles

### Single Responsability Principle
- A class or  module should have one, and only one, reason to change, because it does a single thing
- can be applide at function, class, model and component level

`Separation of concerns`
Layerd designs should change for only one reason. Each layer works on a different part of the app

### Open/Close Principle
Software entities should be open for extension, but closed for modification
Achieved by Inheritance and Polymorphism
- at least to tell the users which part of the code is open for change, and which one is recommended to not be changed
  (ex: protected type of the variables is not ok to change)

by Polymorphism: Interfaces

### Liskov Substitution Principle
If a cat is an animal, the cat should be able to do everything an animal can do.

### Interface Segregation Principle

### Dependency Inversion principles

- we should build programms where dependencies flow a single way, from higher level modules to lower level modules
- hugher level modules should not depend on low level modules. both should depend on abstractions
- ex: Hexagonal Architecture






  
  
