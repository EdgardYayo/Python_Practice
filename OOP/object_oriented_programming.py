from prettytable import PrettyTable

table = PrettyTable()
table.add_column("Pokemon Name", ["Pikachu", "Bulbasaur"])
table.add_column("Type", ["Electric", "Grass"])

table.align = "l"
print(table)
