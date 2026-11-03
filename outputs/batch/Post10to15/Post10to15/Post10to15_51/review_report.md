# Play-Annotation-Generator Annotation Review — Post10to15_51

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Post10to15_51`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Pass_Post10to15`
- **Result:** `Result_Tackle`
- **Result Frame:** 239
- **Player Tracks:** 34
- **Ball Tracks:** 0
- **Action Segments:** 90
- **Validation Warnings:** 93
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 20
- **Exact Matches:** 4
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
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `8` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `15` | `15` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LG | offense | `14` | `14` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | C | offense | `15` | `15` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RG | offense | `17` | `17` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RT | offense | `19` | `19` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LT | offense | `8` | `8` |
| ✅ EXACT | `Action_RunPostRoute` | WR1 | offense | `0` | `0` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `18` | `18` |
| ✅ EXACT | `Action_ThrowPass` | QB | offense | `18` | `18` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `0` | `Group` | 0 | START | 0 | 23 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `1` | `Group` | 0 | START | 0 | 6 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | `10` | `Group` | 0 | START | 0 | 6 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `14` | `Group` | 0 | START | 0 | 9 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `15` | `Group` | 0 | START | 0 | 6 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `17` | `Group` | 0 | START | 0 | 9 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `18` | `Group` | 0 | START | 0 | 6 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `19` | `Group` | 0 | START | 0 | 9 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | `20` | `Group` | 0 | START | 0 | 6 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `8` | `Group` | 0 | START | 0 | 9 |
| ✅ EXACT | `Action_BallSnap` | C | `15` | `15` | 7 | START | 7 | 24 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LG | `14` | `14` | 10 | START | 10 | 31 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | C | `15` | `15` | 10 | START | 25 | 39 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RG | `17` | `17` | 10 | START | 10 | 74 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RT | `19` | `19` | 10 | START | 10 | 29 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LT | `8` | `8` | 10 | START | 10 | 67 |
| ✅ EXACT | `Action_RunPostRoute` | WR1 | `0` | `0` | 24 | START | 24 | 151 |
| ✅ EXACT | `Action_SnapReceive` | QB | `18` | `18` | 24 | END | 7 | 24 |
| ✅ EXACT | `Action_ThrowPass` | QB | `18` | `18` | 77 | START | 77 | 86 |

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
- **Visible Frames:** 0–97
- **Visible Samples:** 98

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 6 | 7 | inferred_complete_timeline |
| `Action_SnapReceive` | 7 | 24 | 18 | inferred_complete_timeline |
| `Action_None` | 25 | 76 | 52 | inferred_complete_timeline |
| `Action_ThrowPass` | 77 | 86 | 10 | inferred_complete_timeline |
| `Action_None` | 87 | 97 | 11 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–151
- **Visible Samples:** 152

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 23 | 24 | inferred_complete_timeline |
| `Action_RunPostRoute` | 24 | 151 | 128 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–180
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 6 | 7 | inferred_complete_timeline |
| `Action_None` | 7 | 180 | 174 | inferred_complete_timeline |

</details>

<details>
<summary>TE1 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–180
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 6 | 7 | inferred_complete_timeline |
| `Action_None` | 7 | 180 | 174 | inferred_complete_timeline |

</details>

<details>
<summary>TE2 — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–47
- **Visible Samples:** 47

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 6 | 7 | inferred_complete_timeline |
| `Action_None` | 7 | 35 | 29 | inferred_complete_timeline |
| `Action_None` | 37 | 47 | 11 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–119
- **Visible Samples:** 116

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 9 | 10 | inferred_complete_timeline |
| `Action_PassBlock` | 10 | 67 | 58 | inferred_complete_timeline |
| `Action_PassBlock` | 71 | 86 | 16 | inferred_complete_timeline |
| `Action_PassBlock` | 88 | 119 | 32 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–58
- **Visible Samples:** 48

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 9 | 10 | inferred_complete_timeline |
| `Action_PassBlock` | 10 | 31 | 22 | inferred_complete_timeline |
| `Action_PassBlock` | 43 | 58 | 16 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–179
- **Visible Samples:** 155

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 6 | 7 | inferred_complete_timeline |
| `Action_BallSnap` | 7 | 24 | 18 | inferred_complete_timeline |
| `Action_PassBlock` | 25 | 39 | 15 | inferred_complete_timeline |
| `Action_PassBlock` | 46 | 105 | 60 | inferred_complete_timeline |
| `Action_PassBlock` | 125 | 179 | 55 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–180
- **Visible Samples:** 179

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 9 | 10 | inferred_complete_timeline |
| `Action_PassBlock` | 10 | 74 | 65 | inferred_complete_timeline |
| `Action_PassBlock` | 77 | 180 | 104 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–131
- **Visible Samples:** 79

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 9 | 10 | inferred_complete_timeline |
| `Action_PassBlock` | 10 | 29 | 20 | inferred_complete_timeline |
| `Action_PassBlock` | 33 | 79 | 47 | inferred_complete_timeline |
| `Action_PassBlock` | 130 | 131 | 2 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–180
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 6 | 7 | inferred_complete_timeline |
| `Action_None` | 7 | 180 | 174 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–180
- **Visible Samples:** 179

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 6 | 7 | inferred_complete_timeline |
| `Action_None` | 7 | 169 | 163 | inferred_complete_timeline |
| `Action_None` | 171 | 174 | 4 | inferred_complete_timeline |
| `Action_None` | 176 | 180 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>DT — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–34
- **Visible Samples:** 35

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 6 | 7 | inferred_complete_timeline |
| `Action_None` | 7 | 34 | 28 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–180
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 6 | 7 | inferred_complete_timeline |
| `Action_None` | 7 | 180 | 174 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–180
- **Visible Samples:** 180

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 6 | 7 | inferred_complete_timeline |
| `Action_None` | 7 | 133 | 127 | inferred_complete_timeline |
| `Action_None` | 135 | 180 | 46 | inferred_complete_timeline |

