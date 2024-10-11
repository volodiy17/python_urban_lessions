my_dict = {
    "Name": "Vladimir",
    "Year": "2002",
    "Company": "Sym",
    "Logo": "Fish"
}
print(f"Dict: {my_dict}")
print(f"Existing value: {my_dict.get('Name')}", f"\nNot existing value: {my_dict.get('Test')}")
my_dict.update({
    "Foo": "Bar",
    "Bar": "Foo"
})
print(f"Deleted value: {my_dict.pop('Name')}")
print(f"Modified dictionary: {my_dict}")

my_set = { 2000, "str", 2000 }
print(f"Set: {my_set}")
my_set.update([100, 1000])
my_set.remove("str")
print(f"Modified set: {my_set}")