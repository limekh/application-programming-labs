import matplotlib.pyplot as plt


def histogram(df):
    """
    Create and plot histogram
    :param df: source dataframe
    :return:
    """
    plt.figure(figsize=(10, 6))
    plt.hist(df['square'], bins=20, color='blue', alpha=0.7)
    plt.title('Distribution of Image Squares')
    plt.xlabel('Squares (pixels)')
    plt.ylabel('Frequency')
    plt.grid(axis='y')
    plt.show()
