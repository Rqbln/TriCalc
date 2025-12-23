import streamlit as st

# --- Time estimates and distances per official triathlon format ---
distances = {
    "XS / Super Sprint": {"swim": 9, "bike": 28, "run": 18, "avg": 55, "swim_dist": 0.4, "bike_dist": 10, "run_dist": 2.5, "t1": 2, "t2": 1},
    "S / Sprint": {"swim": 18, "bike": 40, "run": 28, "avg": 90, "swim_dist": 0.75, "bike_dist": 20, "run_dist": 5, "t1": 3, "t2": 2},
    "M / Olympic": {"swim": 30, "bike": 80, "run": 50, "avg": 160, "swim_dist": 1.5, "bike_dist": 40, "run_dist": 10, "t1": 4, "t2": 2},
    "L / Half Ironman": {"swim": 38, "bike": 210, "run": 115, "avg": 360, "swim_dist": 1.9, "bike_dist": 90, "run_dist": 21.1, "t1": 5, "t2": 3},
    "XL / Ironman": {"swim": 75, "bike": 390, "run": 240, "avg": 750, "swim_dist": 3.8, "bike_dist": 180, "run_dist": 42.2, "t1": 8, "t2": 5}
}

# Format total minutes into HH:MM
def time_to_str(total_min):
    hours = int(total_min // 60)
    minutes = int(total_min % 60)
    return f"{hours}:{minutes:02d}"

# Format percentage difference with color
def format_diff(pct_diff):
    if pct_diff > 0:
        return f":green[{pct_diff:+.1f}% faster than avg]"
    elif pct_diff < 0:
        return f":red[{pct_diff:+.1f}% slower than avg]"
    else:
        return f":gray[On average pace]"

# --- Streamlit interface ---
st.set_page_config(layout="wide", page_title="TriCalc - Triathlon Calculator", page_icon="🏊")
st.title("🏊🚴🏃 TriCalc - Triathlon Time Estimator")

# Distance selection
st.markdown("### 📏 Select your race distance")
distance_choice = st.selectbox("Race distance:", list(distances.keys()), label_visibility="collapsed")
current_defaults = distances[distance_choice]

# Show distance info
st.info(f"**{distance_choice}**: {current_defaults['swim_dist']}km swim · {current_defaults['bike_dist']}km bike · {current_defaults['run_dist']}km run")

st.divider()

# Layout: input columns and result panel
top_col, result_col = st.columns([3, 1], gap="large")

with top_col:
    st.subheader("⏱️ Your estimated times")
    col1, col2, col3 = st.columns(3, gap="medium")

    with col1:
        st.markdown("#### 🏊 Swim")
        lock_swim = st.checkbox("🔒 Lock swim time", help="Lock this time when adjusting other disciplines")
        st.caption(f"📊 Average: **{time_to_str(current_defaults['swim'])}** for {current_defaults['swim_dist']}km")
        swim_time = st.slider("Swim time (min)", 5, 120, current_defaults['swim'], disabled=lock_swim, help="Adjust your estimated swim time")
        swim_pace = swim_time * 100 / (current_defaults['swim_dist'] * 1000)
        pace_min = int(swim_pace)
        pace_sec = int((swim_pace - pace_min) * 60)
        swim_pct_diff = ((current_defaults['swim'] - swim_time) / current_defaults['swim']) * 100
        st.metric(label="Your pace", value=f"{pace_min}:{pace_sec:02d}/100m", delta=f"{time_to_str(swim_time)} total")
        st.markdown(format_diff(swim_pct_diff))

    with col2:
        st.markdown("#### 🚴 Bike")
        lock_bike = st.checkbox("🔒 Lock bike time", help="Lock this time when adjusting other disciplines")
        st.caption(f"📊 Average: **{time_to_str(current_defaults['bike'])}** for {current_defaults['bike_dist']}km")
        bike_time = st.slider("Bike time (min)", 10, 420, current_defaults['bike'], disabled=lock_bike, help="Adjust your estimated bike time")
        bike_speed = current_defaults['bike_dist'] / (bike_time / 60)
        bike_pct_diff = ((current_defaults['bike'] - bike_time) / current_defaults['bike']) * 100
        st.metric(label="Your speed", value=f"{bike_speed:.1f} km/h", delta=f"{time_to_str(bike_time)} total")
        st.markdown(format_diff(bike_pct_diff))

    with col3:
        st.markdown("#### 🏃 Run")
        lock_run = st.checkbox("🔒 Lock run time", help="Lock this time when adjusting other disciplines")
        st.caption(f"📊 Average: **{time_to_str(current_defaults['run'])}** for {current_defaults['run_dist']}km")
        run_time = st.slider("Run time (min)", 10, 300, current_defaults['run'], disabled=lock_run, help="Adjust your estimated run time")
        run_pace = run_time / current_defaults['run_dist']
        pace_min = int(run_pace)
        pace_sec = int((run_pace - pace_min) * 60)
        run_pct_diff = ((current_defaults['run'] - run_time) / current_defaults['run']) * 100
        st.metric(label="Your pace", value=f"{pace_min}:{pace_sec:02d}/km", delta=f"{time_to_str(run_time)} total")
        st.markdown(format_diff(run_pct_diff))

    st.divider()
    
    # Transition times section
    st.subheader("🔄 Transition times")
    t_col1, t_col2 = st.columns(2)
    with t_col1:
        t1_time = st.slider("T1 - Swim to Bike (min)", 1, 15, current_defaults['t1'], help="Time to transition from swim to bike")
    with t_col2:
        t2_time = st.slider("T2 - Bike to Run (min)", 1, 10, current_defaults['t2'], help="Time to transition from bike to run")
    
    st.divider()

    # Target time section
    target_time_enabled = st.checkbox("🎯 Set a target time", help="Set a goal time to compare against your estimate")
    if target_time_enabled:
        target_time = st.slider("Target total time (min)", 30, 1000, current_defaults['avg'])
        target_pct_diff = ((current_defaults['avg'] - target_time) / current_defaults['avg']) * 100
        st.caption(f"🎯 Target: **{time_to_str(target_time)}** ({target_pct_diff:+.1f}% vs average)")
    else:
        target_time = None

# Calculate total estimated time (including transitions)
transition_time = t1_time + t2_time
total_estimated = swim_time + bike_time + run_time + transition_time
total_without_transitions = swim_time + bike_time + run_time

with result_col:
    st.subheader("📊 Results")
    
    # Main result with large display
    total_diff = current_defaults['avg'] - total_estimated
    st.metric(
        "🏁 Estimated total time", 
        time_to_str(total_estimated),
        delta=f"{total_diff:+.0f} min vs avg" if total_diff != 0 else "On average",
        delta_color="normal"
    )
    
    st.caption(f"Disciplines: {time_to_str(total_without_transitions)} + Transitions: {transition_time} min")
    
    st.divider()
    
    st.metric("📈 Average for this distance", time_to_str(current_defaults['avg']))

    if target_time_enabled:
        diff = target_time - total_estimated
        if diff >= 0:
            st.success(f"✅ **{abs(diff):.0f} min under target!**")
        else:
            st.error(f"⚠️ **{abs(diff):.0f} min over target**")
    
    st.divider()
    
    # Time breakdown visualization
    st.markdown("**⏱️ Time breakdown:**")
    swim_pct = (swim_time / total_estimated) * 100
    bike_pct = (bike_time / total_estimated) * 100
    run_pct = (run_time / total_estimated) * 100
    trans_pct = (transition_time / total_estimated) * 100
    
    st.progress(swim_pct / 100, text=f"🏊 Swim: {swim_pct:.0f}%")
    st.progress(bike_pct / 100, text=f"🚴 Bike: {bike_pct:.0f}%")
    st.progress(run_pct / 100, text=f"🏃 Run: {run_pct:.0f}%")
    st.progress(trans_pct / 100, text=f"🔄 T1+T2: {trans_pct:.0f}%")
