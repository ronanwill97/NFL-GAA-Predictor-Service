import requests
from bs4 import BeautifulSoup
import json
from datetime import datetime


def fetch_page_content(url: str) -> str:
    """Fetch page content from the given URL."""
    with requests.Session() as session:
        response = session.get(url)
        response.raise_for_status()
        return response.text


def parse_fixture_data(division: int, html_content: str, fixtures: dict) -> dict:
    """Parse fixture data from HTML content."""
    soup = BeautifulSoup(html_content, "html.parser")
    fixtures_section = soup.find("div", class_="fixtures-results-list")

    for fixture in fixtures_section.find_all("div", class_="match-item"):
        fixture_details = extract_fixture_details(fixture)
        if fixture_details is not None:
            league_round, home_team, away_team, date_time = fixture_details
            update_fixtures_dictionary(fixtures, division, league_round, home_team, away_team, date_time)
    return fixtures


def extract_fixture_details(fixture):
    """Extract details of each fixture."""
    league_round = fixture.find("div", class_="round").get_text(strip=True).split("-")[0]
    if league_round == "Final":
        return None
    home_team = fixture.find("div", class_="team-home").text.strip()
    away_team = fixture.find("div", class_="team-away").text.strip()
    date = fixture.find_previous("h3").get_text(strip=True)
    date_time = datetime.strptime(date, '%A %d %B %Y').replace(hour=12, minute=0)
    return league_round, home_team, away_team, date_time


def update_fixtures_dictionary(fixtures, division, league_round, home_team, away_team, date_time):
    """Update the fixtures dictionary with new fixture data."""
    round_info = fixtures.setdefault(league_round, {"fixtures": {}, "deadline": str(date_time)})
    division_fixtures = round_info["fixtures"].setdefault(f"Division {division}", [])
    division_fixtures.append([home_team, away_team])
    deadline = datetime.strptime(round_info["deadline"], '%Y-%m-%d %H:%M:%S')
    if date_time < deadline:
        round_info["deadline"] = str(date_time)


def get_fixtures_by_division(division: int, fixtures: dict) -> dict:
    """Get fixtures by division."""
    url = f"https://www.gaa.ie/football/football-league-roinn-{division}/fixtures"
    try:
        html_content = fetch_page_content(url)
        fixtures = parse_fixture_data(division,html_content, fixtures)
    except requests.RequestException as e:
        print(f"Error fetching data for division {division}: {e}")
    return fixtures
