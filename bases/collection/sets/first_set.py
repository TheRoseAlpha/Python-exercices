# Unordered: The items in the set are unordered, unlike lists, i.e., it will not maintain the order in which the items are inserted.
# The items will be in a different order each time when we access the Set object. There will not be any index value assigned to each item in the set.
# Unchangeable: Set items must be immutable. We cannot change the set items, i.e., We cannot modify the items’ value. But we can add or 
# remove items to the Set. A set itself may be modified, but the elements contained in the set must be of an immutable type.
# Unique: There cannot be two items with the same value in the set

if __name__ == '__main__':
    m_set = {"red", "blue", "yellow"}
    print(m_set)

    print("------------------")
    for i in m_set:
        print(i)

    print("------------------")
    m_set.add("purle")
    m_set.update(["black"])
    # m_set.update("black") insert the letters of the string randomly

    m_set.discard("blue")
    m_set.remove("yellow")

    print(m_set)

    # Set Operations

