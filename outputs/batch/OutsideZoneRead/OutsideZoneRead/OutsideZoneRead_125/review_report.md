# Play-Annotation-Generator Annotation Review — OutsideZoneRead_125

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `OutsideZoneRead_125`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Run_OutsideZoneRead`
- **Result:** `Result_Tackle`
- **Result Frame:** 239
- **Player Tracks:** 31
- **Ball Tracks:** 0
- **Action Segments:** 91
- **Validation Warnings:** 105
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 15
- **Exact Matches:** 5
- **Group Expanded Events:** 7
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 1
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 74
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR4 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `8` | `Group` |
| ✅ EXACT | `Action_BallSnap` | CB1 | defense | `11` | `10` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | offense | `14` | `13` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `10` | `9` |
| ✅ EXACT | `Action_ReadEdgeDefender` | QB | offense | `10` | `9` |
| ✅ EXACT | `Action_Keep` | QB | offense | `10` | `9` |
| ✅ EXACT | `Action_BallCarry` | QB | offense | `10` | `9` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR4 | `1` | `Group` | 0 | START | 0 | 3 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `10` | `Group` | 0 | START | 0 | 3 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `12` | `Group` | 0 | START | 0 | 3 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `13` | `Group` | 0 | START | 0 | 3 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `14` | `Group` | 0 | START | 0 | 6 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `2` | `Group` | 0 | START | 0 | 3 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `8` | `Group` | 0 | START | 0 | 3 |
| ✅ EXACT | `Action_BallSnap` | CB1 | `11` | `10` | 4 | START | 4 | 17 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | `14` | `13` | 7 | START | 7 | 20 |
| ✅ EXACT | `Action_SnapReceive` | QB | `10` | `9` | 17 | END | 4 | 17 |
| ✅ EXACT | `Action_ReadEdgeDefender` | QB | `10` | `9` | 22 | START | 22 | 25 |
| ✅ EXACT | `Action_Keep` | QB | `10` | `9` | 26 | START | 26 | 43 |
| ✅ EXACT | `Action_BallCarry` | QB | `10` | `9` | 44 | START | 44 | 58 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 83 | BOUNDARY | N/A | N/A |

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
- **Visible Frames:** 0–58
- **Visible Samples:** 59

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 3 | 4 | inferred_complete_timeline |
| `Action_SnapReceive` | 4 | 17 | 14 | inferred_complete_timeline |
| `Action_None` | 18 | 21 | 4 | inferred_complete_timeline |
| `Action_ReadEdgeDefender` | 22 | 25 | 4 | inferred_complete_timeline |
| `Action_Keep` | 26 | 43 | 18 | inferred_complete_timeline |
| `Action_BallCarry` | 44 | 58 | 15 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–150
- **Visible Samples:** 123

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 3 | 4 | inferred_complete_timeline |
| `Action_None` | 4 | 39 | 36 | inferred_complete_timeline |
| `Action_None` | 42 | 54 | 13 | inferred_complete_timeline |
| `Action_None` | 71 | 75 | 5 | inferred_complete_timeline |
| `Action_None` | 83 | 85 | 3 | inferred_complete_timeline |
| `Action_None` | 89 | 150 | 62 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–150
- **Visible Samples:** 151

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 3 | 4 | inferred_complete_timeline |
| `Action_None` | 4 | 150 | 147 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–150
- **Visible Samples:** 151

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 3 | 4 | inferred_complete_timeline |
| `Action_None` | 4 | 150 | 147 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–150
- **Visible Samples:** 151

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 3 | 4 | inferred_complete_timeline |
| `Action_None` | 4 | 150 | 147 | inferred_complete_timeline |

</details>

<details>
<summary>WR4 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–150
- **Visible Samples:** 131

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 3 | 4 | inferred_complete_timeline |
| `Action_None` | 4 | 76 | 73 | inferred_complete_timeline |
| `Action_None` | 83 | 86 | 4 | inferred_complete_timeline |
| `Action_None` | 91 | 94 | 4 | inferred_complete_timeline |
| `Action_None` | 96 | 108 | 13 | inferred_complete_timeline |
| `Action_None` | 118 | 150 | 33 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–32
- **Visible Samples:** 29

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 6 | 7 | inferred_complete_timeline |
| `Action_ZoneBlock` | 7 | 20 | 14 | inferred_complete_timeline |
| `Action_ZoneBlock` | 25 | 32 | 8 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE2 — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–15
- **Visible Samples:** 10

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 3 | 4 | inferred_complete_timeline |
| `Action_None` | 4 | 5 | 2 | inferred_complete_timeline |
| `Action_None` | 11 | 12 | 2 | inferred_complete_timeline |
| `Action_None` | 14 | 15 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–91
- **Visible Samples:** 82

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 3 | 4 | inferred_complete_timeline |
| `Action_None` | 4 | 78 | 75 | inferred_complete_timeline |
| `Action_None` | 89 | 91 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–150
- **Visible Samples:** 110

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 3 | 4 | inferred_complete_timeline |
| `Action_None` | 4 | 20 | 17 | inferred_complete_timeline |
| `Action_None` | 22 | 26 | 5 | inferred_complete_timeline |
| `Action_None` | 30 | 32 | 3 | inferred_complete_timeline |
| `Action_None` | 70 | 150 | 81 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–148
- **Visible Samples:** 149

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 3 | 4 | inferred_complete_timeline |
| `Action_BallSnap` | 4 | 17 | 14 | inferred_complete_timeline |
| `Action_None` | 18 | 148 | 131 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–150
- **Visible Samples:** 151

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 3 | 4 | inferred_complete_timeline |
| `Action_None` | 4 | 150 | 147 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–138
- **Visible Samples:** 133

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 3 | 4 | inferred_complete_timeline |
| `Action_None` | 4 | 97 | 94 | inferred_complete_timeline |
| `Action_None` | 102 | 132 | 31 | inferred_complete_timeline |
| `Action_None` | 135 | 138 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>CB4 — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–108
- **Visible Samples:** 71

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 3 | 4 | inferred_complete_timeline |
| `Action_None` | 4 | 60 | 57 | inferred_complete_timeline |
| `Action_None` | 65 | 68 | 4 | inferred_complete_timeline |
| `Action_None` | 70 | 72 | 3 | inferred_complete_timeline |
| `Action_None` | 106 | 108 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–150
- **Visible Samples:** 151

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 3 | 4 | inferred_complete_timeline |
| `Action_None` | 4 | 150 | 147 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `15` | `16` | Position_Unknown | Team_Unknown | 23–49 | 20 | 3 | Undefined position; Undefined team |
| `16` | `17` | Position_Unknown | Team_Unknown | 24–150 | 84 | 5 | Undefined position; Undefined team |
| `17` | `18` | Position_Unknown | Team_Unknown | 25–26 | 2 | 1 | Undefined position; Undefined team |
| `18` | `19` | Position_Unknown | Team_Unknown | 30–89 | 7 | 2 | Undefined position; Undefined team |
| `19` | `21` | Position_Unknown | Team_Unknown | 58–150 | 74 | 3 | Undefined position; Undefined team |
| `20` | `23` | Position_Unknown | Team_Unknown | 89–103 | 6 | 2 | Undefined position; Undefined team |
| `21` | `26` | Position_Unknown | Team_Unknown | 106–150 | 45 | 1 | Undefined position; Undefined team |
| `22` | `27` | Position_Unknown | Team_Unknown | 108–149 | 36 | 5 | Undefined position; Undefined team |
| `23` | `28` | Position_Unknown | Team_Unknown | 109–150 | 39 | 3 | Undefined position; Undefined team |
| `24` | `29` | Position_Unknown | Team_Unknown | 109–150 | 36 | 2 | Undefined position; Undefined team |
| `25` | `30` | Position_Unknown | Team_Unknown | 109–150 | 25 | 2 | Undefined position; Undefined team |
| `26` | `31` | Position_Unknown | Team_Unknown | 112–135 | 23 | 2 | Undefined position; Undefined team |
| `27` | `32` | Position_Unknown | Team_Unknown | 119–150 | 32 | 1 | Undefined position; Undefined team |
| `28` | `33` | Position_Unknown | Team_Unknown | 123–124 | 2 | 1 | Undefined position; Undefined team |
| `29` | `35` | Position_Unknown | Team_Unknown | 125–150 | 24 | 2 | Undefined position; Undefined team |
| `30` | `38` | Position_Unknown | Team_Unknown | 146–150 | 5 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `14` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `2` (actor_track_id `3`): `SAF` position mapped to `defense` team
- ⚠️ 16 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 16 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 32 |
| Missing visible bounding boxes during action | 72 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Action 'Action_None' range [4-76] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [83-86] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [91-94] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [96-108] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [118-150] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [4-150] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [4-150] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [4-78] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [89-91] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [4-97] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [102-132] for track '4' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [135-138] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [4-60] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [65-68] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [70-72] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [106-108] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [4-150] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [4-150] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [4-20] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [22-26] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [30-32] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [70-150] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [44-58] for track '9' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [18-148] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [4-150] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [4-39] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [42-54] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [71-75] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [83-85] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [89-150] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [7-20] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [25-32] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-3] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [4-5] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [11-12] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [14-15] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [23-34] for track '15' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [39-42] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [46-49] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [24-26] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [31-32] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [39-44] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [51-52] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [80-150] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [25-26] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [30-32] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [86-89] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [58-80] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [87-91] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [105-150] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [89-91] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [101-103] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [106-150] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [108-109] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [111-132] for track '22' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [134-137] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [140-142] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [145-149] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [109-118] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [121-140] for track '23' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [142-150] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [109-112] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [119-150] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [109-110] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [128-150] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [112-131] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [133-135] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [119-150] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [123-124] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [125-129] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [132-150] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [146-150] for track '30' has 1 frames without a visible bounding box.
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

</details>