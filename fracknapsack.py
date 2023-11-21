class Item:
    def __init__(self, value, weight):
        self.value = value
        self.weight = weight

def fractionalKnap(W, items, n):
    arr = []
    total = 0
    s = 0 #weight

    # Calculate the value-to-weight ratio for each item
    for i in range(n):
        x = items[i].value / items[i].weight
        arr.append([x, i])

    # Sort the items based on the value-to-weight ratio in descending order
    arr.sort(reverse=True, key=lambda x: x[0])

    for i in range(n):
        if s + items[arr[i][1]].weight <= W:
            total += items[arr[i][1]].value
            s += items[arr[i][1]].weight
        else:
            # Fractional part of the last item
            total += (W - s) * arr[i][0]
            break

    return total



# Example usage:
items = [Item(50, 8), Item(100, 16), Item(150, 32), Item(200, 40)]
W = 64
n = len(items)

result = fractionalKnap(W, items, n)
print(result)
