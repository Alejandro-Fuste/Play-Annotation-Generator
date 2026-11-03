# Play-Annotation-Generator Annotation Review — OutRoutes_7

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `OutRoutes_7`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Pass_OutRoutes`
- **Result:** `Result_Tackle`
- **Result Frame:** 239
- **Player Tracks:** 31
- **Ball Tracks:** 0
- **Action Segments:** 65
- **Validation Warnings:** 72
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 22
- **Exact Matches:** 7
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 3
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 42
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR4 | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `6` | `Group` |
| ✅ EXACT | `Action_PassBlock` | C | offense | `11` | `11` |
| ✅ EXACT | `Action_PassBlock` | RG | offense | `18` | `18` |
| ✅ EXACT | `Action_PassBlock` | RT | offense | `19` | `19` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LG | offense | `20` | `20` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LT | offense | `6` | `6` |
| ✅ EXACT | `Action_RunOutRoute` | WR3 | offense | `3` | `3` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `13` | `13` |
| ✅ EXACT | `Action_ThrowPass` | QB | offense | `13` | `13` |
| ✅ EXACT | `Action_SecureCatch` | WR1 | offense | `14` | `14` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | WR1 | offense | `14` | `14` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `11` | `Group` | 0 | START | 0 | 5 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `13` | `Group` | 0 | START | 0 | 8 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `14` | `Group` | 0 | START | 0 | 92 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `15` | `Group` | 0 | START | 0 | 180 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `18` | `Group` | 0 | START | 0 | 5 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `19` | `Group` | 0 | START | 0 | 5 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR4 | `2` | `Group` | 0 | START | 0 | 180 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `20` | `Group` | 0 | START | 0 | 5 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `3` | `Group` | 0 | START | 0 | 8 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `5` | `Group` | 0 | START | 0 | 55 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `6` | `Group` | 0 | START | 0 | 5 |
| ✅ EXACT | `Action_PassBlock` | C | `11` | `11` | 6 | START | 6 | 33 |
| ✅ EXACT | `Action_PassBlock` | RG | `18` | `18` | 6 | START | 6 | 180 |
| ✅ EXACT | `Action_PassBlock` | RT | `19` | `19` | 6 | START | 6 | 180 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LG | `20` | `20` | 6 | START | 6 | 20 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LT | `6` | `6` | 6 | START | 6 | 102 |
| ✅ EXACT | `Action_RunOutRoute` | WR3 | `3` | `3` | 9 | START | 9 | 14 |
| ✅ EXACT | `Action_SnapReceive` | QB | `13` | `13` | 9 | END | 9 | 9 |
| ✅ EXACT | `Action_ThrowPass` | QB | `13` | `13` | 63 | START | 63 | 70 |
| ✅ EXACT | `Action_SecureCatch` | WR1 | `14` | `14` | 93 | START | 93 | 100 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | WR1 | `14` | `14` | 101 | START | 101 | 147 |

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
- **Visible Frames:** 0–180
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 8 | 9 | inferred_complete_timeline |
| `Action_SnapReceive` | 9 | 9 | 1 | inferred_complete_timeline |
| `Action_None` | 10 | 62 | 53 | inferred_complete_timeline |
| `Action_ThrowPass` | 63 | 70 | 8 | inferred_complete_timeline |
| `Action_None` | 71 | 180 | 110 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–180
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 180 | 181 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–152
- **Visible Samples:** 151

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 92 | 93 | inferred_complete_timeline |
| `Action_SecureCatch` | 93 | 100 | 8 | inferred_complete_timeline |
| `Action_BallCarry` | 101 | 147 | 47 | inferred_complete_timeline |
| `Action_BallCarry` | 150 | 152 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–180
- **Visible Samples:** 170

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 55 | 56 | inferred_complete_timeline |
| `Action_PreSnap` | 58 | 59 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 69 | 180 | 112 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–180
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 8 | 9 | inferred_complete_timeline |
| `Action_RunOutRoute` | 9 | 14 | 6 | inferred_complete_timeline |
| `Action_None` | 15 | 180 | 166 | inferred_complete_timeline |

</details>

<details>
<summary>WR4 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–180
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 180 | 181 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–180
- **Visible Samples:** 179

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 5 | 6 | inferred_complete_timeline |
| `Action_PassBlock` | 6 | 102 | 97 | inferred_complete_timeline |
| `Action_PassBlock` | 104 | 131 | 28 | inferred_complete_timeline |
| `Action_PassBlock` | 133 | 180 | 48 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–180
- **Visible Samples:** 180

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 5 | 6 | inferred_complete_timeline |
| `Action_PassBlock` | 6 | 20 | 15 | inferred_complete_timeline |
| `Action_PassBlock` | 22 | 180 | 159 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–33
- **Visible Samples:** 34

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 5 | 6 | inferred_complete_timeline |
| `Action_PassBlock` | 6 | 33 | 28 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–180
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 5 | 6 | inferred_complete_timeline |
| `Action_PassBlock` | 6 | 180 | 175 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–180
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 5 | 6 | inferred_complete_timeline |
| `Action_PassBlock` | 6 | 180 | 175 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `21`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `21`
- **team_side:** `defense`
- **Visible Frames:** 0–180
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 180 | 181 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–180
- **Visible Samples:** 179

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 26 | 27 | inferred_complete_timeline |
| `Action_PreSnap` | 29 | 180 | 152 | inferred_complete_timeline |

</details>

<details>
<summary>DT — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–174
- **Visible Samples:** 152

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 39 | 40 | inferred_complete_timeline |
| `Action_PreSnap` | 60 | 69 | 10 | inferred_complete_timeline |
| `Action_PreSnap` | 73 | 174 | 102 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–156
- **Visible Samples:** 157

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 156 | 157 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 0–180
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 180 | 181 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `defense`
- **Visible Frames:** 0–180
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 180 | 181 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–180
- **Visible Samples:** 177

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 69 | 70 | inferred_complete_timeline |
| `Action_PreSnap` | 72 | 168 | 97 | inferred_complete_timeline |
| `Action_PreSnap` | 170 | 175 | 6 | inferred_complete_timeline |
| `Action_PreSnap` | 177 | 180 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–180
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 180 | 181 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–180
- **Visible Samples:** 177

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 82 | 83 | inferred_complete_timeline |
| `Action_PreSnap` | 87 | 180 | 94 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–180
- **Visible Samples:** 180

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 160 | 161 | inferred_complete_timeline |
| `Action_PreSnap` | 162 | 180 | 19 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–180
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 180 | 181 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `22` | `23` | Position_Unknown | Team_Unknown | 55–180 | 126 | 1 | Undefined position; Undefined team |
| `23` | `24` | Position_Unknown | Team_Unknown | 61–66 | 6 | 1 | Undefined position; Undefined team |
| `24` | `25` | Position_Unknown | Team_Unknown | 86–89 | 4 | 1 | Undefined position; Undefined team |
| `25` | `27` | Position_Unknown | Team_Unknown | 118–177 | 37 | 6 | Undefined position; Undefined team |
| `26` | `31` | Position_Unknown | Team_Unknown | 140–162 | 23 | 1 | Undefined position; Undefined team |
| `27` | `32` | Position_Unknown | Team_Unknown | 142–151 | 6 | 2 | Undefined position; Undefined team |
| `28` | `33` | Position_Unknown | Team_Unknown | 157–171 | 6 | 2 | Undefined position; Undefined team |
| `29` | `34` | Position_Unknown | Team_Unknown | 166–180 | 15 | 1 | Undefined position; Undefined team |
| `30` | `35` | Position_Unknown | Team_Unknown | 174–175 | 2 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_PassBlock` and target `20` (2 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `6` (3 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `14` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `10` (actor_track_id `10`): `SAF2` position mapped to `defense` team
- ⚠️ Player track XML ID `12` (actor_track_id `12`): `SAF` position mapped to `defense` team
- ⚠️ Player track XML ID `16` (actor_track_id `16`): `SAF1` position mapped to `defense` team
- ⚠️ 9 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 9 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 18 |
| Missing visible bounding boxes during action | 52 |
| Other | 2 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Action_SnapReceive present in CSV, but paired Action_BallSnap is missing.
- ⚠️ Action 'Action_PreSnap' range [0-180] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-39] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [60-69] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [73-174] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-180] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [15-180] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-69] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [72-168] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [170-175] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [177-180] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-55] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [58-59] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [69-180] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [6-102] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [104-131] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [133-180] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-26] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [29-180] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-180] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-156] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-180] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [6-33] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-82] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [87-180] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [71-180] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [101-147] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [150-152] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-180] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-160] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [162-180] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-180] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [6-180] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [6-180] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [6-20] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [22-180] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-180] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [55-180] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [61-66] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [86-89] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [118-119] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [122-130] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [134-137] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [145-154] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [162-170] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [175-177] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [140-162] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [142-143] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [148-151] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [157-159] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [169-171] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [166-180] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [174-175] for track '30' has 1 frames without a visible bounding box.
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