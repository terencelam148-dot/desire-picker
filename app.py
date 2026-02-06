import streamlit as st
import random

# --- Punishment lists (feel free to edit/add more) ---
medium_punishments = [
    "20 hard spanks (count aloud and thank the Winner for each one).",
    "Edge the Winner for 10 minutes (bring to the brink, stop, repeat 3 times – no release for you).",
    "Naked corner time (5 minutes, hands behind head, describe your arousal out loud in detail).",
    "Worship the Winner's feet/toes for 5 minutes (lick, suck, massage with devotion).",
    "Ice cube tease on sensitive spots (nipples, cock, balls) for 3–5 minutes.",
    "Hold a coin against the wall with your nose for 5 minutes (drop = +5 extra spanks).",
    "Beg on your knees for permission to touch yourself (3 minutes of desperate pleading).",
    "Nipple clamps + light tugging while reciting 10 genuine compliments to the Winner.",
    "Eat dessert off the Winner's body using only your mouth (no hands allowed).",
    "Alternate hot breath and ice on the Winner's cock while you stay completely denied."
]

spicy_punishments = [
    "Full-body oil rubdown + total denial (touch everywhere except the cock for 15 minutes).",
    "Mouth-only service to the Winner (deepthroat training, no hands, 10 minutes timed).",
    "Bound (cuffs + ankles) while the Winner uses a remote toy to edge you (if you own one).",
    "Verbal humiliation: Recite 'I'm your teased slut' 20 times while being stroked but forbidden to cum.",
    "Feet punishment: Blindfolded foot massage + lick Winner's feet + light tickle torture for 5–7 minutes.",
    "Collar and leash: Crawl around the room for 5 laps while the Winner leads you.",
    "Edging marathon: Bring the Winner to the edge 5 times with hands/mouth – you get nothing.",
    "Forced exposure: Stand naked describing your submission fantasy aloud (or near window if private).",
    "Spreader bar + tease: Legs apart, Winner teases with feather/toy/vibrator for 10 minutes.",
    "Write 'Property of [Winner's name]' on your body with washable marker – keep it on all night."
]

extreme_punishments = [
    "Chastity lock: Cock caged (if you have a device) for 1–24 hours – Winner keeps the key.",
    "Impact session: Caning/paddling/flogging (10–20 strikes on thighs/ass – count + beg for each).",
    "Forced denial torture: Tied spread-eagle, edged repeatedly for 30+ minutes, ruined orgasm only.",
    "Human furniture service: Act as table/footrest for 20 minutes + oral worship whenever commanded.",
    "Humiliation ritual: Crawl, beg to cum, perform a slow striptease confessing body insecurities/fantasies.",
    "Intense oral: Winner face-fucks you (controlled & safe) for 10 minutes while you recount your 'loser moments'.",
    "Overnight submission: Sleep cuffed/collar, woken with edging in the morning.",
    "Sensory deprivation + tease: Blindfold + earplugs + tied, randomly teased for 30 minutes.",
    "Cum control challenge: Allowed to cum only after completing 3 extra tasks chosen by Winner.",
    "Total surrender: 1-hour 'slave mode' – obey every command, address Winner as Sir/Master/etc."
]

# --- App UI ---
st.set_page_config(page_title="Hidden Desires Punishment Picker", layout="centered")

st.title("Hidden Desires 🔥 Random Punishment Picker")
st.markdown("Enter the **point deficit** (how many more points the winner has). Then hit 'Reveal Punishment'.")

deficit = st.number_input("Point deficit (1 or more)", min_value=1, step=1, value=1)

if st.button("Reveal Punishment", type="primary"):
    if deficit <= 3:
        level = "Medium 🔥"
        punishment = random.choice(medium_punishments)
    elif deficit <= 6:
        level = "Spicy 🌶️"
        punishment = random.choice(spicy_punishments)
    else:
        level = "Extreme ⚡"
        punishment = random.choice(extreme_punishments)
    
    st.subheader(level)
    st.markdown(f"**Deficit {deficit}** → {punishment}")
    
    st.info("Remember: Safe words first ('red' = stop, 'yellow' = slow down). Aftercare always!")

st.markdown("---")
st.caption("Built for Hidden Desires game • Consent & fun only • Edit punishments in code anytime")
