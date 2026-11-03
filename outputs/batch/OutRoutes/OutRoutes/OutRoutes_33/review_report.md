# Play-Annotation-Generator Annotation Review — OutRoutes_33

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `OutRoutes_33`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Pass_OutRoutes`
- **Result:** `Result_Tackle`
- **Result Frame:** 239
- **Player Tracks:** 33
- **Ball Tracks:** 0
- **Action Segments:** 87
- **Validation Warnings:** 99
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 22
- **Exact Matches:** 5
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 5
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 62
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR4 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `7` | `Group` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LT | offense | `14` | `14` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RT | offense | `17` | `17` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RG | offense | `19` | `19` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | C | offense | `20` | `20` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LG | offense | `21` | `21` |
| ✅ EXACT | `Action_RunOutRoute` | WR4 | offense | `1` | `1` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `15` | `15` |
| ✅ EXACT | `Action_ThrowPass` | QB | offense | `15` | `15` |
| ✅ EXACT | `Action_SecureCatch` | WR4 | offense | `1` | `1` |
| ✅ EXACT | `Action_BallCarry` | WR4 | offense | `1` | `1` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `0` | `Group` | 0 | START | 0 | 150 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR4 | `1` | `Group` | 0 | START | 0 | 2 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `14` | `Group` | 0 | START | 0 | 1 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `15` | `Group` | 0 | START | 0 | 2 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `16` | `Group` | 0 | START | 0 | 9 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `17` | `Group` | 0 | START | 0 | 1 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `19` | `Group` | 0 | START | 0 | 1 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `2` | `Group` | 0 | START | 0 | 142 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `20` | `Group` | 0 | START | 0 | 1 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `21` | `Group` | 0 | START | 0 | 1 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `7` | `Group` | 0 | START | 0 | 150 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LT | `14` | `14` | 2 | START | 2 | 41 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RT | `17` | `17` | 2 | START | 2 | 86 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RG | `19` | `19` | 2 | START | 2 | 57 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | C | `20` | `20` | 2 | START | 2 | 52 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LG | `21` | `21` | 2 | START | 2 | 38 |
| ✅ EXACT | `Action_RunOutRoute` | WR4 | `1` | `1` | 3 | START | 3 | 74 |
| ✅ EXACT | `Action_SnapReceive` | QB | `15` | `15` | 3 | END | 3 | 3 |
| ✅ EXACT | `Action_ThrowPass` | QB | `15` | `15` | 36 | START | 36 | 49 |
| ✅ EXACT | `Action_SecureCatch` | WR4 | `1` | `1` | 75 | START | 75 | 86 |
| ✅ EXACT | `Action_BallCarry` | WR4 | `1` | `1` | 87 | START | 87 | 150 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–106
- **Visible Samples:** 87

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 2 | 3 | inferred_complete_timeline |
| `Action_SnapReceive` | 3 | 3 | 1 | inferred_complete_timeline |
| `Action_None` | 4 | 35 | 32 | inferred_complete_timeline |
| `Action_ThrowPass` | 36 | 49 | 14 | inferred_complete_timeline |
| `Action_None` | 50 | 81 | 32 | inferred_complete_timeline |
| `Action_None` | 102 | 106 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–83
- **Visible Samples:** 51

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 9 | 10 | inferred_complete_timeline |
| `Action_PreSnap` | 11 | 43 | 33 | inferred_complete_timeline |
| `Action_PreSnap` | 45 | 47 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 70 | 72 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 82 | 83 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–150
- **Visible Samples:** 151

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 150 | 151 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–142
- **Visible Samples:** 143

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 142 | 143 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `0`</summary>

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
<summary>WR4 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–150
- **Visible Samples:** 151

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 2 | 3 | inferred_complete_timeline |
| `Action_RunOutRoute` | 3 | 74 | 72 | inferred_complete_timeline |
| `Action_SecureCatch` | 75 | 86 | 12 | inferred_complete_timeline |
| `Action_BallCarry` | 87 | 150 | 64 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–150
- **Visible Samples:** 112

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_PassBlock` | 2 | 41 | 40 | inferred_complete_timeline |
| `Action_PassBlock` | 45 | 51 | 7 | inferred_complete_timeline |
| `Action_PassBlock` | 62 | 63 | 2 | inferred_complete_timeline |
| `Action_PassBlock` | 65 | 78 | 14 | inferred_complete_timeline |
| `Action_PassBlock` | 82 | 86 | 5 | inferred_complete_timeline |
| `Action_PassBlock` | 88 | 91 | 4 | inferred_complete_timeline |
| `Action_PassBlock` | 93 | 94 | 2 | inferred_complete_timeline |
| `Action_PassBlock` | 97 | 109 | 13 | inferred_complete_timeline |
| `Action_PassBlock` | 127 | 131 | 5 | inferred_complete_timeline |
| `Action_PassBlock` | 133 | 150 | 18 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `21`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–71
- **Visible Samples:** 52

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_PassBlock` | 2 | 38 | 37 | inferred_complete_timeline |
| `Action_PassBlock` | 40 | 41 | 2 | inferred_complete_timeline |
| `Action_PassBlock` | 47 | 54 | 8 | inferred_complete_timeline |
| `Action_PassBlock` | 69 | 71 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–73
- **Visible Samples:** 58

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_PassBlock` | 2 | 52 | 51 | inferred_complete_timeline |
| `Action_PassBlock` | 58 | 59 | 2 | inferred_complete_timeline |
| `Action_PassBlock` | 71 | 73 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–62
- **Visible Samples:** 60

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_PassBlock` | 2 | 57 | 56 | inferred_complete_timeline |
| `Action_PassBlock` | 61 | 62 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–106
- **Visible Samples:** 99

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_PassBlock` | 2 | 86 | 85 | inferred_complete_timeline |
| `Action_PassBlock` | 89 | 95 | 7 | inferred_complete_timeline |
| `Action_PassBlock` | 102 | 106 | 5 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `defense`
- **Visible Frames:** 0–52
- **Visible Samples:** 53

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 52 | 53 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–150
- **Visible Samples:** 139

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 22 | 23 | inferred_complete_timeline |
| `Action_PreSnap` | 28 | 57 | 30 | inferred_complete_timeline |
| `Action_PreSnap` | 59 | 92 | 34 | inferred_complete_timeline |
| `Action_PreSnap` | 97 | 99 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 102 | 150 | 49 | inferred_complete_timeline |

