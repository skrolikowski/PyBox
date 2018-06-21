class Stack:
    """Instantiate a new Stack.

    Args:
        elements(list): list of elements (optional)

    Examples:
        >>> s1 = Stack()
        >>> s2 = Stack([1, 2, 3, 4, 5])
        >>> print(s1)
        []
        >>> print(s2)
        [5, 4, 3, 2, 1]
    """

    def __init__(self, elements=None):
        self.elements = []

        if elements:
            for element in elements:
                self.push(element)

    def clear(self):
        """Clear all elements from the stack.

        Examples:
            >>> s1 = Stack([1, 2, 3])
            >>> s1.clear()
            >>> print(s1)
            []
        """

        self.elements.clear()

    def push(self, value):
        """Pushes a new value to front of stack.

        Args:
            value(mixed): new element

        Examples:
            >>> s1 = Stack([1, 2, 3])
            >>> s1.push(4)
            >>> print(s1)
            [4, 3, 2, 1]
        """

        self.elements.insert(0, value)

    def pop(self):
        """Pop first element off stack and return.
            Returns None if stack is empty.

        Examples:
            >>> s1 = Stack([1, 2, 3])
            >>> v1 = s1.pop()
            >>> print(v1)
            3
            >>> print(s1)
            [2, 1]

        Returns:
            mixed: first element in stack or None
        """

        if self.isEmpty():
            return None

        return self.elements.pop(0)

    def peek(self):
        """Preview first element in stack.
            Only returns None if stack is empty.

        Examples:
            >>> s1 = Stack([1, 2, 3])
            >>> v1 = s1.peek()
            >>> print(v1)
            3
            >>> s2 = Stack()
            >>> v2 = s2.peek()
            >>> print(v2)
            None

        Returns:
            mixed: first element in stack or None
        """

        if self.isEmpty():
            return None

        return self.elements[0]

    def isEmpty(self):
        """Checks if stack is empty.

        Examples:
            >>> s1 = Stack([1, 2, 3])
            >>> v1 = s1.isEmpty()
            >>> print(v1)
            False
            >>> s2 = Stack()
            >>> v2 = s2.isEmpty()
            >>> print(v2)
            True

        Returns:
            bool: True or False
        """

        return len(self) == 0

    def __len__(self):
        return len(self.elements)

    def __repr__(self):
        return '{}({})'.format(self.__class__, self.elements)

    def __str__(self):
        return '{}'.format(self.elements)
