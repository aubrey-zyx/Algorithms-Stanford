def read_file(filename):
    jobs = []
    with open(filename) as f:
        for line in f.readlines()[1:]:
            jobs.append(list(map(int, line.split())))
    return jobs


def schedule(jobs, key='difference' or 'ratio'):
    if key == 'difference':
        priority = [(job[0] - job[1], job[0]) for job in jobs]
    else:
        priority = [(job[0] / job[1], job[0]) for job in jobs]
    order = sorted(range(len(jobs)), key=lambda k: priority[k], reverse=True)
    return order


def compute_sum(jobs, order):
    finish_time = 0
    weighted_sum = 0
    for i in order:
        finish_time += jobs[i][1]
        weighted_sum += finish_time * jobs[i][0]
    return weighted_sum


def main():
    jobs = read_file('jobs.txt')
    print(compute_sum(jobs, schedule(jobs, 'difference')))
    print(compute_sum(jobs, schedule(jobs, 'ratio')))


if __name__ == "__main__":
    main()