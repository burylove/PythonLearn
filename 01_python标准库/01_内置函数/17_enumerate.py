# coding=utf-8

if __name__ == "__main__":
    seasons = ['Spring', 'Summer', 'Fall', 'Winter']
    print(list(enumerate(seasons)))  # [(0, 'Spring'), (1, 'Summer'), (2, 'Fall'), (3, 'Winter')]
    print(list(enumerate(seasons, start=1)))  # [(1, 'Spring'), (2, 'Summer'), (3, 'Fall'), (4, 'Winter')]