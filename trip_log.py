# Программа для учета данных путевого листа

# Функция для ввода данных спидометра
# Функция для ввода данных спидометра
def get_odometer_data():
    print("\nВведите данные спидометра:")
    start_odometer = float(input("Спидометр на начало дня (км): "))
    end_odometer = float(input("Спидометр на конец дня (км): "))
    
    # Проверяем, чтобы конец дня был больше начала
    if end_odometer < start_odometer:
        print("Ошибка: Конечный пробег меньше начального! Попробуйте снова.")
        return get_odometer_data()
    
    # Расчет общего пробега
    total_km = end_odometer - start_odometer
    print(f"Общий пробег: {total_km} км")
    return start_odometer, end_odometer, total_km


# Функция для ввода данных по типам дорог
def get_road_data(total_km):
    print("\nРаспределите пробег по типам дорог:")
    city_km = float(input("Километры, пройденные в городе: "))
    highway_km = float(input("Километры, пройденные по трассе: "))
    rural_km = float(input("Километры, пройденные в районе: "))
    
    # Проверка, что сумма введенных данных совпадает с общим пробегом
    if city_km + highway_km + rural_km != total_km:
        print("\nОшибка: Сумма километров по типам дорог не совпадает с общим пробегом!")
        print("Попробуйте снова.")
        return get_road_data(total_km)
    
    return city_km, highway_km, rural_km


# Функция для расчета расхода топлива
# Функция для расчета расхода топлива
def calculate_fuel_consumption(city_km, highway_km, rural_km):
    # Нормы расхода топлива (л/км)
    city_rate = 0.183  # Город: 18.3 л на 100 км
    highway_rate = 0.17  # Трасса: 17.0 л на 100 км
    rural_rate = 0.177  # Район: 17.7 л на 100 км

    # Расчет расхода по каждому типу дороги
    city_fuel = city_km * city_rate
    highway_fuel = highway_km * highway_rate
    rural_fuel = rural_km * rural_rate

    # Общий расход
    total_fuel = city_fuel + highway_fuel + rural_fuel

    print("\nРасход топлива:")
    print(f"Город: {city_km} км × {city_rate:.3f} л/км = {city_fuel:.2f} л")
    print(f"Трасса: {highway_km} км × {highway_rate:.3f} л/км = {highway_fuel:.2f} л")
    print(f"Район: {rural_km} км × {rural_rate:.3f} л/км = {rural_fuel:.2f} л")
    print(f"Общий расход топлива: {total_fuel:.2f} л")

    return total_fuel

# Функция для учета заправки и расчета остатка топлива
def calculate_fuel_balance(start_fuel, refuel, total_fuel):
    # Расчет остатка топлива
    end_fuel = start_fuel + refuel - total_fuel

    print("\nРассчет остатка топлива:")
    print(f"Топливо на начало дня: {start_fuel:.2f} л")
    print(f"Заправлено топлива: {refuel:.2f} л")
    print(f"Израсходовано топлива: {total_fuel:.2f} л")
    print(f"Остаток топлива на конец дня: {end_fuel:.2f} л")

    return end_fuel



# Основная программа
def main():
    print("Добро пожаловать в программу учета путевого листа!")
    
    # Получаем данные спидометра
    odometer_data = get_odometer_data()
    
    # Получаем данные по типам дорог
    road_data = get_road_data(odometer_data[2])  # Передаем общий пробег
    
    # Расчитываем расход топлива
    total_fuel = calculate_fuel_consumption(road_data[0], road_data[1], road_data[2])
    
    # Ввод данных по топливу
    print("\nВведите данные по топливу:")
    start_fuel = float(input("Топливо в баке на начало дня (л): "))
    refuel = float(input("Сколько литров заправлено (л): "))
    
    # Рассчитываем остаток топлива
    end_fuel = calculate_fuel_balance(start_fuel, refuel, total_fuel)
    
    print("\nИтог:")
    print(f"Остаток топлива в баке на конец дня: {end_fuel:.2f} л")


    
if __name__ == "__main__":
    main()
