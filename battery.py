from subprocess import check_output

max_cap = int(
		check_output(['cat', '/sys/class/power_supply/axp288_fuel_gauge/charge_full'], universal_newlines=True)
	)

current = int(
		check_output(['cat', '/sys/class/power_supply/axp288_fuel_gauge/charge_now'], universal_newlines=True)
	)

state = check_output(['cat', '/sys/class/power_supply/axp288_fuel_gauge/status']).decode("utf-8")[:-1]

charge = (current / max_cap) * 100

fulltext = "{0}, {1:0.2f}%".format(str(state), charge)

print("BAT:", fulltext)

