# Play-Annotation-Generator Annotation Review — OutRoutes_97

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `OutRoutes_97`
- **Frame Range:** 0 to 269 (270 total frames)
- **Play:** `Play_Pass_OutRoutes`
- **Result:** `Result_Tackle`
- **Result Frame:** 269
- **Player Tracks:** 38
- **Ball Tracks:** 0
- **Action Segments:** 89
- **Validation Warnings:** 95
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
- **Inferred Coverage Segments (Action_None):** 66
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `8` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `9` | `Group` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | C | offense | `16` | `16` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RG | offense | `17` | `17` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LG | offense | `18` | `18` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RT | offense | `21` | `21` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LT | offense | `8` | `8` |
| ✅ EXACT | `Action_RunOutRoute` | WR2 | offense | `9` | `9` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `15` | `15` |
| ✅ EXACT | `Action_ThrowPass` | QB | offense | `15` | `15` |
| ✅ EXACT | `Action_SecureCatch` | WR2 | offense | `9` | `9` |
| ✅ EXACT | `Action_BallCarry` | WR2 | offense | `9` | `9` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `13` | `Group` | 0 | START | 0 | 128 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `15` | `Group` | 0 | START | 0 | 35 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `16` | `Group` | 0 | START | 0 | 29 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `17` | `Group` | 0 | START | 0 | 29 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `18` | `Group` | 0 | START | 0 | 29 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | `19` | `Group` | 0 | START | 0 | 63 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | `20` | `Group` | 0 | START | 0 | 42 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `21` | `Group` | 0 | START | 2 | 24 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `3` | `Group` | 0 | START | 0 | 269 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `8` | `Group` | 0 | START | 0 | 29 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `9` | `Group` | 0 | START | 0 | 35 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | C | `16` | `16` | 30 | START | 30 | 45 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RG | `17` | `17` | 30 | START | 30 | 32 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LG | `18` | `18` | 30 | START | 30 | 56 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RT | `21` | `21` | 30 | START | 35 | 40 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LT | `8` | `8` | 30 | START | 30 | 56 |
| ✅ EXACT | `Action_RunOutRoute` | WR2 | `9` | `9` | 36 | START | 36 | 115 |
| ✅ EXACT | `Action_SnapReceive` | QB | `15` | `15` | 36 | END | 36 | 36 |
| ✅ EXACT | `Action_ThrowPass` | QB | `15` | `15` | 76 | START | 76 | 84 |
| ✅ EXACT | `Action_SecureCatch` | WR2 | `9` | `9` | 116 | START | 116 | 127 |
| ✅ EXACT | `Action_BallCarry` | WR2 | `9` | `9` | 128 | START | 128 | 263 |

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
- **Visible Frames:** 0–173
- **Visible Samples:** 106

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 35 | 36 | inferred_complete_timeline |
| `Action_SnapReceive` | 36 | 36 | 1 | inferred_complete_timeline |
| `Action_None` | 37 | 75 | 39 | inferred_complete_timeline |
| `Action_ThrowPass` | 76 | 84 | 9 | inferred_complete_timeline |
| `Action_None` | 85 | 98 | 14 | inferred_complete_timeline |
| `Action_None` | 167 | 173 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–128
- **Visible Samples:** 129

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 128 | 129 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 269 | 270 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–263
- **Visible Samples:** 264

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 35 | 36 | inferred_complete_timeline |
| `Action_RunOutRoute` | 36 | 115 | 80 | inferred_complete_timeline |
| `Action_SecureCatch` | 116 | 127 | 12 | inferred_complete_timeline |
| `Action_BallCarry` | 128 | 263 | 136 | inferred_complete_timeline |

</details>

<details>
<summary>TE1 — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 269

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 63 | 64 | inferred_complete_timeline |
| `Action_PreSnap` | 65 | 269 | 205 | inferred_complete_timeline |

</details>

<details>
<summary>TE2 — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–134
- **Visible Samples:** 45

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 42 | 43 | inferred_complete_timeline |
| `Action_PreSnap` | 133 | 134 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 259

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 29 | 30 | inferred_complete_timeline |
| `Action_PassBlock` | 30 | 56 | 27 | inferred_complete_timeline |
| `Action_PassBlock` | 60 | 62 | 3 | inferred_complete_timeline |
| `Action_PassBlock` | 68 | 78 | 11 | inferred_complete_timeline |
| `Action_PassBlock` | 80 | 81 | 2 | inferred_complete_timeline |
| `Action_PassBlock` | 83 | 113 | 31 | inferred_complete_timeline |
| `Action_PassBlock` | 115 | 269 | 155 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 256

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 29 | 30 | inferred_complete_timeline |
| `Action_PassBlock` | 30 | 56 | 27 | inferred_complete_timeline |
| `Action_PassBlock` | 63 | 67 | 5 | inferred_complete_timeline |
| `Action_PassBlock` | 76 | 269 | 194 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 267

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 29 | 30 | inferred_complete_timeline |
| `Action_PassBlock` | 30 | 45 | 16 | inferred_complete_timeline |
| `Action_PassBlock` | 47 | 49 | 3 | inferred_complete_timeline |
| `Action_PassBlock` | 51 | 53 | 3 | inferred_complete_timeline |
| `Action_PassBlock` | 55 | 269 | 215 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–92
- **Visible Samples:** 71

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 29 | 30 | inferred_complete_timeline |
| `Action_PassBlock` | 30 | 32 | 3 | inferred_complete_timeline |
| `Action_PassBlock` | 50 | 84 | 35 | inferred_complete_timeline |
| `Action_PassBlock` | 90 | 92 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `21`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 2–72
- **Visible Samples:** 35

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 2 | 24 | 23 | inferred_complete_timeline |
| `Action_PassBlock` | 35 | 40 | 6 | inferred_complete_timeline |
| `Action_PassBlock` | 67 | 72 | 6 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 269

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 106 | 107 | inferred_complete_timeline |
| `Action_PreSnap` | 108 | 269 | 162 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–91
- **Visible Samples:** 86

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 68 | 69 | inferred_complete_timeline |
| `Action_PreSnap` | 72 | 78 | 7 | inferred_complete_timeline |
| `Action_PreSnap` | 82 | 91 | 10 | inferred_complete_timeline |

