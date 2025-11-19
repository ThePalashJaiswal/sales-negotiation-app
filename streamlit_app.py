import streamlit as st

# =========================
# DATA: Modules, Lessons, Quizzes, Scenarios
# =========================

MODULES = [
    {
        "id": "M1",
        "title": "Why This Training Matters",
        "description": "Mindset shift: conversations, not just selling.",
        "order": 1,
    },
    {
        "id": "M2",
        "title": "Cold Calling Excellence",
        "description": "Mindset, hooks, ghosting, objections, next steps.",
        "order": 2,
    },
    {
        "id": "M3",
        "title": "Negotiation Mastery",
        "description": "Harvard-style negotiation: interests, fairness, win–win.",
        "order": 3,
    },
    {
        "id": "M4",
        "title": "Role-Play & Use Cases",
        "description": "Practice real-life call and negotiation scenarios.",
        "order": 4,
    },
]

LESSONS = [
    # ----- M1: Mindset -----
    {
        "id": "L1",
        "module_id": "M1",
        "title": "Your Voice is Your First Impression",
        "content": """
In sales, your **voice is your first impression**.

- The prospect hears your tone *before* they process your words.
- Great callers don't just pitch; they start meaningful conversations.
- Negotiation is not about *winning*; it's about **creating value on both sides**.

Ask yourself:
> “Do I sound rushed, needy, or calm and confident?”
""",
        "quiz_id": "Q1",
        "order": 1,
    },
    {
        "id": "L2",
        "module_id": "M1",
        "title": "Conversations Build Conversions",
        "content": """
**Sales is not about convincing — it's about connecting.**

Great callers:
- Ask questions.
- Listen more than they speak.
- Treat every call as a conversation, not a battle.

If you remember only one line:
> **"Conversations build conversions."**
""",
        "quiz_id": "Q2",
        "order": 2,
    },

    # ----- M2: Cold Calling Excellence -----
    {
        "id": "L3",
        "module_id": "M2",
        "title": "Rule #1 – Never Cut the Call",
        "content": """
**Rule #1: Never cut the call first.**

- Always let the **prospect** end the call.
- Your patience reflects professionalism.
- Confidence = **Preparation + Calm + Curiosity**.

BATNA mindset:
- Go into the call knowing you have other options.
- That keeps your tone relaxed, not desperate.
""",
        "quiz_id": "Q3",
        "order": 1,
    },
    {
        "id": "L4",
        "module_id": "M2",
        "title": "The Opening Hook – First 30 Seconds",
        "content": """
Make the **first 30 seconds** count.

**Example Script:**

> *“Hi, this is [Name] from Judiciary Gold. This is a cold call — do you have 30 seconds for me?”*

Rules:
- Respect their time.
- Be transparent that it's a cold call.
- Be confident, **not** apologetic.

Most prospects prefer honesty over tricks.
""",
        "quiz_id": "Q4",
        "order": 2,
    },
    {
        "id": "L5",
        "module_id": "M2",
        "title": "Handling Ghosting the Right Way",
        "content": """
When a prospect goes silent, **don't guilt-trip** them.

❌ Wrong approach:
> *“What happened? You said you'd sign!”*

✅ Right approach:
> *“Hey, I missed you last week — did you figure out the solution you were exploring?”*

Principles:
- Be friendly, not frustrated.
- People respond to **warmth**, not pressure.
""",
        "quiz_id": "Q5",
        "order": 3,
    },

    # ----- M3: Negotiation Mastery -----
    {
        "id": "L6",
        "module_id": "M3",
        "title": "Interests vs Positions",
        "content": """
Framework adapted from the **Harvard Negotiation Project**.

**Positions** = what people *say* they want.  
**Interests** = why they want it.

Example: Two men fight over a window.

- Position 1: “Open it.”
- Position 2: “Keep it closed.”

Interests:
- One wants fresh air.
- The other hates wind on his papers.

Solution:
- Open another window or adjust seating → **both win**.

Ask “**Why?**” multiple times to uncover real needs.
""",
        "quiz_id": "Q6",
        "order": 1,
    },
    {
        "id": "L7",
        "module_id": "M3",
        "title": "Use Fair Standards",
        "content": """
Use **objective criteria** to avoid ego battles.

Examples:
- Market rates
- Past precedents
- Industry benchmarks

Instead of:
> “I deserve more” vs “We can’t pay that.”

Say:
> “Let’s check the average market rate for this scope and align on what’s fair.”

Like dividing cake:
- One cuts, the other chooses → fairness built into the process.
""",
        "quiz_id": "Q7",
        "order": 2,
    },
]

