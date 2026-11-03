# Play-Annotation-Generator Annotation Review — OutRoutes_31

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `OutRoutes_31`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Pass_OutRoutes`
- **Result:** `Result_OutOfBounds`
- **Result Frame:** 239
- **Player Tracks:** 31
- **Ball Tracks:** 0
- **Action Segments:** 68
- **Validation Warnings:** 58
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 22
- **Exact Matches:** 8
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 2
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 46
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `9` | `Group` |
| ✅ EXACT | `Action_PassBlock` | LT | offense | `10` | `10` |
| ✅ EXACT | `Action_PassBlock` | RT | offense | `16` | `16` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RG | offense | `17` | `17` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LG | offense | `20` | `20` |
| ✅ EXACT | `Action_PassBlock` | C | offense | `21` | `21` |
| ✅ EXACT | `Action_RunOutRoute` | WR1 | offense | `1` | `1` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `7` | `7` |
| ✅ EXACT | `Action_ThrowPass` | RB | offense | `9` | `9` |
| ✅ EXACT | `Action_SecureCatch` | WR1 | offense | `1` | `1` |
| ✅ EXACT | `Action_BallCarry` | WR1 | offense | `1` | `1` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `1` | `Group` | 0 | START | 0 | 13 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `10` | `Group` | 0 | START | 0 | 10 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `16` | `Group` | 0 | START | 0 | 10 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `17` | `Group` | 0 | START | 0 | 10 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `18` | `Group` | 0 | START | 0 | 239 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `19` | `Group` | 0 | START | 0 | 33 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `20` | `Group` | 0 | START | 0 | 10 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `21` | `Group` | 0 | START | 0 | 10 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `4` | `Group` | 0 | START | 0 | 239 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `7` | `Group` | 0 | START | 0 | 13 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `9` | `Group` | 0 | START | 0 | 85 |
| ✅ EXACT | `Action_PassBlock` | LT | `10` | `10` | 11 | START | 11 | 239 |
| ✅ EXACT | `Action_PassBlock` | RT | `16` | `16` | 11 | START | 11 | 70 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RG | `17` | `17` | 11 | START | 11 | 78 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LG | `20` | `20` | 11 | START | 11 | 229 |
| ✅ EXACT | `Action_PassBlock` | C | `21` | `21` | 11 | START | 11 | 239 |
| ✅ EXACT | `Action_RunOutRoute` | WR1 | `1` | `1` | 14 | START | 14 | 128 |
| ✅ EXACT | `Action_SnapReceive` | QB | `7` | `7` | 14 | END | 14 | 14 |
| ✅ EXACT | `Action_ThrowPass` | RB | `9` | `9` | 86 | START | 86 | 93 |
| ✅ EXACT | `Action_SecureCatch` | WR1 | `1` | `1` | 129 | START | 129 | 137 |
| ✅ EXACT | `Action_BallCarry` | WR1 | `1` | `1` | 138 | START | 138 | 229 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–124
- **Visible Samples:** 124

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 13 | 14 | inferred_complete_timeline |
| `Action_SnapReceive` | 14 | 14 | 1 | inferred_complete_timeline |
| `Action_None` | 15 | 111 | 97 | inferred_complete_timeline |
| `Action_None` | 113 | 124 | 12 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–123
- **Visible Samples:** 124

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 85 | 86 | inferred_complete_timeline |
| `Action_ThrowPass` | 86 | 93 | 8 | inferred_complete_timeline |
| `Action_None` | 94 | 123 | 30 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–229
- **Visible Samples:** 230

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 13 | 14 | inferred_complete_timeline |
| `Action_RunOutRoute` | 14 | 128 | 115 | inferred_complete_timeline |
| `Action_SecureCatch` | 129 | 137 | 9 | inferred_complete_timeline |
| `Action_BallCarry` | 138 | 229 | 92 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 239 | 240 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 239 | 240 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 239

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 33 | 34 | inferred_complete_timeline |
| `Action_PreSnap` | 35 | 239 | 205 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 10 | 11 | inferred_complete_timeline |
| `Action_PassBlock` | 11 | 239 | 229 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 234

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 10 | 11 | inferred_complete_timeline |
| `Action_PassBlock` | 11 | 229 | 219 | inferred_complete_timeline |
| `Action_PassBlock` | 232 | 233 | 2 | inferred_complete_timeline |
| `Action_PassBlock` | 238 | 239 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `21`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 10 | 11 | inferred_complete_timeline |
| `Action_PassBlock` | 11 | 239 | 229 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 235

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 10 | 11 | inferred_complete_timeline |
| `Action_PassBlock` | 11 | 78 | 68 | inferred_complete_timeline |
| `Action_PassBlock` | 82 | 119 | 38 | inferred_complete_timeline |
| `Action_PassBlock` | 122 | 239 | 118 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–70
- **Visible Samples:** 71

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 10 | 11 | inferred_complete_timeline |
| `Action_PassBlock` | 11 | 70 | 60 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 239 | 240 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 234

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 225 | 226 | inferred_complete_timeline |
| `Action_PreSnap` | 232 | 239 | 8 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 229

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 72 | 73 | inferred_complete_timeline |
| `Action_PreSnap` | 76 | 153 | 78 | inferred_complete_timeline |
| `Action_PreSnap` | 155 | 229 | 75 | inferred_complete_timeline |
| `Action_PreSnap` | 237 | 239 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 236

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 95 | 96 | inferred_complete_timeline |
| `Action_PreSnap` | 99 | 100 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 102 | 239 | 138 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 239 | 240 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 230

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 67 | 68 | inferred_complete_timeline |
| `Action_PreSnap` | 70 | 75 | 6 | inferred_complete_timeline |
| `Action_PreSnap` | 80 | 93 | 14 | inferred_complete_timeline |
| `Action_PreSnap` | 95 | 137 | 43 | inferred_complete_timeline |
| `Action_PreSnap` | 141 | 239 | 99 | inferred_complete_timeline |

</details>

<details>
<summary>OLB — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 239 | 240 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–81
- **Visible Samples:** 82

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 81 | 82 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 239 | 240 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `defense`
- **Visible Frames:** 0–98
- **Visible Samples:** 99

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 98 | 99 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–52
- **Visible Samples:** 53

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 52 | 53 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `22` | `22` | Position_Unknown | Team_Unknown | 59–239 | 181 | 1 | Undefined position; Undefined team |
| `23` | `23` | Position_Unknown | Team_Unknown | 85–90 | 6 | 1 | Undefined position; Undefined team |
| `24` | `24` | Position_Unknown | Team_Unknown | 88–239 | 152 | 1 | Undefined position; Undefined team |
| `25` | `25` | Position_Unknown | Team_Unknown | 112–113 | 2 | 1 | Undefined position; Undefined team |
| `26` | `26` | Position_Unknown | Team_Unknown | 116–239 | 120 | 3 | Undefined position; Undefined team |
| `27` | `27` | Position_Unknown | Team_Unknown | 119–217 | 84 | 4 | Undefined position; Undefined team |
| `28` | `30` | Position_Unknown | Team_Unknown | 145–239 | 95 | 1 | Undefined position; Undefined team |
| `29` | `31` | Position_Unknown | Team_Unknown | 148–239 | 92 | 1 | Undefined position; Undefined team |
| `30` | `32` | Position_Unknown | Team_Unknown | 152–237 | 15 | 5 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_PassBlock` and target `17` (3 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `20` (3 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `0` (actor_track_id `0`): `SAF1` position mapped to `defense` team
- ⚠️ Player track XML ID `8` (actor_track_id `8`): `SAF2` position mapped to `defense` team
- ⚠️ 9 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 9 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 18 |
| Missing visible bounding boxes during action | 37 |
| Track-related warning | 1 |
| Other | 2 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 38: Duplicate assignment for track ID '13' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Action_SnapReceive present in CSV, but paired Action_BallSnap is missing.
- ⚠️ Action 'Action_PreSnap' range [0-98] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [138-229] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-225] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-81] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [15-111] for track '7' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [113-124] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-52] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [94-123] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-67] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [70-75] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [80-93] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [95-137] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [141-239] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-72] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [76-153] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [155-229] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-95] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [99-100] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [11-70] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [11-78] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [82-119] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-33] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [11-229] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [232-233] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [85-90] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [112-113] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [116-149] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [153-187] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [119-187] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [193-200] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [206-210] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [216-217] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [152-157] for track '30' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [221-222] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [225-226] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [231-232] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [235-237] for track '30' has 1 frames without a visible bounding box.
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