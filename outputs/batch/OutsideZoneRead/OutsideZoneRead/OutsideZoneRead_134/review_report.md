# Play-Annotation-Generator Annotation Review — OutsideZoneRead_134

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `OutsideZoneRead_134`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Run_OutsideZoneRead`
- **Result:** `Result_Tackle`
- **Result Frame:** 239
- **Player Tracks:** 29
- **Ball Tracks:** 0
- **Action Segments:** 81
- **Validation Warnings:** 91
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 22
- **Exact Matches:** 5
- **Group Expanded Events:** 9
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 1
- **Ambiguous Matches:** 5
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 59
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | offense | `7` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `13` | `12` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | offense | `10` | `9` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | offense | `11` | `10` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | offense | `13` | `12` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | offense | `15` | `14` |
| ✅ EXACT | `Action_ZoneBlock` | LT | offense | `3` | `2` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `6` | `5` |
| ✅ EXACT | `Action_ReadEdgeDefender` | QB | offense | `6` | `5` |
| ⚠️ AMBIGUOUS MATCH | `Action_BlockSecondLevel` | RT | offense | `10` | `9` |
| ✅ EXACT | `Action_Keep` | QB | offense | `6` | `5` |
| ❌ MISSING SEGMENT | `Action_BallCarry` | QB | offense | `6` | `5` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `10` | `Group` | 0 | START | 0 | 7 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `11` | `Group` | 0 | START | 0 | 7 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `12` | `Group` | 0 | START | 0 | 4 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `13` | `Group` | 0 | START | 0 | 4 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `15` | `Group` | 0 | START | 0 | 7 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | `16` | `Group` | 0 | START | 0 | 1 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `3` | `Group` | 0 | START | 0 | 7 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `6` | `Group` | 0 | START | 0 | 4 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | `7` | `Group` | 0 | START | 0 | 4 |
| ✅ EXACT | `Action_BallSnap` | C | `13` | `12` | 5 | START | 5 | 19 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | `10` | `9` | 8 | START | 8 | 32 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | `11` | `10` | 8 | START | 8 | 24 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | `13` | `12` | 8 | START | 20 | 85 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | `15` | `14` | 8 | START | 8 | 20 |
| ✅ EXACT | `Action_ZoneBlock` | LT | `3` | `2` | 8 | START | 8 | 48 |
| ✅ EXACT | `Action_SnapReceive` | QB | `6` | `5` | 19 | END | 5 | 19 |
| ✅ EXACT | `Action_ReadEdgeDefender` | QB | `6` | `5` | 23 | START | 23 | 33 |
| ⚠️ AMBIGUOUS MATCH | `Action_BlockSecondLevel` | RT | `10` | `9` | 33 | START | 33 | 63 |
| ✅ EXACT | `Action_Keep` | QB | `6` | `5` | 34 | START | 34 | 37 |
| ❌ MISSING SEGMENT | `Action_BallCarry` | QB | `6` | `5` | 59 | START | N/A | N/A |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 113 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–37
- **Visible Samples:** 38

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 4 | 5 | inferred_complete_timeline |
| `Action_SnapReceive` | 5 | 19 | 15 | inferred_complete_timeline |
| `Action_None` | 20 | 22 | 3 | inferred_complete_timeline |
| `Action_ReadEdgeDefender` | 23 | 33 | 11 | inferred_complete_timeline |
| `Action_Keep` | 34 | 37 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–95
- **Visible Samples:** 93

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 4 | 5 | inferred_complete_timeline |
| `Action_None` | 5 | 28 | 24 | inferred_complete_timeline |
| `Action_None` | 32 | 95 | 64 | inferred_complete_timeline |

</details>

<details>
<summary>TE1 — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–86
- **Visible Samples:** 86

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 4 | 5 | inferred_complete_timeline |
| `Action_None` | 5 | 36 | 32 | inferred_complete_timeline |
| `Action_None` | 38 | 86 | 49 | inferred_complete_timeline |

</details>

<details>
<summary>TE2 — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–89
- **Visible Samples:** 9

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_None` | 19 | 20 | 2 | inferred_complete_timeline |
| `Action_None` | 85 | 89 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–48
- **Visible Samples:** 49

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 7 | 8 | inferred_complete_timeline |
| `Action_ZoneBlock` | 8 | 48 | 41 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–150
- **Visible Samples:** 140

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 7 | 8 | inferred_complete_timeline |
| `Action_ZoneBlock` | 8 | 20 | 13 | inferred_complete_timeline |
| `Action_ZoneBlock` | 25 | 35 | 11 | inferred_complete_timeline |
| `Action_ZoneBlock` | 43 | 113 | 71 | inferred_complete_timeline |
| `Action_None` | 114 | 150 | 37 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–148
- **Visible Samples:** 145

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 4 | 5 | inferred_complete_timeline |
| `Action_BallSnap` | 5 | 19 | 15 | inferred_complete_timeline |
| `Action_ZoneBlock` | 20 | 85 | 66 | inferred_complete_timeline |
| `Action_ZoneBlock` | 90 | 113 | 24 | inferred_complete_timeline |
| `Action_None` | 114 | 148 | 35 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–150
- **Visible Samples:** 136

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 7 | 8 | inferred_complete_timeline |
| `Action_ZoneBlock` | 8 | 24 | 17 | inferred_complete_timeline |
| `Action_ZoneBlock` | 27 | 52 | 26 | inferred_complete_timeline |
| `Action_ZoneBlock` | 54 | 90 | 37 | inferred_complete_timeline |
| `Action_ZoneBlock` | 92 | 94 | 3 | inferred_complete_timeline |
| `Action_ZoneBlock` | 100 | 101 | 2 | inferred_complete_timeline |
| `Action_ZoneBlock` | 105 | 113 | 9 | inferred_complete_timeline |
| `Action_None` | 114 | 132 | 19 | inferred_complete_timeline |
| `Action_None` | 136 | 150 | 15 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–94
- **Visible Samples:** 67

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 7 | 8 | inferred_complete_timeline |
| `Action_ZoneBlock` | 8 | 32 | 25 | inferred_complete_timeline |
| `Action_BlockSecondLevel` | 33 | 63 | 31 | inferred_complete_timeline |
| `Action_BlockSecondLevel` | 92 | 94 | 3 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–149
- **Visible Samples:** 142

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 4 | 5 | inferred_complete_timeline |
| `Action_None` | 5 | 95 | 91 | inferred_complete_timeline |
| `Action_None` | 97 | 136 | 40 | inferred_complete_timeline |
| `Action_None` | 144 | 149 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–81
- **Visible Samples:** 82

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 4 | 5 | inferred_complete_timeline |
| `Action_None` | 5 | 81 | 77 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–60
- **Visible Samples:** 61

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 4 | 5 | inferred_complete_timeline |
| `Action_None` | 5 | 60 | 56 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–81
- **Visible Samples:** 69

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 4 | 5 | inferred_complete_timeline |
| `Action_None` | 5 | 41 | 37 | inferred_complete_timeline |
| `Action_None` | 45 | 60 | 16 | inferred_complete_timeline |
| `Action_None` | 63 | 66 | 4 | inferred_complete_timeline |
| `Action_None` | 75 | 81 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–52
- **Visible Samples:** 47

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 4 | 5 | inferred_complete_timeline |
| `Action_None` | 5 | 42 | 38 | inferred_complete_timeline |
| `Action_None` | 44 | 45 | 2 | inferred_complete_timeline |
| `Action_None` | 51 | 52 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–147
- **Visible Samples:** 120

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 4 | 5 | inferred_complete_timeline |
| `Action_None` | 5 | 109 | 105 | inferred_complete_timeline |
| `Action_None` | 124 | 125 | 2 | inferred_complete_timeline |
| `Action_None` | 140 | 147 | 8 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–149
- **Visible Samples:** 150

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 4 | 5 | inferred_complete_timeline |
| `Action_None` | 5 | 149 | 145 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `16` | `17` | Position_Unknown | Team_Unknown | 9–15 | 7 | 1 | Undefined position; Undefined team |
| `17` | `18` | Position_Unknown | Team_Unknown | 29–72 | 44 | 1 | Undefined position; Undefined team |
| `18` | `19` | Position_Unknown | Team_Unknown | 38–131 | 94 | 1 | Undefined position; Undefined team |
| `19` | `20` | Position_Unknown | Team_Unknown | 49–150 | 100 | 2 | Undefined position; Undefined team |
| `20` | `21` | Position_Unknown | Team_Unknown | 52–150 | 87 | 2 | Undefined position; Undefined team |
| `21` | `22` | Position_Unknown | Team_Unknown | 63–122 | 57 | 2 | Undefined position; Undefined team |
| `22` | `23` | Position_Unknown | Team_Unknown | 68–150 | 82 | 2 | Undefined position; Undefined team |
| `23` | `24` | Position_Unknown | Team_Unknown | 69–150 | 80 | 2 | Undefined position; Undefined team |
| `24` | `26` | Position_Unknown | Team_Unknown | 90–150 | 61 | 1 | Undefined position; Undefined team |
| `25` | `27` | Position_Unknown | Team_Unknown | 94–102 | 7 | 2 | Undefined position; Undefined team |
| `26` | `28` | Position_Unknown | Team_Unknown | 112–150 | 39 | 1 | Undefined position; Undefined team |
| `27` | `29` | Position_Unknown | Team_Unknown | 116–150 | 35 | 1 | Undefined position; Undefined team |
| `28` | `30` | Position_Unknown | Team_Unknown | 137–146 | 10 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `10` (7 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `11` (6 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `13` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `15` (3 segments found)
- ⚠️ Ambiguous match for action `Action_BlockSecondLevel` and target `10` (2 segments found)
- ❌ Missing segment for action `Action_BallCarry` on target `6` (QB)

### Track Identity Issues

- ⚠️ Player track XML ID `1` (actor_track_id `2`): `SAF` position mapped to `defense` team
- ⚠️ 13 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 13 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 26 |
| Missing visible bounding boxes during action | 59 |
| Track-related warning | 5 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Segment 'Action_BallCarry' for track '5' has invalid range: start=59, end=37. Clamping end to start.
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '10' (RG) duration 106 frames exceeds threshold 90 frames [start=8, end=113].
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '12' (C) duration 106 frames exceeds threshold 90 frames [start=8, end=113].
- ⚠️ Resolved action overlap for track '12' (C): higher_priority='Action_BallSnap' [5–19], lower_priority='Action_ZoneBlock' annotated_start=8, effective_Action_ZoneBlock_start=20.
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '14' (LG) duration 106 frames exceeds threshold 90 frames [start=8, end=113].
- ⚠️ Action 'Action_None' range [5-95] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [97-136] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [144-149] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [5-149] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [8-48] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [5-42] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [44-45] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [51-52] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [5-109] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [124-125] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [140-147] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_Keep' range [34-37] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [5-36] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [38-86] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [5-81] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [5-41] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [45-60] for track '8' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [63-66] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [75-81] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BlockSecondLevel' range [33-63] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BlockSecondLevel' range [92-94] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [8-24] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [27-52] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [54-90] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [92-94] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [100-101] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [114-132] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [136-150] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [5-28] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [32-95] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [20-85] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [114-148] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [5-60] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [8-20] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [25-35] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [43-113] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [114-150] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-1] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [19-20] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [85-89] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [9-15] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [29-72] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [38-131] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [49-97] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [100-150] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [52-126] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [139-150] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [63-91] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [95-122] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [68-104] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [106-150] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [69-113] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [116-150] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [90-150] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [94-97] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [100-102] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [112-150] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [116-150] for track '27' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [137-146] for track '28' has 1 frames without a visible bounding box.
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

</details>