QUIZZES = [
    {
        "id": "Q1",
        "lesson_id": "L1",
        "question": "In sales, what is usually your first impression on a call?",
        "options": [
            "Your company name",
            "Your voice and tone",
            "Your pricing",
            "Your email signature",
        ],
        "correct_index": 1,
    },
    {
        "id": "Q2",
        "lesson_id": "L2",
        "question": "According to this training, sales is mainly about…",
        "options": [
            "Convincing people aggressively",
            "Memorising scripts",
            "Connecting through conversations",
            "Sending more follow-up emails",
        ],
        "correct_index": 2,
    },
    {
        "id": "Q3",
        "lesson_id": "L3",
        "question": "Who should usually end the call in a cold call?",
        "options": [
            "You, to save time",
            "The prospect",
            "Whoever spoke last",
            "It doesn’t matter",
        ],
        "correct_index": 1,
    },
    {
        "id": "Q4",
        "lesson_id": "L4",
        "question": "What is the best opening style for a cold call?",
        "options": [
            "Hide that it’s a cold call",
            "Apologise a lot for disturbing",
            "Be transparent and ask for 30 seconds",
            "Start pitching immediately",
        ],
        "correct_index": 2,
    },
    {
        "id": "Q5",
        "lesson_id": "L5",
        "question": "When handling ghosting, you should sound…",
        "options": [
            "Accusing and firm",
            "Cold and robotic",
            "Friendly and low-pressure",
            "Sarcastic and witty",
        ],
        "correct_index": 2,
    },
    {
        "id": "Q6",
        "lesson_id": "L6",
        "question": "In the window example, what solved the problem?",
        "options": [
            "Flipping a coin",
            "Alternating open/close every hour",
            "Finding a solution that met both interests",
            "Letting the louder person win",
        ],
        "correct_index": 2,
    },
    {
        "id": "Q7",
        "lesson_id": "L7",
        "question": "Using fair standards means relying on…",
        "options": [
            "Market rates and objective criteria",
            "Who negotiates harder",
            "Seniority only",
            "Random discounts",
        ],
        "correct_index": 0,
    },
]

SCENARIOS = [
    {
        "id": "S1",
        "type": "Cold Call",
        "title": "The Busy Prospect – 'Call Me Monday'",
        "setup": "Prospect says, 'Call me Monday.' You suspect they may just be brushing you off.",
        "prompt": "How will you respond **now** to check intent instead of blindly agreeing?",
        "good_example": "Sure, happy to. Just to confirm before I block my calendar – is this something you're actively exploring for your team right now?",
        "bad_example": "Okay, I’ll call Monday. Bye.",
        "hint": "Don’t chase false hope. Always check intent before scheduling.",
    },
    {
        "id": "S2",
        "type": "Negotiation",
        "title": "The Construction Contract – 50% Discount Demand",
        "setup": "Client says, 'We’ll go ahead if you give 50% off.'",
        "prompt": "How will you shift the conversation from emotion to objective criteria?",
        "good_example": "I completely understand budget constraints. Why don't we look at the average market rate for this scope and see what feels fair to both of us?",
        "bad_example": "No way, that’s too low. Take it or leave it.",
        "hint": "Use market benchmarks, not ego battles.",
    },
    {
        "id": "S3",
        "type": "Decision Makers",
        "title": "The Decision Maker Trap",
        "setup": "Prospect says, 'It’s a collaborative effort between me and two partners.'",
        "prompt": "How will you secure a meeting with all decision-makers together?",
        "good_example": "Perfect, let’s plan a quick call when all three of you are available so everyone is aligned. What day usually works for all of you?",
        "bad_example": "Okay, I’ll explain everything to you. You can tell them later.",
        "hint": "Never rely on Chinese whispers for key decisions.",
    },
]

# Build fast lookup tables
LESSONS_BY_MODULE = {}
for lesson in LESSONS:
    LESSONS_BY_MODULE.setdefault(lesson["module_id"], []).append(lesson)

for mid in LESSONS_BY_MODULE:
    LESSONS_BY_MODULE[mid] = sorted(LESSONS_BY_MODULE[mid], key=lambda x: x["order"])

QUIZ_BY_LESSON = {q["lesson_id"]: q for q in QUIZZES}
SCENARIOS_BY_TYPE = {}
for s in SCENARIOS:
    SCENARIOS_BY_TYPE.setdefault(s["type"], []).append(s)


# =========================
# SESSION STATE
# =========================

if "completed_lessons" not in st.session_state:
    st.session_state.completed_lessons = set()

if "quiz_scores" not in st.session_state:
    # dictionary: lesson_id -> True/False (passed or not)
    st.session_state.quiz_scores = {}

if "seen_scenarios" not in st.session_state:
    st.session_state.seen_scenarios = set()


# =========================
# UI HELPERS
# =========================

