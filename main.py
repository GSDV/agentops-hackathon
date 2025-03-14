import asyncio

from dotenv import load_dotenv

from agent_input import run_web_agent

from report import output_report

load_dotenv()



async def fetch_earnings_report(ticker):
    output = await run_web_agent(
        "Earnings Report",
        f"Search the web and find the last quarterly earnings report of {ticker} ticker. Give 3 detailed sentences of how the stock performed at this quarter. If a ticker does not exist, just say that."
    )
    return { "heading": "Earnings", "content": output}

async def fetch_competitors(ticker):
    output = await run_web_agent(
        "Competitors Report",
        f"Find 2-3 competitors of {ticker}. Give 4 detailed sentences on if the competitors are doing stuff that will affect {ticker} ticker."
    )
    return { "heading": "Competitors", "content": output}

async def fetch_ceo_info(ticker):
    output = await run_web_agent(
        "CEO",
        f"Search the web and find information of the CEO of {ticker} ticker. Give 2 detailed sentences of how well of a job the CEO is doing, and what the shareholders think of the him or her."
    )
    return { "heading": "CEO", "content": output}

async def political_activity_info(ticker):
    output = await run_web_agent(
        "Politics",
        f"Search the web and find new, relevant political activity and regulation relating to or affecting {ticker} ticker. Give 3 detailed sentences if the changes will be positive or negative, and how they will affect {ticker} ticker."
    )
    return { "heading": "Politics and Regulation", "content": output}



async def research_ticker():
    ticker = input("Enter a Nasdaq or NYSE ticker to research: ")
    ticker = ticker.upper().strip()
    print("Aggregating report (this may take a minute)...")

    earnings_report = await fetch_earnings_report(ticker)
    competitors_report = await fetch_competitors(ticker)
    political_report = await political_activity_info(ticker)
    ceo_info = await fetch_ceo_info(ticker)
    
    output_report(ticker, [earnings_report, competitors_report, political_report, ceo_info])
    print("Your stock report is ready. Check 'report.md'.")



if __name__ == "__main__":
    asyncio.run(research_ticker())