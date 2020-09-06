'''
Description:
We have a sequence of books: the i-th book has thickness books[i][0] and height books[i][1].
We want to place these books in order onto bookcase shelves that have total width shelf_width.
We choose some of the books to place on this shelf (such that the sum of their thickness is <= shelf_width), then build another level of shelf of the bookcase so that the total height of the bookcase has increased by the maximum height of the books we just put down.  We repeat this process until there are no more books to place.
Note again that at each step of the above process, the order of the books we place is the same order as the given sequence of books.  For example, if we have an ordered list of 5 books, we might place the first and second book onto the first shelf, the third book on the second shelf, and the fourth and fifth book on the last shelf.
Return the minimum possible height that the total bookshelf can be after placing shelves in this manner.
'''


class Solution:
    def minHeightShelves(self, books: List[List[int]], shelf_width: int) -> int:

        min_heights = [0] * (len(books))
        min_heights[0] = books[0][1]

        for book_idx in range(1, len(books)):

            # Case 1: New row
            min_heights[book_idx] = min_heights[book_idx - 1] + books[book_idx][1]

            # Case 2: Move previous book to the current row
            current_book_idx = book_idx
            new_row_width = 0

            while current_book_idx >= 0 and new_row_width < shelf_width:

                current_height = min_heights[current_book_idx - 1] + max(
                    [books[idx][1] for idx in range(current_book_idx, book_idx + 1)]) if current_book_idx > 0 else max(
                    [books[idx][1] for idx in range(current_book_idx, book_idx + 1)])

                new_row_width = sum([books[idx][0] for idx in range(current_book_idx, book_idx + 1)])

                if current_height < min_heights[book_idx] and new_row_width <= shelf_width:
                    min_heights[book_idx] = current_height

                current_book_idx -= 1

        return min_heights[-1]