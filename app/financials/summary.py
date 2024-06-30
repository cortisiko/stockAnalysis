"""
This module provides functions to retrieve and process key statistics and summary details.
It includes functions to get key statistics, summary details, EPS, and PE ratio.

Functions:
    key_stats_data(ticker_object: Any) -> Optional[Dict[str, Any]]
    summary_details_data(ticker_object: Any) -> Optional[Dict[str, Any]]
    earnings_per_share(ticker_object: Any, ticker_symbol: str) -> Optional[float]
    get_pe_ratio(ticker_object: Any, ticker_symbol: str) -> Optional[float]
"""
import logging
from typing import Optional, Dict, Any

# Set up logging
logging.basicConfig(level=logging.ERROR, format='%(asctime)s - %(levelname)s - %(message)s')
# This is the summary tab

def key_stats_data(ticker_object: Any) -> Optional[Dict[str, Any]]:
    """
    Get key statistics data for a given ticker object.

    Args:
        ticker_object (object): The ticker object.

    Returns:
        dict: A dictionary containing key statistics data.
    """
    try:
        return ticker_object.key_stats
    except AttributeError as e:
        logging.error("Failed to retrieve key statistics data: %s", e)
        return None


def summary_details_data(ticker_object: Any) -> Optional[Dict[str, Any]]:
    """
    Get summary details data for a given ticker object.

    Args:
        ticker_object (object): The ticker object.

    Returns:
        dict: A dictionary containing summary details data.
    """
    try:
        return ticker_object.summary_detail
    except AttributeError as e:
        logging.error("Failed to retrieve summary details data: %s", e)
        return None


def earnings_per_share(ticker_object: Any, ticker_symbol: str) -> Optional[float]:
    """
    Get the earnings per share (EPS) for a given ticker object and symbol.

    Args:
        ticker_object (object): The ticker object.
        ticker_symbol (str): The stock ticker symbol.

    Returns:
        float: The trailing earnings per share rounded to 2 decimal places.
    """
    try:
        key_stats = key_stats_data(ticker_object)
        if key_stats:
            trailing_earning_per_share = key_stats.get(ticker_symbol, {}).get("trailingEps")
            if trailing_earning_per_share is not None:
                return round(float(trailing_earning_per_share), 2)
            logging.warning("No EPS found for ticker symbol: %s", ticker_symbol)

        return None
    except (AttributeError, KeyError) as e:
        logging.error("Failed to retrieve EPS for %s: %s", ticker_symbol, e)
        return None


def get_pe_ratio(ticker_object: Any, ticker_symbol: str) -> Optional[float]:
    """
    Get the price-to-earnings (PE) ratio for a given ticker object and symbol.

    Args:
        ticker_object (object): The ticker object.
        ticker_symbol (str): The stock ticker symbol.

    Returns:
        float: The PE ratio rounded to 2 decimal places.
    """
    try:
        summary_data = summary_details_data(ticker_object)
        if summary_data:
            pe_ratio = summary_data.get(ticker_symbol, {}).get("trailingPE")
            if pe_ratio is not None:
                return round(float(pe_ratio), 2)
            logging.warning(f"No PE ratio found for ticker symbol %s: {ticker_symbol}")
        return None
    except (AttributeError, KeyError) as e:
        logging.error(f"Failed to retrieve PE ratio for %s: %s: {ticker_symbol}: {e}")
        return None
