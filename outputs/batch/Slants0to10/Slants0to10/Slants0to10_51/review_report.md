# Play-Annotation-Generator Annotation Review — Slants0to10_51

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Slants0to10_51`
- **Frame Range:** 0 to 299 (300 total frames)
- **Play:** `Play_Pass_Slants0to10`
- **Result:** `Result_Tackle`
- **Result Frame:** 299
- **Player Tracks:** 52
- **Ball Tracks:** 0
- **Action Segments:** 131
- **Validation Warnings:** 177
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 19
- **Exact Matches:** 4
- **Group Expanded Events:** 10
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 4
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 108
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR5 | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR4 | offense | `8` | `Group` |
| ✅ EXACT | `Action_PassBlock` | LG | offense | `18` | `18` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | C | offense | `19` | `19` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LT | offense | `2` | `2` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RT | offense | `21` | `21` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `13` | `13` |
| ✅ EXACT | `Action_RunSlantRoute` | WR1 | offense | `17` | `17` |
| ✅ EXACT | `Action_ThrowPass` | QB | offense | `13` | `13` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | WR1 | offense | `17` | `17` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `1` | `Group` | 0 | START | 0 | 299 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `13` | `Group` | 0 | START | 0 | 1 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `17` | `Group` | 0 | START | 0 | 8 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `18` | `Group` | 0 | START | 0 | 1 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `19` | `Group` | 0 | START | 0 | 1 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `2` | `Group` | 0 | START | 0 | 1 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `21` | `Group` | 0 | START | 0 | 1 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `3` | `Group` | 0 | START | 0 | 25 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR5 | `4` | `Group` | 0 | START | 0 | 266 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR4 | `8` | `Group` | 0 | START | 0 | 185 |
| ✅ EXACT | `Action_PassBlock` | LG | `18` | `18` | 2 | START | 2 | 12 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | C | `19` | `19` | 2 | START | 2 | 5 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LT | `2` | `2` | 2 | START | 2 | 20 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RT | `21` | `21` | 2 | START | 5 | 12 |
| ✅ EXACT | `Action_SnapReceive` | QB | `13` | `13` | 2 | END | 2 | 2 |
| ✅ EXACT | `Action_RunSlantRoute` | WR1 | `17` | `17` | 9 | START | 9 | 60 |
| ✅ EXACT | `Action_ThrowPass` | QB | `13` | `13` | 44 | START | 44 | 51 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | WR1 | `17` | `17` | 84 | START | 84 | 124 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–139
- **Visible Samples:** 104

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_SnapReceive` | 2 | 2 | 1 | inferred_complete_timeline |
| `Action_None` | 3 | 43 | 41 | inferred_complete_timeline |
| `Action_ThrowPass` | 44 | 51 | 8 | inferred_complete_timeline |
| `Action_None` | 52 | 68 | 17 | inferred_complete_timeline |
| `Action_None` | 81 | 91 | 11 | inferred_complete_timeline |
| `Action_None` | 94 | 98 | 5 | inferred_complete_timeline |
| `Action_None` | 105 | 114 | 10 | inferred_complete_timeline |
| `Action_None` | 118 | 123 | 6 | inferred_complete_timeline |
| `Action_None` | 137 | 139 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–290
- **Visible Samples:** 261

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 8 | 9 | inferred_complete_timeline |
| `Action_RunSlantRoute` | 9 | 60 | 52 | inferred_complete_timeline |
| `Action_None` | 61 | 83 | 23 | inferred_complete_timeline |
| `Action_BallCarry` | 84 | 124 | 41 | inferred_complete_timeline |
| `Action_BallCarry` | 131 | 136 | 6 | inferred_complete_timeline |
| `Action_BallCarry` | 150 | 246 | 97 | inferred_complete_timeline |
| `Action_BallCarry` | 256 | 261 | 6 | inferred_complete_timeline |
| `Action_BallCarry` | 264 | 290 | 27 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 294

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 25 | 26 | inferred_complete_timeline |
| `Action_PreSnap` | 29 | 44 | 16 | inferred_complete_timeline |
| `Action_PreSnap` | 48 | 299 | 252 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 300

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 299 | 300 | inferred_complete_timeline |

</details>

<details>
<summary>WR4 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–200
- **Visible Samples:** 195

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 185 | 186 | inferred_complete_timeline |
| `Action_PreSnap` | 192 | 200 | 9 | inferred_complete_timeline |

</details>

