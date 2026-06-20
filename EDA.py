import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
# --- Load engineered dataset ---
df_viz = pd.read_csv("C:/Users/HP/3D Objects/Desktop/DA_using_Python/DA Projects/Project 3 (Airport)/Engineered_Features.csv")

# --- VISUALIZATIONS ---
# 1. Airport Health Score by Origin
top_airports = df_viz.groupby("origin")["airport_health_score"].mean().sort_values(ascending=False).head(15)
sns.barplot(x=top_airports.values, y=top_airports.index, palette="viridis")
plt.title("Top 15 Airports by Health Score")
plt.xlabel("Health Score (0–100)")
plt.ylabel("Airport")
plt.tight_layout()
plt.show()

# 2. Disruption Risk Distribution
sns.histplot(df_viz["disruption_risk_score"], bins=30, kde=True, color="steelblue")
plt.title("Distribution of Disruption Risk Score")
plt.xlabel("Risk Score (0–100)")
plt.ylabel("Frequency")
plt.tight_layout()
plt.show()

# 3. Congestion vs Delay Scatter
sns.scatterplot(data=df_viz, x="congestion_index", y="dep_delay", hue="origin", alpha=0.6, palette="coolwarm")
plt.title("Congestion vs Departure Delay")
plt.xlabel("Congestion Index")
plt.ylabel("Departure Delay (minutes)")
plt.legend([],[], frameon=False)  # hide cluttered legend
plt.tight_layout()
plt.show()

# 4. Operational Stress Index by Route (Top 10)
top_routes = df_viz.groupby("route")["operational_stress_index"].mean().sort_values(ascending=False).head(10)
sns.barplot(x=top_routes.values, y=top_routes.index, palette="mako")
plt.title("Top 10 Routes by Operational Stress")
plt.xlabel("Stress Index")
plt.ylabel("Route")
plt.tight_layout()
plt.show()

# 5. Delay Propagation Heatmap (Origin vs Destination)
pivot = df_viz.pivot_table(values="delay_propagation_index", index="origin", columns="dest", aggfunc="mean")
sns.heatmap(pivot, cmap="crest", cbar_kws={"label":"Propagation Index"})
plt.title("Delay Propagation Heatmap (Origin vs Destination)")