# Play-Annotation-Generator Annotation Review — WRSlowScreens_43

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `WRSlowScreens_43`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Pass_WRSlowScreens`
- **Result:** `Result_Tackle`
- **Result Frame:** 239
- **Player Tracks:** 34
- **Ball Tracks:** 0
- **Action Segments:** 92
- **Validation Warnings:** 94
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 22
- **Exact Matches:** 6
- **Group Expanded Events:** 10
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 5
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 71
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `21` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `14` | `14` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | C | offense | `14` | `14` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LT | offense | `17` | `17` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LG | offense | `18` | `18` |
| ✅ EXACT | `Action_PassBlock` | RT | offense | `19` | `19` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RG | offense | `21` | `21` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `12` | `12` |
| ✅ EXACT | `Action_ReleaseToScreen` | RT | offense | `19` | `19` |
| ✅ EXACT | `Action_TurnToQuarterback` | WR3 | offense | `20` | `20` |
| ✅ EXACT | `Action_ThrowScreenPass` | QB | offense | `12` | `12` |
| ⚠️ AMBIGUOUS MATCH | `Action_RunAfterCatch` | WR3 | offense | `20` | `20` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `1` | `Group` | 0 | START | 0 | 6 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `12` | `Group` | 0 | START | 0 | 6 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `14` | `Group` | 0 | START | 0 | 6 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `15` | `Group` | 0 | START | 0 | 6 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `16` | `Group` | 0 | START | 0 | 6 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `17` | `Group` | 0 | START | 0 | 9 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `18` | `Group` | 0 | START | 0 | 9 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `19` | `Group` | 0 | START | 0 | 9 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `20` | `Group` | 0 | START | 0 | 50 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `21` | `Group` | 0 | START | 0 | 9 |
| ✅ EXACT | `Action_BallSnap` | C | `14` | `14` | 7 | START | 7 | 19 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | C | `14` | `14` | 10 | START | 20 | 95 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LT | `17` | `17` | 10 | START | 10 | 32 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LG | `18` | `18` | 10 | START | 10 | 44 |
| ✅ EXACT | `Action_PassBlock` | RT | `19` | `19` | 10 | START | 10 | 41 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RG | `21` | `21` | 10 | START | 10 | 36 |
| ✅ EXACT | `Action_SnapReceive` | QB | `12` | `12` | 19 | END | 7 | 19 |
| ✅ EXACT | `Action_ReleaseToScreen` | RT | `19` | `19` | 42 | START | 42 | 210 |
| ✅ EXACT | `Action_TurnToQuarterback` | WR3 | `20` | `20` | 51 | START | 51 | 97 |
| ✅ EXACT | `Action_ThrowScreenPass` | QB | `12` | `12` | 68 | START | 68 | 78 |
| ⚠️ AMBIGUOUS MATCH | `Action_RunAfterCatch` | WR3 | `20` | `20` | 98 | START | 98 | 158 |

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
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 6 | 7 | inferred_complete_timeline |
| `Action_SnapReceive` | 7 | 19 | 13 | inferred_complete_timeline |
| `Action_None` | 20 | 67 | 48 | inferred_complete_timeline |
| `Action_ThrowScreenPass` | 68 | 78 | 11 | inferred_complete_timeline |
| `Action_None` | 79 | 210 | 132 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 6 | 7 | inferred_complete_timeline |
| `Action_None` | 7 | 210 | 204 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 6 | 7 | inferred_complete_timeline |
| `Action_None` | 7 | 210 | 204 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–162
- **Visible Samples:** 162

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 50 | 51 | inferred_complete_timeline |
| `Action_TurnToQuarterback` | 51 | 97 | 47 | inferred_complete_timeline |
| `Action_RunAfterCatch` | 98 | 158 | 61 | inferred_complete_timeline |
| `Action_RunAfterCatch` | 160 | 162 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–145
- **Visible Samples:** 142

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 6 | 7 | inferred_complete_timeline |
| `Action_None` | 7 | 137 | 131 | inferred_complete_timeline |
| `Action_None` | 141 | 142 | 2 | inferred_complete_timeline |
| `Action_None` | 144 | 145 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–107
- **Visible Samples:** 105

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 9 | 10 | inferred_complete_timeline |
| `Action_PassBlock` | 10 | 32 | 23 | inferred_complete_timeline |
| `Action_PassBlock` | 36 | 107 | 72 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 198

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 9 | 10 | inferred_complete_timeline |
| `Action_PassBlock` | 10 | 44 | 35 | inferred_complete_timeline |
| `Action_PassBlock` | 48 | 62 | 15 | inferred_complete_timeline |
| `Action_PassBlock` | 73 | 210 | 138 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 198

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 6 | 7 | inferred_complete_timeline |
| `Action_BallSnap` | 7 | 19 | 13 | inferred_complete_timeline |
| `Action_PassBlock` | 20 | 95 | 76 | inferred_complete_timeline |
| `Action_PassBlock` | 105 | 197 | 93 | inferred_complete_timeline |
| `Action_PassBlock` | 202 | 210 | 9 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `21`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 206

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 9 | 10 | inferred_complete_timeline |
| `Action_PassBlock` | 10 | 36 | 27 | inferred_complete_timeline |
| `Action_PassBlock` | 38 | 78 | 41 | inferred_complete_timeline |
| `Action_PassBlock` | 83 | 210 | 128 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 9 | 10 | inferred_complete_timeline |
| `Action_PassBlock` | 10 | 41 | 32 | inferred_complete_timeline |
| `Action_ReleaseToScreen` | 42 | 210 | 169 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 6 | 7 | inferred_complete_timeline |
| `Action_None` | 7 | 210 | 204 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 6 | 7 | inferred_complete_timeline |
| `Action_None` | 7 | 210 | 204 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 6 | 7 | inferred_complete_timeline |
| `Action_None` | 7 | 210 | 204 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 210

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 6 | 7 | inferred_complete_timeline |
| `Action_None` | 7 | 34 | 28 | inferred_complete_timeline |
| `Action_None` | 36 | 210 | 175 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 209

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 6 | 7 | inferred_complete_timeline |
| `Action_None` | 7 | 157 | 151 | inferred_complete_timeline |
| `Action_None` | 160 | 210 | 51 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–70
- **Visible Samples:** 71

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 6 | 7 | inferred_complete_timeline |
| `Action_None` | 7 | 70 | 64 | inferred_complete_timeline |

</details>

<details>
<summary>LB3 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 6 | 7 | inferred_complete_timeline |
| `Action_None` | 7 | 210 | 204 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 6 | 7 | inferred_complete_timeline |
| `Action_None` | 7 | 210 | 204 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 203

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 6 | 7 | inferred_complete_timeline |
| `Action_None` | 7 | 149 | 143 | inferred_complete_timeline |
| `Action_None` | 158 | 210 | 53 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 6 | 7 | inferred_complete_timeline |
| `Action_None` | 7 | 210 | 204 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 206

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 6 | 7 | inferred_complete_timeline |
| `Action_None` | 7 | 160 | 154 | inferred_complete_timeline |
| `Action_None` | 165 | 166 | 2 | inferred_complete_timeline |
| `Action_None` | 168 | 210 | 43 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `11` | `11` | Position_Unknown | Team_Unknown | 0–210 | 211 | 2 | Undefined position; Undefined team |
| `22` | `22` | Position_Unknown | Team_Unknown | 31–36 | 6 | 1 | Undefined position; Undefined team |
| `23` | `25` | Position_Unknown | Team_Unknown | 86–210 | 125 | 1 | Undefined position; Undefined team |
| `24` | `28` | Position_Unknown | Team_Unknown | 105–210 | 106 | 1 | Undefined position; Undefined team |
| `25` | `30` | Position_Unknown | Team_Unknown | 132–161 | 15 | 4 | Undefined position; Undefined team |
| `26` | `31` | Position_Unknown | Team_Unknown | 146–151 | 6 | 1 | Undefined position; Undefined team |
| `27` | `32` | Position_Unknown | Team_Unknown | 147–204 | 36 | 7 | Undefined position; Undefined team |
| `28` | `33` | Position_Unknown | Team_Unknown | 160–196 | 18 | 3 | Undefined position; Undefined team |
| `29` | `34` | Position_Unknown | Team_Unknown | 160–210 | 51 | 1 | Undefined position; Undefined team |
| `30` | `35` | Position_Unknown | Team_Unknown | 164–165 | 2 | 1 | Undefined position; Undefined team |
| `31` | `38` | Position_Unknown | Team_Unknown | 174–192 | 7 | 3 | Undefined position; Undefined team |
| `32` | `39` | Position_Unknown | Team_Unknown | 176–210 | 31 | 3 | Undefined position; Undefined team |
| `33` | `40` | Position_Unknown | Team_Unknown | 207–209 | 3 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_PassBlock` and target `14` (3 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `17` (2 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `18` (3 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `21` (3 segments found)
- ⚠️ Ambiguous match for action `Action_RunAfterCatch` and target `20` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `8` (actor_track_id `8`): `SAF` position mapped to `defense` team
- ⚠️ 13 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 13 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 26 |
| Missing visible bounding boxes during action | 64 |
| Track-related warning | 2 |
| Other | 2 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 36: Duplicate assignment for track ID '4' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Resolved action overlap for track '14' (C): higher_priority='Action_BallSnap' [7–19], lower_priority='Action_PassBlock' annotated_start=10, effective_Action_PassBlock_start=20.
- ⚠️ Action 'Action_None' range [7-210] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [7-210] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [7-210] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [7-210] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [7-70] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [7-34] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [36-210] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [7-157] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [160-210] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [7-210] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [7-160] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [165-166] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [168-210] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [7-210] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [7-210] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [7-210] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [79-210] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [7-149] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [158-210] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [20-95] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [105-197] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [202-210] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [7-210] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [7-137] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [141-142] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [144-145] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [10-32] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [36-107] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [10-44] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [48-62] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [73-210] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ReleaseToScreen' range [42-210] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunAfterCatch' range [98-158] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunAfterCatch' range [160-162] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [10-36] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [38-78] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [83-210] for track '21' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [31-36] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [86-210] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [105-210] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [132-134] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [146-147] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [151-158] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [160-161] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [146-151] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [147-149] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [156-170] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [173-174] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [177-183] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [192-195] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [199-200] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [202-204] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [160-165] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [184-186] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [188-196] for track '28' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [160-210] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [164-165] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [174-176] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [179-180] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [191-192] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [176-188] for track '32' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [191-202] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [205-210] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [207-209] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Player track '11' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '11' has undefined team_side. Will map to Team_Unknown.
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
- ⚠️ Play definition: no definition found for 'Play_Pass_WRSlowScreens'.

</details>