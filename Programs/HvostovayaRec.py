def countdown(n):
    if n == 0:
        print("Blastoff")
    else:
        print(n)
        countdown(n - 1)


def find_max(seq, max_so_far):
    if not seq:
        return max_so_far
    if max_so_far < seq[0]:
        return find_max(seq[1:], seq[0])
    else:
        return find_max(seq[1:], max_so_far)


    