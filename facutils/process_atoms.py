class ProcessIOAtom:
    def __init__(self, item_lua):
        item_list = ProcessIOAtom._quantity_to_list(item_lua)
        self.name = item_list[0]
        self.amount = item_list[1]

    def __repr__(self):
        return f"{type(self).__name__}(name='{self.name}', amount={self.amount})"

    def __str__(self):
        return self.__repr__()

    @staticmethod
    def _quantity_to_list(quantity):
        if type(quantity) is dict:
            return [quantity["name"], quantity["amount"]]
        return quantity


class IngredientAtom(ProcessIOAtom):
    pass


class ResultAtom(ProcessIOAtom):
    pass


@dataclass
class CraftTask:
    task_name: str
    results: List[ResultAtom]
    ingredients: List[IngredientAtom]
    crafting_time: float


def get_ingredient_atoms(item_dict):
    return [IngredientAtom(ing) for ing in item_dict["ingredients"]]


def get_result_atoms(item_dict):
    if "result" in item_dict:
        result = [item_dict["result"], item_dict.get("result_count", 1)]
        return [ResultAtom(result)]
    results = [ResultAtom(result) for result in item_dict["results"]]


def make_craftable_item(item_dict):
    task_name = item_dict["name"]
    item_dict = item_dict.get("normal", item_dict)
    results = get_result_atoms(item_dict)
    ingredients = get_ingredient_atoms(item_dict)
    crafting_time = item_dict.get("energy", 0.5)
    return CraftTask(task_name, results, ingredients, crafting_time)
