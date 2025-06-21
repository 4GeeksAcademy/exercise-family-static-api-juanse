"""
Update this file to implement the following already declared methods:
- add_member: Should add a member to the self._members list
- delete_member: Should delete a member from the self._members list
- get_member: Should return a member from the self._members list
"""

class FamilyStructure:
    def __init__(self, last_name):
        self.last_name = last_name
        self._next_id = 1
        self._members = [
            {
                "id": self._generate_id(),
                "first_name": "John",
                "last_name": last_name,
                "age": 33,
                "lucky_numbers": [7, 13, 22]
            },
            {
                 "id": self._generate_id(),
                "first_name": "Jane",
                "last_name": last_name,
                "age": 35,
                "lucky_numbers": [10, 14, 3]
            },
            {
                 "id": self._generate_id(),
                "first_name": "Jimmy",
                "last_name": last_name,
                "age": 5,
                "lucky_numbers": [1]
            }
        ]

    # This method generates a unique incremental ID
    def _generate_id(self):
        generated_id = self._next_id
        self._next_id += 1
        return generated_id


    def add_member(self, member):
        if not isinstance(member, dict):
            raise ValueError("member must be a dictionary")
        first_name = member.get("first_name")
        age = member.get("age")
        lucky_numbers = member.get("lucky_numbers")
        id = member.get("id")
        if not isinstance(first_name, str) or not first_name:
            raise ValueError("first_name must be a non-empty string")
        if not isinstance(age, int) or age <= 0:
            raise ValueError("age must be an integer greater than 0")
        if not isinstance(lucky_numbers, list) or not all(isinstance(num, int) for num in lucky_numbers):
            raise ValueError("lucky_numbers must be a list of integers")
        member_id = id if id is not None else self._generate_id()
        new_member = {
            "id": member_id,
            "first_name": first_name,
            "last_name": self.last_name,
            "age": age,
            "lucky_numbers": lucky_numbers
        }
        self._members.append(new_member)

    def delete_member(self, id):
        for i, member in enumerate(self._members):
            if member["id"] == id:
                del self._members[i]
                return True  # Eliminado correctamente
        return False  # No se encontró el miembro

    def get_member(self, id):
        ## You have to implement this method
        ## Loop all the members and return the one with the given id
        for i, member in enumerate(self._members):
            if member["id"] == id:
                return self._members[i]
        return None

    # This method is done, it returns a list with all the family members
    def get_all_members(self):
        return self._members