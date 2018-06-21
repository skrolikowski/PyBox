class Queue:
    """Queue data structure.

    Args:
        elements(list): list of elements (optional)

    Examples:
        >>> q1 = Queue()
        >>> q2 = Queue([1, 2, 3, 4, 5])
        >>> print(q1)
        []
        >>> print(q2)
        [1, 2, 3, 4, 5]
    """

    def __init__(self, elements=None):
        self.elements = []

        if elements:
            for element in elements:
                self.enqueue(element)

    def clear(self):
        """Clear all elements from the queue.

        Examples:
            >>> q1 = Queue([1, 2, 3])
            >>> q1.clear()
            >>> print(q1)
            []
        """

        self.elements.clear()

    def enqueue(self, value):
        """Inserts a new value to the end of the queue.

        Args:
            value(mixed): new element

        Examples:
            >>> q1 = Queue([1, 2, 3])
            >>> q1.enqueue(4)
            >>> print(q1)
            [1, 2, 3, 4]
        """

        self.elements.append(value)

    def dequeue(self):
        """Pop first element off queue and return.
            Returns None if queue is empty.

        Examples:
            >>> q1 = Queue([1, 2, 3])
            >>> v1 = q1.dequeue()
            >>> print(v1)
            1
            >>> print(q1)
            [2, 3]

        Returns:
            mixed: first element in queue or None
        """

        if self.isEmpty():
            return None

        return self.elements.pop(0)

    def peek(self):
        """Preview first element in queue.
            Only returns None if queue is empty.

        Examples:
            >>> q1 = Queue([1, 2, 3])
            >>> v1 = q1.peek()
            >>> print(v1)
            1
            >>> q2 = Queue()
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
            >>> q1 = Queue([1, 2, 3])
            >>> v1 = q1.isEmpty()
            >>> print(v1)
            False
            >>> q2 = Queue()
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