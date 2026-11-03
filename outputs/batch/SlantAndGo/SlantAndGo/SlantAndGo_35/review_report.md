# Play-Annotation-Generator Annotation Review — SlantAndGo_35

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `SlantAndGo_35`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Pass_SlantAndGo`
- **Result:** `Result_Rec`
- **Result Frame:** 239
- **Player Tracks:** 31
- **Ball Tracks:** 0
- **Action Segments:** 94
- **Validation Warnings:** 99
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 19
- **Exact Matches:** 5
- **Group Expanded Events:** 8
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 5
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 76
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `8` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `9` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `18` | `18` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LG | offense | `11` | `11` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | C | offense | `18` | `18` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RT | offense | `20` | `20` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RG | offense | `21` | `21` |
| ✅ EXACT | `Action_PassBlock` | LT | offense | `8` | `8` |
| ✅ EXACT | `Action_SnapReceive` | LB2 | defense | `14` | `14` |
| ✅ EXACT | `Action_SellRoute` | CB3 | defense | `16` | `16` |
| ⚠️ AMBIGUOUS MATCH | `Action_VerticalStem` | CB3 | defense | `16` | `16` |
| ✅ EXACT | `Action_ThrowPass` | LB2 | defense | `14` | `14` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `11` | `Group` | 0 | START | 0 | 11 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | `17` | `Group` | 0 | START | 0 | 8 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `18` | `Group` | 0 | START | 0 | 8 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | `19` | `Group` | 0 | START | 0 | 8 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `20` | `Group` | 0 | START | 0 | 11 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `21` | `Group` | 0 | START | 0 | 11 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `8` | `Group` | 0 | START | 0 | 11 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `9` | `Group` | 0 | START | 0 | 8 |
| ✅ EXACT | `Action_BallSnap` | C | `18` | `18` | 9 | START | 9 | 23 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LG | `11` | `11` | 12 | START | 12 | 138 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | C | `18` | `18` | 12 | START | 24 | 86 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RT | `20` | `20` | 12 | START | 12 | 47 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RG | `21` | `21` | 12 | START | 12 | 124 |
| ✅ EXACT | `Action_PassBlock` | LT | `8` | `8` | 12 | START | 12 | 210 |
| ✅ EXACT | `Action_SnapReceive` | LB2 | `14` | `14` | 23 | END | 9 | 23 |
| ✅ EXACT | `Action_SellRoute` | CB3 | `16` | `16` | 47 | START | 47 | 72 |
| ⚠️ AMBIGUOUS MATCH | `Action_VerticalStem` | CB3 | `16` | `16` | 73 | START | 73 | 137 |
| ✅ EXACT | `Action_ThrowPass` | LB2 | `14` | `14` | 88 | START | 88 | 97 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>RB — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 8 | 9 | inferred_complete_timeline |
| `Action_None` | 9 | 210 | 202 | inferred_complete_timeline |

</details>

<details>
<summary>TE1 — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 8 | 9 | inferred_complete_timeline |
| `Action_None` | 9 | 210 | 202 | inferred_complete_timeline |

</details>

<details>
<summary>TE2 — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 193

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 8 | 9 | inferred_complete_timeline |
| `Action_None` | 9 | 75 | 67 | inferred_complete_timeline |
| `Action_None` | 85 | 102 | 18 | inferred_complete_timeline |
| `Action_None` | 105 | 108 | 4 | inferred_complete_timeline |
| `Action_None` | 116 | 210 | 95 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 11 | 12 | inferred_complete_timeline |
| `Action_PassBlock` | 12 | 210 | 199 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 207

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 11 | 12 | inferred_complete_timeline |
| `Action_PassBlock` | 12 | 138 | 127 | inferred_complete_timeline |
| `Action_PassBlock` | 140 | 146 | 7 | inferred_complete_timeline |
| `Action_PassBlock` | 148 | 151 | 4 | inferred_complete_timeline |
| `Action_PassBlock` | 153 | 154 | 2 | inferred_complete_timeline |
| `Action_PassBlock` | 156 | 210 | 55 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–90
- **Visible Samples:** 89

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 8 | 9 | inferred_complete_timeline |
| `Action_BallSnap` | 9 | 23 | 15 | inferred_complete_timeline |
| `Action_PassBlock` | 24 | 86 | 63 | inferred_complete_timeline |
| `Action_PassBlock` | 89 | 90 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `21`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 201

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 11 | 12 | inferred_complete_timeline |
| `Action_PassBlock` | 12 | 124 | 113 | inferred_complete_timeline |
| `Action_PassBlock` | 128 | 140 | 13 | inferred_complete_timeline |
| `Action_PassBlock` | 142 | 152 | 11 | inferred_complete_timeline |
| `Action_PassBlock` | 154 | 164 | 11 | inferred_complete_timeline |
| `Action_PassBlock` | 166 | 167 | 2 | inferred_complete_timeline |
| `Action_PassBlock` | 172 | 210 | 39 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 206

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 11 | 12 | inferred_complete_timeline |
| `Action_PassBlock` | 12 | 47 | 36 | inferred_complete_timeline |
| `Action_PassBlock` | 49 | 52 | 4 | inferred_complete_timeline |
| `Action_PassBlock` | 55 | 66 | 12 | inferred_complete_timeline |
| `Action_PassBlock` | 69 | 210 | 142 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–60
- **Visible Samples:** 56

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 8 | 9 | inferred_complete_timeline |
| `Action_None` | 9 | 52 | 44 | inferred_complete_timeline |
| `Action_None` | 58 | 60 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 8 | 9 | inferred_complete_timeline |
| `Action_None` | 9 | 210 | 202 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 198

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 8 | 9 | inferred_complete_timeline |
| `Action_None` | 9 | 39 | 31 | inferred_complete_timeline |
| `Action_None` | 41 | 45 | 5 | inferred_complete_timeline |
| `Action_None` | 58 | 210 | 153 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–203
- **Visible Samples:** 203

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 8 | 9 | inferred_complete_timeline |
| `Action_None` | 9 | 187 | 179 | inferred_complete_timeline |
| `Action_None` | 189 | 203 | 15 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 8 | 9 | inferred_complete_timeline |
| `Action_SnapReceive` | 9 | 23 | 15 | inferred_complete_timeline |
| `Action_None` | 24 | 87 | 64 | inferred_complete_timeline |
| `Action_ThrowPass` | 88 | 97 | 10 | inferred_complete_timeline |
| `Action_None` | 98 | 210 | 113 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 8 | 9 | inferred_complete_timeline |
| `Action_None` | 9 | 210 | 202 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 207

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 8 | 9 | inferred_complete_timeline |
| `Action_None` | 9 | 180 | 172 | inferred_complete_timeline |
| `Action_None` | 183 | 184 | 2 | inferred_complete_timeline |
| `Action_None` | 187 | 210 | 24 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 192

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 46 | 47 | inferred_complete_timeline |
| `Action_SellRoute` | 47 | 72 | 26 | inferred_complete_timeline |
| `Action_VerticalStem` | 73 | 137 | 65 | inferred_complete_timeline |
| `Action_VerticalStem` | 140 | 175 | 36 | inferred_complete_timeline |
| `Action_VerticalStem` | 183 | 198 | 16 | inferred_complete_timeline |
| `Action_VerticalStem` | 209 | 210 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–90
- **Visible Samples:** 78

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 8 | 9 | inferred_complete_timeline |
| `Action_None` | 9 | 74 | 66 | inferred_complete_timeline |
| `Action_None` | 88 | 90 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 8 | 9 | inferred_complete_timeline |
| `Action_None` | 9 | 210 | 202 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `1` | `1` | Position_Unknown | Team_Unknown | 0–210 | 207 | 4 | Undefined position; Undefined team |
| `4` | `4` | Position_Unknown | Team_Unknown | 0–210 | 209 | 3 | Undefined position; Undefined team |
| `7` | `7` | Position_Unknown | Team_Unknown | 0–210 | 211 | 2 | Undefined position; Undefined team |
| `13` | `13` | Position_Unknown | Team_Unknown | 0–210 | 211 | 2 | Undefined position; Undefined team |
| `22` | `22` | Position_Unknown | Team_Unknown | 33–34 | 2 | 1 | Undefined position; Undefined team |
| `23` | `25` | Position_Unknown | Team_Unknown | 67–77 | 8 | 3 | Undefined position; Undefined team |
| `24` | `27` | Position_Unknown | Team_Unknown | 89–210 | 121 | 2 | Undefined position; Undefined team |
| `25` | `29` | Position_Unknown | Team_Unknown | 96–210 | 109 | 3 | Undefined position; Undefined team |
| `26` | `30` | Position_Unknown | Team_Unknown | 97–210 | 106 | 3 | Undefined position; Undefined team |
| `27` | `31` | Position_Unknown | Team_Unknown | 125–132 | 8 | 1 | Undefined position; Undefined team |
| `28` | `32` | Position_Unknown | Team_Unknown | 135–136 | 2 | 1 | Undefined position; Undefined team |
| `29` | `35` | Position_Unknown | Team_Unknown | 173–180 | 8 | 1 | Undefined position; Undefined team |
| `30` | `36` | Position_Unknown | Team_Unknown | 188–197 | 10 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_PassBlock` and target `11` (5 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `18` (2 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `20` (4 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `21` (6 segments found)
- ⚠️ Ambiguous match for action `Action_VerticalStem` and target `16` (4 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `10` (actor_track_id `10`): `SAF2` position mapped to `defense` team
- ⚠️ Player track XML ID `12` (actor_track_id `12`): `SAF1` position mapped to `defense` team
- ⚠️ 13 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 13 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 26 |
| Missing visible bounding boxes during action | 67 |
| Track-related warning | 5 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 50: Duplicate assignment for track ID '14' in grid. Overwriting previous assignment.
- ⚠️ Row 50: Duplicate assignment for track ID '16' in grid. Overwriting previous assignment.
- ⚠️ Row 50: Duplicate assignment for track ID '12' in grid. Overwriting previous assignment.
- ⚠️ Row 50: Duplicate assignment for track ID '10' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Resolved action overlap for track '18' (C): higher_priority='Action_BallSnap' [9–23], lower_priority='Action_PassBlock' annotated_start=12, effective_Action_PassBlock_start=24.
- ⚠️ Action 'Action_None' range [9-210] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [9-121] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [123-124] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [128-210] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [9-52] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [58-60] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [9-39] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [41-45] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [58-210] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [9-205] for track '4' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [208-210] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [9-210] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [9-180] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [183-184] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [187-210] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [9-210] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [12-210] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [9-210] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [9-210] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [12-138] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [140-146] for track '11' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [148-151] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [153-154] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [156-210] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [9-74] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [88-90] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [9-210] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [98-210] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [9-187] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [189-203] for track '15' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_VerticalStem' range [73-137] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_VerticalStem' range [140-175] for track '16' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_VerticalStem' range [183-198] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_VerticalStem' range [209-210] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [9-75] for track '17' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [85-102] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [105-108] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [116-210] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [24-86] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [89-90] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [9-210] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [12-47] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [49-52] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [55-66] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [69-210] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [12-124] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [128-140] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [142-152] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [154-164] for track '21' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [166-167] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [172-210] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [33-34] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [67-70] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [73-74] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [76-77] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [89-95] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [97-210] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [96-102] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [107-119] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [122-210] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [97-131] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [138-139] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [142-210] for track '26' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [125-132] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [135-136] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [173-180] for track '29' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [188-197] for track '30' has 3 frames without a visible bounding box.
- ⚠️ Player track '1' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '1' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '4' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '4' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '7' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '7' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '13' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '13' has undefined team_side. Will map to Team_Unknown.
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