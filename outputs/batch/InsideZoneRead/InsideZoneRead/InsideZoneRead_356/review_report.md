# Play-Annotation-Generator Annotation Review — InsideZoneRead_356

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `InsideZoneRead_356`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Run_InsideZoneRead`
- **Result:** `Result_OutOfBounds`
- **Result Frame:** 239
- **Player Tracks:** 26
- **Ball Tracks:** 0
- **Action Segments:** 76
- **Validation Warnings:** 82
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 20
- **Exact Matches:** 4
- **Group Expanded Events:** 8
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 2
- **Missing Segments:** 2
- **Ambiguous Matches:** 2
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 56
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `8` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `9` | `Group` |
| ⚠️ START CHANGED | `Action_BallSnap` | Position_Unknown | Team_Unknown | `19` | `17` |
| ❌ MISSING SEGMENT | `Action_ZoneBlock` | LG | offense | `11` | `10` |
| ✅ EXACT | `Action_ZoneBlock` | LT | offense | `13` | `12` |
| ✅ EXACT | `Action_ZoneBlock` | RT | offense | `2` | `1` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | offense | `6` | `5` |
| ✅ EXACT | `Action_ZoneBlock` | C | offense | `9` | `8` |
| ✅ EXACT | `Action_SnapReceive` | LG | offense | `11` | `10` |
| ❌ MISSING SEGMENT | `Action_ReadDefender` | LG | offense | `11` | `10` |
| ⚠️ START CHANGED | `Action_Keep` | LG | offense | `11` | `10` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | LG | offense | `11` | `10` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `10` | `Group` | 0 | START | 0 | 21 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `11` | `Group` | 0 | START | 0 | 21 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `12` | `Group` | 0 | START | 0 | 21 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `13` | `Group` | 0 | START | 0 | 7 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `2` | `Group` | 0 | START | 0 | 24 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `6` | `Group` | 0 | START | 0 | 24 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `8` | `Group` | 0 | START | 0 | 21 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `9` | `Group` | 0 | START | 0 | 24 |
| ⚠️ START CHANGED | `Action_BallSnap` | Position_Unknown | `19` | `17` | 22 | START | 28 | 32 |
| ❌ MISSING SEGMENT | `Action_ZoneBlock` | LG | `11` | `10` | 25 | START | N/A | N/A |
| ✅ EXACT | `Action_ZoneBlock` | LT | `13` | `12` | 25 | START | 25 | 36 |
| ✅ EXACT | `Action_ZoneBlock` | RT | `2` | `1` | 25 | START | 25 | 104 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | `6` | `5` | 25 | START | 25 | 72 |
| ✅ EXACT | `Action_ZoneBlock` | C | `9` | `8` | 25 | START | 25 | 99 |
| ✅ EXACT | `Action_SnapReceive` | LG | `11` | `10` | 32 | END | 22 | 32 |
| ❌ MISSING SEGMENT | `Action_ReadDefender` | LG | `11` | `10` | 41 | START | N/A | N/A |
| ⚠️ START CHANGED | `Action_Keep` | LG | `11` | `10` | 47 | START | 50 | 70 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | LG | `11` | `10` | 71 | START | 71 | 83 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 104 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–172
- **Visible Samples:** 173

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 21 | 22 | inferred_complete_timeline |
| `Action_None` | 22 | 172 | 151 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–132
- **Visible Samples:** 130

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 21 | 22 | inferred_complete_timeline |
| `Action_None` | 22 | 95 | 74 | inferred_complete_timeline |
| `Action_None` | 99 | 132 | 34 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–124
- **Visible Samples:** 122

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 21 | 22 | inferred_complete_timeline |
| `Action_None` | 22 | 119 | 98 | inferred_complete_timeline |
| `Action_None` | 123 | 124 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–36
- **Visible Samples:** 36

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 7 | 8 | inferred_complete_timeline |
| `Action_PreSnap` | 9 | 24 | 16 | inferred_complete_timeline |
| `Action_ZoneBlock` | 25 | 36 | 12 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–136
- **Visible Samples:** 122

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 21 | 22 | inferred_complete_timeline |
| `Action_SnapReceive` | 22 | 32 | 11 | inferred_complete_timeline |
| `Action_None` | 33 | 38 | 6 | inferred_complete_timeline |
| `Action_Keep` | 50 | 70 | 21 | inferred_complete_timeline |
| `Action_BallCarry` | 71 | 83 | 13 | inferred_complete_timeline |
| `Action_BallCarry` | 86 | 88 | 3 | inferred_complete_timeline |
| `Action_BallCarry` | 90 | 93 | 4 | inferred_complete_timeline |
| `Action_BallCarry` | 95 | 136 | 42 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–117
- **Visible Samples:** 102

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 24 | 25 | inferred_complete_timeline |
| `Action_ZoneBlock` | 25 | 99 | 75 | inferred_complete_timeline |
| `Action_None` | 116 | 117 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–119
- **Visible Samples:** 119

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 24 | 25 | inferred_complete_timeline |
| `Action_ZoneBlock` | 25 | 72 | 48 | inferred_complete_timeline |
| `Action_ZoneBlock` | 74 | 104 | 31 | inferred_complete_timeline |
| `Action_None` | 105 | 119 | 15 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–125
- **Visible Samples:** 126

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 24 | 25 | inferred_complete_timeline |
| `Action_ZoneBlock` | 25 | 104 | 80 | inferred_complete_timeline |
| `Action_None` | 105 | 125 | 21 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–48
- **Visible Samples:** 49

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 21 | 22 | inferred_complete_timeline |
| `Action_None` | 22 | 48 | 27 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 239

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 21 | 22 | inferred_complete_timeline |
| `Action_None` | 22 | 83 | 62 | inferred_complete_timeline |
| `Action_None` | 85 | 239 | 155 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 21 | 22 | inferred_complete_timeline |
| `Action_None` | 22 | 239 | 218 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–117
- **Visible Samples:** 113

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 21 | 22 | inferred_complete_timeline |
| `Action_None` | 22 | 94 | 73 | inferred_complete_timeline |
| `Action_None` | 96 | 97 | 2 | inferred_complete_timeline |
| `Action_None` | 102 | 117 | 16 | inferred_complete_timeline |

</details>

<details>
<summary>LB — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 227

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 21 | 22 | inferred_complete_timeline |
| `Action_None` | 22 | 117 | 96 | inferred_complete_timeline |
| `Action_None` | 125 | 136 | 12 | inferred_complete_timeline |
| `Action_None` | 140 | 161 | 22 | inferred_complete_timeline |
| `Action_None` | 165 | 239 | 75 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `13` | `14` | Position_Unknown | Team_Unknown | 0–239 | 239 | 3 | Undefined position; Undefined team |
| `14` | `16` | Position_Unknown | Team_Unknown | 7–201 | 188 | 6 | Undefined position; Undefined team |
| `15` | `17` | Position_Unknown | Team_Unknown | 17–124 | 101 | 4 | Undefined position; Undefined team |
| `16` | `18` | Position_Unknown | Team_Unknown | 27–124 | 31 | 2 | Undefined position; Undefined team |
| `17` | `19` | Position_Unknown | Team_Unknown | 28–139 | 112 | 2 | Undefined position; Undefined team |
| `18` | `22` | Position_Unknown | Team_Unknown | 113–233 | 93 | 2 | Undefined position; Undefined team |
| `19` | `26` | Position_Unknown | Team_Unknown | 141–239 | 98 | 2 | Undefined position; Undefined team |
| `20` | `27` | Position_Unknown | Team_Unknown | 150–239 | 83 | 2 | Undefined position; Undefined team |
| `21` | `28` | Position_Unknown | Team_Unknown | 153–239 | 87 | 1 | Undefined position; Undefined team |
| `22` | `30` | Position_Unknown | Team_Unknown | 184–198 | 13 | 2 | Undefined position; Undefined team |
| `23` | `33` | Position_Unknown | Team_Unknown | 204–213 | 9 | 2 | Undefined position; Undefined team |
| `24` | `34` | Position_Unknown | Team_Unknown | 213–230 | 18 | 1 | Undefined position; Undefined team |
| `25` | `35` | Position_Unknown | Team_Unknown | 225–239 | 7 | 2 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ `Action_BallSnap` for actor_track_id `19` (Position_Unknown): Annotated start 22 != Inferred start 28
- ❌ Missing segment for action `Action_ZoneBlock` on target `11` (LG)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `6` (2 segments found)
- ❌ Missing segment for action `Action_ReadDefender` on target `11` (LG)
- ⚠️ `Action_Keep` for actor_track_id `11` (LG): Annotated start 47 != Inferred start 50
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `11` (4 segments found)

### Track Identity Issues

- ⚠️ 13 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 13 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 26 |
| Missing visible bounding boxes during action | 53 |
| Track-related warning | 1 |
| Other | 2 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Segment 'Action_ZoneBlock' for track '10' has invalid range: start=25, end=21. Clamping end to start.
- ⚠️ Action 'Action_None' range [22-117] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [125-136] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [140-161] for track '0' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [105-125] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [22-48] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [22-83] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [85-239] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [25-72] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [74-104] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [105-119] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [22-94] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [96-97] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [102-117] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [22-119] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [123-124] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [25-99] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [116-117] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [22-95] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [99-132] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [33-38] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_Keep' range [50-70] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [71-83] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [86-88] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [90-93] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [95-136] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [22-172] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-7] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [9-24] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [25-36] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [22-46] for track '13' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [22-70] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [74-144] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [146-175] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [177-197] for track '14' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [200-201] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [22-67] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [69-72] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [79-124] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [27-32] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [100-124] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallSnap' range [28-32] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [33-139] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [113-153] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [182-233] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [141-177] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [179-239] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [150-203] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [184-192] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [195-198] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [204-208] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [210-213] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [213-230] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [225-226] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Player track '13' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '13' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '14' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '14' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '15' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '15' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '16' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '16' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '17' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '17' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '18' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '18' has undefined team_side. Will map to Team_Unknown.
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
- ⚠️ Metadata: no Dataset Summary row found for output_file 'InsideZoneRead_356'; source metadata written as null.

</details>