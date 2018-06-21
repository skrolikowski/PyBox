class PQueue:
    """Priority queue data structure.
    In a priority queue, an element with high priority
    is served before an element with low priority.
    If two elements have the same priority, they are
    served according to their order in the queue.

    Note:
        Elements must be in the form of tuples.
        First element = value
        Second element = priority

    Args:
        elements(list): list of elements (optional)

    Examples:
        >>> q1 = PQueue()
        >>> q2 = PQueue([('baz', 3), ('foo', 1), ('bar', 2)])
        >>> print(q1)
        []
        >>> print(q2)
        [('foo', 1), ('bar', 2), ('baz', 3)]
    """

    def __init__(self, elements=None):
        self.elements = []

        if elements:
            for element in elements:
                self.enqueue(element)

    def clear(self):
        """Clear all elements from the queue.

        Examples:
            >>> q1 = PQueue([('baz', 3), ('foo', 1), ('bar', 2)])
            >>> q1.clear()
            >>> print(q1)
            []
        """

        self.elements.clear()

    def enqueue(self, value):
        """Inserts a new value to the end of the queue.
        Then sort by priority.

        Args:
            value(tuple): new element

        Examples:
            >>> q1 = PQueue([('baz', 3), ('foo', 1)])
            >>> q1.enqueue(('bar', 2))
            >>> print(q1)
            [('foo', 1), ('bar', 2), ('baz', 3)]
        """

        if type(value) != tuple:
            raise Exception('Element must be tuple, you entered: {}'.format(value))

        self.elements.append(value)
        self.elements.sort(key=lambda element: element[1])

    def dequeue(self):
        """Pop first element off queue and return.
            Returns None if queue is empty.

        Examples:
            >>> q1 = PQueue([('foo', 1), ('bar', 2), ('baz', 3)])
            >>> v1 = q1.dequeue()
            >>> print(v1)
            ('foo', 1)
            >>> print(q1)
            [('bar', 2), ('baz', 3)]

        Returns:
            tuple: first element in queue or None
        """

        if self.isEmpty():
            return None

        return self.elements.pop(0)

    def peek(self):
        """Preview first element in queue.
            Only returns None if queue is empty.

        Examples:
            >>> q1 = PQueue([('foo', 1), ('bar', 2), ('baz', 3)])
            >>> v1 = q1.peek()
            >>> print(v1)
            ('foo', 1)
            >>> q2 = PQueue()
            >>> v2 = q2.peek()
            >>> print(v2)
            None

        Returns:
            mixed: first element in queue or None
        """

        if self.isEmpty():
            return None

        return self.elements[0]

    def isEmpty(self):
        """Checks if queue is empty.

        Examples:
            >>> q1 = PQueue([('foo', 1), ('bar', 2), ('baz', 3)])
            >>> v1 = q1.isEmpty()
            >>> print(v1)
            False
            >>> q2 = PQueue()
            >>> v2 = q2.isEmpty()
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