def show_quiz(lesson_id: str):
    quiz = QUIZ_BY_LESSON.get(lesson_id)
    if not quiz:
        st.info("No quiz attached to this lesson yet.")
        return

    st.subheader("Quick Check")

    user_choice = st.radio(
        quiz["question"],
        quiz["options"],
        key=f"quiz_{quiz['id']}",
    )

    if st.button("Submit Answer", key=f"submit_{quiz['id']}"):
        correct_idx = quiz["correct_index"]
        if quiz["options"].index(user_choice) == correct_idx:
            st.success("Correct. Nice work.")
            st.session_state.quiz_scores[lesson_id] = True
            st.session_state.completed_lessons.add(lesson_id)
        else:
            st.error("Not quite. Re-read the lesson and try again.")
            st.session_state.quiz_scores[lesson_id] = False


def show_lesson(lesson):
    st.markdown(f"### {lesson['title']}")
    st.markdown(lesson["content"])

    # Mark as complete button (manual)
    if lesson["id"] in st.session_state.completed_lessons:
        st.success("Marked as completed.")
    else:
        if st.button("Mark this lesson as complete", key=f"complete_{lesson['id']}"):
            st.session_state.completed_lessons.add(lesson["id"])
            st.success("Lesson marked as completed.")

    st.markdown("---")
    show_quiz(lesson["id"])


def show_module(module):
    st.header(module["title"])
    st.caption(module["description"])

    lessons = LESSONS_BY_MODULE.get(module["id"], [])
    if not lessons:
        st.info("No lessons added yet for this module.")
        return

    # List lessons in a selectbox
    lesson_titles = [l["title"] for l in lessons]
    selected_title = st.selectbox(
        "Select a lesson",
        lesson_titles,
        key=f"lesson_select_{module['id']}",
    )
    selected_lesson = next(l for l in lessons if l["title"] == selected_title)

    show_lesson(selected_lesson)


def show_roleplay():
    st.header("Role-Play & Use Cases")

    type_options = list(SCENARIOS_BY_TYPE.keys())
    selected_type = st.selectbox("Select scenario type", type_options)

    scenarios = SCENARIOS_BY_TYPE[selected_type]
    titles = [s["title"] for s in scenarios]
    selected_title = st.selectbox("Select scenario", titles, key="scenario_select")

    scenario = next(s for s in scenarios if s["title"] == selected_title)

    st.subheader(scenario["title"])
    st.markdown(f"**Setup:** {scenario['setup']}")
    st.markdown(f"**Your Task:** {scenario['prompt']}")

    st.text_area(
        "Type how you would respond (you can compare it with the suggested answer below):",
        key=f"answer_{scenario['id']}",
        height=120,
    )

    col1, col2 = st.columns(2)

    with col1:
        if st.button("Show Hint"):
            st.info(scenario["hint"])

    with col2:
        if st.button("Show Suggested Answer"):
            with st.expander("Good Example Response", expanded=True):
                st.markdown(scenario["good_example"])
            with st.expander("Common Weak Response"):
                st.markdown(scenario["bad_example"])

    st.session_state.seen_scenarios.add(scenario["id"])


def show_progress():
    st.header("Your Progress")

    total_lessons = len(LESSONS)
    completed = len(st.session_state.completed_lessons)
    progress = completed / total_lessons if total_lessons else 0

    st.metric("Lessons Completed", f"{completed} / {total_lessons}")
    st.progress(progress)

    if completed == 0:
        st.info("Start with Module 1 to begin your journey.")
    else:
        st.subheader("Completed Lessons")
        for lesson in LESSONS:
            if lesson["id"] in st.session_state.completed_lessons:
                st.write(f"✅ {lesson['title']} ({lesson['module_id']})")

    st.markdown("---")
    st.subheader("Scenario Practice")
    st.write(f"Scenarios attempted: {len(st.session_state.seen_scenarios)}")


# =========================
# MAIN APP
# =========================

def main():
    st.set_page_config(
        page_title="Sales & Negotiation Trainer",
        page_icon="🎧",
        layout="wide",
    )

    st.sidebar.title("Sales & Negotiation App")

    section = st.sidebar.radio(
        "Go to",
        ["Learn", "Role-Play", "Progress", "About"],
    )

    if section == "Learn":
        st.title("Learn: Sales Conversations & Negotiation")

        # Select module
        sorted_modules = sorted(MODULES, key=lambda m: m["order"])
        module_titles = [m["title"] for m in sorted_modules]
        selected_module_title = st.selectbox(
            "Select a module",
            module_titles,
            key="module_select",
        )
        selected_module = next(m for m in sorted_modules if m["title"] == selected_module_title)
        show_module(selected_module)

    elif section == "Role-Play":
        show_roleplay()

    elif section == "Progress":
        show_progress()

    elif section == "About":
        st.title("About This App")
        st.markdown(
            """
This app is designed to help you **self-learn** and practice:

- Cold calling mindset and rules  
- Handling ghosting and objections  
- Building negotiation skills using a **Harvard-style framework**  
- Practising real scenarios through **role-play**  

You can expand the content by adding more lessons, quizzes, and scenarios
in the `LESSONS`, `QUIZZES`, and `SCENARIOS` sections of `streamlit_app.py`.
"""
        )


if __name__ == "__main__":
    main()
