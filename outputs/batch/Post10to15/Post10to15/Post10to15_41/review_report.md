# Play-Annotation-Generator Annotation Review — Post10to15_41

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Post10to15_41`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Pass_Post10to15`
- **Result:** `Result_Tackle`
- **Result Frame:** 239
- **Player Tracks:** 34
- **Ball Tracks:** 0
- **Action Segments:** 113
- **Validation Warnings:** 112
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
- **Inferred Coverage Segments (Action_None):** 93
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `22` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | offense | `3` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `19` | `19` |
| ✅ EXACT | `Action_PassBlock` | RT | offense | `14` | `14` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RG | offense | `17` | `17` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | C | offense | `19` | `19` |
| ✅ EXACT | `Action_PassBlock` | LG | offense | `20` | `20` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LT | offense | `22` | `22` |
| ⚠️ AMBIGUOUS MATCH | `Action_RunPostRoute` | WR2 | offense | `10` | `10` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `16` | `16` |
| ✅ EXACT | `Action_ThrowPass` | QB | offense | `16` | `16` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `0` | `Group` | 0 | START | 0 | 0 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `10` | `Group` | 0 | START | 0 | 10 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `14` | `Group` | 0 | START | 0 | 3 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `15` | `Group` | 0 | START | 0 | 0 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `16` | `Group` | 0 | START | 0 | 0 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `17` | `Group` | 0 | START | 0 | 3 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `19` | `Group` | 0 | START | 0 | 0 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `20` | `Group` | 0 | START | 0 | 3 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | `21` | `Group` | 0 | START | 0 | 0 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `22` | `Group` | 0 | START | 0 | 3 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | `3` | `Group` | 0 | START | 0 | 0 |
| ✅ EXACT | `Action_BallSnap` | C | `19` | `19` | 1 | START | 1 | 11 |
| ✅ EXACT | `Action_PassBlock` | RT | `14` | `14` | 4 | START | 4 | 180 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RG | `17` | `17` | 4 | START | 4 | 138 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | C | `19` | `19` | 4 | START | 12 | 12 |
| ✅ EXACT | `Action_PassBlock` | LG | `20` | `20` | 4 | START | 4 | 19 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LT | `22` | `22` | 4 | START | 4 | 22 |
| ⚠️ AMBIGUOUS MATCH | `Action_RunPostRoute` | WR2 | `10` | `10` | 11 | START | 11 | 79 |
| ✅ EXACT | `Action_SnapReceive` | QB | `16` | `16` | 11 | END | 1 | 11 |
| ✅ EXACT | `Action_ThrowPass` | QB | `16` | `16` | 52 | START | 52 | 63 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–113
- **Visible Samples:** 114

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_SnapReceive` | 1 | 11 | 11 | inferred_complete_timeline |
| `Action_None` | 12 | 51 | 40 | inferred_complete_timeline |
| `Action_ThrowPass` | 52 | 63 | 12 | inferred_complete_timeline |
| `Action_None` | 64 | 113 | 50 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–180
- **Visible Samples:** 177

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 20 | 20 | inferred_complete_timeline |
| `Action_None` | 25 | 180 | 156 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–180
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 180 | 180 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–180
- **Visible Samples:** 177

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 10 | 11 | inferred_complete_timeline |
| `Action_RunPostRoute` | 11 | 79 | 69 | inferred_complete_timeline |
| `Action_RunPostRoute` | 81 | 84 | 4 | inferred_complete_timeline |
| `Action_RunPostRoute` | 87 | 165 | 79 | inferred_complete_timeline |
| `Action_RunPostRoute` | 167 | 180 | 14 | inferred_complete_timeline |

</details>

<details>
<summary>TE1 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–180
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 180 | 180 | inferred_complete_timeline |

</details>

<details>
<summary>TE2 — actor_track_id `21`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–55
- **Visible Samples:** 43

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 38 | 38 | inferred_complete_timeline |
| `Action_None` | 52 | 55 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `22`</summary>

- **xml_track_id:** `22`
- **actor_track_id:** `22`
- **team_side:** `offense`
- **Visible Frames:** 0–180
- **Visible Samples:** 156

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 3 | 4 | inferred_complete_timeline |
| `Action_PassBlock` | 4 | 22 | 19 | inferred_complete_timeline |
| `Action_PassBlock` | 47 | 51 | 5 | inferred_complete_timeline |
| `Action_PassBlock` | 53 | 180 | 128 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–19
- **Visible Samples:** 20

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 3 | 4 | inferred_complete_timeline |
| `Action_PassBlock` | 4 | 19 | 16 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–180
- **Visible Samples:** 147

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_BallSnap` | 1 | 11 | 11 | inferred_complete_timeline |
| `Action_PassBlock` | 12 | 12 | 1 | inferred_complete_timeline |
| `Action_PassBlock` | 39 | 86 | 48 | inferred_complete_timeline |
| `Action_PassBlock` | 92 | 95 | 4 | inferred_complete_timeline |
| `Action_PassBlock` | 98 | 109 | 12 | inferred_complete_timeline |
| `Action_PassBlock` | 111 | 180 | 70 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–180
- **Visible Samples:** 149

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 3 | 4 | inferred_complete_timeline |
| `Action_PassBlock` | 4 | 138 | 135 | inferred_complete_timeline |
| `Action_PassBlock` | 171 | 180 | 10 | inferred_complete_timeline |

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
- **Visible Frames:** 0–52
- **Visible Samples:** 53

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 52 | 52 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–180
- **Visible Samples:** 176

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 31 | 31 | inferred_complete_timeline |
| `Action_None` | 34 | 50 | 17 | inferred_complete_timeline |
| `Action_None` | 52 | 53 | 2 | inferred_complete_timeline |
| `Action_None` | 56 | 180 | 125 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–64
- **Visible Samples:** 29

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 26 | 26 | inferred_complete_timeline |
| `Action_None` | 63 | 64 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–180
- **Visible Samples:** 177

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 52 | 52 | inferred_complete_timeline |
| `Action_None` | 55 | 92 | 38 | inferred_complete_timeline |
| `Action_None` | 95 | 180 | 86 | inferred_complete_timeline |

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
<summary>LB2 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–180
- **Visible Samples:** 165

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 47 | 47 | inferred_complete_timeline |
| `Action_None` | 64 | 180 | 117 | inferred_complete_timeline |