</details>

<details>
<summary>DT — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–52
- **Visible Samples:** 48

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 41 | 42 | inferred_complete_timeline |
| `Action_PreSnap` | 46 | 49 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 51 | 52 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–42
- **Visible Samples:** 39

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 36 | 37 | inferred_complete_timeline |
| `Action_PreSnap` | 41 | 42 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `10`</summary>

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
<summary>CB1 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–127
- **Visible Samples:** 128

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 127 | 128 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–150
- **Visible Samples:** 151

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 150 | 151 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–124
- **Visible Samples:** 125

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 124 | 125 | inferred_complete_timeline |

</details>

<details>
<summary>CB4 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–148
- **Visible Samples:** 149

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 148 | 149 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–150
- **Visible Samples:** 151

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 150 | 151 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–57
- **Visible Samples:** 58

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 57 | 58 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `22` | `25` | Position_Unknown | Team_Unknown | 34–35 | 2 | 1 | Undefined position; Undefined team |
| `23` | `26` | Position_Unknown | Team_Unknown | 48–51 | 4 | 1 | Undefined position; Undefined team |
| `24` | `27` | Position_Unknown | Team_Unknown | 48–150 | 74 | 4 | Undefined position; Undefined team |
| `25` | `28` | Position_Unknown | Team_Unknown | 62–74 | 13 | 1 | Undefined position; Undefined team |
| `26` | `31` | Position_Unknown | Team_Unknown | 78–150 | 26 | 8 | Undefined position; Undefined team |
| `27` | `33` | Position_Unknown | Team_Unknown | 81–111 | 23 | 2 | Undefined position; Undefined team |
| `28` | `35` | Position_Unknown | Team_Unknown | 94–150 | 40 | 3 | Undefined position; Undefined team |
| `29` | `36` | Position_Unknown | Team_Unknown | 102–150 | 49 | 1 | Undefined position; Undefined team |
| `30` | `37` | Position_Unknown | Team_Unknown | 113–150 | 38 | 1 | Undefined position; Undefined team |
| `31` | `40` | Position_Unknown | Team_Unknown | 143–150 | 8 | 1 | Undefined position; Undefined team |
| `32` | `41` | Position_Unknown | Team_Unknown | 146–150 | 5 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_PassBlock` and target `14` (10 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `17` (3 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `19` (2 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `20` (3 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `21` (4 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `12` (actor_track_id `12`): `SAF` position mapped to `defense` team
- ⚠️ Player track XML ID `13` (actor_track_id `13`): `SAF` position mapped to `defense` team
- ⚠️ 11 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 11 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 22 |
| Missing visible bounding boxes during action | 75 |
| Other | 2 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Action_SnapReceive present in CSV, but paired Action_BallSnap is missing.
- ⚠️ Action 'Action_PreSnap' range [0-150] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [87-150] for track '1' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-142] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-127] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-36] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [41-42] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-148] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-22] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [28-57] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [59-92] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [97-99] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [102-150] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-150] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-41] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [46-49] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [51-52] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-124] for track '9' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-150] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-150] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-150] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-57] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [2-41] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [45-51] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [62-63] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [65-78] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [82-86] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [88-91] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [93-94] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [97-109] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [127-131] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [133-150] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [50-81] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [102-106] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-9] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [11-43] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [45-47] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [70-72] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [82-83] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [2-86] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [89-95] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [102-106] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-52] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [2-57] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [61-62] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [2-52] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [58-59] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [71-73] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [2-38] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [40-41] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [47-54] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [69-71] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [34-35] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [48-51] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [48-49] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [75-76] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [78-87] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [91-150] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [62-74] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [78-80] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [83-84] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [88-89] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [92-93] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [99-107] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [130-133] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [145-146] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [149-150] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [81-95] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [104-111] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [94-108] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [121-123] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [129-150] for track '28' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [102-150] for track '29' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [113-150] for track '30' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [143-150] for track '31' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [146-150] for track '32' has 1 frames without a visible bounding box.
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

</details>