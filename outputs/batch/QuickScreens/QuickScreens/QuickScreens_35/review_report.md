# Play-Annotation-Generator Annotation Review — QuickScreens_35

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `QuickScreens_35`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Pass_QuickScreens`
- **Result:** `Result_Tackle`
- **Result Frame:** 239
- **Player Tracks:** 35
- **Ball Tracks:** 0
- **Action Segments:** 91
- **Validation Warnings:** 94
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 17
- **Exact Matches:** 4
- **Group Expanded Events:** 9
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 1
- **Missing Segments:** 1
- **Ambiguous Matches:** 1
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 76
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR4 | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `8` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `9` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `15` | `15` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `12` | `12` |
| ⚠️ AMBIGUOUS MATCH | `Action_ScreenBlock` | WR3 | offense | `6` | `6` |
| ⚠️ START CHANGED | `Action_TurnToQuarterback` | WR2 | offense | `9` | `9` |
| ✅ EXACT | `Action_ThrowScreenPass` | QB | offense | `12` | `12` |
| ✅ EXACT | `Action_SecureCatch` | WR2 | offense | `9` | `9` |
| ❌ MISSING SEGMENT | `Action_RunAfterCatch` | WR2 | offense | `9` | `9` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR4 | `0` | `Group` | 0 | START | 0 | 5 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `12` | `Group` | 0 | START | 0 | 5 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `15` | `Group` | 0 | START | 0 | 5 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `16` | `Group` | 0 | START | 0 | 5 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `18` | `Group` | 0 | START | 0 | 5 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `3` | `Group` | 0 | START | 0 | 5 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `6` | `Group` | 0 | START | 0 | 28 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `8` | `Group` | 0 | START | 0 | 5 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `9` | `Group` | 0 | START | 0 | 21 |
| ✅ EXACT | `Action_BallSnap` | C | `15` | `15` | 6 | START | 6 | 13 |
| ✅ EXACT | `Action_SnapReceive` | QB | `12` | `12` | 19 | END | 6 | 19 |
| ⚠️ AMBIGUOUS MATCH | `Action_ScreenBlock` | WR3 | `6` | `6` | 29 | START | 29 | 41 |
| ⚠️ START CHANGED | `Action_TurnToQuarterback` | WR2 | `9` | `9` | 31 | START | 36 | 53 |
| ✅ EXACT | `Action_ThrowScreenPass` | QB | `12` | `12` | 34 | START | 34 | 42 |
| ✅ EXACT | `Action_SecureCatch` | WR2 | `9` | `9` | 56 | START | 56 | 61 |
| ❌ MISSING SEGMENT | `Action_RunAfterCatch` | WR2 | `9` | `9` | 80 | START | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–173
- **Visible Samples:** 174

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 5 | 6 | inferred_complete_timeline |
| `Action_SnapReceive` | 6 | 19 | 14 | inferred_complete_timeline |
| `Action_None` | 20 | 33 | 14 | inferred_complete_timeline |
| `Action_ThrowScreenPass` | 34 | 42 | 9 | inferred_complete_timeline |
| `Action_None` | 43 | 173 | 131 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–148
- **Visible Samples:** 137

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 5 | 6 | inferred_complete_timeline |
| `Action_None` | 6 | 93 | 88 | inferred_complete_timeline |
| `Action_None` | 102 | 106 | 5 | inferred_complete_timeline |
| `Action_None` | 111 | 148 | 38 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–126
- **Visible Samples:** 127

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 5 | 6 | inferred_complete_timeline |
| `Action_None` | 6 | 126 | 121 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–61
- **Visible Samples:** 48

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 21 | 22 | inferred_complete_timeline |
| `Action_TurnToQuarterback` | 36 | 53 | 18 | inferred_complete_timeline |
| `Action_None` | 54 | 55 | 2 | inferred_complete_timeline |
| `Action_SecureCatch` | 56 | 61 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–71
- **Visible Samples:** 55

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 28 | 29 | inferred_complete_timeline |
| `Action_ScreenBlock` | 29 | 41 | 13 | inferred_complete_timeline |
| `Action_ScreenBlock` | 43 | 45 | 3 | inferred_complete_timeline |
| `Action_ScreenBlock` | 47 | 54 | 8 | inferred_complete_timeline |
| `Action_ScreenBlock` | 70 | 71 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>WR4 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–115
- **Visible Samples:** 116

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 5 | 6 | inferred_complete_timeline |
| `Action_None` | 6 | 115 | 110 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 228

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 5 | 6 | inferred_complete_timeline |
| `Action_None` | 6 | 13 | 8 | inferred_complete_timeline |
| `Action_None` | 15 | 19 | 5 | inferred_complete_timeline |
| `Action_None` | 21 | 28 | 8 | inferred_complete_timeline |
| `Action_None` | 39 | 239 | 201 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–207
- **Visible Samples:** 199

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 5 | 6 | inferred_complete_timeline |
| `Action_None` | 6 | 12 | 7 | inferred_complete_timeline |
| `Action_None` | 22 | 207 | 186 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 232

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 5 | 6 | inferred_complete_timeline |
| `Action_BallSnap` | 6 | 13 | 8 | inferred_complete_timeline |
| `Action_None` | 22 | 239 | 218 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–116
- **Visible Samples:** 117

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 5 | 6 | inferred_complete_timeline |
| `Action_None` | 6 | 116 | 111 | inferred_complete_timeline |

</details>

<details>
<summary>DT — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 236

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 5 | 6 | inferred_complete_timeline |
| `Action_None` | 6 | 16 | 11 | inferred_complete_timeline |
| `Action_None` | 21 | 239 | 219 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 5 | 6 | inferred_complete_timeline |
| `Action_None` | 6 | 239 | 234 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 5 | 6 | inferred_complete_timeline |
| `Action_None` | 6 | 239 | 234 | inferred_complete_timeline |

</details>

<details>
<summary>LB3 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–171
- **Visible Samples:** 172

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 5 | 6 | inferred_complete_timeline |
| `Action_None` | 6 | 171 | 166 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–231
- **Visible Samples:** 219

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 5 | 6 | inferred_complete_timeline |
| `Action_None` | 6 | 88 | 83 | inferred_complete_timeline |
| `Action_None` | 90 | 112 | 23 | inferred_complete_timeline |
| `Action_None` | 116 | 136 | 21 | inferred_complete_timeline |
| `Action_None` | 138 | 155 | 18 | inferred_complete_timeline |
| `Action_None` | 157 | 210 | 54 | inferred_complete_timeline |
| `Action_None` | 214 | 218 | 5 | inferred_complete_timeline |
| `Action_None` | 223 | 231 | 9 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–58
- **Visible Samples:** 57

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 5 | 6 | inferred_complete_timeline |
| `Action_None` | 6 | 52 | 47 | inferred_complete_timeline |
| `Action_None` | 55 | 58 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–161
- **Visible Samples:** 151

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 5 | 6 | inferred_complete_timeline |
| `Action_None` | 6 | 87 | 82 | inferred_complete_timeline |
| `Action_None` | 97 | 107 | 11 | inferred_complete_timeline |
| `Action_None` | 110 | 161 | 52 | inferred_complete_timeline |

</details>

<details>
<summary>CB4 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–144
- **Visible Samples:** 145

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 5 | 6 | inferred_complete_timeline |
| `Action_None` | 6 | 144 | 139 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 233

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 5 | 6 | inferred_complete_timeline |
| `Action_None` | 6 | 167 | 162 | inferred_complete_timeline |
| `Action_None` | 174 | 206 | 33 | inferred_complete_timeline |
| `Action_None` | 208 | 239 | 32 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `19` | `19` | Position_Unknown | Team_Unknown | 21–183 | 163 | 1 | Undefined position; Undefined team |
| `20` | `20` | Position_Unknown | Team_Unknown | 23–239 | 217 | 1 | Undefined position; Undefined team |
| `21` | `21` | Position_Unknown | Team_Unknown | 24–207 | 178 | 2 | Undefined position; Undefined team |
| `22` | `22` | Position_Unknown | Team_Unknown | 83–206 | 63 | 8 | Undefined position; Undefined team |
| `23` | `24` | Position_Unknown | Team_Unknown | 106–107 | 2 | 1 | Undefined position; Undefined team |
| `24` | `26` | Position_Unknown | Team_Unknown | 113–121 | 8 | 2 | Undefined position; Undefined team |
| `25` | `27` | Position_Unknown | Team_Unknown | 114–118 | 5 | 1 | Undefined position; Undefined team |
| `26` | `28` | Position_Unknown | Team_Unknown | 117–239 | 123 | 1 | Undefined position; Undefined team |
| `27` | `29` | Position_Unknown | Team_Unknown | 132–239 | 108 | 1 | Undefined position; Undefined team |
| `28` | `31` | Position_Unknown | Team_Unknown | 148–152 | 5 | 1 | Undefined position; Undefined team |
| `29` | `32` | Position_Unknown | Team_Unknown | 154–156 | 3 | 1 | Undefined position; Undefined team |
| `30` | `33` | Position_Unknown | Team_Unknown | 159–177 | 19 | 1 | Undefined position; Undefined team |
| `31` | `34` | Position_Unknown | Team_Unknown | 163–239 | 77 | 1 | Undefined position; Undefined team |
| `32` | `35` | Position_Unknown | Team_Unknown | 169–239 | 71 | 1 | Undefined position; Undefined team |
| `33` | `36` | Position_Unknown | Team_Unknown | 171–239 | 68 | 2 | Undefined position; Undefined team |
| `34` | `37` | Position_Unknown | Team_Unknown | 235–239 | 5 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_ScreenBlock` and target `6` (4 segments found)
- ⚠️ `Action_TurnToQuarterback` for actor_track_id `9` (WR2): Annotated start 31 != Inferred start 36
- ❌ Missing segment for action `Action_RunAfterCatch` on target `9` (WR2)

