"""
╔══════════════════════════════════════════════════════════════════════════╗
║  PYTHON CODING CHALLENGES  —  LEARNER SHEET                              ║
║  15 problems  ·  7 MEDIUM + 8 COMPLEX                                   ║
║                                                                          ║
║  ALLOWED CONCEPTS ONLY:                                                 ║
║    Python foundations · lists · dictionaries · tuples · sets ·          ║
║    deques · I/O operations · control flow · loops                       ║
║  (No external libraries. `from collections import deque` is allowed.)   ║
╚══════════════════════════════════════════════════════════════════════════╝
 
┌──────────────────────────────────────────────────────────────────────────┐
│  ⚠  HOW THIS IS GRADED — READ THIS FIRST                                 │
│                                                                        │
│  Every problem below is a DELIBERATE VARIATION of a famous, well-known   │
│  problem. The variation (the "twist") is written in plain English but    │
│  is EASY TO MISS if you skim. Read each problem slowly.                  │
│                                                                          │
│  Each problem is graded with TWO sets of hidden tests:                   │
│    1. VISIBLE tests  — the obvious cases (a few are shown to you below   │
│       so you can self-check).                                            │
│    2. TRAP tests     — these specifically exercise THE TWIST.            │
│                                                                          │
│  A solution copy-pasted from an AI usually solves the FAMILIAR version   │
│  of the problem. It will pass the visible tests and FAIL the traps.      │
│  Only a solution that actually implemented the twist passes everything.  │
│                                                                          │
│  PROOF OF UNDERSTANDING (required for each problem):                     │
│    • Add a comment   `# TWIST:`  — state the variation IN YOUR OWN WORDS.│
│    • Add a comment   `# TRACE:`  — hand-compute ONE intermediate value   │
│      for the given canary input and show your working (one line).        │
│  A pasted answer will not contain a correct, specific trace unless you   │
│  genuinely understood the problem.                                       │
│                                                                          │
│  Fill in each  solve_*  function, then run this file to self-check the   │
│  visible cases.                                                          │
└──────────────────────────────────────────────────────────────────────────┘
"""
 
from collections import deque
 
 
# ════════════════════════════════════════════════════════════════════════════
#  MEDIUM 1 — "Lucky FizzBuzz"
# ════════════════════════════════════════════════════════════════════════════
#  Return a list of strings for 1..n following these rules, checked TOP to
#  bottom (first match wins):
#    • If the number's digits contain a '7' anywhere  -> "Lucky"
#    • else if divisible by 15                        -> "BuzzFizz"
#    • else if divisible by 3                         -> "Fizz"
#    • else if divisible by 5                         -> "Buzz"
#    • else                                           -> the number as a string
#
#  Canary input: n = 70   (look closely at 7, 15, 17, 70)
#  Visible self-check below uses n = 5.
#
# # TWIST: any number containing the digit 7 (not divisible by 7) becomes "Lucky", checked before Fizz/Buzz
#  # TRACE: n=70, position 7 (the number 7) -> "Lucky" because str(7) contains '7'
def solve_m1(n):
    result = []
    for i in range(1, 70):
        if '7' in str(i):
            result.append("Lucky")
        elif i % 15 == 0:
            result.append("BuzzFizz")
        elif i % 3 == 0:
            result.append("Fizz")
        elif i % 5 == 0:
            result.append("Buzz")
        else:
            result.append(str(i))
   
    return result
pass
 
 
# ════════════════════════════════════════════════════════════════════════════
#  MEDIUM 2 — "Sometimes-Y Vowel Counter"
# ════════════════════════════════════════════════════════════════════════════
#  Count vowels in a sentence. Vowels are a, e, i, o, u (any case). ALSO count
#  the letter 'y' as a vowel — BUT ONLY when it is NOT the first letter of its
#  word. Return the total count (an int).
#
#  Canary input: "yummy yellow sky"
#
#  # TWIST: ____________________________________________________________
#  # TRACE: in "sky", the 'y' counts because ________________________
def solve_m2(sentence):
    vowels = ['a', 'e', 'i', 'o', 'u']
    count = 0
 
    for i in range(len(sentence)):
        if sentence[i] in vowels:
            count += 1
        elif sentence[i] == 'y' and i != 0:
            count += 1
 
    return count
