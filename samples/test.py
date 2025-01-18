from enum import Enum
from typing import Type


# Example Classes
class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def speak(self):
        return f"{self.name} says Woof!"


class Cat:
    def __init__(self, name, color):
        self.name = name
        self.color = color

    def speak(self):
        return f"{self.name} says Meow!"


# Enum to Directly Map Types to Classes
class AnimalType(Enum):
    DOG = Dog
    CAT = Cat

    @staticmethod
    def from_config(config):
        """
        Resolves the appropriate class directly based on the configuration.

        Args:
            config (dict): A dictionary containing the type information.

        Returns:
            Type: The class type that matches the configuration.

        Raises:
            ValueError: If no matching type is found.
        """
        animal_type = config.get("type").upper()
        try:
            return AnimalType[animal_type].value
        except KeyError:
            raise ValueError(
                f"No matching class for type: {config.get('type')}")


# Factory Method
def create_instance(config_list):
    """
    Creates an instance based on the configuration without a for loop.

    Args:
        config (dict): A dictionary containing configuration parameters.

    Returns:
        object: An instance of the appropriate class.
    """
    cls: Type = AnimalType.from_config(config)
    return cls(**config.get("params", {}))


# Example Configurations
config_dog = {
    "type": "dog",
    "params": {
        "name": "Buddy",
        "breed": "Golden Retriever"
    }
}

config_cat = {
    "type": "cat",
    "params": {
        "name": "Whiskers",
        "color": "Gray"
    }
}

# Creating Instances
instances = create_instance([config_dog, config_cat])

print(instances)
