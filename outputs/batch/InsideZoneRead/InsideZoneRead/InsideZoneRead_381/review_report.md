# Play-Annotation-Generator Annotation Review — InsideZoneRead_381

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `InsideZoneRead_381`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Run_InsideZoneRead`
- **Result:** `Result_OutOfBounds`
- **Result Frame:** 239
- **Player Tracks:** 30
- **Ball Tracks:** 0
- **Action Segments:** 116
- **Validation Warnings:** 112
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 22
- **Exact Matches:** 4
- **Group Expanded Events:** 10
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 1
- **Missing Segments:** 0
- **Ambiguous Matches:** 5
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 91
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | offense | `9` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `20` | `19` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | offense | `12` | `11` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | offense | `14` | `13` |
| ✅ EXACT | `Action_ZoneBlock` | LT | offense | `2` | `1` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | offense | `20` | `19` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | offense | `21` | `20` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `19` | `18` |
| ✅ EXACT | `Action_ReadDefender` | QB | offense | `19` | `18` |
| ⚠️ START CHANGED | `Action_Keep` | QB | offense | `19` | `18` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | QB | offense | `19` | `18` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `10` | `Group` | 0 | START | 0 | 16 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `12` | `Group` | 0 | START | 0 | 19 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `14` | `Group` | 0 | START | 0 | 19 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | `18` | `Group` | 0 | START | 0 | 16 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `19` | `Group` | 0 | START | 0 | 16 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `2` | `Group` | 0 | START | 0 | 19 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `20` | `Group` | 0 | START | 0 | 16 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `21` | `Group` | 0 | START | 0 | 19 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `7` | `Group` | 0 | START | 0 | 16 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | `9` | `Group` | 0 | START | 0 | 16 |
| ✅ EXACT | `Action_BallSnap` | C | `20` | `19` | 17 | START | 17 | 34 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | `12` | `11` | 20 | START | 20 | 45 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | `14` | `13` | 20 | START | 20 | 45 |
| ✅ EXACT | `Action_ZoneBlock` | LT | `2` | `1` | 20 | START | 20 | 109 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | `20` | `19` | 20 | START | 35 | 41 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | `21` | `20` | 20 | START | 20 | 26 |
| ✅ EXACT | `Action_SnapReceive` | QB | `19` | `18` | 34 | END | 17 | 34 |
| ✅ EXACT | `Action_ReadDefender` | QB | `19` | `18` | 39 | START | 39 | 46 |
| ⚠️ START CHANGED | `Action_Keep` | QB | `19` | `18` | 47 | START | 51 | 69 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | QB | `19` | `18` | 70 | START | 70 | 186 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 109 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `19`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–201
- **Visible Samples:** 192

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 16 | 17 | inferred_complete_timeline |
| `Action_SnapReceive` | 17 | 34 | 18 | inferred_complete_timeline |
| `Action_None` | 35 | 38 | 4 | inferred_complete_timeline |
| `Action_ReadDefender` | 39 | 46 | 8 | inferred_complete_timeline |
| `Action_Keep` | 51 | 69 | 19 | inferred_complete_timeline |
| `Action_BallCarry` | 70 | 186 | 117 | inferred_complete_timeline |
| `Action_BallCarry` | 188 | 191 | 4 | inferred_complete_timeline |
| `Action_BallCarry` | 194 | 196 | 3 | inferred_complete_timeline |
| `Action_BallCarry` | 200 | 201 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 16 | 17 | inferred_complete_timeline |
| `Action_None` | 17 | 210 | 194 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–145
- **Visible Samples:** 144

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 16 | 17 | inferred_complete_timeline |
| `Action_None` | 17 | 107 | 91 | inferred_complete_timeline |
| `Action_None` | 110 | 145 | 36 | inferred_complete_timeline |

</details>

<details>
<summary>TE1 — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 199

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 16 | 17 | inferred_complete_timeline |
| `Action_None` | 17 | 45 | 29 | inferred_complete_timeline |
| `Action_None` | 49 | 51 | 3 | inferred_complete_timeline |
| `Action_None` | 58 | 59 | 2 | inferred_complete_timeline |
| `Action_None` | 63 | 210 | 148 | inferred_complete_timeline |

</details>

<details>
<summary>TE2 — actor_track_id `18`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–131
- **Visible Samples:** 71

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 16 | 17 | inferred_complete_timeline |
| `Action_None` | 17 | 48 | 32 | inferred_complete_timeline |
| `Action_None` | 50 | 60 | 11 | inferred_complete_timeline |
| `Action_None` | 62 | 70 | 9 | inferred_complete_timeline |
| `Action_None` | 130 | 131 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 19 | 20 | inferred_complete_timeline |
| `Action_ZoneBlock` | 20 | 109 | 90 | inferred_complete_timeline |
| `Action_None` | 110 | 210 | 101 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `21`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–209
- **Visible Samples:** 110

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 19 | 20 | inferred_complete_timeline |
| `Action_ZoneBlock` | 20 | 26 | 7 | inferred_complete_timeline |
| `Action_ZoneBlock` | 76 | 82 | 7 | inferred_complete_timeline |
| `Action_None` | 124 | 153 | 30 | inferred_complete_timeline |
| `Action_None` | 163 | 203 | 41 | inferred_complete_timeline |
| `Action_None` | 205 | 209 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `20`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–133
- **Visible Samples:** 107

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 16 | 17 | inferred_complete_timeline |
| `Action_BallSnap` | 17 | 34 | 18 | inferred_complete_timeline |
| `Action_ZoneBlock` | 35 | 41 | 7 | inferred_complete_timeline |
| `Action_ZoneBlock` | 62 | 85 | 24 | inferred_complete_timeline |
| `Action_ZoneBlock` | 90 | 106 | 17 | inferred_complete_timeline |
| `Action_None` | 110 | 133 | 24 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–152
- **Visible Samples:** 137

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 19 | 20 | inferred_complete_timeline |
| `Action_ZoneBlock` | 20 | 45 | 26 | inferred_complete_timeline |
| `Action_ZoneBlock` | 58 | 59 | 2 | inferred_complete_timeline |
| `Action_ZoneBlock` | 64 | 109 | 46 | inferred_complete_timeline |
| `Action_None` | 110 | 152 | 43 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–185
- **Visible Samples:** 177

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 19 | 20 | inferred_complete_timeline |
| `Action_ZoneBlock` | 20 | 45 | 26 | inferred_complete_timeline |
| `Action_ZoneBlock` | 54 | 109 | 56 | inferred_complete_timeline |
| `Action_None` | 110 | 181 | 72 | inferred_complete_timeline |
| `Action_None` | 183 | 185 | 3 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 183

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 16 | 17 | inferred_complete_timeline |
| `Action_None` | 17 | 45 | 29 | inferred_complete_timeline |
| `Action_None` | 51 | 59 | 9 | inferred_complete_timeline |
| `Action_None` | 61 | 74 | 14 | inferred_complete_timeline |
| `Action_None` | 77 | 80 | 4 | inferred_complete_timeline |
| `Action_None` | 98 | 106 | 9 | inferred_complete_timeline |
| `Action_None` | 110 | 210 | 101 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 184

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 16 | 17 | inferred_complete_timeline |
| `Action_None` | 17 | 45 | 29 | inferred_complete_timeline |
| `Action_None` | 58 | 59 | 2 | inferred_complete_timeline |
| `Action_None` | 71 | 190 | 120 | inferred_complete_timeline |
| `Action_None` | 192 | 204 | 13 | inferred_complete_timeline |
| `Action_None` | 208 | 210 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–106
- **Visible Samples:** 75

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 16 | 17 | inferred_complete_timeline |
| `Action_None` | 17 | 44 | 28 | inferred_complete_timeline |
| `Action_None` | 58 | 59 | 2 | inferred_complete_timeline |
| `Action_None` | 61 | 71 | 11 | inferred_complete_timeline |
| `Action_None` | 88 | 100 | 13 | inferred_complete_timeline |
| `Action_None` | 103 | 106 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `17`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 0–40
- **Visible Samples:** 41

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 16 | 17 | inferred_complete_timeline |
| `Action_None` | 17 | 40 | 24 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 200

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 16 | 17 | inferred_complete_timeline |
| `Action_None` | 17 | 61 | 45 | inferred_complete_timeline |
| `Action_None` | 73 | 210 | 138 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–154
- **Visible Samples:** 116

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 16 | 17 | inferred_complete_timeline |
| `Action_None` | 17 | 45 | 29 | inferred_complete_timeline |
| `Action_None` | 77 | 80 | 4 | inferred_complete_timeline |
| `Action_None` | 83 | 99 | 17 | inferred_complete_timeline |
| `Action_None` | 101 | 102 | 2 | inferred_complete_timeline |
| `Action_None` | 104 | 105 | 2 | inferred_complete_timeline |
| `Action_None` | 110 | 154 | 45 | inferred_complete_timeline |

</details>

<details>
<summary>LB3 — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–153
- **Visible Samples:** 136

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 16 | 17 | inferred_complete_timeline |
| `Action_None` | 17 | 43 | 27 | inferred_complete_timeline |
| `Action_None` | 51 | 54 | 4 | inferred_complete_timeline |
| `Action_None` | 58 | 59 | 2 | inferred_complete_timeline |
| `Action_None` | 64 | 71 | 8 | inferred_complete_timeline |
| `Action_None` | 75 | 107 | 33 | inferred_complete_timeline |
| `Action_None` | 109 | 153 | 45 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 16 | 17 | inferred_complete_timeline |
| `Action_None` | 17 | 210 | 194 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 16 | 17 | inferred_complete_timeline |
| `Action_None` | 17 | 210 | 194 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 205

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 16 | 17 | inferred_complete_timeline |
| `Action_None` | 17 | 99 | 83 | inferred_complete_timeline |
| `Action_None` | 103 | 106 | 4 | inferred_complete_timeline |
| `Action_None` | 110 | 210 | 101 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 208

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 16 | 17 | inferred_complete_timeline |
| `Action_None` | 17 | 150 | 134 | inferred_complete_timeline |
| `Action_None` | 154 | 210 | 57 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `21` | `23` | Position_Unknown | Team_Unknown | 23–44 | 22 | 1 | Undefined position; Undefined team |
| `22` | `24` | Position_Unknown | Team_Unknown | 65–117 | 48 | 3 | Undefined position; Undefined team |
| `23` | `27` | Position_Unknown | Team_Unknown | 77–210 | 125 | 4 | Undefined position; Undefined team |
| `24` | `31` | Position_Unknown | Team_Unknown | 108–154 | 47 | 1 | Undefined position; Undefined team |
| `25` | `32` | Position_Unknown | Team_Unknown | 114–202 | 86 | 3 | Undefined position; Undefined team |
| `26` | `33` | Position_Unknown | Team_Unknown | 133–137 | 4 | 2 | Undefined position; Undefined team |
| `27` | `38` | Position_Unknown | Team_Unknown | 152–154 | 3 | 1 | Undefined position; Undefined team |
| `28` | `40` | Position_Unknown | Team_Unknown | 154–210 | 57 | 1 | Undefined position; Undefined team |
| `29` | `41` | Position_Unknown | Team_Unknown | 160–180 | 8 | 2 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `12` (3 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `14` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `20` (5 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `21` (2 segments found)
- ⚠️ `Action_Keep` for actor_track_id `19` (QB): Annotated start 47 != Inferred start 51
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `19` (4 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `0` (actor_track_id `1`): `SAF1` position mapped to `defense` team
- ⚠️ Player track XML ID `10` (actor_track_id `11`): `SAF2` position mapped to `defense` team
- ⚠️ 9 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 9 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 18 |
| Missing visible bounding boxes during action | 91 |
| Track-related warning | 2 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 761: Duplicate assignment for track ID '2' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Resolved action overlap for track '19' (C): higher_priority='Action_BallSnap' [17–34], lower_priority='Action_ZoneBlock' annotated_start=20, effective_Action_ZoneBlock_start=35.
- ⚠️ Action 'Action_None' range [17-99] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [103-106] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [110-210] for track '0' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [110-210] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [17-61] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [73-210] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [17-45] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [77-80] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [83-99] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [101-102] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [104-105] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [110-154] for track '3' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [17-210] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [17-43] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [51-54] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [58-59] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [64-71] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [75-107] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [109-153] for track '5' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [17-107] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [110-145] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [17-210] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [17-45] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [49-51] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [58-59] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [63-210] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [17-210] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [17-150] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [154-210] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [20-45] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [58-59] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [64-109] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [110-152] for track '11' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [17-44] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [58-59] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [61-71] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [88-100] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [103-106] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [20-45] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [54-109] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [110-181] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [183-185] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [17-45] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [51-59] for track '14' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [61-74] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [77-80] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [98-106] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [110-210] for track '14' has 6 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [17-45] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [58-59] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [71-190] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [192-204] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [208-210] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [17-40] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [17-48] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [50-60] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [62-70] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [130-131] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ReadDefender' range [39-46] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_Keep' range [51-69] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [70-186] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [188-191] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [194-196] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [200-201] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [35-41] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [62-85] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [90-106] for track '19' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [110-133] for track '19' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [20-26] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [76-82] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [124-153] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [163-203] for track '20' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [205-209] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [23-44] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [65-74] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [76-86] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [91-117] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [77-84] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [91-92] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [95-191] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [193-210] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [108-154] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [114-185] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [188-192] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [194-202] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [133-134] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [136-137] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [152-154] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [154-210] for track '28' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [160-165] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [179-180] for track '29' has 1 frames without a visible bounding box.
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

</details>