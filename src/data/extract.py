import yfinance as yf
import pandas as pd
from pathlib import Path
import logging
from datetime import datetime
from typing import List, Dict

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

def download_asset_data(
    tickers: List[str], 
    start_date: str = "2018-01-01", 
    end_date: str = "2025-06-12",
    output_dir: str = "data/raw"
) -> Dict[str, pd.DataFrame]:
    
    # Create output directory if it doesn't exist
    Path(output_dir).mkdir(parents=True, exist_ok=True)
    
    data_dict = {}
    failed_downloads = []
    
    logger.info(f"Starting download for {len(tickers)} assets from {start_date} to {end_date}")
    
    for ticker in tickers:
        try:
            logger.info(f"Downloading {ticker}...")
            
            # Download data
            data = yf.download(
                ticker, 
                start=start_date, 
                end=end_date,
                progress=False
            )
            
            if data.empty:
                logger.warning(f"No data found for {ticker}")
                failed_downloads.append(ticker)
                continue
            
            # Clean column names (remove multi-level if present)
            if isinstance(data.columns, pd.MultiIndex):
                data.columns = data.columns.droplevel(1)
            
            # Add ticker column for identification
            data['Ticker'] = ticker
            
            # Store in dictionary
            data_dict[ticker] = data
            
            # Save individual CSV file
            output_path = Path(output_dir) / f"{ticker.replace('-', '_')}_raw.csv"
            data.to_csv(output_path)
            
            logger.info(f"✓ {ticker}: {len(data)} rows saved to {output_path}")
            
        except Exception as e:
            logger.error(f"Failed to download {ticker}: {str(e)}")
            failed_downloads.append(ticker)
    
    # Summary
    successful_downloads = len(tickers) - len(failed_downloads)
    logger.info(f"Download complete: {successful_downloads}/{len(tickers)} successful")
    
    if failed_downloads:
        logger.warning(f"Failed downloads: {failed_downloads}")
    
    return data_dict

def main():
    """
    Main execution function - downloads all assets as per research specification.
    """
    
    # Asset universe from research statement
    ASSETS = [
        # Crypto
        "BTC-USD",
        "ETH-USD",
        # Traditional Markets
        "SPY",      # US equities
        "QQQ",      # Tech-heavy equities
        "^VIX",      # Implied volatility
        "GLD",      # Gold ETF (safe haven)
        "TLT"       # 20-year Treasury ETF (safe haven)
    ]
    
    # Time parameters from research statement
    START_DATE = "2018-01-01"
    END_DATE = "2025-06-12"
    OUTPUT_DIR = "data/raw"
    
    logger.info("=== CRYPTO VS TRADITIONAL FINANCE DATA EXTRACTION ===")
    logger.info(f"Research timeframe: {START_DATE} to {END_DATE}")
    logger.info(f"Assets to download: {ASSETS}")
    
    # Download data
    asset_data = download_asset_data(
        tickers=ASSETS,
        start_date=START_DATE,
        end_date=END_DATE,
        output_dir=OUTPUT_DIR
    )
    
    # Create combined dataset
    if asset_data:
        combined_data = pd.concat(asset_data.values(), ignore_index=True)
        combined_path = Path(OUTPUT_DIR) / "all_assets_raw.csv"
        combined_data.to_csv(combined_path, index=False)
        logger.info(f"Combined dataset saved: {combined_path} ({len(combined_data)} total rows)")
    
    logger.info("=== EXTRACTION COMPLETE ===")

if __name__ == "__main__":
    main()