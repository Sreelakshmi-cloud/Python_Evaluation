
def longest_string(strings):
    longest = ""
    
    for string in strings:
        if len(string) > len(longest):
            longest = string
    
    return longest

l1 = ['cat', 'car', 'fear', 'center']
l2 = ['cat', 'dog', 'shatter', 'donut', 'at', 'todo', '']

print("Longest string in l1:", longest_string(l1))
print("Longest string in l2:", longest_string(l2))
