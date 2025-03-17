import streamlit as st
from datetime import datetime, timedelta
import os
from dotenv import load_dotenv
import pandas as pd
from pysh import Client

# Load environment variables
load_dotenv()

# Initialize Phish.net client
API_KEY = os.getenv("PHISHNET_API_KEY")
if not API_KEY:
    st.error("⚠️ PHISHNET_API_KEY not found in environment variables. Please set it in your .env file.")
    st.stop()

client = Client(apikey=API_KEY)

def get_show_by_date(date):
    """Fetch show information for a specific date."""
    formatted_date = date.strftime("%Y-%m-%d")
    shows = client.get_shows(column="showdate", value=formatted_date)
    
    if not shows:
        return None
        
    return shows[0]  # Return the first show if any exist

def get_setlist_by_date(date):
    """Fetch setlist information for a specific date."""
    formatted_date = date.strftime("%Y-%m-%d")
    setlists = client.get_setlists(column="showdate", value=formatted_date)
    
    if not setlists:
        return None
    
    # Get the show ID from the first setlist
    show_id = setlists[0].get('showid')
    if not show_id:
        return None
        
    # Get all songs for this show
    songs = client.get_setlists(column="showid", value=show_id)
    
    if not songs:
        return None
        
    return songs  # Return all songs for the show

def display_setlist(setlist_data):
    """Display setlist information in a formatted way."""
    if not setlist_data:
        st.warning("No setlist data available for this date.")
        return

    if not isinstance(setlist_data, list):
        st.warning("Invalid setlist data format. Expected list.")
        st.write("Received data type:", type(setlist_data))
        return

    # Group songs by set
    sets = {}
    for song in setlist_data:
        if not isinstance(song, dict):
            continue
            
        set_num = song.get('set', 'E')  # 'E' for encore if not specified
        if set_num not in sets:
            sets[set_num] = []
        sets[set_num].append(song)

    if not sets:
        st.warning("No songs found in the setlist data.")
        return

    # Sort sets and display each one
    for set_num in sorted(sets.keys()):
        set_name = "Set Encore" if set_num == 'E' else f"Set {set_num}"
        st.subheader(set_name)
        
        # Create a DataFrame for the set
        set_songs = []
        for song in sorted(sets[set_num], key=lambda x: x.get('position', 0)):
            transition = "→" if song.get('transition') == 1 else ""
            set_songs.append({
                'Position': song.get('position', ''),
                'Song': song.get('song', 'Unknown') + transition,
                'Notes': song.get('footnote', '')
            })
        
        if set_songs:
            df = pd.DataFrame(set_songs)
            st.dataframe(df, use_container_width=True, hide_index=True)

def main():
    st.title("🎸 Phish.net Setlist Explorer")
    st.write("Select a date to view Phish setlist information")

    # Date selection
    today = datetime.now()
    min_date = datetime(1983, 12, 2)  # Phish's first show
    max_date = today + timedelta(days=30)  # Allow future dates for upcoming shows
    
    selected_date = st.date_input(
        "Select a date",
        value=datetime(1999, 7, 24),  # Set default to July 24, 1999
        min_value=min_date,
        max_value=max_date
    )

    if selected_date:
        st.subheader(f"Show Information for {selected_date.strftime('%B %d, %Y')}")
        
        # Fetch and display show information
        show_data = get_show_by_date(selected_date)
        if show_data and isinstance(show_data, dict):
            col1, col2 = st.columns(2)
            with col1:
                st.write("**Venue:**", show_data.get('venue', 'Unknown'))
                st.write("**Location:**", f"{show_data.get('city', 'Unknown')}, {show_data.get('state', 'Unknown')}")
            with col2:
                st.write("**Show ID:**", show_data.get('showid', 'Unknown'))
                st.write("**Artist:**", show_data.get('artist_name', 'Unknown'))
        else:
            st.warning("No show information available for this date.")
        
        # Fetch and display setlist information
        setlist_data = get_setlist_by_date(selected_date)
        display_setlist(setlist_data)

if __name__ == "__main__":
    main() 