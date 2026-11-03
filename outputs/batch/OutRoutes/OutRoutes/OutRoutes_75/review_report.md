# Play-Annotation-Generator Annotation Review — OutRoutes_75

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `OutRoutes_75`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Pass_OutRoutes`
- **Result:** `Result_Tackle`
- **Result Frame:** 239
- **Player Tracks:** 29
- **Ball Tracks:** 0
- **Action Segments:** 71
- **Validation Warnings:** 80
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 21
- **Exact Matches:** 6
- **Group Expanded Events:** 10
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 4
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 48
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `9` | `Group` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LT | offense | `14` | `14` |
| ✅ EXACT | `Action_PassBlock` | LG | offense | `15` | `15` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RG | offense | `19` | `19` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | C | offense | `20` | `20` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RT | offense | `21` | `21` |
| ✅ EXACT | `Action_RunOutRoute` | TE | offense | `9` | `9` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `13` | `13` |
| ✅ EXACT | `Action_ThrowPass` | QB | offense | `13` | `13` |
| ✅ EXACT | `Action_SecureCatch` | TE | offense | `9` | `9` |
| ✅ EXACT | `Action_BallCarry` | TE | offense | `9` | `9` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `0` | `Group` | 0 | START | 0 | 150 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `13` | `Group` | 0 | START | 0 | 35 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `14` | `Group` | 0 | START | 0 | 29 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `15` | `Group` | 0 | START | 0 | 29 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `19` | `Group` | 0 | START | 0 | 29 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `2` | `Group` | 0 | START | 0 | 150 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `20` | `Group` | 0 | START | 0 | 29 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `21` | `Group` | 0 | START | 0 | 29 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `7` | `Group` | 0 | START | 0 | 41 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `9` | `Group` | 0 | START | 0 | 35 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LT | `14` | `14` | 30 | START | 30 | 47 |
| ✅ EXACT | `Action_PassBlock` | LG | `15` | `15` | 30 | START | 30 | 64 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RG | `19` | `19` | 30 | START | 30 | 46 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | C | `20` | `20` | 30 | START | 30 | 55 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RT | `21` | `21` | 30 | START | 30 | 46 |
| ✅ EXACT | `Action_RunOutRoute` | TE | `9` | `9` | 36 | START | 36 | 106 |
| ✅ EXACT | `Action_SnapReceive` | QB | `13` | `13` | 36 | END | 36 | 36 |
| ✅ EXACT | `Action_ThrowPass` | QB | `13` | `13` | 79 | START | 79 | 80 |
| ✅ EXACT | `Action_SecureCatch` | TE | `9` | `9` | 107 | START | 107 | 114 |
| ✅ EXACT | `Action_BallCarry` | TE | `9` | `9` | 115 | START | 115 | 150 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–80
- **Visible Samples:** 81

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 35 | 36 | inferred_complete_timeline |
| `Action_SnapReceive` | 36 | 36 | 1 | inferred_complete_timeline |
| `Action_None` | 37 | 78 | 42 | inferred_complete_timeline |
| `Action_ThrowPass` | 79 | 80 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–150
- **Visible Samples:** 57

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 41 | 42 | inferred_complete_timeline |
| `Action_PreSnap` | 131 | 132 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 135 | 141 | 7 | inferred_complete_timeline |
| `Action_PreSnap` | 145 | 150 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–150
- **Visible Samples:** 151

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 150 | 151 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–150
- **Visible Samples:** 151

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 150 | 151 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–150
- **Visible Samples:** 151

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 35 | 36 | inferred_complete_timeline |
| `Action_RunOutRoute` | 36 | 106 | 71 | inferred_complete_timeline |
| `Action_SecureCatch` | 107 | 114 | 8 | inferred_complete_timeline |
| `Action_BallCarry` | 115 | 150 | 36 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–67
- **Visible Samples:** 64

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 29 | 30 | inferred_complete_timeline |
| `Action_PassBlock` | 30 | 47 | 18 | inferred_complete_timeline |
| `Action_PassBlock` | 52 | 67 | 16 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–64
- **Visible Samples:** 65

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 29 | 30 | inferred_complete_timeline |
| `Action_PassBlock` | 30 | 64 | 35 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–150
- **Visible Samples:** 117

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 29 | 30 | inferred_complete_timeline |
| `Action_PassBlock` | 30 | 55 | 26 | inferred_complete_timeline |
| `Action_PassBlock` | 57 | 58 | 2 | inferred_complete_timeline |
| `Action_PassBlock` | 61 | 63 | 3 | inferred_complete_timeline |
| `Action_PassBlock` | 92 | 95 | 4 | inferred_complete_timeline |
| `Action_PassBlock` | 99 | 150 | 52 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–70
- **Visible Samples:** 62

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 29 | 30 | inferred_complete_timeline |
| `Action_PassBlock` | 30 | 46 | 17 | inferred_complete_timeline |
| `Action_PassBlock` | 52 | 64 | 13 | inferred_complete_timeline |
| `Action_PassBlock` | 69 | 70 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `21`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–70
- **Visible Samples:** 62

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 29 | 30 | inferred_complete_timeline |
| `Action_PassBlock` | 30 | 46 | 17 | inferred_complete_timeline |
| `Action_PassBlock` | 51 | 63 | 13 | inferred_complete_timeline |
| `Action_PassBlock` | 69 | 70 | 2 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–106
- **Visible Samples:** 98

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 68 | 69 | inferred_complete_timeline |
| `Action_PreSnap` | 77 | 85 | 9 | inferred_complete_timeline |
| `Action_PreSnap` | 87 | 106 | 20 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `defense`
- **Visible Frames:** 0–79
- **Visible Samples:** 62

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 46 | 47 | inferred_complete_timeline |
| `Action_PreSnap` | 55 | 58 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 60 | 63 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 69 | 70 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 74 | 76 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 78 | 79 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 0–84
- **Visible Samples:** 65

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 46 | 47 | inferred_complete_timeline |
| `Action_PreSnap` | 50 | 64 | 15 | inferred_complete_timeline |
| `Action_PreSnap` | 82 | 84 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–70
- **Visible Samples:** 67

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 64 | 65 | inferred_complete_timeline |
| `Action_PreSnap` | 69 | 70 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–63
- **Visible Samples:** 59

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 46 | 47 | inferred_complete_timeline |
| `Action_PreSnap` | 52 | 63 | 12 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–63
- **Visible Samples:** 62

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 58 | 59 | inferred_complete_timeline |
| `Action_PreSnap` | 61 | 63 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–150
- **Visible Samples:** 151

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 150 | 151 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–150
- **Visible Samples:** 151

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 150 | 151 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–143
- **Visible Samples:** 144

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 143 | 144 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–150
- **Visible Samples:** 151

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 150 | 151 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–150
- **Visible Samples:** 151

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 150 | 151 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `1` | `1` | Position_Unknown | Team_Unknown | 0–150 | 151 | 1 | Undefined position; Undefined team |
| `22` | `22` | Position_Unknown | Team_Unknown | 46–150 | 76 | 3 | Undefined position; Undefined team |
| `23` | `23` | Position_Unknown | Team_Unknown | 79–87 | 9 | 1 | Undefined position; Undefined team |
| `24` | `24` | Position_Unknown | Team_Unknown | 94–150 | 57 | 1 | Undefined position; Undefined team |
| `25` | `25` | Position_Unknown | Team_Unknown | 105–150 | 31 | 4 | Undefined position; Undefined team |
| `26` | `27` | Position_Unknown | Team_Unknown | 111–143 | 30 | 2 | Undefined position; Undefined team |
| `27` | `28` | Position_Unknown | Team_Unknown | 125–150 | 26 | 1 | Undefined position; Undefined team |
| `28` | `29` | Position_Unknown | Team_Unknown | 127–150 | 23 | 2 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_PassBlock` and target `14` (2 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `19` (3 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `20` (5 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `21` (3 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `3` (actor_track_id `3`): `SAF1` position mapped to `defense` team
- ⚠️ Player track XML ID `11` (actor_track_id `11`): `SAF2` position mapped to `defense` team
- ⚠️ 8 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 8 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 16 |
| Missing visible bounding boxes during action | 61 |
| Track-related warning | 1 |
| Other | 2 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 82: Duplicate assignment for track ID '11' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Action_SnapReceive present in CSV, but paired Action_BallSnap is missing.
- ⚠️ Action 'Action_PreSnap' range [0-150] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-150] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-150] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-150] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-68] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [77-85] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [87-106] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-143] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-150] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-41] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [131-132] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [135-141] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [145-150] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-46] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [52-63] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_RunOutRoute' range [36-106] for track '9' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [115-150] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-150] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-150] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-58] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [61-63] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ThrowPass' range [79-80] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [30-47] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [52-67] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [30-64] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-64] for track '16' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [69-70] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-46] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [50-64] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [82-84] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-46] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [55-58] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [60-63] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [69-70] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [74-76] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [78-79] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [30-46] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [52-64] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [69-70] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [30-55] for track '20' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [57-58] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [61-63] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [92-95] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [99-150] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [30-46] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [51-63] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [69-70] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [46-64] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [93-120] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [122-150] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [79-87] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [94-150] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [105-121] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [123-128] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [139-140] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [145-150] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [111-124] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [128-143] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [125-150] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [127-131] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [133-150] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Player track '1' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '1' has undefined team_side. Will map to Team_Unknown.
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