</details>

<details>
<summary>LB3 — actor_track_id `7`</summary>

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
- **Visible Samples:** 168

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 138 | 138 | inferred_complete_timeline |
| `Action_None` | 144 | 150 | 7 | inferred_complete_timeline |
| `Action_None` | 159 | 180 | 22 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–123
- **Visible Samples:** 107

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 83 | 83 | inferred_complete_timeline |
| `Action_None` | 88 | 89 | 2 | inferred_complete_timeline |
| `Action_None` | 102 | 103 | 2 | inferred_complete_timeline |
| `Action_None` | 105 | 123 | 19 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–138
- **Visible Samples:** 131

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 111 | 111 | inferred_complete_timeline |
| `Action_None` | 117 | 119 | 3 | inferred_complete_timeline |
| `Action_None` | 121 | 132 | 12 | inferred_complete_timeline |
| `Action_None` | 135 | 138 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–180
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 180 | 180 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `18` | `18` | Position_Unknown | Team_Unknown | 0–97 | 98 | 2 | Undefined position; Undefined team |
| `23` | `23` | Position_Unknown | Team_Unknown | 0–62 | 57 | 4 | Undefined position; Undefined team |
| `24` | `25` | Position_Unknown | Team_Unknown | 21–55 | 19 | 5 | Undefined position; Undefined team |
| `25` | `30` | Position_Unknown | Team_Unknown | 29–91 | 39 | 7 | Undefined position; Undefined team |
| `26` | `31` | Position_Unknown | Team_Unknown | 30–33 | 4 | 1 | Undefined position; Undefined team |
| `27` | `34` | Position_Unknown | Team_Unknown | 76–180 | 99 | 2 | Undefined position; Undefined team |
| `28` | `35` | Position_Unknown | Team_Unknown | 82–180 | 85 | 4 | Undefined position; Undefined team |
| `29` | `37` | Position_Unknown | Team_Unknown | 103–107 | 5 | 1 | Undefined position; Undefined team |
| `30` | `38` | Position_Unknown | Team_Unknown | 104–180 | 73 | 2 | Undefined position; Undefined team |
| `31` | `39` | Position_Unknown | Team_Unknown | 111–167 | 27 | 7 | Undefined position; Undefined team |
| `32` | `40` | Position_Unknown | Team_Unknown | 120–129 | 10 | 1 | Undefined position; Undefined team |
| `33` | `42` | Position_Unknown | Team_Unknown | 131–167 | 32 | 2 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_PassBlock` and target `17` (2 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `19` (5 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `22` (3 segments found)
- ⚠️ Ambiguous match for action `Action_RunPostRoute` and target `10` (4 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `9` (actor_track_id `9`): `SAF2` position mapped to `defense` team
- ⚠️ Player track XML ID `11` (actor_track_id `11`): `SAF1` position mapped to `defense` team
- ⚠️ 12 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 12 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 24 |
| Missing visible bounding boxes during action | 86 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Resolved action overlap for track '19' (C): higher_priority='Action_BallSnap' [1–11], lower_priority='Action_PassBlock' annotated_start=4, effective_Action_PassBlock_start=12.
- ⚠️ Action 'Action_None' range [1-180] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-52] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-138] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [144-150] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [159-180] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-180] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-47] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [64-180] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-180] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-31] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [34-50] for track '6' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [52-53] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [56-180] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-180] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-26] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [63-64] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-180] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunPostRoute' range [11-79] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunPostRoute' range [81-84] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunPostRoute' range [87-165] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunPostRoute' range [167-180] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-111] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [117-119] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [121-132] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [135-138] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-52] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [55-92] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [95-180] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-83] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [88-89] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [102-103] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [105-123] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [4-180] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-20] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [25-180] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [64-113] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [4-138] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [171-180] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-97] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' for track '19' starts at frame 12, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_PassBlock' range [12-12] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [39-86] for track '19' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [92-95] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [98-109] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [111-180] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [4-19] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-38] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [52-55] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [4-22] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [47-51] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [53-180] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-24] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [26-55] for track '23' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [61-62] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [21-22] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [25-27] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [32-40] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [42-43] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [53-55] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [29-38] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [41-42] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [48-56] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [60-65] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [68-69] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [72-78] for track '25' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [89-91] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [30-33] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [76-77] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [84-180] for track '27' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [82-88] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [95-96] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [104-105] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [107-180] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [103-107] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [104-112] for track '30' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [117-180] for track '30' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [111-112] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [122-124] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [137-147] for track '31' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [149-150] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [153-154] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [157-159] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [164-167] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [120-129] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [131-158] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [164-167] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Player track '18' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '18' has undefined team_side. Will map to Team_Unknown.
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