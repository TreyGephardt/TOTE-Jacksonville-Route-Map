import plotly.graph_objects as go

cities = {
    "Jacksonville": (-81.66, 30.33),
    "San Juan":     (-66.11, 18.47),
    "Seattle":      (-122.33, 47.61),
    "Portland":     (-122.68, 45.52),
    "Oakland":      (-122.27, 37.80),
    "Los Angeles":  (-118.24, 34.05),
    "Salt Lake City": (-111.89, 40.76),
    "Denver":       (-104.99, 39.74),
    "El Paso":      (-106.49, 31.76),
    "Dallas":       (-96.80, 32.78),
    "Minneapolis":  (-93.27, 44.98),
    "Chicago":      (-87.63, 41.88),
    "Memphis":      (-90.05, 35.15),
    "Atlanta":      (-84.39, 33.75),
    "Baltimore":    (-76.61, 39.29),
    "Syracuse":     (-76.15, 43.05),
    "Kearny":       (-74.11, 40.77),
}

red_cities = [
    "Seattle", "Portland", "Oakland", "Los Angeles",
    "Salt Lake City", "Denver", "El Paso", "Dallas",
    "Minneapolis", "Chicago", "Memphis", "Atlanta",
    "Baltimore", "Syracuse", "Kearny"
]

jax = cities["Jacksonville"]
sju = cities["San Juan"]

fig = go.Figure()

# Red dashed lines to Jacksonville
for city in red_cities:
    lon, lat = cities[city]
    fig.add_trace(go.Scattergeo(
        lon=[lon, jax[0]],
        lat=[lat, jax[1]],
        mode="lines",
        line=dict(color="#ff4444", width=1.5, dash="dash"),
        showlegend=False
    ))

# Tan dashed line Jacksonville to San Juan
fig.add_trace(go.Scattergeo(
    lon=[jax[0], sju[0]],
    lat=[jax[1], sju[1]],
    mode="lines",
    line=dict(color="#c8a96e", width=2, dash="dash"),
    showlegend=False
))

# Regular city dots
reg_lons = [cities[c][0] for c in red_cities]
reg_lats = [cities[c][1] for c in red_cities]
reg_names = list(red_cities)

fig.add_trace(go.Scattergeo(
    lon=reg_lons,
    lat=reg_lats,
    mode="markers+text",
    marker=dict(size=8, color="#4488ff", line=dict(color="white", width=1)),
    text=reg_names,
    textposition="top right",
    textfont=dict(color="white", size=10),
    showlegend=False
))

# Jacksonville and San Juan
fig.add_trace(go.Scattergeo(
    lon=[jax[0], sju[0]],
    lat=[jax[1], sju[1]],
    mode="markers+text",
    marker=dict(size=14, color="#ff4444", line=dict(color="white", width=1.5)),
    text=["Jacksonville", "San Juan"],
    textposition="middle right",
    textfont=dict(color="white", size=13, family="Arial Black"),
    showlegend=False
))

fig.update_layout(
    geo=dict(
        scope="world",
        projection_type="mercator",
        showland=True,
        landcolor="#1a3a5c",
        showocean=True,
        oceancolor="#0a1f44",
        showlakes=True,
        lakecolor="#0a1f44",
        showsubunits=True,
        subunitcolor="white",
        subunitwidth=0.5,
        countrycolor="white",
        countrywidth=0.8,
        bgcolor="#0a1f44",
        lataxis_range=[15, 55],
        lonaxis_range=[-130, -60],
        resolution=50,
    ),
    paper_bgcolor="#0a1f44",
    title=dict(text="Jacksonville Route Map", font=dict(color="white", size=16)),
    margin=dict(l=0, r=0, t=40, b=0),
    height=600
)

fig.show()