</details>

<details>
<summary>DT — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–82
- **Visible Samples:** 81

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 56 | 57 | inferred_complete_timeline |
| `Action_PreSnap` | 59 | 82 | 24 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 269 | 270 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 269 | 270 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `defense`
- **Visible Frames:** 0–174
- **Visible Samples:** 175

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 174 | 175 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 269 | 270 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–263
- **Visible Samples:** 264

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 263 | 264 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 269 | 270 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 269 | 270 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `7` | `7` | Position_Unknown | Team_Unknown | 0–59 | 60 | 1 | Undefined position; Undefined team |
| `22` | `22` | Position_Unknown | Team_Unknown | 7–269 | 207 | 6 | Undefined position; Undefined team |
| `23` | `23` | Position_Unknown | Team_Unknown | 66–269 | 201 | 2 | Undefined position; Undefined team |
| `24` | `24` | Position_Unknown | Team_Unknown | 77–269 | 191 | 3 | Undefined position; Undefined team |
| `25` | `25` | Position_Unknown | Team_Unknown | 81–108 | 28 | 1 | Undefined position; Undefined team |
| `26` | `27` | Position_Unknown | Team_Unknown | 105–269 | 139 | 3 | Undefined position; Undefined team |
| `27` | `28` | Position_Unknown | Team_Unknown | 109–269 | 161 | 1 | Undefined position; Undefined team |
| `28` | `29` | Position_Unknown | Team_Unknown | 109–259 | 151 | 1 | Undefined position; Undefined team |
| `29` | `31` | Position_Unknown | Team_Unknown | 114–269 | 156 | 1 | Undefined position; Undefined team |
| `30` | `32` | Position_Unknown | Team_Unknown | 121–269 | 148 | 2 | Undefined position; Undefined team |
| `31` | `33` | Position_Unknown | Team_Unknown | 127–128 | 2 | 1 | Undefined position; Undefined team |
| `32` | `36` | Position_Unknown | Team_Unknown | 163–185 | 14 | 3 | Undefined position; Undefined team |
| `33` | `37` | Position_Unknown | Team_Unknown | 171–201 | 22 | 4 | Undefined position; Undefined team |
| `34` | `38` | Position_Unknown | Team_Unknown | 183–269 | 85 | 2 | Undefined position; Undefined team |
| `35` | `40` | Position_Unknown | Team_Unknown | 231–263 | 12 | 3 | Undefined position; Undefined team |
| `36` | `41` | Position_Unknown | Team_Unknown | 254–269 | 16 | 1 | Undefined position; Undefined team |
| `37` | `43` | Position_Unknown | Team_Unknown | 258–269 | 12 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_PassBlock` and target `16` (4 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `17` (3 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `18` (3 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `21` (2 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `8` (6 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `1` (actor_track_id `1`): `SAF` position mapped to `defense` team
- ⚠️ Player track XML ID `10` (actor_track_id `10`): `SAF1` position mapped to `defense` team
- ⚠️ Player track XML ID `11` (actor_track_id `11`): `SAF2` position mapped to `defense` team
- ⚠️ 17 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 17 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 34 |
| Missing visible bounding boxes during action | 59 |
| Other | 2 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 269 as fallback play end.
- ⚠️ Action_SnapReceive present in CSV, but paired Action_BallSnap is missing.
- ⚠️ Action 'Action_PreSnap' range [0-174] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-263] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-106] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-59] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [30-56] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [60-62] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [68-78] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [80-81] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [83-113] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [128-263] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-56] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [59-82] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-128] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-68] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [72-78] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [82-91] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [85-98] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [167-173] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [30-45] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [47-49] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [51-53] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [30-32] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [50-84] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [90-92] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [30-56] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [63-67] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-63] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [65-269] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-42] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [133-134] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [2-24] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [35-40] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [67-72] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [7-8] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [39-78] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [82-84] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [86-157] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [177-182] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [186-269] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [66-68] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [77-96] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [98-129] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [81-108] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [105-108] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [131-133] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [109-259] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [121-122] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [127-128] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [163-170] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [176-179] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [184-185] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [171-182] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [188-189] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [192-196] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [199-201] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [183-198] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [231-234] for track '35' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [253-257] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [261-263] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Player track '7' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '7' has undefined team_side. Will map to Team_Unknown.
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

</details>