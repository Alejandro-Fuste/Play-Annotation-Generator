# Play-Annotation-Generator Annotation Review — OutRoutes_83

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `OutRoutes_83`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Pass_OutRoutes`
- **Result:** `Result_OutOfBounds`
- **Result Frame:** 239
- **Player Tracks:** 29
- **Ball Tracks:** 0
- **Action Segments:** 64
- **Validation Warnings:** 70
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 21
- **Exact Matches:** 5
- **Group Expanded Events:** 10
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 5
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 41
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `9` | `Group` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RT | offense | `15` | `15` |
| ✅ EXACT | `Action_PassBlock` | LT | offense | `16` | `16` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LG | offense | `17` | `17` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | C | offense | `18` | `18` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RG | offense | `21` | `21` |
| ⚠️ AMBIGUOUS MATCH | `Action_RunOutRoute` | WR2 | offense | `2` | `2` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `12` | `12` |
| ✅ EXACT | `Action_ThrowPass` | QB | offense | `12` | `12` |
| ✅ EXACT | `Action_SecureCatch` | WR2 | offense | `2` | `2` |
| ✅ EXACT | `Action_BallCarry` | WR2 | offense | `2` | `2` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `1` | `Group` | 0 | START | 0 | 100 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `11` | `Group` | 0 | START | 0 | 180 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `12` | `Group` | 0 | START | 0 | 22 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `15` | `Group` | 0 | START | 0 | 17 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `16` | `Group` | 0 | START | 0 | 17 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `17` | `Group` | 0 | START | 0 | 17 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `18` | `Group` | 0 | START | 0 | 17 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `2` | `Group` | 0 | START | 0 | 22 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `21` | `Group` | 0 | START | 0 | 7 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `9` | `Group` | 0 | START | 0 | 64 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RT | `15` | `15` | 18 | START | 18 | 92 |
| ✅ EXACT | `Action_PassBlock` | LT | `16` | `16` | 18 | START | 18 | 143 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LG | `17` | `17` | 18 | START | 18 | 57 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | C | `18` | `18` | 18 | START | 18 | 115 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RG | `21` | `21` | 18 | START | 18 | 27 |
| ⚠️ AMBIGUOUS MATCH | `Action_RunOutRoute` | WR2 | `2` | `2` | 23 | START | 23 | 75 |
| ✅ EXACT | `Action_SnapReceive` | QB | `12` | `12` | 23 | END | 23 | 23 |
| ✅ EXACT | `Action_ThrowPass` | QB | `12` | `12` | 78 | START | 78 | 87 |
| ✅ EXACT | `Action_SecureCatch` | WR2 | `2` | `2` | 113 | START | 113 | 119 |
| ✅ EXACT | `Action_BallCarry` | WR2 | `2` | `2` | 120 | START | 120 | 180 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–145
- **Visible Samples:** 124

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 22 | 23 | inferred_complete_timeline |
| `Action_SnapReceive` | 23 | 23 | 1 | inferred_complete_timeline |
| `Action_None` | 24 | 77 | 54 | inferred_complete_timeline |
| `Action_ThrowPass` | 78 | 87 | 10 | inferred_complete_timeline |
| `Action_None` | 88 | 107 | 20 | inferred_complete_timeline |
| `Action_None` | 130 | 145 | 16 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–180
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 180 | 181 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–180
- **Visible Samples:** 179

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 64 | 65 | inferred_complete_timeline |
| `Action_PreSnap` | 67 | 180 | 114 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–180
- **Visible Samples:** 179

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 22 | 23 | inferred_complete_timeline |
| `Action_RunOutRoute` | 23 | 75 | 53 | inferred_complete_timeline |
| `Action_RunOutRoute` | 78 | 112 | 35 | inferred_complete_timeline |
| `Action_SecureCatch` | 113 | 119 | 7 | inferred_complete_timeline |
| `Action_BallCarry` | 120 | 180 | 61 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–119
- **Visible Samples:** 119

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 100 | 101 | inferred_complete_timeline |
| `Action_PreSnap` | 102 | 119 | 18 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–143
- **Visible Samples:** 144

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 17 | 18 | inferred_complete_timeline |
| `Action_PassBlock` | 18 | 143 | 126 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–85
- **Visible Samples:** 62

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 17 | 18 | inferred_complete_timeline |
| `Action_PassBlock` | 18 | 57 | 40 | inferred_complete_timeline |
| `Action_PassBlock` | 59 | 60 | 2 | inferred_complete_timeline |
| `Action_PassBlock` | 84 | 85 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–121
- **Visible Samples:** 119

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 17 | 18 | inferred_complete_timeline |
| `Action_PassBlock` | 18 | 115 | 98 | inferred_complete_timeline |
| `Action_PassBlock` | 119 | 121 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `21`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–137
- **Visible Samples:** 124

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 7 | 8 | inferred_complete_timeline |
| `Action_PreSnap` | 12 | 17 | 6 | inferred_complete_timeline |
| `Action_PassBlock` | 18 | 27 | 10 | inferred_complete_timeline |
| `Action_PassBlock` | 38 | 137 | 100 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–131
- **Visible Samples:** 127

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 17 | 18 | inferred_complete_timeline |
| `Action_PassBlock` | 18 | 92 | 75 | inferred_complete_timeline |
| `Action_PassBlock` | 94 | 100 | 7 | inferred_complete_timeline |
| `Action_PassBlock` | 105 | 131 | 27 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `defense`
- **Visible Frames:** 0–133
- **Visible Samples:** 124

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 60 | 61 | inferred_complete_timeline |
| `Action_PreSnap` | 64 | 79 | 16 | inferred_complete_timeline |
| `Action_PreSnap` | 87 | 133 | 47 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–180
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 180 | 181 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–72
- **Visible Samples:** 73

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 72 | 73 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `defense`
- **Visible Frames:** 0–38
- **Visible Samples:** 39

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 38 | 39 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–180
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 180 | 181 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–180
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 180 | 181 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–67
- **Visible Samples:** 68

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 67 | 68 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–180
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 180 | 181 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–113
- **Visible Samples:** 114

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 113 | 114 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–180
- **Visible Samples:** 170

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 137 | 138 | inferred_complete_timeline |
| `Action_PreSnap` | 142 | 148 | 7 | inferred_complete_timeline |
| `Action_PreSnap` | 152 | 167 | 16 | inferred_complete_timeline |
| `Action_PreSnap` | 169 | 170 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 174 | 180 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `defense`
- **Visible Frames:** 0–180
- **Visible Samples:** 173

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 156 | 157 | inferred_complete_timeline |
| `Action_PreSnap` | 165 | 180 | 16 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `8` | `8` | Position_Unknown | Team_Unknown | 0–180 | 179 | 2 | Undefined position; Undefined team |
| `22` | `23` | Position_Unknown | Team_Unknown | 69–130 | 62 | 1 | Undefined position; Undefined team |
| `23` | `24` | Position_Unknown | Team_Unknown | 80–180 | 100 | 2 | Undefined position; Undefined team |
| `24` | `25` | Position_Unknown | Team_Unknown | 81–180 | 98 | 2 | Undefined position; Undefined team |
| `25` | `30` | Position_Unknown | Team_Unknown | 99–100 | 2 | 1 | Undefined position; Undefined team |
| `26` | `32` | Position_Unknown | Team_Unknown | 107–180 | 68 | 3 | Undefined position; Undefined team |
| `27` | `34` | Position_Unknown | Team_Unknown | 143–180 | 38 | 1 | Undefined position; Undefined team |
| `28` | `35` | Position_Unknown | Team_Unknown | 150–180 | 31 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_PassBlock` and target `15` (3 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `17` (3 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `18` (2 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `21` (2 segments found)
- ⚠️ Ambiguous match for action `Action_RunOutRoute` and target `2` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `0` (actor_track_id `0`): `SAF2` position mapped to `defense` team
- ⚠️ Player track XML ID `7` (actor_track_id `7`): `SAF1` position mapped to `defense` team
- ⚠️ 8 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 8 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 16 |
| Missing visible bounding boxes during action | 52 |
| Other | 2 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Action_SnapReceive present in CSV, but paired Action_BallSnap is missing.
- ⚠️ Action 'Action_PreSnap' range [0-156] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [165-180] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-100] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [102-119] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunOutRoute' range [23-75] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [120-180] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-113] for track '3' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-180] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-180] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-180] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-137] for track '7' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [142-148] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [152-167] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [169-170] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [174-180] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-95] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [98-180] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-64] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [67-180] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-180] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-180] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [88-107] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [130-145] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-67] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-72] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [18-92] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [94-100] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [105-131] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [18-143] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [18-57] for track '17' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [59-60] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [84-85] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [18-115] for track '18' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [119-121] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-60] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [64-79] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [87-133] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-38] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-7] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [18-27] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [38-137] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [69-130] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [80-169] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [171-180] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [81-97] for track '24' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [100-180] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [99-100] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [107-110] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [116-150] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [152-180] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [143-180] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [150-180] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Player track '8' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '8' has undefined team_side. Will map to Team_Unknown.
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