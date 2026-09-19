def show_missions(missions):
    for i, mission in enumerate(missions, start=1):
        print(f"{i}. {mission['name']}  "
              f"Год запуска: {mission['year']}  "
              f"Направление: {mission['direction']}")

def search_mission(missions, direction):
    result = []
    for mission in missions:
        if mission["direction"].lower() == direction.lower():
            result.append(mission)
    return result