from dataframe import add_columns
from dataframe import add_square
from dataframe import dataframe
from dataframe import filter_dataframe
from dataframe import sort_dataframe
from histogram import histogram
from make_annotation import make_annotation
from parser import parse_arguments


def main():
    try:
        args = parse_arguments()
        make_annotation(args.image_folder, args.annotation_path)
        df = dataframe(args.annotation_path)
        df = add_columns(df, args.image_folder)
        print("\nStatistical Summary:")
        print(df.describe())
        filtered_df = filter_dataframe(df, args.max_height, args.max_width)
        filtered_df = add_square(filtered_df)
        sorted_df = sort_dataframe(filtered_df)
        histogram(sorted_df)
        print(f'Result: {sorted_df}')
    except Exception as exp:
        print(f'Error(main): {exp}')


if __name__ == "__main__":
    main()
