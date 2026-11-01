# Play-Annotation-Generator Annotation Review — InsideZoneRead_353

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `InsideZoneRead_353`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Run_InsideZoneRead`
- **Result:** `Result_Tackle`
- **Result Frame:** 239
- **Player Tracks:** 26
- **Ball Tracks:** 0
- **Action Segments:** 106
- **Validation Warnings:** 89
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 23
- **Exact Matches:** 5
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 1
- **Missing Segments:** 0
- **Ambiguous Matches:** 4
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 77
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB2 | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB1 | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `8` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `20` | `19` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | offense | `14` | `13` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | offense | `17` | `16` |
| ⚠️ START CHANGED | `Action_ZoneBlock` | C | offense | `20` | `19` |
| ✅ EXACT | `Action_ZoneBlock` | LT | offense | `5` | `4` |
| ✅ EXACT | `Action_ZoneBlock` | LG | offense | `8` | `7` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `21` | `20` |
| ✅ EXACT | `Action_ReadDefender` | QB | offense | `21` | `20` |
| ⚠️ AMBIGUOUS MATCH | `Action_Keep` | QB | offense | `21` | `20` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | QB | offense | `21` | `20` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB2 | `10` | `Group` | 0 | START | 0 | 0 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB1 | `12` | `Group` | 0 | START | 0 | 0 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `14` | `Group` | 0 | START | 0 | 3 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `17` | `Group` | 0 | START | 0 | 3 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `2` | `Group` | 0 | START | 0 | 0 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `20` | `Group` | 0 | START | 0 | 0 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `21` | `Group` | 0 | START | 0 | 0 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `3` | `Group` | 0 | START | 0 | 0 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `5` | `Group` | 0 | START | 0 | 3 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `6` | `Group` | 0 | START | 0 | 0 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `8` | `Group` | 0 | START | 0 | 3 |
| ✅ EXACT | `Action_BallSnap` | C | `20` | `19` | 1 | START | 1 | 15 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | `14` | `13` | 4 | START | 4 | 15 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | `17` | `16` | 4 | START | 4 | 49 |
| ⚠️ START CHANGED | `Action_ZoneBlock` | C | `20` | `19` | 4 | START | 16 | 33 |
| ✅ EXACT | `Action_ZoneBlock` | LT | `5` | `4` | 4 | START | 4 | 82 |
| ✅ EXACT | `Action_ZoneBlock` | LG | `8` | `7` | 4 | START | 4 | 82 |
| ✅ EXACT | `Action_SnapReceive` | QB | `21` | `20` | 15 | END | 1 | 15 |
| ✅ EXACT | `Action_ReadDefender` | QB | `21` | `20` | 19 | START | 19 | 27 |
| ⚠️ AMBIGUOUS MATCH | `Action_Keep` | QB | `21` | `20` | 28 | START | 28 | 29 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | QB | `21` | `20` | 54 | START | 54 | 134 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 82 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `21`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–178
- **Visible Samples:** 165

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_SnapReceive` | 1 | 15 | 15 | inferred_complete_timeline |
| `Action_None` | 16 | 18 | 3 | inferred_complete_timeline |
| `Action_ReadDefender` | 19 | 27 | 9 | inferred_complete_timeline |
| `Action_Keep` | 28 | 29 | 2 | inferred_complete_timeline |
| `Action_Keep` | 31 | 53 | 23 | inferred_complete_timeline |
| `Action_BallCarry` | 54 | 134 | 81 | inferred_complete_timeline |
| `Action_BallCarry` | 140 | 160 | 21 | inferred_complete_timeline |
| `Action_BallCarry` | 166 | 169 | 4 | inferred_complete_timeline |
| `Action_BallCarry` | 171 | 174 | 4 | inferred_complete_timeline |
| `Action_BallCarry` | 177 | 178 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>RB1 — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–134
- **Visible Samples:** 133

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 80 | 80 | inferred_complete_timeline |
| `Action_None` | 83 | 134 | 52 | inferred_complete_timeline |

</details>