</details>

<details>
<summary>OLB1 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–180
- **Visible Samples:** 162

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 6 | 7 | inferred_complete_timeline |
| `Action_None` | 7 | 92 | 86 | inferred_complete_timeline |
| `Action_None` | 106 | 107 | 2 | inferred_complete_timeline |
| `Action_None` | 110 | 111 | 2 | inferred_complete_timeline |
| `Action_None` | 113 | 147 | 35 | inferred_complete_timeline |
| `Action_None` | 150 | 153 | 4 | inferred_complete_timeline |
| `Action_None` | 155 | 180 | 26 | inferred_complete_timeline |

</details>

<details>
<summary>OLB2 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–180
- **Visible Samples:** 170

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 6 | 7 | inferred_complete_timeline |
| `Action_None` | 7 | 57 | 51 | inferred_complete_timeline |
| `Action_None` | 63 | 129 | 67 | inferred_complete_timeline |
| `Action_None` | 132 | 173 | 42 | inferred_complete_timeline |
| `Action_None` | 178 | 180 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–180
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 6 | 7 | inferred_complete_timeline |
| `Action_None` | 7 | 180 | 174 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–180
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 6 | 7 | inferred_complete_timeline |
| `Action_None` | 7 | 180 | 174 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–180
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 6 | 7 | inferred_complete_timeline |
| `Action_None` | 7 | 180 | 174 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–180
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 6 | 7 | inferred_complete_timeline |
| `Action_None` | 7 | 180 | 174 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `21` | `21` | Position_Unknown | Team_Unknown | 7–26 | 20 | 1 | Undefined position; Undefined team |
| `22` | `22` | Position_Unknown | Team_Unknown | 44–169 | 76 | 4 | Undefined position; Undefined team |
| `23` | `23` | Position_Unknown | Team_Unknown | 54–178 | 107 | 4 | Undefined position; Undefined team |
| `24` | `25` | Position_Unknown | Team_Unknown | 79–180 | 102 | 1 | Undefined position; Undefined team |
| `25` | `26` | Position_Unknown | Team_Unknown | 102–170 | 58 | 4 | Undefined position; Undefined team |
| `26` | `27` | Position_Unknown | Team_Unknown | 115–180 | 66 | 1 | Undefined position; Undefined team |
| `27` | `30` | Position_Unknown | Team_Unknown | 126–173 | 48 | 1 | Undefined position; Undefined team |
| `28` | `32` | Position_Unknown | Team_Unknown | 140–180 | 41 | 1 | Undefined position; Undefined team |
| `29` | `34` | Position_Unknown | Team_Unknown | 154–180 | 13 | 3 | Undefined position; Undefined team |
| `30` | `37` | Position_Unknown | Team_Unknown | 171–179 | 9 | 1 | Undefined position; Undefined team |
| `31` | `38` | Position_Unknown | Team_Unknown | 173–180 | 8 | 1 | Undefined position; Undefined team |
| `32` | `39` | Position_Unknown | Team_Unknown | 177–180 | 4 | 1 | Undefined position; Undefined team |
| `33` | `40` | Position_Unknown | Team_Unknown | 178–180 | 3 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_PassBlock` and target `14` (2 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `15` (3 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `17` (2 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `19` (3 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `8` (3 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `5` (actor_track_id `5`): `SAF1` position mapped to `defense` team
- ⚠️ Player track XML ID `13` (actor_track_id `13`): `SAF2` position mapped to `defense` team
- ⚠️ 13 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 13 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 26 |
| Missing visible bounding boxes during action | 65 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Resolved action overlap for track '15' (C): higher_priority='Action_BallSnap' [7–24], lower_priority='Action_PassBlock' annotated_start=10, effective_Action_PassBlock_start=25.
- ⚠️ Action 'Action_RunPostRoute' range [24-151] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [7-180] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [7-57] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [63-129] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [132-173] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [178-180] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [7-169] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [171-174] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [176-180] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [7-180] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [7-180] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [7-133] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [135-180] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [7-34] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [10-67] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [71-86] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [88-119] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [7-180] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [7-180] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [7-92] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [106-107] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [110-111] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [113-147] for track '11' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [150-153] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [155-180] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [7-180] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [7-180] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [10-31] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [43-58] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [25-39] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [46-105] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [125-179] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [7-180] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [10-74] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [77-180] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [87-97] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [10-29] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [33-79] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [130-131] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [7-35] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [37-47] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [7-26] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [44-66] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [89-135] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [137-138] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [166-169] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [54-72] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [80-158] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [166-171] for track '23' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [176-178] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [79-180] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [102-121] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [127-150] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [152-163] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [169-170] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [115-180] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [126-173] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [140-180] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [154-157] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [166-171] for track '29' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [178-180] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [171-179] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [173-180] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [177-180] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [178-180] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Player track '21' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '21' has undefined team_side. Will map to Team_Unknown.
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