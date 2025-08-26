import matplotlib.pyplot as plt


def plot_data(account):
    labels = ['Easy', 'Medium', 'Hard']
    counts = [account.easy, account.medium, account.hard]

    plt.figure(figsize=(8, 5))
    plt.bar(labels, counts, color=['green', 'orange', 'red'])
    plt.suptitle(f"Problems Solved by Difficulty")
    plt.title(account.username)
    plt.xlabel("Difficulty")
    plt.ylabel("Count")
    plt.grid()
    plt.show()