pass
 

 
# ════════════════════════════════════════════════════════════════════════════
#  MEDIUM 3 — "Keep the LAST One"
# ════════════════════════════════════════════════════════════════════════════
#  Remove duplicate values from a list. Keep each value at the position of its
#  LAST occurrence (NOT its first). Return the de-duplicated list.
#
#  Canary input: [1, 2, 3, 2, 1, 4]
#
# # TWIST: dedupe but keep each value's LAST occurrence position, not its first
#  # TRACE: value 1 last appears at index 4, so it ends up after the 3
def solve_m3(items):
    
    last_index = {}
    for i, v in enumerate(items):
        last_index[v] = i
    result = []
    seen = set()
    for i, v in enumerate(items):
        if last_index[v] == i and v not in seen:
            result.append(v)
            seen.add(v)
    return result
pass
 
 
# ════════════════════════════════════════════════════════════════════════════
#  MEDIUM 4 — "Running Max with Reset"
# ════════════════════════════════════════════════════════════════════════════
#  Walk the list left to right, outputting the maximum seen so far at each
#  step. BUT every time you hit a 0, output 0 AND reset the running maximum
#  (start fresh from after the zero). Return the list of running values.
#
#  Canary input: [3, 1, 4, 0, 2, 5, 1]
#
#  # TWIST: ____________________________________________________________
#  # TRACE: right after the 0, the running max becomes ___ then ___
def solve_m4(nums):
    max_val=nums[0]
    result=[]
    for i in range(len(nums)) :
        if nums[i] == 0 :
            result.append(nums[i])
           
       
        if nums[i] < max_val :
            result.append(max_val)
           
        if nums[i] > max_val :
            result.append(max_val)
            result.append(nums[i])
            max_val=nums[i]  
    return result
pass
 
 
 
 
# ════════════════════════════════════════════════════════════════════════════
#  MEDIUM 5 — "Top Word, Original Casing"
# ════════════════════════════════════════════════════════════════════════════
#  Find the most frequent word in a sentence, counting case-INsensitively
#  ("Go" and "go" are the same word). RETURN the winner spelled in the casing
#  it was FIRST seen in. Tie-break rules, in order:
#    1. higher count wins
#    2. if counts tie, the SHORTER word wins
#    3. if still tied, the alphabetically-first (lowercased) word wins
#
#  Canary input: "Go go STOP Stop go Stop"
#
#  # TWIST: ____________________________________________________________
#  # TRACE: counts are go=__ , stop=__ ; winner chosen because ________
def solve_m5(sentence):
  # your code here
  pass
 
 
# ════════════════════════════════════════════════════════════════════════════
#  MEDIUM 6 — "Circle Count with Boundary Penalty"
# ════════════════════════════════════════════════════════════════════════════
#  ).Given a list of (x, y) integer points and a radius r (circle centred at the
#  origin), return a single integer score:
#    • +1 for each point STRICTLY inside the circle
#    • -1 for each point EXACTLY on the boundary
#    •  0 (ignore) for points outside
#  Use integer math: compare x*x + y*y against r*r (avoid floats
#
#  Canary input: points=[(0,0),(3,0),(5,0),(0,5),(4,3)], r=5
#
#  # TWIST: points exactly on the boundary score -1 (penalty), not 0 — only strictly outside is ignored
# # TRACE: point (5,0) gives d2=25 vs r*r=25, so it scores -1
def solve_m6(points, r):
    
    score = 0
    r2 = r*r
    for (x,y) in points:
        d2 = x*x + y*y
        if d2 < r2:
            score += 1
        elif d2 == r2:
            score -= 1
    
    return score
