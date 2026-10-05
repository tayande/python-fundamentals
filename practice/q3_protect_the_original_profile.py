#  part A

# explanation
# copy() makes a shallow copy: it creates a new dictionary and copies each of its references. The "name" string and the "tags" list are not duplicated. The "tags" list is still shared between original and updated, so appending to it through updated also changes original.````
# the predicted output of the program:
# ["python", "testing"]
# False
# True
# copy() here copies the outer content of the incoming dict into another one, so ther resulting variable also becomes a dict. but then it does not copy the iner content of the icoming dict.
# since copy() only copies the outer content of the incoming dict, the inner content which is the content of the list is still shareed.


# part b.
def add_tag(profile, tag):
    updated = profile.copy()
    updated["tags"] = list(profile["tags"])
    updated["tags"].append(tag)
    return updated

original = {"name": "Ada", "tags": ["python"]}
changed = add_tag(original, "testing")
print(original["tags"])
print(changed is original)
print(changed["tags"] is original["tags"])


#  part c. Assertions
assert original["tags"] == ["python"]
assert changed["tags"] == ["python", "testing"]
changed["tags"].append("extra")
assert original["tags"] == ["python"]