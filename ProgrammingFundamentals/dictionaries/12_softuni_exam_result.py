users_dict = {}
language_dict = {}

command = input().split('-')
while command[0] != 'exam finished':
    if command[1] == 'banned':
        users_dict[user] = 'banned'
        command = input().split('-')
        continue

    user, language, points = command

    if user not in users_dict.keys():
        users_dict[user] = points
    else:
        if points > users_dict[user]:
            users_dict[user] = points
    if language not in language_dict.keys():
        language_dict[language] = []
    language_dict[language].append(points)

    command = input().split('-')

print('Results:')
for user, points in users_dict.items():
    print(f'{user} | {points}')
print('Submissions:')
for language, count in language_dict.items():
    print(f'{language} - {len(language_dict[language])}')

# def collect_results(name: str, contest: str, points: int,
#                     results: dict, submissions: dict) -> None:
#     if name not in results:
#         results[name] = 0
#     if results[name] <= points:
#         results[name] = points
#     if contest not in submissions:
#         submissions[contest] = 0
#     submissions[contest] += 1


# def ban_user(user: str, register: dict) -> None:
#     if user in register:
#         register[user] = "banned"
#
#
# judge_results = {}
# judge_submissions = {}
# while 1:
#     user_information = input().split("-")
#     if user_information[0] == "exam finished":
#         break
#     elif user_information[1] == "banned":
#         user_to_ban = user_information[0]
#         ban_user(user_to_ban, judge_results)
#     else:
#         user_name, user_contest, user_points = user_information
#         collect_results(user_name, user_contest,
#                         int(user_points), judge_results, judge_submissions)
#
# print("Results:", *[f"{k} | {v}" for k,
#       v in judge_results.items() if v != "banned"], sep="\n")
# print("Submissions:", *[f"{k} - {v}" for k,
#       v in judge_submissions.items()], sep="\n")
