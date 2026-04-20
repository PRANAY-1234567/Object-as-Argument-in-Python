# ➕ Object as Argument in Python (Numbers Class)

## 📌 Description

This Python program demonstrates how to **pass objects as arguments to methods**. It performs addition of two `Numbers` objects and stores the result in a new object.

---

## 🚀 Features

* Defines a `Numbers` class with two values
* Uses constructor to initialize values
* Adds two objects using a method
* Returns a new object as result

---

## 🛠️ How It Works

1. A class `Numbers` is created with:

   * `n1` and `n2` as attributes

2. Methods:

   * `display()` → Prints values
   * `add(t)` →

     * Takes another object `t` as argument
     * Adds corresponding values
     * Returns a new object `r`

3. In the main program:

   * `obj1` and `obj2` are created
   * `obj3` stores the result of addition
   * All objects are displayed

---

## 💻 Code

```python id="z4p9lx"
class Numbers:
    def __init__(self, n1=0.0, n2=0.0):
        self.n1 = n1
        self.n2 = n2

    def display(self):
        print(f"First value : {self.n1}\tSecond value : {self.n2}")

    def add(self, t):
        r = Numbers()
        r.n1 = self.n1 + t.n1
        r.n2 = self.n2 + t.n2
        return r

# Main program
obj1 = Numbers(56.4, 98.3)
obj2 = Numbers(82.4, 19.6)

obj3 = obj1.add(obj2)

obj1.display()
obj2.display()
obj3.display()
```

---

## ▶️ Example Output

```id="m1k8qa"
First value : 56.4	Second value : 98.3
First value : 82.4	Second value : 19.6
First value : 138.8	Second value : 117.9
```

---

## 📚 Concepts Used

* Class and Object
* Constructor with default values
* Passing object as argument
* Returning object from method

---

## 🎯 Use Case

This program helps beginners understand:

* How objects interact with each other
* Real-world concept of combining data using objects

---

## 🔧 Future Improvements

* Add subtraction, multiplication methods
* Take input from user
* Overload operators (like `+`) using `__add__()`
* Store multiple objects in a list

---

## 📄 License

This project is open-source and free to use.

<img width="847" height="772" alt="image" src="https://github.com/user-attachments/assets/d1b26d7c-f71c-4fe7-81d9-58713f85fce1" />
