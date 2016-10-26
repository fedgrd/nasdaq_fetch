"""
Fetch last sale data from Nasdaq.
Author: Federico Giordani
"""

from page_range_ns import page_range

tick = str(raw_input('Please specify stock ticker: ').lower())
page_range(tick)
