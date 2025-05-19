import streamlit as st

# --- Time estimates and distances per official triathlon format ---
distances = {
    "XS / Super Sprint": {"swim": 9, "bike": 28, "run": 18, "avg": 55, "swim_dist": 0.4, "bike_dist": 10, "run_dist": 2.5},
    "S / Sprint": {"swim": 18, "bike": 40, "run": 28, "avg": 90, "swim_dist": 0.75, "bike_dist": 20, "run_dist": 5},
    "M / Olympic": {"swim": 30, "bike": 80, "run": 50, "avg": 160, "swim_dist": 1.5, "bike_dist": 40, "run_dist": 10},
    "L / Half Ironman": {"swim": 38, "bike": 210, "run": 115, "avg": 360, "swim_dist": 1.9, "bike_dist": 90, "run_dist": 21.1},
    "XL / Ironman": {"swim": 75, "bike": 390, "run": 240, "avg": 750, "swim_dist": 3.8, "bike_dist": 180, "run_dist": 42.2}
}

# Format total minutes into HH:MM
def time_to_str(total_min):
    hours = int(total_min // 60)
    minutes = int(total_min % 60)
    return f"{hours}:{minutes:02d}"

# --- Streamlit interface ---
st.set_page_config(layout="wide")
st.title("Triathlon Time Estimator")

# Distance selection
distance_choice = st.selectbox("Select your race distance:", list(distances.keys()))
current_defaults = distances[distance_choice]

# Layout: input columns and result panel
top_col, result_col = st.columns([3, 1], gap="large")

with top_col:
    st.subheader("Your estimated times")
    col1, col2, col3 = st.columns(3, gap="medium")

    with col1:
        lock_swim = st.checkbox("Lock swim")
        st.caption(f"⏱️ Avg swim time: {time_to_str(current_defaults['swim'])}")
        swim_time = st.slider("Swim time (min)", 5, 120, current_defaults['swim'], disabled=lock_swim)
        swim_pace = swim_time * 100 / (current_defaults['swim_dist'] * 1000)  # min/100m
        st.text(f"🏊 {current_defaults['swim_dist']} km")
        st.text(f"Pace: {swim_pace:.1f} min/100m ({time_to_str(swim_time)})")

    with col2:
        lock_bike = st.checkbox("Lock bike")
        st.caption(f"⏱️ Avg bike time: {time_to_str(current_defaults['bike'])}")
        bike_time = st.slider("Bike time (min)", 10, 420, current_defaults['bike'], disabled=lock_bike)
        bike_speed = current_defaults['bike_dist'] / (bike_time / 60)  # km/h
        st.text(f"🚴 {current_defaults['bike_dist']} km")
        st.text(f"Speed: {bike_speed:.1f} km/h ({time_to_str(bike_time)})")

    with col3:
        lock_run = st.checkbox("Lock run")
        st.caption(f"⏱️ Avg run time: {time_to_str(current_defaults['run'])}")
        run_time = st.slider("Run time (min)", 10, 300, current_defaults['run'], disabled=lock_run)
        run_pace = run_time / current_defaults['run_dist']  # min/km
        st.text(f"🏃 {current_defaults['run_dist']} km")
        st.text(f"Pace: {run_pace:.1f} min/km ({time_to_str(run_time)})")

    target_time_enabled = st.checkbox("Set a target time")
    if target_time_enabled:
        target_time = st.slider("Target total time (min)", 30, 1000, current_defaults['avg'])
        st.caption(f"🎯 Target: {time_to_str(target_time)}")
    else:
        target_time = None

# Calculate total estimated time
total_estimated = swim_time + bike_time + run_time

with result_col:
    st.subheader("Results")
    st.metric("Estimated total time", time_to_str(total_estimated))
    st.metric("Average time for this distance", time_to_str(current_defaults['avg']))

    if target_time_enabled:
        diff = target_time - total_estimated
        st.metric("Difference from target", f"{diff:+.0f} min")

st.markdown("---")
