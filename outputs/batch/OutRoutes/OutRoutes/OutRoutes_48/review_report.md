# Play-Annotation-Generator Annotation Review — OutRoutes_48

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `OutRoutes_48`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Pass_OutRoutes`
- **Result:** `Result_Tackle`
- **Result Frame:** 239
- **Player Tracks:** 56
- **Ball Tracks:** 0
- **Action Segments:** 117
- **Validation Warnings:** 191
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 17
- **Exact Matches:** 3
- **Group Expanded Events:** 8
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 1
- **Missing Segments:** 4
- **Ambiguous Matches:** 0
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 99
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `9` | `Group` |
| ⚠️ START CHANGED | `Action_PassBlock` | LG | offense | `1` | `1` |
| ✅ EXACT | `Action_PassBlock` | RG | offense | `4` | `4` |
| ✅ EXACT | `Action_PassBlock` | RT | offense | `7` | `7` |
| ✅ EXACT | `Action_RunOutRoute` | DE2 | defense | `2` | `2` |
| ❌ MISSING SEGMENT | `Action_SnapReceive` | Position_Unknown | Team_Unknown | `19` | `18` |
| ❌ MISSING SEGMENT | `Action_ThrowPass` | Position_Unknown | Team_Unknown | `19` | `18` |
| ❌ MISSING SEGMENT | `Action_SecureCatch` | DE2 | defense | `2` | `2` |
| ❌ MISSING SEGMENT | `Action_BallCarry` | DE2 | defense | `2` | `2` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `1` | `Group` | 0 | START | 0 | 59 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `10` | `Group` | 0 | START | 0 | 74 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `11` | `Group` | 0 | START | 0 | 81 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `14` | `Group` | 0 | START | 0 | 52 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `16` | `Group` | 0 | START | 0 | 29 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `4` | `Group` | 0 | START | 0 | 48 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `7` | `Group` | 0 | START | 0 | 66 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `9` | `Group` | 0 | START | 0 | 66 |
| ⚠️ START CHANGED | `Action_PassBlock` | LG | `1` | `1` | 67 | START | 68 | 106 |
| ✅ EXACT | `Action_PassBlock` | RG | `4` | `4` | 67 | START | 67 | 74 |
| ✅ EXACT | `Action_PassBlock` | RT | `7` | `7` | 67 | START | 67 | 71 |
| ✅ EXACT | `Action_RunOutRoute` | DE2 | `2` | `2` | 74 | START | 74 | 122 |
| ❌ MISSING SEGMENT | `Action_SnapReceive` | Position_Unknown | `19` | `18` | 74 | END | N/A | N/A |
| ❌ MISSING SEGMENT | `Action_ThrowPass` | Position_Unknown | `19` | `18` | 117 | START | N/A | N/A |
| ❌ MISSING SEGMENT | `Action_SecureCatch` | DE2 | `2` | `2` | 150 | START | N/A | N/A |
| ❌ MISSING SEGMENT | `Action_BallCarry` | DE2 | `2` | `2` | 161 | START | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–222
- **Visible Samples:** 135

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 29 | 30 | inferred_complete_timeline |
| `Action_PreSnap` | 32 | 77 | 46 | inferred_complete_timeline |
| `Action_PreSnap` | 81 | 88 | 8 | inferred_complete_timeline |
| `Action_PreSnap` | 172 | 222 | 51 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–82
- **Visible Samples:** 78

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 74 | 75 | inferred_complete_timeline |
| `Action_PreSnap` | 80 | 82 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–81
- **Visible Samples:** 82

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 81 | 82 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–75
- **Visible Samples:** 75

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 52 | 53 | inferred_complete_timeline |
| `Action_PreSnap` | 54 | 75 | 22 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–66
- **Visible Samples:** 67

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 66 | 67 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–106
- **Visible Samples:** 99

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 59 | 60 | inferred_complete_timeline |
| `Action_PassBlock` | 68 | 106 | 39 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–74
- **Visible Samples:** 68

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 48 | 49 | inferred_complete_timeline |
| `Action_PreSnap` | 56 | 66 | 11 | inferred_complete_timeline |
| `Action_PassBlock` | 67 | 74 | 8 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–71
- **Visible Samples:** 72

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 66 | 67 | inferred_complete_timeline |
| `Action_PassBlock` | 67 | 71 | 5 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 193

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 90 | 91 | inferred_complete_timeline |
| `Action_PreSnap` | 138 | 239 | 102 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–122
- **Visible Samples:** 123

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 73 | 74 | inferred_complete_timeline |
| `Action_RunOutRoute` | 74 | 122 | 49 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–94
- **Visible Samples:** 95

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 94 | 95 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–30
- **Visible Samples:** 31

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 30 | 31 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–58
- **Visible Samples:** 59

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 58 | 59 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–72
- **Visible Samples:** 73

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 72 | 73 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–80
- **Visible Samples:** 81

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 80 | 81 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–63
- **Visible Samples:** 64

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 63 | 64 | inferred_complete_timeline |

</details>

<details>
<summary>SAF3 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–82
- **Visible Samples:** 83

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 82 | 83 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `17` | `17` | Position_Unknown | Team_Unknown | 22–77 | 49 | 2 | Undefined position; Undefined team |
| `18` | `19` | Position_Unknown | Team_Unknown | 34–91 | 41 | 3 | Undefined position; Undefined team |
| `19` | `20` | Position_Unknown | Team_Unknown | 40–86 | 23 | 4 | Undefined position; Undefined team |
| `20` | `21` | Position_Unknown | Team_Unknown | 43–67 | 11 | 2 | Undefined position; Undefined team |
| `21` | `22` | Position_Unknown | Team_Unknown | 56–171 | 95 | 4 | Undefined position; Undefined team |
| `22` | `24` | Position_Unknown | Team_Unknown | 61–66 | 6 | 1 | Undefined position; Undefined team |
| `23` | `25` | Position_Unknown | Team_Unknown | 62–239 | 56 | 5 | Undefined position; Undefined team |
| `24` | `26` | Position_Unknown | Team_Unknown | 74–239 | 156 | 3 | Undefined position; Undefined team |
| `25` | `27` | Position_Unknown | Team_Unknown | 77–86 | 8 | 2 | Undefined position; Undefined team |
| `26` | `28` | Position_Unknown | Team_Unknown | 78–215 | 95 | 3 | Undefined position; Undefined team |
| `27` | `29` | Position_Unknown | Team_Unknown | 82–158 | 44 | 3 | Undefined position; Undefined team |
| `28` | `30` | Position_Unknown | Team_Unknown | 88–98 | 10 | 2 | Undefined position; Undefined team |
| `29` | `31` | Position_Unknown | Team_Unknown | 88–96 | 6 | 2 | Undefined position; Undefined team |
| `30` | `32` | Position_Unknown | Team_Unknown | 88–89 | 2 | 1 | Undefined position; Undefined team |
| `31` | `33` | Position_Unknown | Team_Unknown | 115–239 | 118 | 2 | Undefined position; Undefined team |
| `32` | `34` | Position_Unknown | Team_Unknown | 120–239 | 115 | 2 | Undefined position; Undefined team |
| `33` | `35` | Position_Unknown | Team_Unknown | 124–169 | 20 | 2 | Undefined position; Undefined team |
| `34` | `37` | Position_Unknown | Team_Unknown | 133–136 | 4 | 1 | Undefined position; Undefined team |
| `35` | `40` | Position_Unknown | Team_Unknown | 142–239 | 98 | 1 | Undefined position; Undefined team |
| `36` | `42` | Position_Unknown | Team_Unknown | 151–174 | 20 | 3 | Undefined position; Undefined team |
| `37` | `43` | Position_Unknown | Team_Unknown | 157–213 | 46 | 4 | Undefined position; Undefined team |
| `38` | `44` | Position_Unknown | Team_Unknown | 158–226 | 54 | 3 | Undefined position; Undefined team |
| `39` | `45` | Position_Unknown | Team_Unknown | 163–239 | 74 | 2 | Undefined position; Undefined team |
| `40` | `46` | Position_Unknown | Team_Unknown | 163–219 | 27 | 2 | Undefined position; Undefined team |
| `41` | `47` | Position_Unknown | Team_Unknown | 169–239 | 41 | 5 | Undefined position; Undefined team |
| `42` | `48` | Position_Unknown | Team_Unknown | 169–174 | 6 | 1 | Undefined position; Undefined team |
| `43` | `49` | Position_Unknown | Team_Unknown | 169–175 | 7 | 1 | Undefined position; Undefined team |
| `44` | `50` | Position_Unknown | Team_Unknown | 169–171 | 3 | 1 | Undefined position; Undefined team |
| `45` | `53` | Position_Unknown | Team_Unknown | 175–176 | 2 | 1 | Undefined position; Undefined team |
| `46` | `54` | Position_Unknown | Team_Unknown | 176–225 | 24 | 5 | Undefined position; Undefined team |
| `47` | `55` | Position_Unknown | Team_Unknown | 177–222 | 38 | 2 | Undefined position; Undefined team |
| `48` | `57` | Position_Unknown | Team_Unknown | 181–228 | 17 | 3 | Undefined position; Undefined team |
| `49` | `58` | Position_Unknown | Team_Unknown | 182–192 | 11 | 1 | Undefined position; Undefined team |
| `50` | `59` | Position_Unknown | Team_Unknown | 184–239 | 55 | 2 | Undefined position; Undefined team |
| `51` | `61` | Position_Unknown | Team_Unknown | 186–230 | 45 | 1 | Undefined position; Undefined team |
| `52` | `63` | Position_Unknown | Team_Unknown | 191–239 | 48 | 2 | Undefined position; Undefined team |
| `53` | `64` | Position_Unknown | Team_Unknown | 198–207 | 6 | 2 | Undefined position; Undefined team |
| `54` | `65` | Position_Unknown | Team_Unknown | 231–239 | 9 | 1 | Undefined position; Undefined team |
| `55` | `66` | Position_Unknown | Team_Unknown | 232–239 | 7 | 2 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ `Action_PassBlock` for actor_track_id `1` (LG): Annotated start 67 != Inferred start 68
- ❌ Missing segment for action `Action_SnapReceive` on target `18` (Position_Unknown)
- ❌ Missing segment for action `Action_ThrowPass` on target `18` (Position_Unknown)
- ❌ Missing segment for action `Action_SecureCatch` on target `2` (DE2)
- ❌ Missing segment for action `Action_BallCarry` on target `2` (DE2)

### Track Identity Issues

- ⚠️ Player track XML ID `3` (actor_track_id `3`): `SAF2` position mapped to `defense` team
- ⚠️ Player track XML ID `5` (actor_track_id `5`): `SAF3` position mapped to `defense` team
- ⚠️ 39 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 39 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 78 |
| Missing visible bounding boxes during action | 106 |
| Track-related warning | 5 |
| Other | 2 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 56: Duplicate assignment for track ID '2' in grid. Overwriting previous assignment.
- ⚠️ Row 56: Duplicate assignment for track ID '5' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Action_SnapReceive present in CSV, but paired Action_BallSnap is missing.
- ⚠️ Segment 'Action_SecureCatch' for track '2' has invalid range: start=150, end=122. Clamping end to start.
- ⚠️ Segment 'Action_BallCarry' for track '2' has invalid range: start=161, end=122. Clamping end to start.
- ⚠️ Segment 'Action_ThrowPass' for track '18' has invalid range: start=117, end=91. Clamping end to start.
- ⚠️ Action 'Action_PreSnap' range [0-90] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-59] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [68-106] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunOutRoute' range [74-122] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-63] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-48] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [67-74] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-82] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-72] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [67-71] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-94] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-66] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-74] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [80-82] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-81] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-30] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-80] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-52] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [54-75] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-58] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-29] for track '16' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [32-77] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [81-88] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [172-222] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [22-26] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [34-77] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [34-63] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [66-71] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [87-91] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [40-48] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [60-63] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [68-75] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [85-86] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [43-44] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [59-67] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [56-87] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [89-100] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [106-135] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [151-171] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [61-66] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [62-63] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [129-136] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [192-202] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [204-222] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [224-239] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [74-103] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [106-186] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [77-79] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [82-86] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [78-163] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [174-177] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [211-215] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [82-84] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [86-93] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [126-158] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [88-90] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [92-98] for track '28' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [88-91] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [95-96] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [88-89] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [115-179] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [120-126] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [124-139] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [166-169] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [133-136] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [151-163] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [167-171] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [173-174] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [157-177] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [181-197] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [204-208] for track '37' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [211-213] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [158-161] for track '38' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [166-169] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [181-226] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [163-222] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [163-186] for track '40' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [217-219] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [169-188] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [191-196] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [221-230] for track '41' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [234-236] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [238-239] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [169-174] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [169-175] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [169-171] for track '44' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [175-176] for track '45' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [176-190] for track '46' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [199-201] for track '46' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [210-211] for track '46' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [221-222] for track '46' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [224-225] for track '46' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [177-188] for track '47' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [197-222] for track '47' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [181-185] for track '48' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [201-204] for track '48' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [221-228] for track '48' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [182-192] for track '49' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [184-228] for track '50' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [186-230] for track '51' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [191-195] for track '52' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [197-239] for track '52' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [198-201] for track '53' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [206-207] for track '53' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [232-236] for track '55' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [238-239] for track '55' has 1 frames without a visible bounding box.
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
- ⚠️ Player track '52' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '52' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '53' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '53' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '54' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '54' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '55' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '55' has undefined team_side. Will map to Team_Unknown.

</details>