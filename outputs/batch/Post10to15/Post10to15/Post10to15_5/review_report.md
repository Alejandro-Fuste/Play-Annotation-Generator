# Play-Annotation-Generator Annotation Review — Post10to15_5

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Post10to15_5`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Pass_Post10to15`
- **Result:** `Result_Tackle`
- **Result Frame:** 239
- **Player Tracks:** 35
- **Ball Tracks:** 0
- **Action Segments:** 89
- **Validation Warnings:** 91
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 21
- **Exact Matches:** 6
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 1
- **Missing Segments:** 0
- **Ambiguous Matches:** 2
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 69
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `7` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `19` | `19` |
| ✅ EXACT | `Action_PassBlock` | LT | offense | `14` | `14` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LG | offense | `16` | `16` |
| ✅ EXACT | `Action_PassBlock` | RG | offense | `17` | `17` |
| ⚠️ START CHANGED | `Action_PassBlock` | C | offense | `19` | `19` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RT | offense | `21` | `21` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `11` | `11` |
| ✅ EXACT | `Action_RunPostRoute` | WR1 | offense | `0` | `0` |
| ✅ EXACT | `Action_ThrowPass` | QB | offense | `11` | `11` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `0` | `Group` | 0 | START | 0 | 22 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `11` | `Group` | 0 | START | 0 | 5 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `14` | `Group` | 0 | START | 0 | 8 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `16` | `Group` | 0 | START | 0 | 8 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `17` | `Group` | 0 | START | 0 | 8 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `19` | `Group` | 0 | START | 0 | 5 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `20` | `Group` | 0 | START | 0 | 5 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `21` | `Group` | 0 | START | 0 | 8 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `3` | `Group` | 0 | START | 0 | 5 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `4` | `Group` | 0 | START | 0 | 5 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `7` | `Group` | 0 | START | 0 | 5 |
| ✅ EXACT | `Action_BallSnap` | C | `19` | `19` | 6 | START | 6 | 20 |
| ✅ EXACT | `Action_PassBlock` | LT | `14` | `14` | 9 | START | 9 | 72 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LG | `16` | `16` | 9 | START | 9 | 198 |
| ✅ EXACT | `Action_PassBlock` | RG | `17` | `17` | 9 | START | 9 | 42 |
| ⚠️ START CHANGED | `Action_PassBlock` | C | `19` | `19` | 9 | START | 21 | 172 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RT | `21` | `21` | 9 | START | 9 | 24 |
| ✅ EXACT | `Action_SnapReceive` | QB | `11` | `11` | 20 | END | 6 | 20 |
| ✅ EXACT | `Action_RunPostRoute` | WR1 | `0` | `0` | 23 | START | 23 | 156 |
| ✅ EXACT | `Action_ThrowPass` | QB | `11` | `11` | 58 | START | 58 | 69 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–135
- **Visible Samples:** 136

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 5 | 6 | inferred_complete_timeline |
| `Action_SnapReceive` | 6 | 20 | 15 | inferred_complete_timeline |
| `Action_None` | 21 | 57 | 37 | inferred_complete_timeline |
| `Action_ThrowPass` | 58 | 69 | 12 | inferred_complete_timeline |
| `Action_None` | 70 | 135 | 66 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–155
- **Visible Samples:** 152

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 5 | 6 | inferred_complete_timeline |
| `Action_None` | 6 | 124 | 119 | inferred_complete_timeline |
| `Action_None` | 127 | 129 | 3 | inferred_complete_timeline |
| `Action_None` | 132 | 155 | 24 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–156
- **Visible Samples:** 157

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 22 | 23 | inferred_complete_timeline |
| `Action_RunPostRoute` | 23 | 156 | 134 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–157
- **Visible Samples:** 158

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 5 | 6 | inferred_complete_timeline |
| `Action_None` | 6 | 157 | 152 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 5 | 6 | inferred_complete_timeline |
| `Action_None` | 6 | 210 | 205 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–161
- **Visible Samples:** 162

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 5 | 6 | inferred_complete_timeline |
| `Action_None` | 6 | 161 | 156 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–72
- **Visible Samples:** 73

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 8 | 9 | inferred_complete_timeline |
| `Action_PassBlock` | 9 | 72 | 64 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 207

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 8 | 9 | inferred_complete_timeline |
| `Action_PassBlock` | 9 | 198 | 190 | inferred_complete_timeline |
| `Action_PassBlock` | 200 | 201 | 2 | inferred_complete_timeline |
| `Action_PassBlock` | 205 | 210 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–172
- **Visible Samples:** 173

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 5 | 6 | inferred_complete_timeline |
| `Action_BallSnap` | 6 | 20 | 15 | inferred_complete_timeline |
| `Action_PassBlock` | 21 | 172 | 152 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–42
- **Visible Samples:** 43

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 8 | 9 | inferred_complete_timeline |
| `Action_PassBlock` | 9 | 42 | 34 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `21`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–97
- **Visible Samples:** 73

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 8 | 9 | inferred_complete_timeline |
| `Action_PassBlock` | 9 | 24 | 16 | inferred_complete_timeline |
| `Action_PassBlock` | 29 | 58 | 30 | inferred_complete_timeline |
| `Action_PassBlock` | 62 | 68 | 7 | inferred_complete_timeline |
| `Action_PassBlock` | 74 | 76 | 3 | inferred_complete_timeline |
| `Action_PassBlock` | 78 | 79 | 2 | inferred_complete_timeline |
| `Action_PassBlock` | 92 | 97 | 6 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 5 | 6 | inferred_complete_timeline |
| `Action_None` | 6 | 210 | 205 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 208

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 5 | 6 | inferred_complete_timeline |
| `Action_None` | 6 | 91 | 86 | inferred_complete_timeline |
| `Action_None` | 95 | 210 | 116 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 207

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 5 | 6 | inferred_complete_timeline |
| `Action_None` | 6 | 47 | 42 | inferred_complete_timeline |
| `Action_None` | 52 | 210 | 159 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–55
- **Visible Samples:** 55

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 5 | 6 | inferred_complete_timeline |
| `Action_None` | 6 | 45 | 40 | inferred_complete_timeline |
| `Action_None` | 47 | 55 | 9 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 5 | 6 | inferred_complete_timeline |
| `Action_None` | 6 | 210 | 205 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–49
- **Visible Samples:** 50

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 5 | 6 | inferred_complete_timeline |
| `Action_None` | 6 | 49 | 44 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 209

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 5 | 6 | inferred_complete_timeline |
| `Action_None` | 6 | 169 | 164 | inferred_complete_timeline |
| `Action_None` | 172 | 210 | 39 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–189
- **Visible Samples:** 190

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 5 | 6 | inferred_complete_timeline |
| `Action_None` | 6 | 189 | 184 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `defense`
- **Visible Frames:** 0–209
- **Visible Samples:** 210

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 5 | 6 | inferred_complete_timeline |
| `Action_None` | 6 | 209 | 204 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–128
- **Visible Samples:** 129

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 5 | 6 | inferred_complete_timeline |
| `Action_None` | 6 | 128 | 123 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 5 | 6 | inferred_complete_timeline |
| `Action_None` | 6 | 210 | 205 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `22` | `23` | Position_Unknown | Team_Unknown | 52–57 | 4 | 2 | Undefined position; Undefined team |
| `23` | `24` | Position_Unknown | Team_Unknown | 62–210 | 127 | 6 | Undefined position; Undefined team |
| `24` | `25` | Position_Unknown | Team_Unknown | 74–75 | 2 | 1 | Undefined position; Undefined team |
| `25` | `26` | Position_Unknown | Team_Unknown | 77–199 | 122 | 2 | Undefined position; Undefined team |
| `26` | `27` | Position_Unknown | Team_Unknown | 93–206 | 114 | 1 | Undefined position; Undefined team |
| `27` | `29` | Position_Unknown | Team_Unknown | 103–113 | 10 | 2 | Undefined position; Undefined team |
| `28` | `31` | Position_Unknown | Team_Unknown | 106–166 | 44 | 4 | Undefined position; Undefined team |
| `29` | `32` | Position_Unknown | Team_Unknown | 110–121 | 12 | 1 | Undefined position; Undefined team |
| `30` | `34` | Position_Unknown | Team_Unknown | 130–210 | 81 | 1 | Undefined position; Undefined team |
| `31` | `36` | Position_Unknown | Team_Unknown | 145–210 | 62 | 2 | Undefined position; Undefined team |
| `32` | `37` | Position_Unknown | Team_Unknown | 156–210 | 50 | 3 | Undefined position; Undefined team |
| `33` | `39` | Position_Unknown | Team_Unknown | 168–176 | 8 | 2 | Undefined position; Undefined team |
| `34` | `40` | Position_Unknown | Team_Unknown | 179–210 | 32 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_PassBlock` and target `16` (3 segments found)
- ⚠️ `Action_PassBlock` for actor_track_id `19` (C): Annotated start 9 != Inferred start 21
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `21` (6 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `2` (actor_track_id `2`): `SAF1` position mapped to `defense` team
- ⚠️ Player track XML ID `13` (actor_track_id `13`): `SAF2` position mapped to `defense` team
- ⚠️ 13 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 13 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 26 |
| Missing visible bounding boxes during action | 63 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Resolved action overlap for track '19' (C): higher_priority='Action_BallSnap' [6–20], lower_priority='Action_PassBlock' annotated_start=9, effective_Action_PassBlock_start=21.
- ⚠️ Action 'Action_RunPostRoute' range [23-156] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [6-210] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [6-128] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [6-157] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [6-124] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [127-129] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [132-155] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [6-169] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [172-210] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [6-189] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [6-210] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [6-45] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [47-55] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [6-91] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [95-210] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [6-47] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [52-210] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [70-135] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [6-49] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [6-210] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [9-72] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [6-210] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [9-198] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [200-201] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [205-210] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [9-42] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [6-209] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [21-172] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [6-161] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [9-24] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [29-58] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [62-68] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [74-76] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [78-79] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [92-97] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [52-53] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [56-57] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [62-64] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [67-72] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [77-79] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [86-88] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [90-94] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [104-210] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [74-75] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [77-196] for track '25' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [198-199] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [93-206] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [103-110] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [112-113] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [106-107] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [123-132] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [134-135] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [137-166] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [110-121] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [130-210] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [145-147] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [152-210] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [156-164] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [166-170] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [175-210] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [168-172] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [174-176] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [179-210] for track '34' has 1 frames without a visible bounding box.
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

</details>