""" "
LIST 🎵 Analogy: Your spotify Playlist
"""
 
print("=" * 60)
print("  LIST  —  Your Spotify Playlist")
print("=" * 60)
 
print("""
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  DEFINITION
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 
  A LIST is an ordered, changeable (mutable) collection of items.
  Items sit in numbered positions (index 0, 1, 2 …).
  The same item can appear more than once.
  You can store anything: strings, numbers, booleans, other lists.
 
  ANALOGY  🎵
  ───────────
  Think of a Spotify playlist.
    → Songs are in a specific order  (track 1, track 2, ...)
    → You can add new songs          (.append)
    → You can remove songs           (.remove / .pop)
    → You can rearrange songs        (.sort / .reverse)
    → The same song can appear twice (duplicates allowed)
 
  SYNTAX:  playlist = ["song1", "song2", "song3"]
 
  PROPERTIES:
    ✅ Ordered     — position is preserved and meaningful
    ✅ Mutable     — change it after creation
    ✅ Duplicates  — allowed
    ✅ Mixed types — can hold strings, ints, bools together
    ✅ Created with  [ ]
""")
 
 
print("""
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  WHY USE A LIST?
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 
  1. ORDER MATTERS to you.
     A playlist without order is just a pile of songs.
     A to-do list without order loses priority.
     A list keeps things in the sequence you put them in.
 
  2. THE COLLECTION WILL CHANGE over time.
     You'll add, remove, or rearrange items.
     A list is the most flexible structure for that.
 
  3. YOU NEED TO WORK THROUGH ITEMS SEQUENTIALLY.
     Processing records one after another.
     Displaying items on a screen in order.
 
  4. PYTHON'S BUILT-IN TOOLS support lists deeply.
     sorted(), reversed(), max(), min(), sum(), len()
     all work out of the box on any list.
""")
 
 
# WHEN TO USE / WHEN NOT TO USE
 
print("""
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  WHEN TO USE A LIST
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  ✅ Storing a sequence of items where ORDER matters
     → playlist, rankings, queue of tasks, exam answers
 
  ✅ Collection GROWS or SHRINKS during the program
     → adding songs, removing completed tasks
 
  ✅ You need to ACCESS ITEMS BY POSITION (index)
     → "give me the 3rd song"  →  playlist[2]
 
  ✅ DUPLICATES are valid and meaningful
     → same song twice in a playlist is perfectly fine
 
  ✅ You want to SORT or SEARCH through items
     → sorted(), sorted(reverse=True), .index()
 
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  WHEN NOT TO USE A LIST
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  ❌ You need FAST MEMBERSHIP CHECKS on large data
     "is this username already taken?" on 1 million users
     → Use a SET instead (O(1) lookup vs O(n) for list)
 
  ❌ Items need LABELS (names), not positions
     "what is Alice's grade?" is not "what is grade[0]?"
     → Use a DICT instead
 
  ❌ The data should NEVER CHANGE once created
     GPS coordinates, RGB colour values, config constants
     → Use a TUPLE instead (prevents accidental changes)
 
  ❌ You frequently ADD/REMOVE from the FRONT
     Processing a print queue, dequeuing tasks
     → Use a DEQUE instead (O(1) at both ends vs O(n) for list)
 
  ❌ You need to GUARANTEE UNIQUENESS automatically
     Attendance list where each student appears once
     → Use a SET instead
""")
 
print("── CREATE ──────────────────────────────────────────────────")
 
playlist = ["Blinding Lights", "Levitating", "HUMBLE.", "Anti-Hero", "Bad Guy"]
print(f"Literal      : {playlist}")
print(f"Type         : {type(playlist)}")
print(f"Length       : {len(playlist)} songs")
 
raw = "Watermelon Sugar, Golden, Adore You"
from_str = raw.split(", ")
print(f"From string  : {from_str}")
 
track_numbers = list(range(1, 6))
print(f"From range   : {track_numbers}")
 
empty = []
print(f"Empty list   : {empty}")
 
# ══════════════════════════════════════════════════════════════════════════
#  READ
# ══════════════════════════════════════════════════════════════════════════
 
print("\n── READ ────────────────────────────────────────────────────")
 
playlist = ["Blinding Lights", "Levitating", "HUMBLE.", "Anti-Hero", "Bad Guy"]
#  index →         0               1             2           3            4
#  neg   →        -5              -4            -3          -2           -1
 
print(f"First song    : {playlist[0]}")
print(f"Last song     : {playlist[-1]}")
print(f"Second last   : {playlist[-2]}")
 
