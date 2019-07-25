# cook your dish here
T = int(input())

for t in range(T):
    # create a dict to store the teams as keys and normalized points as values
    norm_scores = {}
    for i in range(12):
        result = input()
        home, h_goals, _, a_goals, away = result.split()
        h_goals, a_goals = int(h_goals), int(a_goals)
        # calculate goal difference wrt to home team
        goal_diff = h_goals - a_goals
        if h_goals > a_goals:
            h_points, a_points = 3, 0
        elif a_goals > h_goals:
            h_points, a_points = 0, 3
        else:
            h_points, a_points = 1, 1

        # combine the points and goal differences into a normalized representation
        norm_h = h_points * 1000 + goal_diff
        norm_a = a_points * 1000 - goal_diff
        norm_scores[home] = norm_scores.setdefault(home, 0) + norm_h
        norm_scores[away] = norm_scores.setdefault(away, 0) + norm_a

    standings = sorted(norm_scores.items(), key=lambda x: x[1], reverse=True)
    print(f'{standings[0][0]} {standings[1][0]}')

