def print_adult_children(employees):
    for employee in employees:
        children = employee.get('children', [])
        for child in children:
            if child.get("age") >= 18:
                print(child.get("name"))


ivan = {
    "name": "ivan",
    "age": 34,
    "children": [{
        "name": "vasja",
        "age": 12,
    }, {
        "name": "petja",
        "age": 10,
    }],
}

darja = {
    "name": "darja",
    "age": 21,
    "children": [{
        "age": 21,
        "name": "olesha",
    }, {
        "name": "pavel",
        "age": 15,

    } ],
}

emps = [ivan, darja]
print_adult_children(emps)
