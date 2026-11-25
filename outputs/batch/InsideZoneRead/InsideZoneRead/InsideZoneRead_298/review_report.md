# Play-Annotation-Generator Annotation Review — InsideZoneRead_298

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `InsideZoneRead_298`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Run_InsideZoneRead`
- **Result:** `Result_Tackle`
- **Result Frame:** 239
- **Player Tracks:** 34
- **Ball Tracks:** 0
- **Action Segments:** 87
- **Validation Warnings:** 112
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 20
- **Exact Matches:** 0
- **Group Expanded Events:** 8
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 2
- **Missing Segments:** 3
- **Ambiguous Matches:** 5
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 67
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | FB | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `8` | `Group` |
| ⚠️ START CHANGED | `Action_BallSnap` | Position_Unknown | Team_Unknown | `23` | `20` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | offense | `11` | `10` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | offense | `14` | `13` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | offense | `15` | `14` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | offense | `16` | `15` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | offense | `4` | `3` |
| ❌ MISSING SEGMENT | `Action_SnapReceive` | Position_Unknown | Team_Unknown | `22` | `19` |
| ❌ MISSING SEGMENT | `Action_ReadDefender` | Position_Unknown | Team_Unknown | `22` | `19` |
| ❌ MISSING SEGMENT | `Action_Keep` | Position_Unknown | Team_Unknown | `22` | `19` |
| ⚠️ START CHANGED | `Action_BallCarry` | Position_Unknown | Team_Unknown | `22` | `19` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | FB | `10` | `Group` | 0 | START | 0 | 16 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `11` | `Group` | 0 | START | 0 | 19 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `13` | `Group` | 0 | START | 0 | 16 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `14` | `Group` | 0 | START | 0 | 19 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `15` | `Group` | 0 | START | 0 | 19 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `16` | `Group` | 0 | START | 0 | 19 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `4` | `Group` | 0 | START | 0 | 19 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `8` | `Group` | 0 | START | 0 | 16 |
| ⚠️ START CHANGED | `Action_BallSnap` | Position_Unknown | `23` | `20` | 17 | START | 99 | 99 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | `11` | `10` | 20 | START | 20 | 51 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | `14` | `13` | 20 | START | 20 | 97 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | `15` | `14` | 20 | START | 20 | 82 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | `16` | `15` | 20 | START | 20 | 24 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | `4` | `3` | 20 | START | 20 | 40 |
| ❌ MISSING SEGMENT | `Action_SnapReceive` | Position_Unknown | `22` | `19` | 29 | END | N/A | N/A |
| ❌ MISSING SEGMENT | `Action_ReadDefender` | Position_Unknown | `22` | `19` | 34 | START | N/A | N/A |
| ❌ MISSING SEGMENT | `Action_Keep` | Position_Unknown | `22` | `19` | 40 | START | N/A | N/A |
| ⚠️ START CHANGED | `Action_BallCarry` | Position_Unknown | `22` | `19` | 62 | START | 89 | 210 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 97 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–209
- **Visible Samples:** 204

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 16 | 17 | inferred_complete_timeline |
| `Action_None` | 17 | 198 | 182 | inferred_complete_timeline |
| `Action_None` | 202 | 203 | 2 | inferred_complete_timeline |
| `Action_None` | 207 | 209 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>FB — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–87
- **Visible Samples:** 88

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 16 | 17 | inferred_complete_timeline |
| `Action_None` | 17 | 87 | 71 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 190

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 16 | 17 | inferred_complete_timeline |
| `Action_None` | 17 | 32 | 16 | inferred_complete_timeline |
| `Action_None` | 54 | 210 | 157 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–98
- **Visible Samples:** 99

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 19 | 20 | inferred_complete_timeline |
| `Action_ZoneBlock` | 20 | 97 | 78 | inferred_complete_timeline |
| `Action_None` | 98 | 98 | 1 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 204

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 19 | 20 | inferred_complete_timeline |
| `Action_ZoneBlock` | 20 | 51 | 32 | inferred_complete_timeline |
| `Action_ZoneBlock` | 59 | 97 | 39 | inferred_complete_timeline |
| `Action_None` | 98 | 210 | 113 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–41
- **Visible Samples:** 32

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 19 | 20 | inferred_complete_timeline |
| `Action_ZoneBlock` | 20 | 24 | 5 | inferred_complete_timeline |
| `Action_ZoneBlock` | 29 | 32 | 4 | inferred_complete_timeline |
| `Action_ZoneBlock` | 39 | 41 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–120
- **Visible Samples:** 112

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 19 | 20 | inferred_complete_timeline |
| `Action_ZoneBlock` | 20 | 40 | 21 | inferred_complete_timeline |
| `Action_ZoneBlock` | 46 | 71 | 26 | inferred_complete_timeline |
| `Action_ZoneBlock` | 74 | 97 | 24 | inferred_complete_timeline |
| `Action_None` | 98 | 115 | 18 | inferred_complete_timeline |
| `Action_None` | 118 | 120 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 207

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 19 | 20 | inferred_complete_timeline |
| `Action_ZoneBlock` | 20 | 82 | 63 | inferred_complete_timeline |
| `Action_ZoneBlock` | 85 | 97 | 13 | inferred_complete_timeline |
| `Action_None` | 98 | 142 | 45 | inferred_complete_timeline |
| `Action_None` | 145 | 210 | 66 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–93
- **Visible Samples:** 94

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 16 | 17 | inferred_complete_timeline |
| `Action_None` | 17 | 93 | 77 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 16 | 17 | inferred_complete_timeline |
| `Action_None` | 17 | 210 | 194 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–84
- **Visible Samples:** 76

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 16 | 17 | inferred_complete_timeline |
| `Action_None` | 17 | 60 | 44 | inferred_complete_timeline |
| `Action_None` | 70 | 84 | 15 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–130
- **Visible Samples:** 131

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 16 | 17 | inferred_complete_timeline |
| `Action_None` | 17 | 130 | 114 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 16 | 17 | inferred_complete_timeline |
| `Action_None` | 17 | 210 | 194 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–165
- **Visible Samples:** 164

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 16 | 17 | inferred_complete_timeline |
| `Action_None` | 17 | 86 | 70 | inferred_complete_timeline |
| `Action_None` | 89 | 165 | 77 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–104
- **Visible Samples:** 105

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 16 | 17 | inferred_complete_timeline |
| `Action_None` | 17 | 104 | 88 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `8` | `9` | Position_Unknown | Team_Unknown | 0–210 | 201 | 4 | Undefined position; Undefined team |
| `16` | `17` | Position_Unknown | Team_Unknown | 4–210 | 177 | 10 | Undefined position; Undefined team |
| `17` | `18` | Position_Unknown | Team_Unknown | 32–44 | 13 | 1 | Undefined position; Undefined team |
| `18` | `19` | Position_Unknown | Team_Unknown | 47–210 | 154 | 5 | Undefined position; Undefined team |
| `19` | `22` | Position_Unknown | Team_Unknown | 89–210 | 122 | 1 | Undefined position; Undefined team |
| `20` | `23` | Position_Unknown | Team_Unknown | 99–210 | 112 | 2 | Undefined position; Undefined team |
| `21` | `25` | Position_Unknown | Team_Unknown | 124–210 | 87 | 1 | Undefined position; Undefined team |
| `22` | `26` | Position_Unknown | Team_Unknown | 126–164 | 39 | 1 | Undefined position; Undefined team |
| `23` | `27` | Position_Unknown | Team_Unknown | 130–210 | 81 | 1 | Undefined position; Undefined team |
| `24` | `28` | Position_Unknown | Team_Unknown | 130–178 | 47 | 3 | Undefined position; Undefined team |
| `25` | `29` | Position_Unknown | Team_Unknown | 135–210 | 76 | 1 | Undefined position; Undefined team |
| `26` | `31` | Position_Unknown | Team_Unknown | 146–210 | 65 | 1 | Undefined position; Undefined team |
| `27` | `33` | Position_Unknown | Team_Unknown | 147–162 | 16 | 1 | Undefined position; Undefined team |
| `28` | `34` | Position_Unknown | Team_Unknown | 160–210 | 51 | 1 | Undefined position; Undefined team |
| `29` | `37` | Position_Unknown | Team_Unknown | 173–210 | 38 | 1 | Undefined position; Undefined team |
| `30` | `38` | Position_Unknown | Team_Unknown | 177–210 | 34 | 1 | Undefined position; Undefined team |
| `31` | `39` | Position_Unknown | Team_Unknown | 177–210 | 17 | 3 | Undefined position; Undefined team |
| `32` | `40` | Position_Unknown | Team_Unknown | 177–178 | 2 | 1 | Undefined position; Undefined team |
| `33` | `41` | Position_Unknown | Team_Unknown | 205–210 | 6 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ `Action_BallSnap` for actor_track_id `23` (Position_Unknown): Annotated start 17 != Inferred start 99
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `11` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `14` (3 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `15` (5 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `16` (3 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `4` (3 segments found)
- ❌ Missing segment for action `Action_SnapReceive` on target `22` (Position_Unknown)
- ❌ Missing segment for action `Action_ReadDefender` on target `22` (Position_Unknown)
- ❌ Missing segment for action `Action_Keep` on target `22` (Position_Unknown)
- ⚠️ `Action_BallCarry` for actor_track_id `22` (Position_Unknown): Annotated start 62 != Inferred start 89

### Track Identity Issues

- ⚠️ Player track XML ID `4` (actor_track_id `5`): `SAF` position mapped to `defense` team
- ⚠️ Player track XML ID `6` (actor_track_id `7`): `SAF` position mapped to `defense` team
- ⚠️ 19 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 19 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 38 |
| Missing visible bounding boxes during action | 67 |
| Track-related warning | 5 |
| Other | 2 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 596: Duplicate assignment for track ID '7' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Segment 'Action_SnapReceive' for track '19' has invalid range: start=89, end=29. Clamping end to start.
- ⚠️ Segment 'Action_ReadDefender' for track '19' has invalid range: start=89, end=39. Clamping end to start.
- ⚠️ Segment 'Action_Keep' for track '19' has invalid range: start=89, end=61. Clamping end to start.
- ⚠️ Segment 'Action_BallSnap' for track '20' has invalid range: start=99, end=29. Clamping end to start.
- ⚠️ Action 'Action_None' range [17-210] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [17-130] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [17-210] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [20-40] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [46-71] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [98-115] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [118-120] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [17-86] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [89-165] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [17-93] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [17-104] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [17-198] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [202-203] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [207-209] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [17-111] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [119-131] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [135-210] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [17-87] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [20-51] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [98-210] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [17-60] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [70-84] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [17-32] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [54-210] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' for track '13' starts at frame 98, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_None' range [98-98] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [20-82] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [98-142] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [145-210] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [20-24] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [29-32] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [39-41] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [4-7] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [13-16] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [17-67] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [70-74] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [79-83] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [90-100] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [109-116] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [119-120] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [123-172] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [174-210] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [32-44] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [47-49] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [57-59] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [61-187] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [189-192] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [194-210] for track '18' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [89-210] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [100-210] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [124-210] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [126-164] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [130-210] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [130-162] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [164-172] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [174-178] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [135-210] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [146-210] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [147-162] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [160-210] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [173-210] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [177-210] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [177-181] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [198-205] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [207-210] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [177-178] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [205-210] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Player track '8' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '8' has undefined team_side. Will map to Team_Unknown.
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
- ⚠️ Metadata: no Dataset Summary row found for output_file 'InsideZoneRead_298'; source metadata written as null.

</details>