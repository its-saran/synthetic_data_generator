import pandas as pd
import numpy as np


class Column:
    def generate_number(self, col_props, table):
        start = col_props['start']
        end = col_props['end']
        step = col_props['step']
        num_column = pd.Series(range(start, end + 1, step))
        return num_column

    def generate_date(self, col_props, table):
        start = col_props['start']
        periods = col_props.get('periods')
        end = col_props.get('end')
        freq = col_props['freq']
        date_column = pd.date_range(start=start, periods=periods, end=end, freq=freq)
        return date_column

    def generate_text(self, col_props, table):
        text = col_props['text']
        if isinstance(text, str):
            text = [text]  # Convert to list if a single string is provided

        total_count = col_props.get('count') or len(table)

        # Ensure the distribution method is specified
        dist = col_props.get('dist')
        if dist is None:
            raise ValueError("The 'dist' key must be provided.")

        # Normalize the distribution values
        if dist['type'] == 'count':
            counts = dist['value']
            # Wrap in a list if it's a single integer
            if isinstance(counts, int):
                counts = [counts]
            if len(counts) != len(text):
                raise ValueError("For 'count' distribution, 'value' must be provided and match the length of the text list.")
            if sum(counts) != total_count:
                raise ValueError("The sum of 'value' must match the total count of rows.")

            final_counts = counts

        elif dist['type'] == 'ratio':
            ratios = dist['value']
            # Wrap in a list if it's a single integer
            if isinstance(ratios, int):
                ratios = [ratios]
            if len(ratios) != len(text):
                raise ValueError("For 'ratio' distribution, 'value' must be provided and match the length of the text list.")

            ratios = np.array(ratios) / np.sum(ratios)  # Normalize ratios to sum to 1
            final_counts = (ratios * total_count).astype(int)

            # Adjust for rounding differences in ratio
            total_assigned = np.sum(final_counts)
            remainder = total_count - total_assigned
            if remainder > 0:
                final_counts[0] += remainder  # Add the remainder to the first text item

        else:
            raise ValueError("The 'dist' key must specify a valid distribution type: 'count' or 'ratio'.")

        # Generate the text column based on the final counts
        text_column = np.concatenate([np.repeat(t, c) for t, c in zip(text, final_counts)])
        np.random.shuffle(text_column)  # Shuffle to randomize the order
        return pd.Series(text_column[:total_count])  # Ensure the length matches 'count'



    # def generate_text(self, col_props, table):
    #     text = col_props['text']
    #     if isinstance(text, str):
    #         text = [text]  # Convert to list if a single string is provided
    #
    #     total_count = col_props.get('count') or len(table)
    #
    #     # Ensure the distribution method is specified
    #     dist = col_props.get('dist')
    #     if dist is None:
    #         raise ValueError("The 'dist' key must be provided.")
    #
    #     # Normalize the distribution values
    #     if dist['type'] == 'count':
    #         counts = dist['value']
    #         # Wrap in a list if it's a single integer
    #         if isinstance(counts, int):
    #             counts = [counts]
    #         if len(counts) != len(text):
    #             raise ValueError("For 'count' distribution, 'value' must be provided and match the length of the text list.")
    #         if sum(counts) != total_count:
    #             raise ValueError("The sum of 'value' must match the total count of rows.")
    #
    #         final_counts = counts
    #
    #     elif dist['type'] == 'ratio':
    #         ratios = dist['value']
    #         # Wrap in a list if it's a single integer
    #         if isinstance(ratios, int):
    #             ratios = [ratios]
    #         if len(ratios) != len(text):
    #             raise ValueError("For 'ratio' distribution, 'value' must be provided and match the length of the text list.")
    #
    #         ratios = np.array(ratios) / np.sum(ratios)  # Normalize ratios to sum to 1
    #         final_counts = (ratios * total_count).astype(int)
    #
    #         # Adjust for rounding differences in ratio
    #         total_assigned = np.sum(final_counts)
    #         remainder = total_count - total_assigned
    #         if remainder > 0:
    #             final_counts[0] += remainder  # Add the remainder to the first text item
    #
    #     else:
    #         raise ValueError("The 'dist' key must specify a valid distribution type: 'count' or 'ratio'.")
    #
    #     # Generate the text column based on the final counts
    #     text_column = np.concatenate([np.repeat(t, c) for t, c in zip(text, final_counts)])
    #     np.random.shuffle(text_column)  # Shuffle to randomize the order
    #     return pd.Series(text_column[:total_count])  # Ensure the length matches 'count'