pass



# ════════════════════════════════════════════════════════════════════════════
#  MEDIUM 7 — "Symmetric Difference, No Fives"
# ════════════════════════════════════════════════════════════════════════════
#  Given two lists, compute the values that appear in exactly one of them
#  (the symmetric difference). THEN drop any value that is a multiple of 5.
#  Return the survivors as a sorted (ascending) list.
#
#  Canary input: a=[1,2,3,4,5,10], b=[3,4,5,6,15]
#
#  # TWIST: ____________________________________________________________
#  # TRACE: symmetric difference is {____} ; after dropping fives -> ____
def solve_m7(a, b):
 
    temp_list=[]
    temp_list2=[]
    for i in range(len(a)):
        for j in range(len(b)):
            if a[i] == b[j]:
                break
        else:
            temp_list.append(a[i])
 
    for i in range(len(b)):
        for j in range(len(a)):
            if b[i] == a[j]:
                break
        else:
            temp_list.append(b[i])        
           
            
    for i in range(len(temp_list)):
        if temp_list[i] %5 != 0 :
            temp_list2.append(temp_list[i])
            
    return temp_list2
    pass
  
# ════════════════════════════════════════════════════════════════════════════
#  COMPLEX 1 — "Brackets + Loose Angles"
# ════════════════════════════════════════════════════════════════════════════
#  Validate a string of brackets. The (), [], {} pairs must be properly
#  nested (use a stack). HOWEVER, the angle brackets < and > only need to be
#  balanced in TOTAL COUNT — their order and nesting do NOT matter, and they
#  do NOT interact with the other brackets' nesting at all. Return True/False.
#
#  Canary input: "(<)>"   (note the angle brackets straddle the parens)
#
#  # TWIST: ____________________________________________________________
#  # TRACE: for "(<)>", the parens are ____ ; '<' count=__ , '>' count=__
def solve_c1(s):
# your code here   
 pass
 
 
# ════════════════════════════════════════════════════════════════════════════
#  COMPLEX 2 — "FIFO Inventory with Oversell Flag"
# ════════════════════════════════════════════════════════════════════════════
#  Process a list of transactions, each a tuple:
#      ("buy",  qty, price)   add a lot of inventory at that unit price
#      ("sell", qty, price)   sell units, matched to oldest inventory FIRST
#  Accumulate profit = units_sold * (sell_price - buy_price_of_those_units),
#  using FIFO cost basis. Selling more than you currently hold IS allowed and
#  creates a deficit. At the END, if any deficit remains, return the string
#  "INVALID: oversold by N" (N = leftover deficit). Otherwise return the
#  total profit as an int.
#
#  Canary input: [("buy",10,5),("sell",4,8),("buy",5,6),("sell",8,9)]
#
#  # TWIST: ____________________________________________________________
#  # TRACE: first sell matches __ units from the 10@5 lot -> profit += ____
def solve_c2(txns):
  # your code here
 pass
 
 
# ════════════════════════════════════════════════════════════════════════════
#  COMPLEX 3 — "Round Robin, Two-Strikes-Out"
# ════════════════════════════════════════════════════════════════════════════
#  Given a list of team names and a list of results (teamA, teamB, winner),
#  processed IN ORDER, return the surviving teams (sorted). A team is
#  ELIMINATED the moment it loses TWO MATCHES IN A ROW (a win resets its
#  losing streak to zero). Once a team is eliminated, any later match that
#  involves it is SKIPPED entirely (it has no effect on anyone).
#
#  Canary input:
#    teams = ["A","B","C"]
#    results = [("A","B","B"),("A","C","C"),("A","B","A"),
#               ("B","C","C"),("B","C","C")]
#
#  # TWIST: elimination needs two CONSECUTIVE losses; a win in between resets the streak to 0
#  #TRACE: A loses match 1 (streak=1) then match 2 (streak=2) -> A is eliminated
def solve_c3(teams, results):
    
    streak = {t: 0 for t in teams}
    eliminated = set()
    for a, b, w in results:
        if a in eliminated or b in eliminated:
            continue
        loser = a if w == b else b
        streak[w] = 0
        streak[loser] += 1
        if streak[loser] >= 2:
            eliminated.add(loser)
    
    return sorted([t for t in teams if t not in eliminated])
