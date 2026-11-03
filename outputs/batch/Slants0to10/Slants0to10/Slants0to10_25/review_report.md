# Play-Annotation-Generator Annotation Review — Slants0to10_25

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Slants0to10_25`
- **Frame Range:** 0 to 299 (300 total frames)
- **Play:** `Play_Pass_Slants0to10`
- **Result:** `Result_Tackle`
- **Result Frame:** 299
- **Player Tracks:** 42
- **Ball Tracks:** 0
- **Action Segments:** 139
- **Validation Warnings:** 143
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 22
- **Exact Matches:** 5
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 5
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 118
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR4 | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `4` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `18` | `18` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LT | offense | `10` | `10` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LG | offense | `12` | `12` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | C | offense | `18` | `18` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RG | offense | `21` | `21` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RT | offense | `4` | `4` |
| ✅ EXACT | `Action_RunSlantRoute` | WR3 | offense | `1` | `1` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `14` | `14` |
| ✅ EXACT | `Action_ThrowPass` | QB | offense | `14` | `14` |
| ✅ EXACT | `Action_BallCarry` | WR3 | offense | `1` | `1` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR4 | `0` | `Group` | 0 | START | 0 | 2 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `1` | `Group` | 0 | START | 0 | 11 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `10` | `Group` | 0 | START | 0 | 6 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `12` | `Group` | 0 | START | 0 | 6 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `14` | `Group` | 0 | START | 0 | 2 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `18` | `Group` | 0 | START | 0 | 2 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `19` | `Group` | 0 | START | 0 | 2 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `2` | `Group` | 0 | START | 0 | 2 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `21` | `Group` | 0 | START | 0 | 6 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `3` | `Group` | 0 | START | 0 | 2 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `4` | `Group` | 0 | START | 0 | 6 |
| ✅ EXACT | `Action_BallSnap` | C | `18` | `18` | 3 | START | 3 | 16 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LT | `10` | `10` | 7 | START | 7 | 51 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LG | `12` | `12` | 7 | START | 7 | 35 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | C | `18` | `18` | 7 | START | 17 | 98 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RG | `21` | `21` | 7 | START | 7 | 70 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RT | `4` | `4` | 7 | START | 7 | 53 |
| ✅ EXACT | `Action_RunSlantRoute` | WR3 | `1` | `1` | 12 | START | 12 | 74 |
| ✅ EXACT | `Action_SnapReceive` | QB | `14` | `14` | 16 | END | 3 | 16 |
| ✅ EXACT | `Action_ThrowPass` | QB | `14` | `14` | 55 | START | 55 | 64 |
| ✅ EXACT | `Action_BallCarry` | WR3 | `1` | `1` | 81 | START | 81 | 110 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–238
- **Visible Samples:** 239

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 2 | 3 | inferred_complete_timeline |
| `Action_SnapReceive` | 3 | 16 | 14 | inferred_complete_timeline |
| `Action_None` | 17 | 54 | 38 | inferred_complete_timeline |
| `Action_ThrowPass` | 55 | 64 | 10 | inferred_complete_timeline |
| `Action_None` | 65 | 238 | 174 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 298

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 2 | 3 | inferred_complete_timeline |
| `Action_None` | 3 | 22 | 20 | inferred_complete_timeline |
| `Action_None` | 25 | 299 | 275 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–201
- **Visible Samples:** 198

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 2 | 3 | inferred_complete_timeline |
| `Action_None` | 3 | 128 | 126 | inferred_complete_timeline |
| `Action_None` | 133 | 201 | 69 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–275
- **Visible Samples:** 276

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 2 | 3 | inferred_complete_timeline |
| `Action_None` | 3 | 275 | 273 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–110
- **Visible Samples:** 111

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 11 | 12 | inferred_complete_timeline |
| `Action_RunSlantRoute` | 12 | 74 | 63 | inferred_complete_timeline |
| `Action_None` | 75 | 80 | 6 | inferred_complete_timeline |
| `Action_BallCarry` | 81 | 110 | 30 | inferred_complete_timeline |

</details>

<details>
<summary>WR4 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 291

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 2 | 3 | inferred_complete_timeline |
| `Action_None` | 3 | 289 | 287 | inferred_complete_timeline |
| `Action_None` | 299 | 299 | 1 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–60
- **Visible Samples:** 54

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 6 | 7 | inferred_complete_timeline |
| `Action_PassBlock` | 7 | 51 | 45 | inferred_complete_timeline |
| `Action_PassBlock` | 59 | 60 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–90
- **Visible Samples:** 65

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 6 | 7 | inferred_complete_timeline |
| `Action_PassBlock` | 7 | 35 | 29 | inferred_complete_timeline |
| `Action_PassBlock` | 53 | 55 | 3 | inferred_complete_timeline |
| `Action_PassBlock` | 59 | 73 | 15 | inferred_complete_timeline |
| `Action_PassBlock` | 77 | 83 | 7 | inferred_complete_timeline |
| `Action_PassBlock` | 86 | 87 | 2 | inferred_complete_timeline |
| `Action_PassBlock` | 89 | 90 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 281

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 2 | 3 | inferred_complete_timeline |
| `Action_BallSnap` | 3 | 16 | 14 | inferred_complete_timeline |
| `Action_PassBlock` | 17 | 98 | 82 | inferred_complete_timeline |
| `Action_PassBlock` | 112 | 191 | 80 | inferred_complete_timeline |
| `Action_PassBlock` | 195 | 238 | 44 | inferred_complete_timeline |
| `Action_PassBlock` | 240 | 257 | 18 | inferred_complete_timeline |
| `Action_PassBlock` | 260 | 299 | 40 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `21`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–83
- **Visible Samples:** 82

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 6 | 7 | inferred_complete_timeline |
| `Action_PassBlock` | 7 | 70 | 64 | inferred_complete_timeline |
| `Action_PassBlock` | 72 | 73 | 2 | inferred_complete_timeline |
| `Action_PassBlock` | 75 | 83 | 9 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 284

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 6 | 7 | inferred_complete_timeline |
| `Action_PassBlock` | 7 | 53 | 47 | inferred_complete_timeline |
| `Action_PassBlock` | 57 | 72 | 16 | inferred_complete_timeline |
| `Action_PassBlock` | 74 | 99 | 26 | inferred_complete_timeline |
| `Action_PassBlock` | 101 | 105 | 5 | inferred_complete_timeline |
| `Action_PassBlock` | 108 | 164 | 57 | inferred_complete_timeline |
| `Action_PassBlock` | 174 | 299 | 126 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 276

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 2 | 3 | inferred_complete_timeline |
| `Action_None` | 3 | 100 | 98 | inferred_complete_timeline |
| `Action_None` | 122 | 126 | 5 | inferred_complete_timeline |
| `Action_None` | 130 | 299 | 170 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–218
- **Visible Samples:** 213

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 2 | 3 | inferred_complete_timeline |
| `Action_None` | 3 | 191 | 189 | inferred_complete_timeline |
| `Action_None` | 193 | 208 | 16 | inferred_complete_timeline |
| `Action_None` | 214 | 218 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–265
- **Visible Samples:** 260

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 2 | 3 | inferred_complete_timeline |
| `Action_None` | 3 | 38 | 36 | inferred_complete_timeline |
| `Action_None` | 41 | 74 | 34 | inferred_complete_timeline |
| `Action_None` | 79 | 265 | 187 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 293

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 2 | 3 | inferred_complete_timeline |
| `Action_None` | 3 | 39 | 37 | inferred_complete_timeline |
| `Action_None` | 41 | 96 | 56 | inferred_complete_timeline |
| `Action_None` | 101 | 105 | 5 | inferred_complete_timeline |
| `Action_None` | 108 | 299 | 192 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–286
- **Visible Samples:** 260

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 2 | 3 | inferred_complete_timeline |
| `Action_None` | 3 | 192 | 190 | inferred_complete_timeline |
| `Action_None` | 215 | 228 | 14 | inferred_complete_timeline |
| `Action_None` | 231 | 236 | 6 | inferred_complete_timeline |
| `Action_None` | 238 | 282 | 45 | inferred_complete_timeline |
| `Action_None` | 285 | 286 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `defense`
- **Visible Frames:** 0–61
- **Visible Samples:** 42

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 2 | 3 | inferred_complete_timeline |
| `Action_None` | 3 | 39 | 37 | inferred_complete_timeline |
| `Action_None` | 60 | 61 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–88
- **Visible Samples:** 82

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 2 | 3 | inferred_complete_timeline |
| `Action_None` | 3 | 79 | 77 | inferred_complete_timeline |
| `Action_None` | 87 | 88 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 285

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 2 | 3 | inferred_complete_timeline |
| `Action_None` | 3 | 81 | 79 | inferred_complete_timeline |
| `Action_None` | 83 | 84 | 2 | inferred_complete_timeline |
| `Action_None` | 87 | 131 | 45 | inferred_complete_timeline |
| `Action_None` | 133 | 134 | 2 | inferred_complete_timeline |
| `Action_None` | 138 | 141 | 4 | inferred_complete_timeline |
| `Action_None` | 149 | 175 | 27 | inferred_complete_timeline |
| `Action_None` | 177 | 299 | 123 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–180
- **Visible Samples:** 176

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 2 | 3 | inferred_complete_timeline |
| `Action_None` | 3 | 135 | 133 | inferred_complete_timeline |
| `Action_None` | 137 | 168 | 32 | inferred_complete_timeline |
| `Action_None` | 173 | 180 | 8 | inferred_complete_timeline |

</details>

<details>
<summary>CB4 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 300

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 2 | 3 | inferred_complete_timeline |
| `Action_None` | 3 | 299 | 297 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–132
- **Visible Samples:** 133

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 2 | 3 | inferred_complete_timeline |
| `Action_None` | 3 | 132 | 130 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `22` | `23` | Position_Unknown | Team_Unknown | 48–98 | 51 | 1 | Undefined position; Undefined team |
| `23` | `24` | Position_Unknown | Team_Unknown | 51–70 | 16 | 2 | Undefined position; Undefined team |
| `24` | `26` | Position_Unknown | Team_Unknown | 56–85 | 30 | 1 | Undefined position; Undefined team |
| `25` | `29` | Position_Unknown | Team_Unknown | 81–86 | 4 | 2 | Undefined position; Undefined team |
| `26` | `33` | Position_Unknown | Team_Unknown | 97–191 | 66 | 3 | Undefined position; Undefined team |
| `27` | `34` | Position_Unknown | Team_Unknown | 97–299 | 193 | 4 | Undefined position; Undefined team |
| `28` | `35` | Position_Unknown | Team_Unknown | 120–267 | 138 | 4 | Undefined position; Undefined team |
| `29` | `36` | Position_Unknown | Team_Unknown | 128–299 | 172 | 1 | Undefined position; Undefined team |
| `30` | `37` | Position_Unknown | Team_Unknown | 131–208 | 77 | 2 | Undefined position; Undefined team |
| `31` | `39` | Position_Unknown | Team_Unknown | 133–293 | 156 | 3 | Undefined position; Undefined team |
| `32` | `40` | Position_Unknown | Team_Unknown | 150–299 | 128 | 3 | Undefined position; Undefined team |
| `33` | `41` | Position_Unknown | Team_Unknown | 223–225 | 3 | 1 | Undefined position; Undefined team |
| `34` | `42` | Position_Unknown | Team_Unknown | 227–299 | 72 | 2 | Undefined position; Undefined team |
| `35` | `43` | Position_Unknown | Team_Unknown | 229–286 | 38 | 7 | Undefined position; Undefined team |
| `36` | `45` | Position_Unknown | Team_Unknown | 237–282 | 28 | 4 | Undefined position; Undefined team |
| `37` | `47` | Position_Unknown | Team_Unknown | 262–265 | 4 | 1 | Undefined position; Undefined team |
| `38` | `48` | Position_Unknown | Team_Unknown | 276–299 | 23 | 2 | Undefined position; Undefined team |
| `39` | `49` | Position_Unknown | Team_Unknown | 276–290 | 15 | 1 | Undefined position; Undefined team |
| `40` | `50` | Position_Unknown | Team_Unknown | 278–299 | 22 | 1 | Undefined position; Undefined team |
| `41` | `51` | Position_Unknown | Team_Unknown | 295–299 | 5 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_PassBlock` and target `10` (2 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `12` (6 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `18` (5 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `21` (3 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `4` (6 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `16` (actor_track_id `16`): `SAF` position mapped to `defense` team
- ⚠️ 20 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 20 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 40 |
| Missing visible bounding boxes during action | 100 |
| Track-related warning | 1 |
| Other | 2 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 299 as fallback play end.
- ⚠️ Resolved action overlap for track '18' (C): higher_priority='Action_BallSnap' [3–16], lower_priority='Action_PassBlock' annotated_start=7, effective_Action_PassBlock_start=17.
- ⚠️ Action 'Action_None' range [3-289] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [81-110] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [3-128] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [133-201] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [3-275] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [7-53] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [57-72] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [74-99] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [101-105] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [108-164] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [3-135] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [137-168] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [173-180] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [3-191] for track '7' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [193-208] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [214-218] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [3-192] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [215-228] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [231-236] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [238-282] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [285-286] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [3-79] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [87-88] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [7-51] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [59-60] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [3-39] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [41-96] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [101-105] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [108-299] for track '11' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [7-35] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [53-55] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [59-73] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [77-83] for track '12' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [86-87] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [89-90] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [3-81] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [83-84] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [87-131] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [133-134] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [138-141] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [149-175] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [65-238] for track '14' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [3-38] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [41-74] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [79-265] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [3-132] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [3-100] for track '17' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [122-126] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [130-299] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [17-98] for track '18' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [112-191] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [195-238] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [240-257] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [260-299] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [3-22] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [3-39] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [60-61] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [7-70] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [72-73] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [75-83] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [48-98] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [51-62] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [67-70] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [56-85] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [81-82] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [85-86] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [97-147] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [153-165] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [190-191] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [97-171] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [175-229] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [234-238] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [120-123] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [132-135] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [137-251] for track '28' has 6 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [253-267] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [131-204] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [206-208] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [133-134] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [138-233] for track '31' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [236-293] for track '31' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [150-195] for track '32' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [202-228] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [223-225] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [227-234] for track '34' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [236-299] for track '34' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [229-238] for track '35' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [241-248] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [251-255] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [266-268] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [272-273] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [275-278] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [281-286] for track '35' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [237-238] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [240-241] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [246-248] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [262-282] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [262-265] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [276-287] for track '38' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [276-290] for track '39' has 1 frames without a visible bounding box.
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
- ⚠️ Player track '35' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '35' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '36' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '36' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '37' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '37' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '38' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '38' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '39' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '39' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '40' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '40' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '41' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '41' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Play definition: no definition found for 'Play_Pass_Slants0to10'.

</details>