<details>
<summary>WR5 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–282
- **Visible Samples:** 279

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 266 | 267 | inferred_complete_timeline |
| `Action_PreSnap` | 268 | 270 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 274 | 282 | 9 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–69
- **Visible Samples:** 51

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_PassBlock` | 2 | 20 | 19 | inferred_complete_timeline |
| `Action_PassBlock` | 38 | 39 | 2 | inferred_complete_timeline |
| `Action_PassBlock` | 42 | 69 | 28 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–12
- **Visible Samples:** 13

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_PassBlock` | 2 | 12 | 11 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–42
- **Visible Samples:** 17

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_PassBlock` | 2 | 5 | 4 | inferred_complete_timeline |
| `Action_PassBlock` | 12 | 13 | 2 | inferred_complete_timeline |
| `Action_PassBlock` | 16 | 19 | 4 | inferred_complete_timeline |
| `Action_PassBlock` | 33 | 34 | 2 | inferred_complete_timeline |
| `Action_PassBlock` | 40 | 42 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `21`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–31
- **Visible Samples:** 17

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_PassBlock` | 5 | 12 | 8 | inferred_complete_timeline |
| `Action_PassBlock` | 16 | 18 | 3 | inferred_complete_timeline |
| `Action_PassBlock` | 21 | 22 | 2 | inferred_complete_timeline |
| `Action_PassBlock` | 30 | 31 | 2 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `defense`
- **Visible Frames:** 0–68
- **Visible Samples:** 62

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 12 | 13 | inferred_complete_timeline |
| `Action_PreSnap` | 16 | 19 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 22 | 28 | 7 | inferred_complete_timeline |
| `Action_PreSnap` | 30 | 36 | 7 | inferred_complete_timeline |
| `Action_PreSnap` | 38 | 68 | 31 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–6
- **Visible Samples:** 7

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 6 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–148
- **Visible Samples:** 92

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 9 | 10 | inferred_complete_timeline |
| `Action_PreSnap` | 16 | 19 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 30 | 69 | 40 | inferred_complete_timeline |
| `Action_PreSnap` | 111 | 148 | 38 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–68
- **Visible Samples:** 62

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 26 | 27 | inferred_complete_timeline |
| `Action_PreSnap` | 30 | 31 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 33 | 63 | 31 | inferred_complete_timeline |
| `Action_PreSnap` | 67 | 68 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 274

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 73 | 74 | inferred_complete_timeline |
| `Action_PreSnap` | 78 | 81 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 92 | 99 | 8 | inferred_complete_timeline |
| `Action_PreSnap` | 102 | 133 | 32 | inferred_complete_timeline |
| `Action_PreSnap` | 138 | 141 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 147 | 214 | 68 | inferred_complete_timeline |
| `Action_PreSnap` | 216 | 299 | 84 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 275

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 256 | 257 | inferred_complete_timeline |
| `Action_PreSnap` | 282 | 299 | 18 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 297

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 219 | 220 | inferred_complete_timeline |
| `Action_PreSnap` | 222 | 287 | 66 | inferred_complete_timeline |
| `Action_PreSnap` | 289 | 299 | 11 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 300

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 299 | 300 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–57
- **Visible Samples:** 58

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 57 | 58 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 299

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 220 | 221 | inferred_complete_timeline |
| `Action_PreSnap` | 222 | 299 | 78 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–96
- **Visible Samples:** 96

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 87 | 88 | inferred_complete_timeline |
| `Action_PreSnap` | 89 | 96 | 8 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `20` | `20` | Position_Unknown | Team_Unknown | 0–29 | 15 | 2 | Undefined position; Undefined team |
| `22` | `22` | Position_Unknown | Team_Unknown | 0–76 | 76 | 2 | Undefined position; Undefined team |
| `23` | `24` | Position_Unknown | Team_Unknown | 5–168 | 122 | 8 | Undefined position; Undefined team |
| `24` | `25` | Position_Unknown | Team_Unknown | 52–114 | 25 | 4 | Undefined position; Undefined team |
| `25` | `26` | Position_Unknown | Team_Unknown | 53–58 | 4 | 2 | Undefined position; Undefined team |
| `26` | `27` | Position_Unknown | Team_Unknown | 61–76 | 8 | 3 | Undefined position; Undefined team |
| `27` | `28` | Position_Unknown | Team_Unknown | 64–299 | 224 | 4 | Undefined position; Undefined team |
| `28` | `29` | Position_Unknown | Team_Unknown | 68–73 | 6 | 1 | Undefined position; Undefined team |
| `29` | `30` | Position_Unknown | Team_Unknown | 83–112 | 20 | 2 | Undefined position; Undefined team |
| `30` | `32` | Position_Unknown | Team_Unknown | 87–90 | 4 | 1 | Undefined position; Undefined team |
| `31` | `33` | Position_Unknown | Team_Unknown | 87–92 | 6 | 1 | Undefined position; Undefined team |
| `32` | `34` | Position_Unknown | Team_Unknown | 92–93 | 2 | 1 | Undefined position; Undefined team |
| `33` | `35` | Position_Unknown | Team_Unknown | 93–94 | 2 | 1 | Undefined position; Undefined team |
| `34` | `36` | Position_Unknown | Team_Unknown | 106–114 | 9 | 1 | Undefined position; Undefined team |
| `35` | `38` | Position_Unknown | Team_Unknown | 109–299 | 187 | 2 | Undefined position; Undefined team |
| `36` | `39` | Position_Unknown | Team_Unknown | 111–116 | 6 | 1 | Undefined position; Undefined team |
| `37` | `42` | Position_Unknown | Team_Unknown | 123–124 | 2 | 1 | Undefined position; Undefined team |
| `38` | `43` | Position_Unknown | Team_Unknown | 129–132 | 4 | 1 | Undefined position; Undefined team |
| `39` | `45` | Position_Unknown | Team_Unknown | 132–299 | 168 | 1 | Undefined position; Undefined team |
| `40` | `46` | Position_Unknown | Team_Unknown | 139–201 | 63 | 1 | Undefined position; Undefined team |
| `41` | `47` | Position_Unknown | Team_Unknown | 139–140 | 2 | 1 | Undefined position; Undefined team |
| `42` | `50` | Position_Unknown | Team_Unknown | 144–145 | 2 | 1 | Undefined position; Undefined team |
| `43` | `51` | Position_Unknown | Team_Unknown | 145–243 | 72 | 3 | Undefined position; Undefined team |
| `44` | `52` | Position_Unknown | Team_Unknown | 146–299 | 154 | 1 | Undefined position; Undefined team |
| `45` | `54` | Position_Unknown | Team_Unknown | 156–299 | 143 | 2 | Undefined position; Undefined team |
| `46` | `57` | Position_Unknown | Team_Unknown | 182–194 | 9 | 2 | Undefined position; Undefined team |
| `47` | `66` | Position_Unknown | Team_Unknown | 223–259 | 37 | 1 | Undefined position; Undefined team |
| `48` | `69` | Position_Unknown | Team_Unknown | 267–299 | 33 | 1 | Undefined position; Undefined team |
| `49` | `70` | Position_Unknown | Team_Unknown | 285–290 | 6 | 1 | Undefined position; Undefined team |
| `50` | `71` | Position_Unknown | Team_Unknown | 288–299 | 12 | 1 | Undefined position; Undefined team |
| `51` | `72` | Position_Unknown | Team_Unknown | 291–299 | 9 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_PassBlock` and target `19` (5 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `2` (3 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `21` (4 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `17` (5 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `7` (actor_track_id `7`): `SAF1` position mapped to `defense` team
- ⚠️ Player track XML ID `9` (actor_track_id `9`): `SAF2` position mapped to `defense` team
- ⚠️ 31 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 31 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 62 |
| Missing visible bounding boxes during action | 111 |
| Track-related warning | 1 |
| Other | 3 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 51: Duplicate assignment for track ID '21' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 299 as fallback play end.
- ⚠️ Action_SnapReceive present in CSV, but paired Action_BallSnap is missing.
- ⚠️ Action 'Action_PreSnap' range [0-12] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [16-19] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [22-28] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [30-36] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [38-68] for track '0' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [2-20] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [38-39] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [42-69] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-25] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [29-44] for track '3' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [48-299] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-266] for track '4' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [268-270] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [274-282] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-219] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [222-287] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [289-299] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-256] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-220] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-185] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [192-200] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-87] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [89-96] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-73] for track '10' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [78-81] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [92-99] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [102-133] for track '10' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [138-141] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [147-214] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-299] for track '11' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-26] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [30-31] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [33-63] for track '12' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [67-68] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [52-68] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [81-91] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [94-98] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [105-114] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [118-123] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [137-139] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-9] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [16-19] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [30-69] for track '14' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [111-148] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-6] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-57] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [84-124] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [131-136] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [150-246] for track '17' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [256-261] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [264-290] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [2-12] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [2-5] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [12-13] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [16-19] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [33-34] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [40-42] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-9] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [25-29] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-1] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [5-12] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [16-18] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [21-22] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [30-31] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-12] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [14-76] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [5-8] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [10-20] for track '23' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [33-37] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [39-68] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [70-74] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [100-114] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [116-120] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [122-168] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [52-68] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [70-72] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [75-76] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [112-114] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [53-54] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [57-58] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [61-62] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [64-67] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [75-76] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [64-163] for track '27' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [171-198] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [201-205] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [209-299] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [68-73] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [83-93] for track '29' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [104-112] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [87-90] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [87-92] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [92-93] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [93-94] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [106-114] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [109-129] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [111-116] for track '36' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [123-124] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [129-132] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [139-201] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [139-140] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [144-145] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [145-211] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [229-230] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [241-243] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [156-270] for track '45' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [182-183] for track '46' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [188-194] for track '46' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [223-259] for track '47' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [285-290] for track '49' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [288-299] for track '50' has 1 frames without a visible bounding box.
- ⚠️ Player track '20' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '20' has undefined team_side. Will map to Team_Unknown.
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
- ⚠️ Player track '42' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '42' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '43' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '43' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '44' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '44' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '45' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '45' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '46' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '46' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '47' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '47' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '48' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '48' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '49' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '49' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '50' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '50' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '51' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '51' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Play definition: no definition found for 'Play_Pass_Slants0to10'.

</details>