import json
import pandas as pd
from pathlib import Path

folder = Path("archive-2")
manifest = pd.read_csv(next(folder.rglob("manifest.csv")))
print(manifest.head())

files = sorted(folder.rglob("*.json"))


def first_player(ep):
	for step in ep["steps"]:
		vis = step[0].get("visualize")
		if vis and vis[0]["current"]["firstPlayer"] != -1:
			return vis[0]["current"]["firstPlayer"]
	return None


rows = []
for path in files[:20]:
	with open(path) as f:
		ep = json.load(f)
	rewards = ep["rewards"]
	winner = rewards.index(1) if 1 in rewards else None
	first = first_player(ep)
	rows.append({"file": path.name, "teams": ep["info"].get("TeamNames"),
	             "first": first, "winner": winner,
	             "first_won": first == winner, "n_steps": len(ep["steps"])})

games = pd.DataFrame(rows)
print(games)
print("Share of games won by the first player:", games["first_won"].mean())