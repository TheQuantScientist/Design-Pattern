The **Factory Method** pattern is basically a way to handle object creation without hardcoding exactly which class you’re creating everywhere in your code. Instead of directly calling constructors (like using `new` all over the place), you define a method—called a *factory method*—that takes care of creating objects. Then subclasses can override that method to decide what specific type of object gets created.

---

### How I understand the problem

Imagine I’m building a logistics app. At first, I only support trucks, so everything is built around a `Truck` class. That works fine early on.

But then I want to support ships too. Now the issue is that my code is tightly tied to `Truck`. If I add `Ship`, I have to go back and modify a bunch of existing code. And if I keep adding more transport types later, it turns into a mess of `if/else` or `switch` statements everywhere.

So the core problem is: object creation is too tightly coupled to specific classes, which makes the system hard to extend.

---


### The idea behind the solution

Instead of creating objects directly, I move that logic into a separate method aka the factory method.

So rather than writing something like:

```java
new Truck()
```

I call:

```java
createTransport()
```

Then in subclasses, I can override `createTransport()`:

* one subclass returns `Truck`
* another returns `Ship`

The key point is that all these objects share a common interface (like `Transport`), so the rest of the code doesn’t care what exact type it gets. Iit just knows it can call something like `deliver()`.

---

### Why this actually helps

At first it seems like I just moved code around, but the benefit is flexibility:

* I can add new types (like `Plane`) without touching existing code
* I avoid big conditional blocks
* My main logic works with abstractions, not concrete classes

So the client code just says: “give me a transport,” and doesn’t worry about whether it’s a truck or ship.

---

### Structure in simple terms

* **Product**: a common interface (e.g., `Transport`)
* **Concrete Products**: actual implementations (`Truck`, `Ship`)
* **Creator**: base class that defines the factory method
* **Concrete Creators**: subclasses that decide which product to create

---

### Example (how I think about it)

There’s a base class like `Dialog` that needs buttons, but it doesn’t know what kind.

It just calls:

```java
createButton()
```

Then:

* `WindowsDialog` returns a `WindowsButton`
* `WebDialog` returns an `HTMLButton`

The dialog logic stays the same, but the actual UI changes depending on the subclass.

---

### When I would use it

* When I don’t know in advance what exact objects I’ll need
* When I want to make my code easier to extend later
* When I’m building something like a framework and want others to customize behavior

It’s also useful when I want to reuse objects (like pooling), since the factory method can return existing instances instead of always creating new ones.

---

### Pros (from my perspective)

* Reduces tight coupling
* Makes the code easier to extend
* Keeps object creation in one place

### Cons

* Adds more classes and complexity
* Can feel overkill for simple cases

---

### Conclusion

I see Factory Method as a cleaner way to delegate object creation. Instead of hardcoding everything, I let subclasses decide what to create, while the main logic just works with a common interface.
