# Play-Annotation-Generator Annotation Review — InsideZoneRead_376

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `InsideZoneRead_376`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Run_InsideZoneRead`
- **Result:** `Result_Touchdown`
- **Result Frame:** 239
- **Player Tracks:** 19
- **Ball Tracks:** 1
- **Action Segments:** 51
- **Validation Warnings:** 56
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 19
- **Exact Matches:** 4
- **Group Expanded Events:** 7
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 3
- **Missing Segments:** 3
- **Ambiguous Matches:** 0
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 34
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `8` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `9` | `Group` |
| ⚠️ START CHANGED | `Action_BallSnap` | Position_Unknown | Team_Unknown | `22` | `18` |
| ✅ EXACT | `Action_ZoneBlock` | C | offense | `1` | `0` |
| ✅ EXACT | `Action_ZoneBlock` | RT | offense | `11` | `10` |
| ⚠️ START CHANGED | `Action_ZoneBlock` | RG | offense | `13` | `12` |
| ✅ EXACT | `Action_ZoneBlock` | LG | offense | `4` | `3` |
| ✅ EXACT | `Action_ZoneBlock` | LT | offense | `9` | `8` |
| ❌ MISSING SEGMENT | `Action_SnapReceive` | Position_Unknown | Team_Unknown | `21` | `17` |
| ❌ MISSING SEGMENT | `Action_ReadDefender` | Position_Unknown | Team_Unknown | `21` | `17` |
| ❌ MISSING SEGMENT | `Action_Keep` | Position_Unknown | Team_Unknown | `21` | `17` |
| ⚠️ START CHANGED | `Action_BallCarry` | Position_Unknown | Team_Unknown | `21` | `17` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `1` | `Group` | 0 | START | 0 | 27 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `10` | `Group` | 0 | START | 0 | 24 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `11` | `Group` | 0 | START | 0 | 27 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `13` | `Group` | 0 | START | 0 | 24 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `4` | `Group` | 0 | START | 0 | 27 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `8` | `Group` | 0 | START | 0 | 24 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `9` | `Group` | 0 | START | 0 | 27 |
| ⚠️ START CHANGED | `Action_BallSnap` | Position_Unknown | `22` | `18` | 25 | START | 131 | 131 |
| ✅ EXACT | `Action_ZoneBlock` | C | `1` | `0` | 28 | START | 28 | 79 |
| ✅ EXACT | `Action_ZoneBlock` | RT | `11` | `10` | 28 | START | 28 | 77 |
| ⚠️ START CHANGED | `Action_ZoneBlock` | RG | `13` | `12` | 28 | START | 32 | 34 |
| ✅ EXACT | `Action_ZoneBlock` | LG | `4` | `3` | 28 | START | 28 | 79 |
| ✅ EXACT | `Action_ZoneBlock` | LT | `9` | `8` | 28 | START | 28 | 79 |
| ❌ MISSING SEGMENT | `Action_SnapReceive` | Position_Unknown | `21` | `17` | 38 | END | N/A | N/A |
| ❌ MISSING SEGMENT | `Action_ReadDefender` | Position_Unknown | `21` | `17` | 44 | START | N/A | N/A |
| ❌ MISSING SEGMENT | `Action_Keep` | Position_Unknown | `21` | `17` | 49 | START | N/A | N/A |
| ⚠️ START CHANGED | `Action_BallCarry` | Position_Unknown | `21` | `17` | 63 | START | 128 | 150 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 79 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–150
- **Visible Samples:** 144

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 24 | 25 | inferred_complete_timeline |
| `Action_None` | 25 | 48 | 24 | inferred_complete_timeline |
| `Action_None` | 50 | 56 | 7 | inferred_complete_timeline |
| `Action_None` | 58 | 136 | 79 | inferred_complete_timeline |
| `Action_None` | 142 | 150 | 9 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–150
- **Visible Samples:** 141

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 24 | 25 | inferred_complete_timeline |
| `Action_None` | 25 | 46 | 22 | inferred_complete_timeline |
| `Action_None` | 48 | 64 | 17 | inferred_complete_timeline |
| `Action_None` | 70 | 72 | 3 | inferred_complete_timeline |
| `Action_None` | 77 | 150 | 74 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–90
- **Visible Samples:** 91

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 27 | 28 | inferred_complete_timeline |
| `Action_ZoneBlock` | 28 | 79 | 52 | inferred_complete_timeline |
| `Action_None` | 80 | 90 | 11 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–150
- **Visible Samples:** 113

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 27 | 28 | inferred_complete_timeline |
| `Action_ZoneBlock` | 28 | 79 | 52 | inferred_complete_timeline |
| `Action_None` | 80 | 99 | 20 | inferred_complete_timeline |
| `Action_None` | 106 | 112 | 7 | inferred_complete_timeline |
| `Action_None` | 145 | 150 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–92
- **Visible Samples:** 93

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 27 | 28 | inferred_complete_timeline |
| `Action_ZoneBlock` | 28 | 79 | 52 | inferred_complete_timeline |
| `Action_None` | 80 | 92 | 13 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–34
- **Visible Samples:** 28

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 24 | 25 | inferred_complete_timeline |
| `Action_ZoneBlock` | 32 | 34 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–150
- **Visible Samples:** 145

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 27 | 28 | inferred_complete_timeline |
| `Action_ZoneBlock` | 28 | 77 | 50 | inferred_complete_timeline |
| `Action_None` | 84 | 150 | 67 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–87
- **Visible Samples:** 88

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 24 | 25 | inferred_complete_timeline |
| `Action_None` | 25 | 87 | 63 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–94
- **Visible Samples:** 82

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 24 | 25 | inferred_complete_timeline |
| `Action_None` | 25 | 60 | 36 | inferred_complete_timeline |
| `Action_None` | 63 | 64 | 2 | inferred_complete_timeline |
| `Action_None` | 70 | 76 | 7 | inferred_complete_timeline |
| `Action_None` | 82 | 90 | 9 | inferred_complete_timeline |
| `Action_None` | 92 | 94 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–150
- **Visible Samples:** 150

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 24 | 25 | inferred_complete_timeline |
| `Action_None` | 25 | 70 | 46 | inferred_complete_timeline |
| `Action_None` | 72 | 150 | 79 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–92
- **Visible Samples:** 93

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 24 | 25 | inferred_complete_timeline |
| `Action_None` | 25 | 92 | 68 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–150
- **Visible Samples:** 151

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 24 | 25 | inferred_complete_timeline |
| `Action_None` | 25 | 150 | 126 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `6` | `7` | Position_Unknown | Team_Unknown | 0–150 | 151 | 2 | Undefined position; Undefined team |
| `13` | `14` | Position_Unknown | Team_Unknown | 52–150 | 95 | 2 | Undefined position; Undefined team |
| `14` | `18` | Position_Unknown | Team_Unknown | 112–150 | 39 | 1 | Undefined position; Undefined team |
| `15` | `19` | Position_Unknown | Team_Unknown | 122–150 | 29 | 1 | Undefined position; Undefined team |
| `16` | `20` | Position_Unknown | Team_Unknown | 126–150 | 25 | 1 | Undefined position; Undefined team |
| `17` | `21` | Position_Unknown | Team_Unknown | 128–150 | 23 | 1 | Undefined position; Undefined team |
| `18` | `22` | Position_Unknown | Team_Unknown | 131–150 | 20 | 2 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

| xml_track_id | actor_track_id | First Visible Frame | Last Visible Frame | Visible Samples | Coverage | Missing Frame Ranges |
| --- | --- | --- | --- | --- | --- | --- |
| `19` | `23` | 131 | 131 | 1 | 100.0% | None |

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ `Action_BallSnap` for actor_track_id `22` (Position_Unknown): Annotated start 25 != Inferred start 131
- ⚠️ `Action_ZoneBlock` for actor_track_id `13` (RG): Annotated start 28 != Inferred start 32
- ❌ Missing segment for action `Action_SnapReceive` on target `17` (Position_Unknown)
- ❌ Missing segment for action `Action_ReadDefender` on target `17` (Position_Unknown)
- ❌ Missing segment for action `Action_Keep` on target `17` (Position_Unknown)
- ⚠️ `Action_BallCarry` for actor_track_id `21` (Position_Unknown): Annotated start 63 != Inferred start 128

### Track Identity Issues

- ⚠️ 7 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 7 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 14 |
| Missing visible bounding boxes during action | 35 |
| Track-related warning | 5 |
| Other | 2 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Track ID '17' in Player Track ID sheet does not exist in MOT gt.txt.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Segment 'Action_SnapReceive' for track '17' has invalid range: start=128, end=38. Clamping end to start.
- ⚠️ Segment 'Action_ReadDefender' for track '17' has invalid range: start=128, end=48. Clamping end to start.
- ⚠️ Segment 'Action_Keep' for track '17' has invalid range: start=128, end=62. Clamping end to start.
- ⚠️ Segment 'Action_BallSnap' for track '18' has invalid range: start=131, end=38. Clamping end to start.
- ⚠️ Action 'Action_None' range [80-92] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [25-60] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [63-64] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [70-76] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [82-90] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [92-94] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [25-150] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [80-99] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [106-112] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [145-150] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [25-70] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [72-150] for track '4' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [25-92] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [25-150] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [25-46] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [48-64] for track '7' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [70-72] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [77-150] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [80-90] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [25-48] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [50-56] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [58-136] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [142-150] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [28-77] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [84-150] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [25-87] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-24] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [32-34] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [52-81] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [86-150] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [112-150] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [122-150] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [126-150] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [128-150] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [132-150] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Player track '6' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '6' has undefined team_side. Will map to Team_Unknown.
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
- ⚠️ Metadata: no Dataset Summary row found for output_file 'InsideZoneRead_376'; source metadata written as null.

</details>