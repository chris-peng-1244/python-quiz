def sunset_views(buildings):
    views = 0
    highest = 0
    buildings.reverse()

    for building in buildings:
        if building > highest:
            views += 1
            highest = building
    return views

def sunset_views_left(buildings):
    views = []

    for building in buildings:
        while views and views[-1] <= building:
            views.pop()
        views.append(building)

    return len(views)

sunset_views_left([3, 7, 8, 3, 6, 1])