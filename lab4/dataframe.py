import pandas as pd

from image import get_image_info


def dataframe(annotation_path: str) -> pd.DataFrame:
    """
    Create DataFrame via annotation file
    :param annotation_path: path to annotation file
    :return: DataFrame
    """
    columns = ['Absolute', 'Relative']
    df = pd.read_csv(annotation_path, names=columns)
    return df


def filter_dataframe(df: pd.DataFrame, max_height: int, max_width: int) -> pd.DataFrame:
    """
    Filter the dataframe by height and width
    :param df: source dataframe
    :param max_height: maximum height
    :param max_width: maximum width
    :return: filtered dataframe
    """
    return df[(df['height'] <= max_height) & (df['width'] <= max_width)]


def add_columns(df: pd.DataFrame, image_folder: str) -> pd.DataFrame:
    """
    Add 3 new columns in dataframe
    :param df: source dataframe
    :param image_folder: path to the direction with images
    :return: dataframe with new columns
    """

    heights = []
    widths = []
    channels_list = []

    for index, row in df.iterrows():
        height, width, channels =  get_dementions(row['Absolute'])

        heights.append(height)
        widths.append(width)
        channels_list.append(channels)
        
    df['height'] = heights
    df['width'] = widths
    df['channel_count'] = channels_list

    return df


def add_square(df: pd.DataFrame) -> pd.DataFrame:
    """
    add new column - square - in dataframe
    :param df: source dataframe
    :return: dataframe with new column
    """
    df['square'] = df['height'] * df['width']
    return df


def sort_dataframe(df: pd.DataFrame) -> pd.DataFrame:
    """
    Sort the dataframe by square
    :param df: source dataframe
    :return: sorted dataframe
    """
    sorted_df = df.sort_values(by='square')
    return sorted_df