print(f"First 3       : {playlist[0:3]}")
print(f"Last 2        : {playlist[-2:]}")
print(f"Middle 1–3    : {playlist[1:4]}")
print(f"Reversed copy : {playlist[::-1]}")
 
print(f"Has HUMBLE.?  : {'HUMBLE.' in playlist}")
print(f"Has Closer?   : {'Closer' not in playlist}")
print(f"Index Anti-H  : {playlist.index('Anti-Hero')}")
 
with_repeat = ["HUMBLE.", "Levitating", "HUMBLE.", "Bad Guy"]
print(f"HUMBLE. count : {with_repeat.count('HUMBLE.')}")
 
play_counts = [120, 340, 89, 450, 210]
print(f"Max plays  : {max(play_counts)}")
print(f"Min plays  : {min(play_counts)}")
print(f"Total      : {sum(play_counts)}")
print(f"Average    : {sum(play_counts) / len(play_counts):.1f}")
 
# ══════════════════════════════════════════════════════════════════════════
#  UPDATE
# ══════════════════════════════════════════════════════════════════════════
 
print("\n── UPDATE ──────────────────────────────────────────────────")
 
playlist = ["Blinding Lights", "Levitating", "HUMBLE.", "Anti-Hero", "Bad Guy"]
print(f"Before       : {playlist}")
 
playlist[2] = "SICKO MODE"
print(f"Replace [2]  : {playlist}")
 
playlist.append("Golden")
print(f"append()     : {playlist}")
 
playlist.insert(1, "Adore You")
print(f"insert(1,…)  : {playlist}")
 
bonus = ["Watermelon Sugar", "Fine Line"]
playlist.extend(bonus)
print(f"extend([…])  : {playlist}")
 
playlist.sort()
print(f"sort() A→Z   : {playlist}")
 
playlist.sort(reverse=True)
print(f"sort() Z→A   : {playlist}")
 
playlist.reverse()
print(f"reverse()    : {playlist}")
 
plays = [120, 340, 89, 450, 210]
ranked = sorted(plays, reverse=True)
print(f"sorted() new : {ranked}")
print(f"original ok  : {plays}")
 
# ══════════════════════════════════════════════════════════════════════════
#  DELETE
# ══════════════════════════════════════════════════════════════════════════
 
print("\n── DELETE ──────────────────────────────────────────────────")
 
playlist = ["Blinding Lights", "Levitating", "HUMBLE.", "Anti-Hero", "Bad Guy"]
print(f"Before       : {playlist}")
 
playlist.remove("Levitating")
print(f"remove()     : {playlist}")
 
removed = playlist.pop(1)
print(f"pop(1) got   : {removed!r}  →  {playlist}")
 
last = playlist.pop()
print(f"pop() got    : {last!r}  →  {playlist}")
 
playlist.clear()
print(f"clear()      : {playlist}")
 
 
print("\n── BONUS: List Comprehension ───────────────────────────────")
 
songs = ["blinding lights", "levitating", "humble."]
titled = [s.title() for s in songs]
long = [s for s in songs if len(s) > 10]
lengths = [len(s) for s in songs]
 
print(f"Title-cased  : {titled}")
print(f"Long names   : {long}")
print(f"Lengths      : {lengths}")
 
 
print("""
┌──────────────────────────────────────────────────────────┐
│  LIST CHEAT SHEET                                        │
├─────────────────┬────────────────────────────────────────┤
│  DEFINITION     │  Ordered, mutable, duplicates OK       │
│  ANALOGY        │  Spotify playlist                       │
│  SYNTAX         │  pl = ["a", "b", "c"]                  │
├─────────────────┼────────────────────────────────────────┤
│  USE WHEN       │  order matters, data changes,          │
│                 │  need index access, duplicates OK       │
│  AVOID WHEN     │  need fast search → use Set            │
│                 │  need labels → use Dict                 │
│                 │  data is fixed → use Tuple             │
│                 │  remove from front often → use Deque   │
├─────────────────┼────────────────────────────────────────┤
│  CREATE         │  ["a","b"]   str.split()   range()     │
│  READ           │  pl[0]  pl[-1]  pl[1:3]  pl[::-1]     │
│                 │  "x" in pl   .index()  .count()        │
│                 │  len()  max()  min()  sum()             │
│  UPDATE         │  pl[0]="new"  .append()  .insert()     │
│                 │  .extend()   .sort()  .reverse()        │
│                 │  sorted() → new list, original safe     │
│  DELETE         │  .remove("x")  .pop(i)  .pop()         │
│                 │  .clear()                              │
└─────────────────┴────────────────────────────────────────┘
""")
 