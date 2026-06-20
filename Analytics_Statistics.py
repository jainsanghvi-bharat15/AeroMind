import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from scipy import stats

# Load engineered dataset
df = pd.read_csv("C:/Users/HP/3D Objects/Desktop/DA_using_Python/DA Projects/Project 3 (Airport)/Feature & EDA/Engineered_Features.csv")

# --- 1. CORRELATION ANALYSIS ---
corr_vars = ["dep_delay","arr_delay","carrier_delay","weather_delay",
             "nas_delay","security_delay","late_aircraft_delay",
             "congestion_index","operational_stress_index"]
corr_matrix = df[corr_vars].corr()
sns.heatmap(corr_matrix, annot=True, cmap="crest", cbar_kws={"label":"Correlation"})
plt.title("Correlation Matrix of Delay Drivers")
plt.tight_layout()
plt.show()

# --- 2. CONTRIBUTION ANALYSIS ---
delay_contrib = df[["carrier_delay","weather_delay","nas_delay", "security_delay","late_aircraft_delay"]].sum()
delay_contrib = delay_contrib / delay_contrib.sum() * 100
sns.barplot(x=delay_contrib.values, y=delay_contrib.index, palette="viridis")
plt.title("Contribution of Delay Causes (%)")
plt.xlabel("Percentage Contribution")
plt.ylabel("Delay Cause")
plt.tight_layout()
plt.show()

# --- 3. STATISTICAL TESTING ---
# H1: Weather significantly impacts delays
weather_corr, pval_weather = stats.pearsonr(df["weather_delay"], df["arr_delay"])
print(f"H1 Test: Correlation={weather_corr:.3f}, p-value={pval_weather:.5f}")

# H2: Weekend delays exceed weekday delays
df["is_weekend"] = df["day_of_week"].isin([6,7]).astype(int)
weekend_delays = df[df["is_weekend"]==1]["arr_delay"]
weekday_delays = df[df["is_weekend"]==0]["arr_delay"]
tstat, pval_weekend = stats.ttest_ind(weekend_delays, weekday_delays, equal_var=False)
print(f"H2 Test: t-stat={tstat:.3f}, p-value={pval_weekend:.5f}")

# H3: Route length vs delay propagation
route_corr, pval_route = stats.pearsonr(df["distance"], df["delay_propagation_index"])
print(f"H3 Test: Correlation={route_corr:.3f}, p-value={pval_route:.5f}")

# H4: Carrier reliability differences
carrier_perf = df.groupby("op_unique_carrier")["on_time_flag"].mean()
sns.barplot(x=carrier_perf.values, y=carrier_perf.index, palette="mako")
plt.title("Carrier On-Time Reliability")
plt.xlabel("On-Time Performance (%)")
plt.ylabel("Carrier")
plt.tight_layout()
plt.show()