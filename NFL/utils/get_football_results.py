import requests
from bs4 import BeautifulSoup
import json
from datetime import datetime
import logging


logger = logging.getLogger("django")

def fetch_page_content(url: str) -> str:
    """Fetch page content from the given URL."""
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.text
    except requests.RequestException as e:
        print(f"Error fetching data: {e}")
        return ""


def parse_results_data(division: int, expected_round: int,year:int, html_content: str, results: dict) -> dict:
    """Parse results data from HTML content."""
    soup = BeautifulSoup(html_content, "html.parser")
    results_section = soup.find("div", class_="fixtures-results-list")

    for result in results_section.find_all("div", class_="match-item"):
        date, league_round = extract_match_details(result)
        if date.year == year and league_round == f"Round {expected_round}":
            logger.info(date)
            home_team, away_team, match_result = extract_match_result(result)
            update_results_dictionary(results, division, league_round, home_team, away_team, match_result)
    return results


def extract_match_details(result):
    """Extract match details from result item."""
    date_text = result.find_previous("h3").get_text(strip=True)
    date = datetime.strptime(date_text, '%A %d %B %Y')
    league_round = result.find("div", class_="round").get_text(strip=True).split("-")[0]
    return date, league_round


def extract_match_result(result):
    """Extract the result of the match."""
    home_team = result.find("div", class_="team-home").get_text(strip=True)
    away_team = result.find("div", class_="team-away").get_text(strip=True)
    score = result.find("div", class_="score").get_text(strip=True)
    home_score, away_score = convert_scores(score.split())

    if home_score > away_score:
        match_result = home_team
    elif away_score > home_score:
        match_result = away_team
    else:
        match_result = "Draw"

    return home_team, away_team, match_result


def convert_scores(scores):
    """Convert scores to numeric values."""
    result = []
    for score in scores:
        goals, points = map(int, score.split('-'))
        result.append(goals * 3 + points)
    return result


def update_results_dictionary(results, division, league_round, home_team, away_team, match_result):
    """Update the results dictionary with new result data."""
    round_info = results.setdefault(league_round, {})
    division_results = round_info.setdefault(f"Division {division}", [])
    division_results.append([home_team, away_team, match_result])


def get_results_by_division(division: int, expected_round: int,year:int,results: dict) -> dict:
    """Get results by division."""
    url = f"https://www.gaa.ie/football/football-league-roinn-{division}/results"
    html_content = fetch_page_content(url)
    if html_content:
        results = parse_results_data(division, expected_round,year, html_content, results)
    return results
