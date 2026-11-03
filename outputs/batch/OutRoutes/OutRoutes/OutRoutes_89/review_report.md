# Play-Annotation-Generator Annotation Review — OutRoutes_89

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `OutRoutes_89`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Pass_OutRoutes`
- **Result:** `Result_Tackle`
- **Result Frame:** 239
- **Player Tracks:** 32
- **Ball Tracks:** 0
- **Action Segments:** 69
- **Validation Warnings:** 63
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
- **Inferred Coverage Segments (Action_None):** 44
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR4 | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `8` | `Group` |
| ✅ EXACT | `Action_PassBlock` | C | offense | `18` | `18` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RT | offense | `19` | `19` |
| ✅ EXACT | `Action_PassBlock` | LG | offense | `20` | `20` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RG | offense | `21` | `21` |
| ✅ EXACT | `Action_PassBlock` | LT | offense | `8` | `8` |
| ✅ EXACT | `Action_RunOutRoute` | WR1 | offense | `0` | `0` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `17` | `17` |
| ✅ EXACT | `Action_ThrowPass` | QB | offense | `17` | `17` |
| ✅ EXACT | `Action_SecureCatch` | WR1 | offense | `0` | `0` |
| ✅ EXACT | `Action_BallCarry` | WR1 | offense | `0` | `0` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `0` | `Group` | 0 | START | 0 | 49 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `1` | `Group` | 0 | START | 0 | 239 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `13` | `Group` | 0 | START | 0 | 107 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR4 | `15` | `Group` | 0 | START | 0 | 239 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `16` | `Group` | 0 | START | 0 | 92 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `17` | `Group` | 0 | START | 0 | 49 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `18` | `Group` | 0 | START | 0 | 45 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `19` | `Group` | 0 | START | 0 | 45 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `20` | `Group` | 0 | START | 0 | 45 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `21` | `Group` | 0 | START | 0 | 45 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `8` | `Group` | 0 | START | 0 | 45 |
| ✅ EXACT | `Action_PassBlock` | C | `18` | `18` | 46 | START | 46 | 239 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RT | `19` | `19` | 46 | START | 46 | 79 |
| ✅ EXACT | `Action_PassBlock` | LG | `20` | `20` | 46 | START | 46 | 239 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RG | `21` | `21` | 46 | START | 46 | 59 |
| ✅ EXACT | `Action_PassBlock` | LT | `8` | `8` | 46 | START | 46 | 239 |
| ✅ EXACT | `Action_RunOutRoute` | WR1 | `0` | `0` | 50 | START | 50 | 129 |
| ✅ EXACT | `Action_SnapReceive` | QB | `17` | `17` | 50 | END | 50 | 50 |
| ✅ EXACT | `Action_ThrowPass` | QB | `17` | `17` | 82 | START | 82 | 97 |
| ✅ EXACT | `Action_SecureCatch` | WR1 | `0` | `0` | 130 | START | 130 | 139 |
| ✅ EXACT | `Action_BallCarry` | WR1 | `0` | `0` | 140 | START | 140 | 173 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 49 | 50 | inferred_complete_timeline |
| `Action_SnapReceive` | 50 | 50 | 1 | inferred_complete_timeline |
| `Action_None` | 51 | 81 | 31 | inferred_complete_timeline |
| `Action_ThrowPass` | 82 | 97 | 16 | inferred_complete_timeline |
| `Action_None` | 98 | 239 | 142 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–108
- **Visible Samples:** 95

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 92 | 93 | inferred_complete_timeline |
| `Action_PreSnap` | 107 | 108 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–173
- **Visible Samples:** 174

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 49 | 50 | inferred_complete_timeline |
| `Action_RunOutRoute` | 50 | 129 | 80 | inferred_complete_timeline |
| `Action_SecureCatch` | 130 | 139 | 10 | inferred_complete_timeline |
| `Action_BallCarry` | 140 | 173 | 34 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 226

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 107 | 108 | inferred_complete_timeline |
| `Action_PreSnap` | 111 | 116 | 6 | inferred_complete_timeline |
| `Action_PreSnap` | 123 | 137 | 15 | inferred_complete_timeline |
| `Action_PreSnap` | 143 | 239 | 97 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 239 | 240 | inferred_complete_timeline |

</details>

<details>
<summary>WR4 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 239 | 240 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 45 | 46 | inferred_complete_timeline |
| `Action_PassBlock` | 46 | 239 | 194 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 45 | 46 | inferred_complete_timeline |
| `Action_PassBlock` | 46 | 239 | 194 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 45 | 46 | inferred_complete_timeline |
| `Action_PassBlock` | 46 | 239 | 194 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `21`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 233

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 45 | 46 | inferred_complete_timeline |
| `Action_PassBlock` | 46 | 59 | 14 | inferred_complete_timeline |
| `Action_PassBlock` | 62 | 64 | 3 | inferred_complete_timeline |
| `Action_PassBlock` | 67 | 71 | 5 | inferred_complete_timeline |
| `Action_PassBlock` | 74 | 89 | 16 | inferred_complete_timeline |
| `Action_PassBlock` | 91 | 239 | 149 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 239

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 45 | 46 | inferred_complete_timeline |
| `Action_PassBlock` | 46 | 79 | 34 | inferred_complete_timeline |
| `Action_PassBlock` | 81 | 239 | 159 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE2 — actor_track_id `2`</summary>

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
<summary>DT1 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 239 | 240 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 234

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 110 | 111 | inferred_complete_timeline |
| `Action_PreSnap` | 117 | 239 | 123 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 239 | 240 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 239 | 240 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 239 | 240 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–91
- **Visible Samples:** 92

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 91 | 92 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `11`</summary>

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
<summary>CB4 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 239 | 240 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–238
- **Visible Samples:** 235

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 213 | 214 | inferred_complete_timeline |
| `Action_PreSnap` | 218 | 238 | 21 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `3` | `3` | Position_Unknown | Team_Unknown | 0–239 | 240 | 1 | Undefined position; Undefined team |
| `22` | `22` | Position_Unknown | Team_Unknown | 37–54 | 5 | 2 | Undefined position; Undefined team |
| `23` | `25` | Position_Unknown | Team_Unknown | 91–92 | 2 | 1 | Undefined position; Undefined team |
| `24` | `27` | Position_Unknown | Team_Unknown | 115–134 | 8 | 2 | Undefined position; Undefined team |
| `25` | `29` | Position_Unknown | Team_Unknown | 121–239 | 115 | 3 | Undefined position; Undefined team |
| `26` | `30` | Position_Unknown | Team_Unknown | 140–239 | 74 | 4 | Undefined position; Undefined team |
| `27` | `31` | Position_Unknown | Team_Unknown | 155–239 | 53 | 6 | Undefined position; Undefined team |
| `28` | `33` | Position_Unknown | Team_Unknown | 166–169 | 4 | 1 | Undefined position; Undefined team |
| `29` | `34` | Position_Unknown | Team_Unknown | 182–220 | 39 | 1 | Undefined position; Undefined team |
| `30` | `35` | Position_Unknown | Team_Unknown | 217–239 | 15 | 3 | Undefined position; Undefined team |
| `31` | `36` | Position_Unknown | Team_Unknown | 217–238 | 22 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_PassBlock` and target `19` (2 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `21` (5 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `14` (actor_track_id `14`): `SAF` position mapped to `defense` team
- ⚠️ 11 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 11 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 22 |
| Missing visible bounding boxes during action | 38 |
| Track-related warning | 1 |
| Other | 2 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 96: Duplicate assignment for track ID '2' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Action_SnapReceive present in CSV, but paired Action_BallSnap is missing.
- ⚠️ Action 'Action_BallCarry' range [140-173] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-110] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [117-239] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-239] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-91] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-107] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [111-116] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [123-137] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [143-239] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-213] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [218-238] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-92] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [107-108] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [46-79] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [46-59] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [62-64] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [67-71] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [74-89] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [37-38] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [52-54] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [91-92] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [115-120] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [133-134] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [121-126] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [128-142] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [140-143] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [153-154] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [156-202] for track '26' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [155-157] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [162-171] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [173-174] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [195-199] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [204-224] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [166-169] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [182-220] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [217-225] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [231-232] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [217-238] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Player track '3' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '3' has undefined team_side. Will map to Team_Unknown.
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

</details>