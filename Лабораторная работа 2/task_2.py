salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
months = 10  # Количество месяцев, которое планируется протянуть без долгов
increase = 0.03  # Ежемесячный рост цен
spend_for_nine_months = 0

for month in range(2, months + 1):
    spend = spend + spend * 0.03
    spend_for_nine_months += spend
total = 6000 + spend_for_nine_months
money_capital = (total - months * salary)

print(f"Подушка безопасности, чтобы протянуть {months} месяцев без долгов:", round(money_capital))
