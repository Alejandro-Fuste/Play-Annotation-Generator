# Play-Annotation-Generator Annotation Review — SplitZone_294

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `SplitZone_294`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Run_SplitZone`
- **Result:** `Result_Touchdown`
- **Result Frame:** 239
- **Player Tracks:** 30
- **Ball Tracks:** 0
- **Action Segments:** 100
- **Validation Warnings:** 83
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 25
- **Exact Matches:** 6
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 1
- **Missing Segments:** 2
- **Ambiguous Matches:** 4
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 76
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | HB | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `7` | `Group` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallSnap` | C | offense | `20` | `20` |
| ⚠️ AMBIGUOUS MATCH | `Action_SplitBlock` | HB | offense | `4` | `4` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `19` | `19` |
| ✅ EXACT | `Action_PressEdge` | RB | offense | `7` | `7` |
| ✅ EXACT | `Action_ReadEdgeDefender` | QB | offense | `19` | `19` |
| ✅ EXACT | `Action_BlockSecondLevel` | LG | offense | `17` | `17` |
| ✅ EXACT | `Action_Handoff` | QB | offense | `19` | `19` |
| ✅ EXACT | `Action_BallCarry` | RB | offense | `7` | `7` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | offense | `12` | `12` |
| ⚠️ START CHANGED | `Action_ZoneBlock` | LG | offense | `17` | `17` |
| ❌ MISSING SEGMENT | `Action_ZoneBlock` | C | offense | `20` | `20` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | offense | `21` | `21` |
| ❌ MISSING SEGMENT | `Action_ZoneBlock` | LT | offense | `6` | `6` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `0` | `Group` | 0 | START | 0 | 26 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `12` | `Group` | 0 | START | 0 | 74 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `15` | `Group` | 0 | START | 0 | 26 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `17` | `Group` | 0 | START | 0 | 55 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `19` | `Group` | 0 | START | 0 | 26 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `2` | `Group` | 0 | START | 0 | 26 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `20` | `Group` | 0 | START | 0 | 26 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `21` | `Group` | 0 | START | 0 | 39 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | HB | `4` | `Group` | 0 | START | 0 | 30 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `6` | `Group` | 0 | START | 0 | 62 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `7` | `Group` | 0 | START | 0 | 42 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallSnap` | C | `20` | `20` | 27 | START | 27 | 36 |
| ⚠️ AMBIGUOUS MATCH | `Action_SplitBlock` | HB | `4` | `4` | 31 | START | 31 | 79 |
| ✅ EXACT | `Action_SnapReceive` | QB | `19` | `19` | 39 | END | 27 | 39 |
| ✅ EXACT | `Action_PressEdge` | RB | `7` | `7` | 43 | START | 43 | 63 |
| ✅ EXACT | `Action_ReadEdgeDefender` | QB | `19` | `19` | 43 | START | 43 | 57 |
| ✅ EXACT | `Action_BlockSecondLevel` | LG | `17` | `17` | 56 | START | 56 | 73 |
| ✅ EXACT | `Action_Handoff` | QB | `19` | `19` | 58 | START | 58 | 68 |
| ✅ EXACT | `Action_BallCarry` | RB | `7` | `7` | 64 | START | 64 | 233 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | `12` | `12` | 85 | START | 85 | 86 |
| ⚠️ START CHANGED | `Action_ZoneBlock` | LG | `17` | `17` | 85 | START | 91 | 98 |
| ❌ MISSING SEGMENT | `Action_ZoneBlock` | C | `20` | `20` | 85 | START | N/A | N/A |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | `21` | `21` | 85 | START | 85 | 86 |
| ❌ MISSING SEGMENT | `Action_ZoneBlock` | LT | `6` | `6` | 85 | START | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–203
- **Visible Samples:** 204

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 26 | 27 | inferred_complete_timeline |
| `Action_SnapReceive` | 27 | 39 | 13 | inferred_complete_timeline |
| `Action_None` | 40 | 42 | 3 | inferred_complete_timeline |
| `Action_ReadEdgeDefender` | 43 | 57 | 15 | inferred_complete_timeline |
| `Action_Handoff` | 58 | 68 | 11 | inferred_complete_timeline |
| `Action_None` | 69 | 203 | 135 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–233
- **Visible Samples:** 234

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 42 | 43 | inferred_complete_timeline |
| `Action_PressEdge` | 43 | 63 | 21 | inferred_complete_timeline |
| `Action_BallCarry` | 64 | 233 | 170 | inferred_complete_timeline |

</details>

<details>
<summary>HB — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 231

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 30 | 31 | inferred_complete_timeline |
| `Action_SplitBlock` | 31 | 79 | 49 | inferred_complete_timeline |
| `Action_SplitBlock` | 83 | 84 | 2 | inferred_complete_timeline |
| `Action_SplitBlock` | 91 | 96 | 6 | inferred_complete_timeline |
| `Action_None` | 97 | 239 | 143 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 26 | 27 | inferred_complete_timeline |
| `Action_None` | 27 | 239 | 213 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–205
- **Visible Samples:** 203

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 26 | 27 | inferred_complete_timeline |
| `Action_None` | 27 | 74 | 48 | inferred_complete_timeline |
| `Action_None` | 76 | 110 | 35 | inferred_complete_timeline |
| `Action_None` | 113 | 205 | 93 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–139
- **Visible Samples:** 140

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 26 | 27 | inferred_complete_timeline |
| `Action_None` | 27 | 139 | 113 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–62
- **Visible Samples:** 63

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 62 | 63 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–209
- **Visible Samples:** 187

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 55 | 56 | inferred_complete_timeline |
| `Action_BlockSecondLevel` | 56 | 73 | 18 | inferred_complete_timeline |
| `Action_None` | 74 | 77 | 4 | inferred_complete_timeline |
| `Action_None` | 83 | 84 | 2 | inferred_complete_timeline |
| `Action_ZoneBlock` | 91 | 98 | 8 | inferred_complete_timeline |
| `Action_None` | 99 | 150 | 52 | inferred_complete_timeline |
| `Action_None` | 154 | 159 | 6 | inferred_complete_timeline |
| `Action_None` | 162 | 179 | 18 | inferred_complete_timeline |
| `Action_None` | 181 | 182 | 2 | inferred_complete_timeline |
| `Action_None` | 186 | 190 | 5 | inferred_complete_timeline |
| `Action_None` | 193 | 203 | 11 | inferred_complete_timeline |
| `Action_None` | 205 | 209 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–63
- **Visible Samples:** 61

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 26 | 27 | inferred_complete_timeline |
| `Action_BallSnap` | 27 | 36 | 10 | inferred_complete_timeline |
| `Action_BallSnap` | 38 | 39 | 2 | inferred_complete_timeline |
| `Action_None` | 40 | 50 | 11 | inferred_complete_timeline |
| `Action_None` | 53 | 63 | 11 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `21`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–234
- **Visible Samples:** 188

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 39 | 40 | inferred_complete_timeline |
| `Action_PreSnap` | 83 | 84 | 2 | inferred_complete_timeline |
| `Action_ZoneBlock` | 85 | 86 | 2 | inferred_complete_timeline |
| `Action_ZoneBlock` | 91 | 98 | 8 | inferred_complete_timeline |
| `Action_None` | 99 | 234 | 136 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–104
- **Visible Samples:** 93

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 74 | 75 | inferred_complete_timeline |
| `Action_PreSnap` | 83 | 84 | 2 | inferred_complete_timeline |
| `Action_ZoneBlock` | 85 | 86 | 2 | inferred_complete_timeline |
| `Action_ZoneBlock` | 91 | 98 | 8 | inferred_complete_timeline |
| `Action_None` | 99 | 104 | 6 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–212
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 26 | 27 | inferred_complete_timeline |
| `Action_None` | 27 | 83 | 57 | inferred_complete_timeline |
| `Action_None` | 86 | 212 | 127 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–84
- **Visible Samples:** 68

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 26 | 27 | inferred_complete_timeline |
| `Action_None` | 27 | 65 | 39 | inferred_complete_timeline |
| `Action_None` | 83 | 84 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>DT — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–195
- **Visible Samples:** 183

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 26 | 27 | inferred_complete_timeline |
| `Action_None` | 27 | 72 | 46 | inferred_complete_timeline |
| `Action_None` | 83 | 86 | 4 | inferred_complete_timeline |
| `Action_None` | 89 | 92 | 4 | inferred_complete_timeline |
| `Action_None` | 94 | 195 | 102 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–197
- **Visible Samples:** 176

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 26 | 27 | inferred_complete_timeline |
| `Action_None` | 27 | 66 | 40 | inferred_complete_timeline |
| `Action_None` | 69 | 74 | 6 | inferred_complete_timeline |
| `Action_None` | 95 | 197 | 103 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 237

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 26 | 27 | inferred_complete_timeline |
| `Action_None` | 27 | 79 | 53 | inferred_complete_timeline |
| `Action_None` | 83 | 239 | 157 | inferred_complete_timeline |

</details>

<details>
<summary>LB3 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–206
- **Visible Samples:** 207

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 26 | 27 | inferred_complete_timeline |
| `Action_None` | 27 | 206 | 180 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 26 | 27 | inferred_complete_timeline |
| `Action_None` | 27 | 239 | 213 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 26 | 27 | inferred_complete_timeline |
| `Action_None` | 27 | 239 | 213 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–144
- **Visible Samples:** 141

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 26 | 27 | inferred_complete_timeline |
| `Action_None` | 27 | 116 | 90 | inferred_complete_timeline |
| `Action_None` | 121 | 144 | 24 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–223
- **Visible Samples:** 216

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 26 | 27 | inferred_complete_timeline |
| `Action_None` | 27 | 116 | 90 | inferred_complete_timeline |
| `Action_None` | 125 | 223 | 99 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–166
- **Visible Samples:** 167

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 26 | 27 | inferred_complete_timeline |
| `Action_None` | 27 | 166 | 140 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `22` | `22` | Position_Unknown | Team_Unknown | 49–60 | 9 | 3 | Undefined position; Undefined team |
| `23` | `24` | Position_Unknown | Team_Unknown | 53–232 | 168 | 6 | Undefined position; Undefined team |
| `24` | `25` | Position_Unknown | Team_Unknown | 63–64 | 2 | 1 | Undefined position; Undefined team |
| `25` | `26` | Position_Unknown | Team_Unknown | 66–239 | 165 | 3 | Undefined position; Undefined team |
| `26` | `29` | Position_Unknown | Team_Unknown | 97–224 | 128 | 1 | Undefined position; Undefined team |
| `27` | `30` | Position_Unknown | Team_Unknown | 98–224 | 126 | 2 | Undefined position; Undefined team |
| `28` | `37` | Position_Unknown | Team_Unknown | 185–239 | 55 | 1 | Undefined position; Undefined team |
| `29` | `38` | Position_Unknown | Team_Unknown | 225–239 | 15 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_BallSnap` and target `20` (2 segments found)
- ⚠️ Ambiguous match for action `Action_SplitBlock` and target `4` (3 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `12` (2 segments found)
- ⚠️ `Action_ZoneBlock` for actor_track_id `17` (LG): Annotated start 85 != Inferred start 91
- ❌ Missing segment for action `Action_ZoneBlock` on target `20` (C)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `21` (2 segments found)
- ❌ Missing segment for action `Action_ZoneBlock` on target `6` (LT)

### Track Identity Issues

- ⚠️ Player track XML ID `13` (actor_track_id `13`): `SAF1` position mapped to `defense` team
- ⚠️ Player track XML ID `16` (actor_track_id `16`): `SAF2` position mapped to `defense` team
- ⚠️ 8 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 8 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 16 |
| Missing visible bounding boxes during action | 64 |
| Track-related warning | 2 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Segment 'Action_ZoneBlock' for track '6' has invalid range: start=85, end=62. Clamping end to start.
- ⚠️ Segment 'Action_ZoneBlock' for track '20' has invalid range: start=85, end=63. Clamping end to start.
- ⚠️ Action 'Action_None' range [27-139] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [27-116] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [121-144] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [27-74] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [76-110] for track '2' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [113-205] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [27-83] for track '3' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [86-212] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_SplitBlock' range [31-79] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_SplitBlock' range [83-84] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [27-65] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [83-84] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-62] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [64-233] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [27-206] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [27-239] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [27-66] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [69-74] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [95-197] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [27-72] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [83-86] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [89-92] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [94-195] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-74] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [85-86] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [91-98] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [99-104] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [27-116] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [125-223] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [27-79] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [27-166] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [74-77] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [83-84] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [99-150] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [154-159] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [162-179] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [181-182] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [186-190] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [193-203] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [205-209] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [69-203] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BallSnap' range [27-36] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [40-50] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [53-63] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-39] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [83-84] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [85-86] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [99-234] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [49-50] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [53-56] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [58-60] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [53-63] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [65-75] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [83-86] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [88-181] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [184-203] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [205-232] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [63-64] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [66-75] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [83-86] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [89-239] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [97-224] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [98-110] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [112-224] for track '27' has 1 frames without a visible bounding box.
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

</details>