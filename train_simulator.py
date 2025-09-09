import streamlit as st
import matplotlib.pyplot as plt
import time

# ---------------------------
# Config
# ---------------------------
tracks = [1, 2]  # two tracks
train_length = 2  # time units length for each train

# Example train setup
trains = [
    {"id": "T1", "position": 0, "track": 1, "priority": "High", "hold": False},
    {"id": "T2", "position": 3, "track": 2, "priority": "Medium", "hold": False},
    {"id": "T3", "position": 6, "track": 1, "priority": "Low", "hold": False},
]

# ---------------------------
# Helper: draw trains
# ---------------------------
def plot_trains(trains, t):
    fig, ax = plt.subplots(figsize=(8, 3))
    colors = {"T1": "blue", "T2": "green", "T3": "red"}

    for train in trains:
        start = train["position"]
        end = start + train_length
        ax.plot([start, end], [train["track"], train["track"]],
                color=colors[train["id"]], linewidth=6, solid_capstyle="butt")
        ax.text(start + 1, train["track"] + 0.05,
                train["id"], color="white", weight="bold",
                ha="center", va="bottom", fontsize=10,
                bbox=dict(facecolor=colors[train["id"]], alpha=0.7, pad=2))

    ax.set_xlim(0, 20)
    ax.set_ylim(0.5, len(tracks) + 0.5)
    ax.set_yticks(tracks)
    ax.set_xlabel("Distance (time units)")
    ax.set_ylabel("Track")
    ax.set_title(f"🚆 Train Movements at time {t}")
    st.pyplot(fig)

# ---------------------------
# Streamlit App
# ---------------------------
def main():
    st.title("🚆 Interactive Train Movement Simulator")

    st.write("You can **hold/release trains** below to manage traffic.")

    # Sidebar controls
    for train in trains:
        train["hold"] = st.sidebar.checkbox(f"Hold {train['id']}?", value=False)

    # Simulation speed
    speed = st.sidebar.slider("Simulation speed (sec per step)", 0.1, 1.0, 0.3)

    # Run simulation
    start_btn = st.button("▶ Start Simulation")
    if start_btn:
        placeholder = st.empty()
        for t in range(20):
            # Update train positions
            for train in trains:
                if not train["hold"]:
                    train["position"] += 1  # move forward

            # Draw
            with placeholder.container():
                plot_trains(trains, t)
                time.sleep(speed)

if __name__ == "__main__":
    main()