pass


teams = ["A","B","C"]
results = [("A","B","B"),("A","C","C"),("A","B","A"),
            ("B","C","C"),("B","C","C")]
 
 
# ════════════════════════════════════════════════════════════════════════════
#  COMPLEX 4 — "CSV with Quotes and a SUM Formula"
# ════════════════════════════════════════════════════════════════════════════
#  Parse one CSV line into a list of fields. Fields are comma-separated, but a
#  comma INSIDE double quotes is literal text (and the quote characters
#  themselves are removed). THEN: any field whose text starts with '=' is a
#  FORMULA equal to the SUM of all integer-valued fields to its RIGHT. Replace
#  that field with the computed sum (as a string). Return the list of fields.
#
#  Canary input: 'x,=,10,20,foo,30'
#
#  # TWIST: ____________________________________________________________
#  # TRACE: the '=' field sums the integers to its right: __ + __ + __ = ____
def solve_c4(line):
   # your code here  
 pass
 
 
# ════════════════════════════════════════════════════════════════════════════
#  COMPLEX 5 — "Maze BFS with Teleports"
# ════════════════════════════════════════════════════════════════════════════
#  A grid (list of equal-length strings):  'S' start, 'E' end, '#' wall,
#  '.' open floor. Lowercase letters are TELEPORT pads: stepping onto a pad
#  instantly moves you to the OTHER pad with the same letter (the teleport
#  itself costs no extra step). Find the FEWEST steps from S to E moving in 4
#  directions. Return the step count, or -1 if E is unreachable.
#
#  Canary input: ["S.b", "###", "b.E"]
#
#  # TWIST: ____________________________________________________________
#  # TRACE: stepping onto 'b' at (0,2) teleports you to ______
def solve_c5(grid):
   # your code here 
 pass
 
 
# ════════════════════════════════════════════════════════════════════════════
#  COMPLEX 6 — "Instant Runoff, Eliminate Alphabetically-Last on Ties"
# ════════════════════════════════════════════════════════════════════════════
#  Run instant-runoff voting. Each ballot is a ranked list of candidate names.
#  Each round: count first-choice votes among still-active candidates. If a
#  candidate has STRICTLY MORE than half of the ballots, they win. Otherwise
#  eliminate the candidate with the FEWEST first-choice votes and re-count
#  (ballots fall through to their next active choice). TWIST: when several
#  candidates TIE for fewest, eliminate the one whose name is alphabetically
#  LAST. Return the winning candidate.
#
#  Canary input:
#    ballots = [["A","B","C"],["B","A","C"],["C","A","B"]]
#    candidates = ["A","B","C"]
#
#  # TWIST: ____________________________________________________________
#  # TRACE: round 1 counts are A=__ B=__ C=__ ; tie -> eliminate ____
def solve_c6(ballots, candidates):
  # your code here
 pass
 
 
