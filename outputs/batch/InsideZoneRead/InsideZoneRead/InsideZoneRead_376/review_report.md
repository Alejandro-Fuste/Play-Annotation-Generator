# Play-Annotation-Generator Annotation Review — InsideZoneRead_376

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `InsideZoneRead_376`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Run_InsideZoneRead`
- **Result:** `Result_Tackle`
- **Result Frame:** 239
- **Player Tracks:** 19
- **Ball Tracks:** 1
- **Action Segments:** 58
- **Validation Warnings:** 52
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 20
- **Exact Matches:** 8
- **Group Expanded Events:** 7
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 3
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 37
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
| ✅ EXACT | `Action_BallSnap` | RT | offense | `11` | `10` |
| ✅ EXACT | `Action_ZoneBlock` | C | offense | `1` | `0` |
| ✅ EXACT | `Action_ZoneBlock` | RT | offense | `11` | `10` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | offense | `13` | `12` |
| ✅ EXACT | `Action_ZoneBlock` | LG | offense | `4` | `3` |
| ✅ EXACT | `Action_ZoneBlock` | LT | offense | `9` | `8` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `10` | `9` |
| ✅ EXACT | `Action_ReadDefender` | QB | offense | `10` | `9` |
| ⚠️ AMBIGUOUS MATCH | `Action_Keep` | QB | offense | `10` | `9` |
| ✅ EXACT | `Action_BlockSecondLevel` | RT | offense | `11` | `10` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | QB | offense | `10` | `9` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `1` | `Group` | 0 | START | 0 | 13 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `10` | `Group` | 0 | START | 0 | 10 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `11` | `Group` | 0 | START | 0 | 10 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `13` | `Group` | 0 | START | 0 | 13 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `4` | `Group` | 0 | START | 0 | 13 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `8` | `Group` | 0 | START | 0 | 10 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `9` | `Group` | 0 | START | 0 | 13 |
| ✅ EXACT | `Action_BallSnap` | RT | `11` | `10` | 11 | START | 11 | 13 |
| ✅ EXACT | `Action_ZoneBlock` | C | `1` | `0` | 14 | START | 14 | 76 |
| ✅ EXACT | `Action_ZoneBlock` | RT | `11` | `10` | 14 | START | 14 | 35 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | `13` | `12` | 14 | START | 14 | 24 |
| ✅ EXACT | `Action_ZoneBlock` | LG | `4` | `3` | 14 | START | 14 | 76 |
| ✅ EXACT | `Action_ZoneBlock` | LT | `9` | `8` | 14 | START | 14 | 76 |
| ✅ EXACT | `Action_SnapReceive` | QB | `10` | `9` | 25 | END | 11 | 25 |
| ✅ EXACT | `Action_ReadDefender` | QB | `10` | `9` | 29 | START | 29 | 34 |
| ⚠️ AMBIGUOUS MATCH | `Action_Keep` | QB | `10` | `9` | 35 | START | 35 | 48 |
| ✅ EXACT | `Action_BlockSecondLevel` | RT | `11` | `10` | 36 | START | 36 | 76 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | QB | `10` | `9` | 55 | START | 55 | 56 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 76 | BOUNDARY | N/A | N/A |

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
| `Action_PreSnap` | 0 | 10 | 11 | inferred_complete_timeline |
| `Action_SnapReceive` | 11 | 25 | 15 | inferred_complete_timeline |
| `Action_None` | 26 | 28 | 3 | inferred_complete_timeline |
| `Action_ReadDefender` | 29 | 34 | 6 | inferred_complete_timeline |
| `Action_Keep` | 35 | 48 | 14 | inferred_complete_timeline |
| `Action_Keep` | 50 | 54 | 5 | inferred_complete_timeline |
| `Action_BallCarry` | 55 | 56 | 2 | inferred_complete_timeline |
| `Action_BallCarry` | 58 | 136 | 79 | inferred_complete_timeline |
| `Action_BallCarry` | 142 | 150 | 9 | inferred_complete_timeline |

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
| `Action_PreSnap` | 0 | 10 | 11 | inferred_complete_timeline |
| `Action_None` | 11 | 46 | 36 | inferred_complete_timeline |
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
| `Action_PreSnap` | 0 | 13 | 14 | inferred_complete_timeline |
| `Action_ZoneBlock` | 14 | 76 | 63 | inferred_complete_timeline |
| `Action_None` | 77 | 90 | 14 | inferred_complete_timeline |

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
| `Action_PreSnap` | 0 | 13 | 14 | inferred_complete_timeline |
| `Action_ZoneBlock` | 14 | 76 | 63 | inferred_complete_timeline |
| `Action_None` | 77 | 99 | 23 | inferred_complete_timeline |
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
| `Action_PreSnap` | 0 | 13 | 14 | inferred_complete_timeline |
| `Action_ZoneBlock` | 14 | 76 | 63 | inferred_complete_timeline |
| `Action_None` | 77 | 92 | 16 | inferred_complete_timeline |

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
| `Action_PreSnap` | 0 | 13 | 14 | inferred_complete_timeline |
| `Action_ZoneBlock` | 14 | 24 | 11 | inferred_complete_timeline |
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
| `Action_PreSnap` | 0 | 10 | 11 | inferred_complete_timeline |
| `Action_BallSnap` | 11 | 13 | 3 | inferred_complete_timeline |
| `Action_ZoneBlock` | 14 | 35 | 22 | inferred_complete_timeline |
| `Action_BlockSecondLevel` | 36 | 76 | 41 | inferred_complete_timeline |
| `Action_None` | 77 | 77 | 1 | inferred_complete_timeline |
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
| `Action_PreSnap` | 0 | 10 | 11 | inferred_complete_timeline |
| `Action_None` | 11 | 87 | 77 | inferred_complete_timeline |

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
| `Action_PreSnap` | 0 | 10 | 11 | inferred_complete_timeline |
| `Action_None` | 11 | 60 | 50 | inferred_complete_timeline |
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
| `Action_PreSnap` | 0 | 10 | 11 | inferred_complete_timeline |
| `Action_None` | 11 | 70 | 60 | inferred_complete_timeline |
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
| `Action_PreSnap` | 0 | 10 | 11 | inferred_complete_timeline |
| `Action_None` | 11 | 92 | 82 | inferred_complete_timeline |

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
| `Action_PreSnap` | 0 | 10 | 11 | inferred_complete_timeline |
| `Action_None` | 11 | 150 | 140 | inferred_complete_timeline |

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
| `18` | `22` | Position_Unknown | Team_Unknown | 131–150 | 20 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

| xml_track_id | actor_track_id | First Visible Frame | Last Visible Frame | Visible Samples | Coverage | Missing Frame Ranges |
| --- | --- | --- | --- | --- | --- | --- |
| `19` | `23` | 131 | 131 | 1 | 100.0% | None |

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `13` (2 segments found)
- ⚠️ Ambiguous match for action `Action_Keep` and target `10` (2 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `10` (3 segments found)

### Track Identity Issues

- ⚠️ 7 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 7 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 14 |
| Missing visible bounding boxes during action | 36 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Track ID '17' in Player Track ID sheet does not exist in MOT gt.txt.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Action 'Action_None' range [77-92] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [11-60] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [63-64] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [70-76] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [82-90] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [92-94] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [11-150] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [77-99] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [106-112] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [145-150] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [11-70] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [72-150] for track '4' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [11-92] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [11-150] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [11-46] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [48-64] for track '7' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [70-72] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [77-150] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [77-90] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_Keep' range [35-48] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [55-56] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [58-136] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [142-150] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' for track '10' starts at frame 77, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_None' range [77-77] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [84-150] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [11-87] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [14-24] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [32-34] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [52-81] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [86-150] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [112-150] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [122-150] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [126-150] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [128-150] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [131-150] for track '18' has 1 frames without a visible bounding box.
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

</details>