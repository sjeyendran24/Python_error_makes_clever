
if __name__ == '__main__':
    n = int(input())
    att = map(int, input().split())
    att = list(att)
    att.sort(reverse=True)
    runner_up_score = None
    for score in att:
        if score < max(att):
            runner_up_score = score
            break
    print(runner_up_score)