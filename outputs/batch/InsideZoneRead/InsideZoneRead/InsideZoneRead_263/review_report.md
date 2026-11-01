# Play-Annotation-Generator Annotation Review — InsideZoneRead_263

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `InsideZoneRead_263`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Run_InsideZoneRead`
- **Result:** `Result_Tackle`
- **Result Frame:** 239
- **Player Tracks:** 41
- **Ball Tracks:** 0
- **Action Segments:** 164
- **Validation Warnings:** 187
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 22
- **Exact Matches:** 5
- **Group Expanded Events:** 10
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 5
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 141
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `3` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `16` | `15` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | offense | `14` | `13` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | offense | `15` | `14` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | offense | `16` | `15` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | offense | `17` | `16` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `13` | `12` |
| ✅ EXACT | `Action_ReadDefender` | QB | offense | `13` | `12` |
| ⚠️ AMBIGUOUS MATCH | `Action_BlockSecondLevel` | DT1 | defense | `19` | `18` |
| ✅ EXACT | `Action_Keep` | QB | offense | `13` | `12` |
| ✅ EXACT | `Action_BallCarry` | QB | offense | `13` | `12` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `1` | `Group` | 0 | START | 0 | 10 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `11` | `Group` | 0 | START | 0 | 10 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `12` | `Group` | 0 | START | 0 | 10 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `13` | `Group` | 0 | START | 0 | 10 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `14` | `Group` | 0 | START | 0 | 13 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `15` | `Group` | 0 | START | 0 | 13 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `16` | `Group` | 0 | START | 0 | 10 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `17` | `Group` | 0 | START | 0 | 13 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `2` | `Group` | 0 | START | 0 | 10 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `3` | `Group` | 0 | START | 0 | 10 |
| ✅ EXACT | `Action_BallSnap` | C | `16` | `15` | 11 | START | 11 | 21 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | `14` | `13` | 14 | START | 14 | 54 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | `15` | `14` | 14 | START | 14 | 83 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | `16` | `15` | 14 | START | 25 | 54 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | `17` | `16` | 14 | START | 14 | 37 |
| ✅ EXACT | `Action_SnapReceive` | QB | `13` | `12` | 23 | END | 11 | 23 |
| ✅ EXACT | `Action_ReadDefender` | QB | `13` | `12` | 26 | START | 26 | 35 |
| ⚠️ AMBIGUOUS MATCH | `Action_BlockSecondLevel` | DT1 | `19` | `18` | 32 | START | 32 | 54 |
| ✅ EXACT | `Action_Keep` | QB | `13` | `12` | 36 | START | 36 | 46 |
| ✅ EXACT | `Action_BallCarry` | QB | `13` | `12` | 47 | START | 47 | 88 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 83 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–88
- **Visible Samples:** 89

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 10 | 11 | inferred_complete_timeline |
| `Action_SnapReceive` | 11 | 23 | 13 | inferred_complete_timeline |
| `Action_None` | 24 | 25 | 2 | inferred_complete_timeline |
| `Action_ReadDefender` | 26 | 35 | 10 | inferred_complete_timeline |
| `Action_Keep` | 36 | 46 | 11 | inferred_complete_timeline |
| `Action_BallCarry` | 47 | 88 | 42 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–77
- **Visible Samples:** 78

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 10 | 11 | inferred_complete_timeline |
| `Action_None` | 11 | 77 | 67 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 10 | 11 | inferred_complete_timeline |
| `Action_None` | 11 | 210 | 200 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 210

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 10 | 11 | inferred_complete_timeline |
| `Action_None` | 11 | 188 | 178 | inferred_complete_timeline |
| `Action_None` | 190 | 210 | 21 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–146
- **Visible Samples:** 147

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 10 | 11 | inferred_complete_timeline |
| `Action_None` | 11 | 146 | 136 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–165
- **Visible Samples:** 121

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 10 | 11 | inferred_complete_timeline |
| `Action_None` | 11 | 88 | 78 | inferred_complete_timeline |
| `Action_None` | 91 | 109 | 19 | inferred_complete_timeline |
| `Action_None` | 111 | 112 | 2 | inferred_complete_timeline |
| `Action_None` | 124 | 125 | 2 | inferred_complete_timeline |
| `Action_None` | 129 | 130 | 2 | inferred_complete_timeline |
| `Action_None` | 159 | 165 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–130
- **Visible Samples:** 122

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 13 | 14 | inferred_complete_timeline |
| `Action_ZoneBlock` | 14 | 83 | 70 | inferred_complete_timeline |
| `Action_None` | 84 | 88 | 5 | inferred_complete_timeline |
| `Action_None` | 94 | 97 | 4 | inferred_complete_timeline |
| `Action_None` | 102 | 130 | 29 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 189

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 13 | 14 | inferred_complete_timeline |
| `Action_ZoneBlock` | 14 | 54 | 41 | inferred_complete_timeline |
| `Action_ZoneBlock` | 74 | 83 | 10 | inferred_complete_timeline |
| `Action_None` | 84 | 90 | 7 | inferred_complete_timeline |
| `Action_None` | 94 | 210 | 117 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–67
- **Visible Samples:** 64

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 10 | 11 | inferred_complete_timeline |
| `Action_BallSnap` | 11 | 21 | 11 | inferred_complete_timeline |
| `Action_ZoneBlock` | 25 | 54 | 30 | inferred_complete_timeline |
| `Action_ZoneBlock` | 56 | 67 | 12 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `17`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–86
- **Visible Samples:** 81

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 13 | 14 | inferred_complete_timeline |
| `Action_ZoneBlock` | 14 | 37 | 24 | inferred_complete_timeline |
| `Action_ZoneBlock` | 43 | 54 | 12 | inferred_complete_timeline |
| `Action_ZoneBlock` | 56 | 83 | 28 | inferred_complete_timeline |
| `Action_None` | 84 | 86 | 3 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DT1 — actor_track_id `19`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `19`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 156

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 5 | 6 | inferred_complete_timeline |
| `Action_PreSnap` | 9 | 31 | 23 | inferred_complete_timeline |
| `Action_BlockSecondLevel` | 32 | 54 | 23 | inferred_complete_timeline |
| `Action_BlockSecondLevel` | 56 | 83 | 28 | inferred_complete_timeline |
| `Action_None` | 84 | 86 | 3 | inferred_complete_timeline |
| `Action_None` | 130 | 200 | 71 | inferred_complete_timeline |
| `Action_None` | 209 | 210 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `18`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `18`
- **team_side:** `defense`
- **Visible Frames:** 0–208
- **Visible Samples:** 119

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 5 | 6 | inferred_complete_timeline |
| `Action_PreSnap` | 9 | 10 | 2 | inferred_complete_timeline |
| `Action_None` | 11 | 20 | 10 | inferred_complete_timeline |
| `Action_None` | 22 | 40 | 19 | inferred_complete_timeline |
| `Action_None` | 63 | 77 | 15 | inferred_complete_timeline |
| `Action_None` | 79 | 81 | 3 | inferred_complete_timeline |
| `Action_None` | 85 | 86 | 2 | inferred_complete_timeline |
| `Action_None` | 124 | 125 | 2 | inferred_complete_timeline |
| `Action_None` | 129 | 130 | 2 | inferred_complete_timeline |
| `Action_None` | 133 | 134 | 2 | inferred_complete_timeline |
| `Action_None` | 147 | 167 | 21 | inferred_complete_timeline |
| `Action_None` | 169 | 177 | 9 | inferred_complete_timeline |
| `Action_None` | 179 | 182 | 4 | inferred_complete_timeline |
| `Action_None` | 184 | 201 | 18 | inferred_complete_timeline |
| `Action_None` | 205 | 208 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–97
- **Visible Samples:** 80

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 10 | 11 | inferred_complete_timeline |
| `Action_None` | 11 | 52 | 42 | inferred_complete_timeline |
| `Action_None` | 56 | 60 | 5 | inferred_complete_timeline |
| `Action_None` | 62 | 64 | 3 | inferred_complete_timeline |
| `Action_None` | 67 | 75 | 9 | inferred_complete_timeline |
| `Action_None` | 80 | 86 | 7 | inferred_complete_timeline |
| `Action_None` | 95 | 97 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–95
- **Visible Samples:** 91

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 10 | 11 | inferred_complete_timeline |
| `Action_None` | 11 | 52 | 42 | inferred_complete_timeline |
| `Action_None` | 55 | 88 | 34 | inferred_complete_timeline |
| `Action_None` | 92 | 95 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 10 | 11 | inferred_complete_timeline |
| `Action_None` | 11 | 210 | 200 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 10 | 11 | inferred_complete_timeline |
| `Action_None` | 11 | 210 | 200 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–146
- **Visible Samples:** 147

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 10 | 11 | inferred_complete_timeline |
| `Action_None` | 11 | 146 | 136 | inferred_complete_timeline |

</details>

<details>
<summary>CB4 — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 208

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 10 | 11 | inferred_complete_timeline |
| `Action_None` | 11 | 141 | 131 | inferred_complete_timeline |
| `Action_None` | 143 | 198 | 56 | inferred_complete_timeline |
| `Action_None` | 201 | 210 | 10 | inferred_complete_timeline |

</details>

<details>
<summary>CB5 — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–88
- **Visible Samples:** 89

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 10 | 11 | inferred_complete_timeline |
| `Action_None` | 11 | 88 | 78 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `19` | `20` | Position_Unknown | Team_Unknown | 3–97 | 80 | 5 | Undefined position; Undefined team |
| `20` | `21` | Position_Unknown | Team_Unknown | 13–99 | 70 | 5 | Undefined position; Undefined team |
| `21` | `22` | Position_Unknown | Team_Unknown | 13–210 | 120 | 10 | Undefined position; Undefined team |
| `22` | `23` | Position_Unknown | Team_Unknown | 34–134 | 91 | 4 | Undefined position; Undefined team |
| `23` | `24` | Position_Unknown | Team_Unknown | 101–130 | 24 | 2 | Undefined position; Undefined team |
| `24` | `25` | Position_Unknown | Team_Unknown | 104–210 | 107 | 1 | Undefined position; Undefined team |
| `25` | `27` | Position_Unknown | Team_Unknown | 118–130 | 13 | 1 | Undefined position; Undefined team |
| `26` | `29` | Position_Unknown | Team_Unknown | 131–210 | 51 | 5 | Undefined position; Undefined team |
| `27` | `30` | Position_Unknown | Team_Unknown | 137–138 | 2 | 1 | Undefined position; Undefined team |
| `28` | `32` | Position_Unknown | Team_Unknown | 139–203 | 23 | 5 | Undefined position; Undefined team |
| `29` | `33` | Position_Unknown | Team_Unknown | 140–194 | 46 | 5 | Undefined position; Undefined team |
| `30` | `34` | Position_Unknown | Team_Unknown | 141–143 | 3 | 1 | Undefined position; Undefined team |
| `31` | `35` | Position_Unknown | Team_Unknown | 144–210 | 42 | 7 | Undefined position; Undefined team |
| `32` | `36` | Position_Unknown | Team_Unknown | 146–210 | 32 | 6 | Undefined position; Undefined team |
| `33` | `37` | Position_Unknown | Team_Unknown | 149–210 | 47 | 8 | Undefined position; Undefined team |
| `34` | `38` | Position_Unknown | Team_Unknown | 149–198 | 45 | 2 | Undefined position; Undefined team |
| `35` | `40` | Position_Unknown | Team_Unknown | 173–210 | 27 | 4 | Undefined position; Undefined team |
| `36` | `42` | Position_Unknown | Team_Unknown | 183–184 | 2 | 1 | Undefined position; Undefined team |
| `37` | `43` | Position_Unknown | Team_Unknown | 189–196 | 7 | 2 | Undefined position; Undefined team |
| `38` | `45` | Position_Unknown | Team_Unknown | 194–199 | 6 | 1 | Undefined position; Undefined team |
| `39` | `46` | Position_Unknown | Team_Unknown | 195–210 | 16 | 1 | Undefined position; Undefined team |
| `40` | `47` | Position_Unknown | Team_Unknown | 196–210 | 15 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `14` (3 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `15` (3 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `16` (5 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `17` (3 segments found)
- ⚠️ Ambiguous match for action `Action_BlockSecondLevel` and target `19` (2 segments found)

### Track Identity Issues

- ⚠️ 22 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 22 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 44 |
| Missing visible bounding boxes during action | 140 |
| Track-related warning | 2 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 526: Duplicate assignment for track ID '7' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Resolved action overlap for track '15' (C): higher_priority='Action_BallSnap' [11–23], lower_priority='Action_ZoneBlock' annotated_start=14, effective_Action_ZoneBlock_start=24.
- ⚠️ Action 'Action_None' range [11-210] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [11-146] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [11-188] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [190-210] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [11-146] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [11-141] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [143-198] for track '4' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [201-210] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [11-210] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [11-52] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [55-88] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [92-95] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [11-88] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [11-210] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [11-52] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [56-60] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [62-64] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [67-75] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [80-86] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [95-97] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [11-77] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [11-88] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [91-109] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [111-112] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [124-125] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [129-130] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [159-165] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [47-88] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [14-54] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [84-90] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [94-210] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [84-88] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [94-97] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [102-130] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallSnap' range [11-21] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [25-54] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [56-67] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [14-37] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [43-54] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [56-83] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' for track '16' starts at frame 84, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_None' range [84-86] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-5] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' for track '17' starts at frame 11, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_None' range [11-20] for track '17' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [22-40] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [63-77] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [79-81] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [85-86] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [124-125] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [129-130] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [133-134] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [147-167] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [169-177] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [179-182] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [184-201] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [205-208] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-5] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BlockSecondLevel' range [32-54] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' for track '18' starts at frame 84, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_None' range [84-86] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [130-200] for track '18' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [209-210] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [3-5] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [11-50] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [60-64] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [68-97] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [13-39] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [43-44] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [47-52] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [63-91] for track '20' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [94-99] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [13-24] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [41-43] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [91-97] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [101-106] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [109-120] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [122-123] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [125-145] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [149-165] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [170-186] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [188-210] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [34-52] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [56-57] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [60-88] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [94-134] for track '22' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [101-102] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [109-130] for track '23' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [104-210] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [118-130] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [131-144] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [159-169] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [172-177] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [184-187] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [195-210] for track '26' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [137-138] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [139-142] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [144-146] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [159-162] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [175-176] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [194-203] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [140-165] for track '29' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [167-169] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [172-178] for track '29' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [181-182] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [187-194] for track '29' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [141-143] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [144-148] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [150-159] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [161-176] for track '31' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [188-189] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [192-193] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [195-199] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [209-210] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [146-155] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [171-172] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [177-179] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [188-193] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [198-205] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [208-210] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [149-152] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [157-162] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [164-182] for track '33' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [185-187] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [190-197] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [201-202] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [205-207] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [209-210] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [149-153] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [159-198] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [173-176] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [179-180] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [189-191] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [193-210] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [183-184] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [189-193] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [195-196] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [194-199] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [195-210] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [196-210] for track '40' has 1 frames without a visible bounding box.
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

</details>