<details>
<summary>RB2 — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–180
- **Visible Samples:** 167

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 15 | 15 | inferred_complete_timeline |
| `Action_None` | 18 | 136 | 119 | inferred_complete_timeline |
| `Action_None` | 142 | 143 | 2 | inferred_complete_timeline |
| `Action_None` | 151 | 180 | 30 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–180
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 180 | 180 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–180
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 180 | 180 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–180
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 180 | 180 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–174
- **Visible Samples:** 170

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 3 | 4 | inferred_complete_timeline |
| `Action_ZoneBlock` | 4 | 82 | 79 | inferred_complete_timeline |
| `Action_None` | 83 | 160 | 78 | inferred_complete_timeline |
| `Action_None` | 166 | 174 | 9 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–180
- **Visible Samples:** 161

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 3 | 4 | inferred_complete_timeline |
| `Action_ZoneBlock` | 4 | 82 | 79 | inferred_complete_timeline |
| `Action_None` | 83 | 150 | 68 | inferred_complete_timeline |
| `Action_None` | 167 | 168 | 2 | inferred_complete_timeline |
| `Action_None` | 170 | 174 | 5 | inferred_complete_timeline |
| `Action_None` | 178 | 180 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `20`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–33
- **Visible Samples:** 34

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_BallSnap` | 1 | 15 | 15 | inferred_complete_timeline |
| `Action_ZoneBlock` | 16 | 33 | 18 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–167
- **Visible Samples:** 138

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 3 | 4 | inferred_complete_timeline |
| `Action_ZoneBlock` | 4 | 15 | 12 | inferred_complete_timeline |
| `Action_ZoneBlock` | 17 | 30 | 14 | inferred_complete_timeline |
| `Action_ZoneBlock` | 36 | 82 | 47 | inferred_complete_timeline |
| `Action_None` | 83 | 115 | 33 | inferred_complete_timeline |
| `Action_None` | 117 | 121 | 5 | inferred_complete_timeline |
| `Action_None` | 123 | 125 | 3 | inferred_complete_timeline |
| `Action_None` | 143 | 150 | 8 | inferred_complete_timeline |
| `Action_None` | 152 | 161 | 10 | inferred_complete_timeline |
| `Action_None` | 166 | 167 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `17`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–180
- **Visible Samples:** 177

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 3 | 4 | inferred_complete_timeline |
| `Action_ZoneBlock` | 4 | 49 | 46 | inferred_complete_timeline |
| `Action_ZoneBlock` | 52 | 82 | 31 | inferred_complete_timeline |
| `Action_None` | 83 | 143 | 61 | inferred_complete_timeline |
| `Action_None` | 146 | 180 | 35 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–180
- **Visible Samples:** 175

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 26 | 26 | inferred_complete_timeline |
| `Action_None` | 31 | 169 | 139 | inferred_complete_timeline |
| `Action_None` | 172 | 180 | 9 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–172
- **Visible Samples:** 96

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 40 | 40 | inferred_complete_timeline |
| `Action_None` | 67 | 72 | 6 | inferred_complete_timeline |
| `Action_None` | 108 | 109 | 2 | inferred_complete_timeline |
| `Action_None` | 124 | 126 | 3 | inferred_complete_timeline |
| `Action_None` | 129 | 172 | 44 | inferred_complete_timeline |

</details>

<details>
<summary>DT — actor_track_id `18`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `18`
- **team_side:** `defense`
- **Visible Frames:** 0–180
- **Visible Samples:** 176

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 39 | 39 | inferred_complete_timeline |
| `Action_None` | 45 | 180 | 136 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `19`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `19`
- **team_side:** `defense`
- **Visible Frames:** 0–170
- **Visible Samples:** 147

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 98 | 98 | inferred_complete_timeline |
| `Action_None` | 102 | 103 | 2 | inferred_complete_timeline |
| `Action_None` | 107 | 136 | 30 | inferred_complete_timeline |
| `Action_None` | 155 | 170 | 16 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–180
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 180 | 180 | inferred_complete_timeline |

</details>

<details>
<summary>LB3 — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–178
- **Visible Samples:** 178

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 78 | 78 | inferred_complete_timeline |
| `Action_None` | 80 | 178 | 99 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–160
- **Visible Samples:** 151

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 129 | 129 | inferred_complete_timeline |
| `Action_None` | 131 | 146 | 16 | inferred_complete_timeline |
| `Action_None` | 156 | 160 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–180
- **Visible Samples:** 180

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 136 | 136 | inferred_complete_timeline |
| `Action_None` | 138 | 180 | 43 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–180
- **Visible Samples:** 178

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 143 | 143 | inferred_complete_timeline |
| `Action_None` | 147 | 180 | 34 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `22`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `22`
- **team_side:** `defense`
- **Visible Frames:** 0–180
- **Visible Samples:** 161

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 69 | 69 | inferred_complete_timeline |
| `Action_None` | 71 | 75 | 5 | inferred_complete_timeline |
| `Action_None` | 83 | 100 | 18 | inferred_complete_timeline |
| `Action_None` | 102 | 110 | 9 | inferred_complete_timeline |
| `Action_None` | 116 | 118 | 3 | inferred_complete_timeline |
| `Action_None` | 122 | 123 | 2 | inferred_complete_timeline |
| `Action_None` | 126 | 127 | 2 | inferred_complete_timeline |
| `Action_None` | 129 | 180 | 52 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–134
- **Visible Samples:** 122

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 96 | 96 | inferred_complete_timeline |
| `Action_None` | 98 | 104 | 7 | inferred_complete_timeline |
| `Action_None` | 113 | 123 | 11 | inferred_complete_timeline |
| `Action_None` | 128 | 134 | 7 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `22` | `23` | Position_Unknown | Team_Unknown | 37–48 | 12 | 1 | Undefined position; Undefined team |
| `23` | `24` | Position_Unknown | Team_Unknown | 56–180 | 122 | 2 | Undefined position; Undefined team |
| `24` | `27` | Position_Unknown | Team_Unknown | 125–131 | 7 | 1 | Undefined position; Undefined team |
| `25` | `28` | Position_Unknown | Team_Unknown | 149–180 | 18 | 2 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `14` (3 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `17` (2 segments found)
- ⚠️ `Action_ZoneBlock` for actor_track_id `20` (C): Annotated start 4 != Inferred start 16
- ⚠️ Ambiguous match for action `Action_Keep` and target `21` (2 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `21` (5 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `14` (actor_track_id `15`): `SAF2` position mapped to `defense` team
- ⚠️ Player track XML ID `21` (actor_track_id `22`): `SAF1` position mapped to `defense` team
- ⚠️ 4 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 4 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 8 |
| Missing visible bounding boxes during action | 79 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Resolved action overlap for track '19' (C): higher_priority='Action_BallSnap' [1–15], lower_priority='Action_ZoneBlock' annotated_start=4, effective_Action_ZoneBlock_start=16.
- ⚠️ Action 'Action_None' range [1-143] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [147-180] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-180] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-180] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-78] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [80-178] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [83-160] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [166-174] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-180] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-129] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [131-146] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [156-160] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [83-150] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [167-168] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [170-174] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [178-180] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-180] for track '8' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-15] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [18-136] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [142-143] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [151-180] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-136] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [138-180] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-80] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [83-134] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-40] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [67-72] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [108-109] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [124-126] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [129-172] for track '12' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [4-15] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [17-30] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [36-82] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [83-115] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [117-121] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [123-125] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [143-150] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [152-161] for track '13' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [166-167] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-96] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [98-104] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [113-123] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [128-134] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-26] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [31-169] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [172-180] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [4-49] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [52-82] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [83-143] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [146-180] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-39] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [45-180] for track '17' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-98] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [102-103] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [107-136] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [155-170] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [16-33] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_SnapReceive' range [1-15] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_Keep' range [28-29] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_Keep' range [31-53] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [54-134] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [140-160] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [166-169] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [171-174] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [177-178] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-69] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [71-75] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [83-100] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [102-110] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [116-118] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [122-123] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [126-127] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [129-180] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [37-48] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [56-58] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [62-180] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [125-131] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [149-163] for track '25' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [178-180] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Player track '22' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '22' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '23' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '23' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '24' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '24' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '25' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '25' has undefined team_side. Will map to Team_Unknown.

</details>