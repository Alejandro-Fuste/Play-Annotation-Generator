# Play-Annotation-Generator Annotation Review — InsideZoneRead_341

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `InsideZoneRead_341`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Run_InsideZoneRead`
- **Result:** `Result_Touchdown`
- **Result Frame:** 239
- **Player Tracks:** 30
- **Ball Tracks:** 0
- **Action Segments:** 117
- **Validation Warnings:** 117
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 22
- **Exact Matches:** 1
- **Group Expanded Events:** 10
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 1
- **Missing Segments:** 3
- **Ambiguous Matches:** 5
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 92
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR4 | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `8` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `9` | `Group` |
| ✅ EXACT | `Action_BallSnap` | WR1 | offense | `9` | `8` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | offense | `13` | `12` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | offense | `17` | `16` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | offense | `19` | `18` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | offense | `20` | `19` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | offense | `21` | `20` |
| ⚠️ END CHANGED | `Action_SnapReceive` | RB | offense | `8` | `7` |
| ❌ MISSING SEGMENT | `Action_ReadDefender` | RB | offense | `8` | `7` |
| ❌ MISSING SEGMENT | `Action_Keep` | RB | offense | `8` | `7` |
| ❌ MISSING SEGMENT | `Action_BallCarry` | RB | offense | `8` | `7` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `13` | `Group` | 0 | START | 0 | 22 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `17` | `Group` | 0 | START | 0 | 22 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `19` | `Group` | 0 | START | 0 | 22 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `2` | `Group` | 0 | START | 0 | 19 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `20` | `Group` | 0 | START | 0 | 22 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `21` | `Group` | 0 | START | 0 | 13 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR4 | `5` | `Group` | 0 | START | 0 | 19 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `7` | `Group` | 0 | START | 0 | 19 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `8` | `Group` | 0 | START | 0 | 19 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `9` | `Group` | 0 | START | 0 | 19 |
| ✅ EXACT | `Action_BallSnap` | WR1 | `9` | `8` | 20 | START | 20 | 40 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | `13` | `12` | 23 | START | 23 | 27 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | `17` | `16` | 23 | START | 23 | 65 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | `19` | `18` | 23 | START | 23 | 35 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | `20` | `19` | 23 | START | 23 | 30 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | `21` | `20` | 23 | START | 23 | 29 |
| ⚠️ END CHANGED | `Action_SnapReceive` | RB | `8` | `7` | 40 | END | 20 | 28 |
| ❌ MISSING SEGMENT | `Action_ReadDefender` | RB | `8` | `7` | 45 | START | N/A | N/A |
| ❌ MISSING SEGMENT | `Action_Keep` | RB | `8` | `7` | 51 | START | N/A | N/A |
| ❌ MISSING SEGMENT | `Action_BallCarry` | RB | `8` | `7` | 61 | START | N/A | N/A |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 76 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–179
- **Visible Samples:** 141

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 19 | 20 | inferred_complete_timeline |
| `Action_None` | 20 | 82 | 63 | inferred_complete_timeline |
| `Action_None` | 88 | 126 | 39 | inferred_complete_timeline |
| `Action_None` | 133 | 143 | 11 | inferred_complete_timeline |
| `Action_None` | 158 | 161 | 4 | inferred_complete_timeline |
| `Action_None` | 171 | 172 | 2 | inferred_complete_timeline |
| `Action_None` | 178 | 179 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–28
- **Visible Samples:** 29

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 19 | 20 | inferred_complete_timeline |
| `Action_SnapReceive` | 20 | 28 | 9 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–180
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 19 | 20 | inferred_complete_timeline |
| `Action_BallSnap` | 20 | 40 | 21 | inferred_complete_timeline |
| `Action_None` | 41 | 180 | 140 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–180
- **Visible Samples:** 178

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 19 | 20 | inferred_complete_timeline |
| `Action_None` | 20 | 164 | 145 | inferred_complete_timeline |
| `Action_None` | 166 | 175 | 10 | inferred_complete_timeline |
| `Action_None` | 178 | 180 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>WR4 — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–180
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 19 | 20 | inferred_complete_timeline |
| `Action_None` | 20 | 180 | 161 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `20`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–180
- **Visible Samples:** 178

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 22 | 23 | inferred_complete_timeline |
| `Action_ZoneBlock` | 23 | 30 | 8 | inferred_complete_timeline |
| `Action_ZoneBlock` | 32 | 55 | 24 | inferred_complete_timeline |
| `Action_ZoneBlock` | 58 | 76 | 19 | inferred_complete_timeline |
| `Action_None` | 77 | 180 | 104 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `17`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–180
- **Visible Samples:** 170

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 22 | 23 | inferred_complete_timeline |
| `Action_ZoneBlock` | 23 | 65 | 43 | inferred_complete_timeline |
| `Action_ZoneBlock` | 72 | 76 | 5 | inferred_complete_timeline |
| `Action_None` | 77 | 83 | 7 | inferred_complete_timeline |
| `Action_None` | 89 | 180 | 92 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `21`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–62
- **Visible Samples:** 58

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 13 | 14 | inferred_complete_timeline |
| `Action_PreSnap` | 16 | 22 | 7 | inferred_complete_timeline |
| `Action_ZoneBlock` | 23 | 29 | 7 | inferred_complete_timeline |
| `Action_ZoneBlock` | 32 | 35 | 4 | inferred_complete_timeline |
| `Action_ZoneBlock` | 37 | 62 | 26 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–180
- **Visible Samples:** 169

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 22 | 23 | inferred_complete_timeline |
| `Action_ZoneBlock` | 23 | 27 | 5 | inferred_complete_timeline |
| `Action_ZoneBlock` | 31 | 42 | 12 | inferred_complete_timeline |
| `Action_ZoneBlock` | 45 | 50 | 6 | inferred_complete_timeline |
| `Action_ZoneBlock` | 52 | 76 | 25 | inferred_complete_timeline |
| `Action_None` | 77 | 83 | 7 | inferred_complete_timeline |
| `Action_None` | 90 | 180 | 91 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `19`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–180
- **Visible Samples:** 178

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 22 | 23 | inferred_complete_timeline |
| `Action_ZoneBlock` | 23 | 35 | 13 | inferred_complete_timeline |
| `Action_ZoneBlock` | 37 | 46 | 10 | inferred_complete_timeline |
| `Action_ZoneBlock` | 49 | 76 | 28 | inferred_complete_timeline |
| `Action_None` | 77 | 180 | 104 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–36
- **Visible Samples:** 37

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 19 | 20 | inferred_complete_timeline |
| `Action_None` | 20 | 36 | 17 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–41
- **Visible Samples:** 38

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 19 | 20 | inferred_complete_timeline |
| `Action_None` | 20 | 35 | 16 | inferred_complete_timeline |
| `Action_None` | 40 | 41 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `18`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `18`
- **team_side:** `defense`
- **Visible Frames:** 0–83
- **Visible Samples:** 73

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 14 | 15 | inferred_complete_timeline |
| `Action_PreSnap` | 18 | 19 | 2 | inferred_complete_timeline |
| `Action_None` | 20 | 26 | 7 | inferred_complete_timeline |
| `Action_None` | 31 | 62 | 32 | inferred_complete_timeline |
| `Action_None` | 64 | 66 | 3 | inferred_complete_timeline |
| `Action_None` | 69 | 70 | 2 | inferred_complete_timeline |
| `Action_None` | 72 | 83 | 12 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–40
- **Visible Samples:** 40

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 19 | 20 | inferred_complete_timeline |
| `Action_None` | 20 | 36 | 17 | inferred_complete_timeline |
| `Action_None` | 38 | 40 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–180
- **Visible Samples:** 156

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 19 | 20 | inferred_complete_timeline |
| `Action_None` | 20 | 62 | 43 | inferred_complete_timeline |
| `Action_None` | 82 | 84 | 3 | inferred_complete_timeline |
| `Action_None` | 91 | 180 | 90 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–180
- **Visible Samples:** 169

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 19 | 20 | inferred_complete_timeline |
| `Action_None` | 20 | 46 | 27 | inferred_complete_timeline |
| `Action_None` | 48 | 66 | 19 | inferred_complete_timeline |
| `Action_None` | 68 | 69 | 2 | inferred_complete_timeline |
| `Action_None` | 71 | 137 | 67 | inferred_complete_timeline |
| `Action_None` | 143 | 162 | 20 | inferred_complete_timeline |
| `Action_None` | 166 | 167 | 2 | inferred_complete_timeline |
| `Action_None` | 169 | 180 | 12 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–179
- **Visible Samples:** 170

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 19 | 20 | inferred_complete_timeline |
| `Action_None` | 20 | 148 | 129 | inferred_complete_timeline |
| `Action_None` | 154 | 165 | 12 | inferred_complete_timeline |
| `Action_None` | 170 | 174 | 5 | inferred_complete_timeline |
| `Action_None` | 176 | 179 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–180
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 19 | 20 | inferred_complete_timeline |
| `Action_None` | 20 | 180 | 161 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `22`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `22`
- **team_side:** `defense`
- **Visible Frames:** 0–164
- **Visible Samples:** 146

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 19 | 20 | inferred_complete_timeline |
| `Action_None` | 20 | 25 | 6 | inferred_complete_timeline |
| `Action_None` | 28 | 29 | 2 | inferred_complete_timeline |
| `Action_None` | 34 | 37 | 4 | inferred_complete_timeline |
| `Action_None` | 41 | 43 | 3 | inferred_complete_timeline |
| `Action_None` | 52 | 85 | 34 | inferred_complete_timeline |
| `Action_None` | 87 | 148 | 62 | inferred_complete_timeline |
| `Action_None` | 150 | 164 | 15 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–180
- **Visible Samples:** 180

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 19 | 20 | inferred_complete_timeline |
| `Action_None` | 20 | 86 | 67 | inferred_complete_timeline |
| `Action_None` | 88 | 180 | 93 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–180
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 19 | 20 | inferred_complete_timeline |
| `Action_None` | 20 | 180 | 161 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `0` | `1` | Position_Unknown | Team_Unknown | 0–180 | 176 | 3 | Undefined position; Undefined team |
| `22` | `23` | Position_Unknown | Team_Unknown | 35–180 | 146 | 1 | Undefined position; Undefined team |
| `23` | `24` | Position_Unknown | Team_Unknown | 46–180 | 132 | 3 | Undefined position; Undefined team |
| `24` | `25` | Position_Unknown | Team_Unknown | 61–180 | 95 | 7 | Undefined position; Undefined team |
| `25` | `26` | Position_Unknown | Team_Unknown | 78–180 | 96 | 4 | Undefined position; Undefined team |
| `26` | `32` | Position_Unknown | Team_Unknown | 95–180 | 74 | 2 | Undefined position; Undefined team |
| `27` | `33` | Position_Unknown | Team_Unknown | 96–133 | 38 | 1 | Undefined position; Undefined team |
| `28` | `34` | Position_Unknown | Team_Unknown | 134–140 | 6 | 2 | Undefined position; Undefined team |
| `29` | `38` | Position_Unknown | Team_Unknown | 155–163 | 4 | 2 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `13` (4 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `17` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `19` (6 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `20` (6 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `21` (3 segments found)
- ❌ Missing segment for action `Action_ReadDefender` on target `8` (RB)
- ❌ Missing segment for action `Action_Keep` on target `8` (RB)
- ❌ Missing segment for action `Action_BallCarry` on target `8` (RB)

### Track Identity Issues

- ⚠️ Player track XML ID `5` (actor_track_id `6`): `SAF1` position mapped to `defense` team
- ⚠️ Player track XML ID `10` (actor_track_id `11`): `SAF2` position mapped to `defense` team
- ⚠️ 9 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 9 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 18 |
| Missing visible bounding boxes during action | 93 |
| Track-related warning | 4 |
| Other | 2 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 682: Duplicate assignment for track ID '11' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Segment 'Action_ReadDefender' for track '7' has invalid range: start=45, end=28. Clamping end to start.
- ⚠️ Segment 'Action_Keep' for track '7' has invalid range: start=51, end=28. Clamping end to start.
- ⚠️ Segment 'Action_BallCarry' for track '7' has invalid range: start=61, end=28. Clamping end to start.
- ⚠️ Action 'Action_None' range [20-125] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [131-180] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [20-164] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [166-175] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [178-180] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [20-148] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [154-165] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [170-174] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [176-179] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [20-46] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [48-66] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [68-69] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [71-137] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [143-162] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [166-167] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [169-180] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [20-180] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [20-86] for track '5' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [88-180] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [20-82] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [88-126] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [133-143] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [158-161] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [171-172] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [178-179] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_SnapReceive' range [20-28] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallSnap' range [20-40] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [41-180] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [20-180] for track '9' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [20-180] for track '10' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [20-36] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [23-27] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [31-42] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [45-50] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [77-83] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [90-180] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [20-36] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [38-40] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [20-62] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [82-84] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [91-180] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [20-35] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [40-41] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [23-65] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [77-83] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [89-180] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-14] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [20-26] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [31-62] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [64-66] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [69-70] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [72-83] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-22] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [23-35] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [37-46] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [77-180] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-22] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [23-30] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [32-55] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [77-180] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-13] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [23-29] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [32-35] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [37-62] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [20-25] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [28-29] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [34-37] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [41-43] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [52-85] for track '21' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [87-148] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [150-164] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [35-180] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [46-65] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [68-164] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [166-180] for track '23' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [61-65] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [72-74] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [76-82] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [88-97] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [107-161] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [163-165] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [169-180] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [78-86] for track '25' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [89-95] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [100-102] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [104-180] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [95-106] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [119-180] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [96-133] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [134-137] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [139-140] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [155-156] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [162-163] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Player track '0' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '0' has undefined team_side. Will map to Team_Unknown.
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
- ⚠️ Metadata: no Dataset Summary row found for output_file 'InsideZoneRead_341'; source metadata written as null.

</details>