### Track Identity Issues

- ⚠️ Player track XML ID `7` (actor_track_id `7`): `SAF` position mapped to `defense` team
- ⚠️ 16 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 16 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 32 |
| Missing visible bounding boxes during action | 59 |
| Track-related warning | 2 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 40: Duplicate assignment for track ID '2' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Segment 'Action_RunAfterCatch' for track '9' has invalid range: start=80, end=61. Clamping end to start.
- ⚠️ Action 'Action_None' range [6-115] for track '0' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [6-88] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [90-112] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [116-136] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [138-155] for track '1' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [157-210] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [214-218] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [223-231] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [6-144] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [6-93] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [102-106] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [111-148] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [6-52] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [55-58] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ScreenBlock' range [29-41] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ScreenBlock' range [43-45] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ScreenBlock' range [47-54] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ScreenBlock' range [70-71] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [6-167] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [174-206] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [6-126] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-21] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_TurnToQuarterback' range [36-53] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_SecureCatch' range [56-61] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [6-87] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [97-107] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [110-161] for track '11' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [43-173] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [6-171] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [6-116] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallSnap' range [6-13] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [6-13] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [15-19] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [21-28] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [39-239] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [6-16] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [21-239] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [6-12] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [22-207] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [21-183] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [24-123] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [130-207] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [83-96] for track '22' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [99-108] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [113-119] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [122-123] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [125-127] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [129-131] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [182-202] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [204-206] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [106-107] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [113-115] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [117-121] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [114-118] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [117-239] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [148-152] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [154-156] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [159-177] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [171-176] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Player track '19' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '19' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '20' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '20' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '21' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '21' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '22' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '22' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '23' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '23' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '24' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '24' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '25' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '25' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '26' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '26' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '27' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '27' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '28' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '28' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '29' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '29' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '30' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '30' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '31' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '31' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '32' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '32' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '33' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '33' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '34' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '34' has undefined team_side. Will map to Team_Unknown.

</details>