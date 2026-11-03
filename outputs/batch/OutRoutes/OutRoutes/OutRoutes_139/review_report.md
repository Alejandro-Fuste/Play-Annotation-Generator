# Play-Annotation-Generator Annotation Review — OutRoutes_139

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `OutRoutes_139`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Pass_OutRoutes`
- **Result:** `Result_OutOfBounds`
- **Result Frame:** 239
- **Player Tracks:** 34
- **Ball Tracks:** 0
- **Action Segments:** 66
- **Validation Warnings:** 81
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 23
- **Exact Matches:** 9
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 2
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 39
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR5 | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR4 | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `5` | `Group` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LG | offense | `10` | `10` |
| ✅ EXACT | `Action_PassBlock` | RT | offense | `14` | `14` |
| ✅ EXACT | `Action_PassBlock` | LT | offense | `2` | `2` |
| ✅ EXACT | `Action_PassBlock` | C | offense | `20` | `20` |
| ✅ EXACT | `Action_PassBlock` | RG | offense | `21` | `21` |
| ⚠️ AMBIGUOUS MATCH | `Action_RunOutRoute` | WR3 | offense | `1` | `1` |
| ✅ EXACT | `Action_RunOutRoute` | WR2 | offense | `5` | `5` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `18` | `18` |
| ✅ EXACT | `Action_ThrowPass` | QB | offense | `18` | `18` |
| ✅ EXACT | `Action_SecureCatch` | WR2 | offense | `5` | `5` |
| ✅ EXACT | `Action_BallCarry` | WR2 | offense | `5` | `5` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR5 | `0` | `Group` | 0 | START | 0 | 180 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `1` | `Group` | 0 | START | 0 | 29 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `10` | `Group` | 0 | START | 0 | 19 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `14` | `Group` | 0 | START | 0 | 19 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `18` | `Group` | 0 | START | 0 | 26 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `2` | `Group` | 0 | START | 0 | 19 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `20` | `Group` | 0 | START | 0 | 19 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `21` | `Group` | 0 | START | 0 | 19 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `3` | `Group` | 0 | START | 0 | 105 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR4 | `4` | `Group` | 0 | START | 0 | 70 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `5` | `Group` | 0 | START | 0 | 29 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LG | `10` | `10` | 20 | START | 20 | 91 |
| ✅ EXACT | `Action_PassBlock` | RT | `14` | `14` | 20 | START | 20 | 180 |
| ✅ EXACT | `Action_PassBlock` | LT | `2` | `2` | 20 | START | 20 | 94 |
| ✅ EXACT | `Action_PassBlock` | C | `20` | `20` | 20 | START | 20 | 86 |
| ✅ EXACT | `Action_PassBlock` | RG | `21` | `21` | 20 | START | 20 | 180 |
| ⚠️ AMBIGUOUS MATCH | `Action_RunOutRoute` | WR3 | `1` | `1` | 30 | START | 30 | 125 |
| ✅ EXACT | `Action_RunOutRoute` | WR2 | `5` | `5` | 30 | START | 30 | 98 |
| ✅ EXACT | `Action_SnapReceive` | QB | `18` | `18` | 30 | END | 30 | 30 |
| ✅ EXACT | `Action_ThrowPass` | QB | `18` | `18` | 71 | START | 71 | 80 |
| ✅ EXACT | `Action_SecureCatch` | WR2 | `5` | `5` | 99 | START | 99 | 109 |
| ✅ EXACT | `Action_BallCarry` | WR2 | `5` | `5` | 110 | START | 110 | 131 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–107
- **Visible Samples:** 105

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 26 | 27 | inferred_complete_timeline |
| `Action_SnapReceive` | 30 | 30 | 1 | inferred_complete_timeline |
| `Action_None` | 31 | 70 | 40 | inferred_complete_timeline |
| `Action_ThrowPass` | 71 | 80 | 10 | inferred_complete_timeline |
| `Action_None` | 81 | 107 | 27 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–132
- **Visible Samples:** 125

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 105 | 106 | inferred_complete_timeline |
| `Action_PreSnap` | 114 | 132 | 19 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–131
- **Visible Samples:** 132

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 29 | 30 | inferred_complete_timeline |
| `Action_RunOutRoute` | 30 | 98 | 69 | inferred_complete_timeline |
| `Action_SecureCatch` | 99 | 109 | 11 | inferred_complete_timeline |
| `Action_BallCarry` | 110 | 131 | 22 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–161
- **Visible Samples:** 139

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 29 | 30 | inferred_complete_timeline |
| `Action_RunOutRoute` | 30 | 125 | 96 | inferred_complete_timeline |
| `Action_RunOutRoute` | 129 | 131 | 3 | inferred_complete_timeline |
| `Action_RunOutRoute` | 135 | 136 | 2 | inferred_complete_timeline |
| `Action_RunOutRoute` | 153 | 155 | 3 | inferred_complete_timeline |
| `Action_RunOutRoute` | 157 | 161 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>WR4 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–180
- **Visible Samples:** 173

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 70 | 71 | inferred_complete_timeline |
| `Action_PreSnap` | 76 | 99 | 24 | inferred_complete_timeline |
| `Action_PreSnap` | 101 | 102 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 104 | 105 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 107 | 180 | 74 | inferred_complete_timeline |

</details>

<details>
<summary>WR5 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–180
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 180 | 181 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–94
- **Visible Samples:** 95

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 19 | 20 | inferred_complete_timeline |
| `Action_PassBlock` | 20 | 94 | 75 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–180
- **Visible Samples:** 176

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 19 | 20 | inferred_complete_timeline |
| `Action_PassBlock` | 20 | 91 | 72 | inferred_complete_timeline |
| `Action_PassBlock` | 97 | 180 | 84 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–86
- **Visible Samples:** 87

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 19 | 20 | inferred_complete_timeline |
| `Action_PassBlock` | 20 | 86 | 67 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `21`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–180
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 19 | 20 | inferred_complete_timeline |
| `Action_PassBlock` | 20 | 180 | 161 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–180
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 19 | 20 | inferred_complete_timeline |
| `Action_PassBlock` | 20 | 180 | 161 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–180
- **Visible Samples:** 176

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 49 | 50 | inferred_complete_timeline |
| `Action_PreSnap` | 55 | 180 | 126 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `defense`
- **Visible Frames:** 0–180
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 180 | 181 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–92
- **Visible Samples:** 87

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 37 | 38 | inferred_complete_timeline |
| `Action_PreSnap` | 40 | 49 | 10 | inferred_complete_timeline |
| `Action_PreSnap` | 53 | 64 | 12 | inferred_complete_timeline |
| `Action_PreSnap` | 66 | 92 | 27 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–180
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 180 | 181 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–153
- **Visible Samples:** 154

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 153 | 154 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–180
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 180 | 181 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 0–148
- **Visible Samples:** 145

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 140 | 141 | inferred_complete_timeline |
| `Action_PreSnap` | 145 | 148 | 4 | inferred_complete_timeline |

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
<summary>CB3 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–180
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 180 | 181 | inferred_complete_timeline |

</details>

<details>
<summary>CB4 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–166
- **Visible Samples:** 164

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 158 | 159 | inferred_complete_timeline |
| `Action_PreSnap` | 162 | 166 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–180
- **Visible Samples:** 164

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 137 | 138 | inferred_complete_timeline |
| `Action_PreSnap` | 155 | 180 | 26 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `22` | `23` | Position_Unknown | Team_Unknown | 61–62 | 2 | 1 | Undefined position; Undefined team |
| `23` | `24` | Position_Unknown | Team_Unknown | 61–62 | 2 | 1 | Undefined position; Undefined team |
| `24` | `26` | Position_Unknown | Team_Unknown | 74–84 | 11 | 1 | Undefined position; Undefined team |
| `25` | `30` | Position_Unknown | Team_Unknown | 83–180 | 91 | 2 | Undefined position; Undefined team |
| `26` | `31` | Position_Unknown | Team_Unknown | 84–180 | 92 | 2 | Undefined position; Undefined team |
| `27` | `32` | Position_Unknown | Team_Unknown | 92–107 | 16 | 1 | Undefined position; Undefined team |
| `28` | `33` | Position_Unknown | Team_Unknown | 93–99 | 7 | 1 | Undefined position; Undefined team |
| `29` | `35` | Position_Unknown | Team_Unknown | 101–180 | 80 | 1 | Undefined position; Undefined team |
| `30` | `37` | Position_Unknown | Team_Unknown | 104–180 | 77 | 1 | Undefined position; Undefined team |
| `31` | `38` | Position_Unknown | Team_Unknown | 107–108 | 2 | 1 | Undefined position; Undefined team |
| `32` | `41` | Position_Unknown | Team_Unknown | 140–142 | 3 | 1 | Undefined position; Undefined team |
| `33` | `42` | Position_Unknown | Team_Unknown | 146–153 | 8 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_PassBlock` and target `10` (2 segments found)
- ⚠️ Ambiguous match for action `Action_RunOutRoute` and target `1` (5 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `13` (actor_track_id `13`): `SAF` position mapped to `defense` team
- ⚠️ 12 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 12 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 24 |
| Missing visible bounding boxes during action | 55 |
| Other | 2 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Action_SnapReceive present in CSV, but paired Action_BallSnap is missing.
- ⚠️ Action 'Action_PreSnap' range [0-180] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunOutRoute' range [30-125] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_RunOutRoute' range [129-131] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunOutRoute' range [135-136] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunOutRoute' range [153-155] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunOutRoute' range [157-161] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [20-94] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-105] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [114-132] for track '3' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-70] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [76-99] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [101-102] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [104-105] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [107-180] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunOutRoute' range [30-98] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [110-131] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-180] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-180] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-153] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-180] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [20-91] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [97-180] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-158] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [162-166] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-49] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [55-180] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-137] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [155-180] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [20-180] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-37] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [40-49] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [53-64] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [66-92] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-180] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-140] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [145-148] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-26] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [81-107] for track '18' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-180] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [20-86] for track '20' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [20-180] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [61-62] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [61-62] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [74-84] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [83-110] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [118-180] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [84-85] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [91-180] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [92-107] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [93-99] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [101-180] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [104-180] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [107-108] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [140-142] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [146-153] for track '33' has 1 frames without a visible bounding box.
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

</details>