# ════════════════════════════════════════════════════════════════════════════
#  COMPLEX 7 — "Curved Grades"
# ════════════════════════════════════════════════════════════════════════════
#  Given a list of integer scores, assign letter grades RELATIVE to the class
#  average (avg = sum // len, integer division). Boundaries:
#    A: score >= avg + 15
#    B: score >= avg + 5
#    C: score >= avg - 5
#    D: score >= avg - 15
#    F: otherwise
#  Return a list of letter grades aligned with the input order.
#
#  Canary input: [50, 55, 60, 62, 63]
#
#  # TWIST: ____________________________________________________________
#  # TRACE: avg = depend on all scores ; so the A-boundary is 73 and the C-boundary is 53
def solve_c7(scores):
 
    grade=["A","B","C","D","F"]
    result=[]
    sum1=sum(scores)
    avg=sum1//len(scores)
    for i in range(len(scores)) :
        if scores[i] >=avg+15:
             result.append(grade[0])
        elif scores[i] >=avg+5:
             result.append(grade[1])
        elif scores[i] >=avg-5:
            result.append(grade[2])
        elif scores[i] >=avg-15:
            result.append(grade[3])
        else :
            result.append(grade[4])
    return result
pass
 
 
# ════════════════════════════════════════════════════════════════════════════
#  COMPLEX 8 — "Rebuild the Chain, or Detect a Cycle"
    # ════════════════════════════════════════════════════════════════════════════
    #  Given a list of pairs (a, b), each meaning "a comes immediately before b",
    #  rebuild the single linear ordering of all items and return it as a list.
    #  Every item has at most one successor and one predecessor. If the links form
#  a CYCLE (so there is no valid starting point / linear order), return the
#  string "CYCLE DETECTED" instead.
#
#  Canary input: [("c","d"),("a","b"),("b","c")]
#
#  # TWIST: ____________________________________________________________
#  # TRACE: the unique start is the item with no predecessor, which is ____
def solve_c8(pairs):
  # your code here    
 pass
 
 
# ════════════════════════════════════════════════════════════════════════════
#  SELF-CHECK  (VISIBLE cases only — passing these is NOT enough!)
#  The hidden TRAP tests check the twist. Read each problem carefully.
# ════════════════════════════════════════════════════════════════════════════
def _row(name, got, expected):
    status = "ok " if got == expected else "XX "
    if got is None:
        status = "-- "   # not attempted yet
    print(f"  [{status}] {name:<5} got={str(got):<22} expected={expected}")
 
def self_check():
    print("=" * 64)
    print("  VISIBLE SELF-CHECK  (the obvious cases only)")
    print("  Passing every line here does NOT mean you passed — the")
    print("  hidden trap tests check the twist in each problem.")
    print("=" * 64)
 
    # MEDIUM visible cases
    m1 = solve_m1(5) if solve_m1(5) is not None else None
    _row("M1", m1[2] if m1 else None, "Fizz")          # n=3
    _row("M2", solve_m2("apple orange"), 5)
    _row("M3", solve_m3([1, 2, 3]), [1, 2, 3])
    _row("M4", solve_m4([3, 1, 4, 2]), [3, 3, 4, 4])
    _row("M5", solve_m5("hi hi bye"), "hi")
    _row("M6", solve_m6([(0, 0), (1, 1)], 5), 2)
    _row("M7", solve_m7([1, 2, 3], [3, 4]), [1, 2, 4])
 
    # COMPLEX visible cases
    _row("C1", solve_c1("([]){}"), True)
    _row("C2", solve_c2([("buy", 10, 5), ("sell", 4, 8)]), 12)
    _row("C3", solve_c3(["A", "B"], [("A", "B", "A")]), ["A", "B"])
    _row("C4", solve_c4("a,b,c"), ["a", "b", "c"])
    _row("C5", solve_c5(["S.", ".E"]), 2)
    _row("C6", solve_c6([["A"], ["A"], ["B"]], ["A", "B"]), "A")
    _row("C7", solve_c7([70, 70, 70]), ["C", "C", "C"])
    _row("C8", solve_c8([("a", "b"), ("b", "c")]), ["a", "b", "c"])
 
    print("-" * 64)
    print("  Reminder: fill in your  # TWIST:  and  # TRACE:  comments.")
    print("  The grader runs HIDDEN trap tests on the canary inputs.")
    print("=" * 64)
 
 
if __name__ == "__main__":
    self_check()