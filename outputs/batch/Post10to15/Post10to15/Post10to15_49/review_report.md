# Play-Annotation-Generator Annotation Review — Post10to15_49

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Post10to15_49`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Pass_Post10to15`
- **Result:** `Result_Tackle`
- **Result Frame:** 239
- **Player Tracks:** 31
- **Ball Tracks:** 0
- **Action Segments:** 85
- **Validation Warnings:** 79
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 21
- **Exact Matches:** 5
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 4
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 65
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `4` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `20` | `20` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LT | offense | `13` | `13` |
| ✅ EXACT | `Action_PassBlock` | RT | offense | `16` | `16` |
| ✅ EXACT | `Action_PassBlock` | RG | offense | `18` | `18` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | C | offense | `20` | `20` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LG | offense | `21` | `21` |
| ⚠️ AMBIGUOUS MATCH | `Action_RunPostRoute` | WR1 | offense | `0` | `0` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `19` | `19` |
| ✅ EXACT | `Action_ThrowPass` | QB | offense | `19` | `19` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `0` | `Group` | 0 | START | 0 | 13 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `13` | `Group` | 0 | START | 0 | 3 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `14` | `Group` | 0 | START | 0 | 0 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `15` | `Group` | 0 | START | 0 | 0 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `16` | `Group` | 0 | START | 0 | 3 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `17` | `Group` | 0 | START | 0 | 0 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `18` | `Group` | 0 | START | 0 | 3 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `19` | `Group` | 0 | START | 0 | 0 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `20` | `Group` | 0 | START | 0 | 0 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `21` | `Group` | 0 | START | 0 | 3 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `4` | `Group` | 0 | START | 0 | 0 |
| ✅ EXACT | `Action_BallSnap` | C | `20` | `20` | 1 | START | 1 | 14 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LT | `13` | `13` | 4 | START | 4 | 55 |
| ✅ EXACT | `Action_PassBlock` | RT | `16` | `16` | 4 | START | 4 | 180 |
| ✅ EXACT | `Action_PassBlock` | RG | `18` | `18` | 4 | START | 4 | 180 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | C | `20` | `20` | 4 | START | 15 | 84 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LG | `21` | `21` | 4 | START | 4 | 41 |
| ⚠️ AMBIGUOUS MATCH | `Action_RunPostRoute` | WR1 | `0` | `0` | 14 | START | 14 | 124 |
| ✅ EXACT | `Action_SnapReceive` | QB | `19` | `19` | 14 | END | 1 | 14 |
| ✅ EXACT | `Action_ThrowPass` | QB | `19` | `19` | 68 | START | 68 | 78 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–180
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_SnapReceive` | 1 | 14 | 14 | inferred_complete_timeline |
| `Action_None` | 15 | 67 | 53 | inferred_complete_timeline |
| `Action_ThrowPass` | 68 | 78 | 11 | inferred_complete_timeline |
| `Action_None` | 79 | 180 | 102 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–180
- **Visible Samples:** 177

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 27 | 27 | inferred_complete_timeline |
| `Action_None` | 32 | 180 | 149 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–180
- **Visible Samples:** 180

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 13 | 14 | inferred_complete_timeline |
| `Action_RunPostRoute` | 14 | 124 | 111 | inferred_complete_timeline |
| `Action_RunPostRoute` | 126 | 180 | 55 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–180
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 180 | 180 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–180
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 180 | 180 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–136
- **Visible Samples:** 130

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 74 | 74 | inferred_complete_timeline |
| `Action_None` | 79 | 117 | 39 | inferred_complete_timeline |
| `Action_None` | 121 | 136 | 16 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–75
- **Visible Samples:** 71

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 3 | 4 | inferred_complete_timeline |
| `Action_PassBlock` | 4 | 55 | 52 | inferred_complete_timeline |
| `Action_PassBlock` | 58 | 63 | 6 | inferred_complete_timeline |
| `Action_PassBlock` | 65 | 70 | 6 | inferred_complete_timeline |
| `Action_PassBlock` | 73 | 75 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `21`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–180
- **Visible Samples:** 180

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 3 | 4 | inferred_complete_timeline |
| `Action_PassBlock` | 4 | 41 | 38 | inferred_complete_timeline |
| `Action_PassBlock` | 43 | 180 | 138 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–180
- **Visible Samples:** 178

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_BallSnap` | 1 | 14 | 14 | inferred_complete_timeline |
| `Action_PassBlock` | 15 | 84 | 70 | inferred_complete_timeline |
| `Action_PassBlock` | 88 | 180 | 93 | inferred_complete_timeline |

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
| `Action_PreSnap` | 0 | 3 | 4 | inferred_complete_timeline |
| `Action_PassBlock` | 4 | 180 | 177 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–180
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 3 | 4 | inferred_complete_timeline |
| `Action_PassBlock` | 4 | 180 | 177 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–81
- **Visible Samples:** 68

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 57 | 57 | inferred_complete_timeline |
| `Action_None` | 59 | 63 | 5 | inferred_complete_timeline |
| `Action_None` | 77 | 81 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–180
- **Visible Samples:** 174

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 71 | 71 | inferred_complete_timeline |
| `Action_None` | 79 | 180 | 102 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–180
- **Visible Samples:** 155

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 29 | 29 | inferred_complete_timeline |
| `Action_None` | 53 | 67 | 15 | inferred_complete_timeline |
| `Action_None` | 70 | 73 | 4 | inferred_complete_timeline |
| `Action_None` | 75 | 180 | 106 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–180
- **Visible Samples:** 166

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 31 | 31 | inferred_complete_timeline |
| `Action_None` | 34 | 59 | 26 | inferred_complete_timeline |
| `Action_None` | 62 | 66 | 5 | inferred_complete_timeline |
| `Action_None` | 75 | 136 | 62 | inferred_complete_timeline |
| `Action_None` | 138 | 143 | 6 | inferred_complete_timeline |
| `Action_None` | 145 | 156 | 12 | inferred_complete_timeline |
| `Action_None` | 158 | 180 | 23 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–180
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 180 | 180 | inferred_complete_timeline |

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
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 180 | 180 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–180
- **Visible Samples:** 171

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 97 | 97 | inferred_complete_timeline |
| `Action_None` | 108 | 180 | 73 | inferred_complete_timeline |

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
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 180 | 180 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–175
- **Visible Samples:** 176

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 175 | 175 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–106
- **Visible Samples:** 107

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 106 | 106 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–136
- **Visible Samples:** 136

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 79 | 79 | inferred_complete_timeline |
| `Action_None` | 81 | 136 | 56 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `22` | `22` | Position_Unknown | Team_Unknown | 8–9 | 2 | 1 | Undefined position; Undefined team |
| `23` | `25` | Position_Unknown | Team_Unknown | 35–91 | 40 | 3 | Undefined position; Undefined team |
| `24` | `28` | Position_Unknown | Team_Unknown | 91–180 | 90 | 1 | Undefined position; Undefined team |
| `25` | `30` | Position_Unknown | Team_Unknown | 110–180 | 71 | 1 | Undefined position; Undefined team |
| `26` | `31` | Position_Unknown | Team_Unknown | 120–138 | 18 | 2 | Undefined position; Undefined team |
| `27` | `35` | Position_Unknown | Team_Unknown | 150–177 | 20 | 3 | Undefined position; Undefined team |
| `28` | `36` | Position_Unknown | Team_Unknown | 152–156 | 5 | 1 | Undefined position; Undefined team |
| `29` | `41` | Position_Unknown | Team_Unknown | 170–180 | 11 | 1 | Undefined position; Undefined team |
| `30` | `42` | Position_Unknown | Team_Unknown | 176–177 | 2 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_PassBlock` and target `13` (4 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `20` (2 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `21` (2 segments found)
- ⚠️ Ambiguous match for action `Action_RunPostRoute` and target `0` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `8` (actor_track_id `8`): `SAF` position mapped to `defense` team
- ⚠️ Player track XML ID `11` (actor_track_id `11`): `SAF` position mapped to `defense` team
- ⚠️ 9 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 9 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 18 |
| Missing visible bounding boxes during action | 59 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Resolved action overlap for track '20' (C): higher_priority='Action_BallSnap' [1–14], lower_priority='Action_PassBlock' annotated_start=4, effective_Action_PassBlock_start=15.
- ⚠️ Action 'Action_RunPostRoute' range [14-124] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunPostRoute' range [126-180] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-57] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [59-63] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [77-81] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-97] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [108-180] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-31] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [34-59] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [62-66] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [75-136] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [138-143] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [145-156] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [158-180] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-180] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-180] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-180] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-180] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-106] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-29] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [53-67] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [70-73] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [75-180] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-175] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-79] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [81-136] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-71] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [79-180] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [4-55] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [58-63] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [65-70] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [73-75] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-180] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-74] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [79-117] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [121-136] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [4-180] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-27] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [32-180] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [4-180] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [79-180] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [15-84] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [88-180] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [4-41] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [43-180] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [8-9] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [35-41] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [56-57] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [61-91] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [91-180] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [110-180] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [120-133] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [135-138] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [150-162] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [170-174] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [176-177] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [152-156] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [170-180] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [176-177] for track '30' has 1 frames without a visible bounding box.
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