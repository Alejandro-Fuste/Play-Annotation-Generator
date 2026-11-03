# Play-Annotation-Generator Annotation Review — Post10to15_7

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Post10to15_7`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Pass_Post10to15`
- **Result:** `Result_Tackle`
- **Result Frame:** 239
- **Player Tracks:** 39
- **Ball Tracks:** 0
- **Action Segments:** 97
- **Validation Warnings:** 107
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
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 3
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 77
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `8` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `16` | `16` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | C | offense | `16` | `16` |
| ✅ EXACT | `Action_PassBlock` | RT | offense | `17` | `17` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LT | offense | `19` | `19` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LG | offense | `20` | `20` |
| ✅ EXACT | `Action_PassBlock` | RG | offense | `21` | `21` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `8` | `8` |
| ✅ EXACT | `Action_RunPostRoute` | WR1 | offense | `0` | `0` |
| ✅ EXACT | `Action_ThrowPass` | QB | offense | `8` | `8` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `0` | `Group` | 0 | START | 0 | 34 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `14` | `Group` | 0 | START | 0 | 21 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `16` | `Group` | 0 | START | 0 | 21 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `17` | `Group` | 0 | START | 0 | 24 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `19` | `Group` | 0 | START | 0 | 24 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `2` | `Group` | 0 | START | 0 | 21 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `20` | `Group` | 0 | START | 0 | 24 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `21` | `Group` | 0 | START | 0 | 24 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `3` | `Group` | 0 | START | 0 | 21 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `7` | `Group` | 0 | START | 0 | 21 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `8` | `Group` | 0 | START | 0 | 21 |
| ✅ EXACT | `Action_BallSnap` | C | `16` | `16` | 22 | START | 22 | 34 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | C | `16` | `16` | 25 | START | 35 | 90 |
| ✅ EXACT | `Action_PassBlock` | RT | `17` | `17` | 25 | START | 25 | 41 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LT | `19` | `19` | 25 | START | 25 | 148 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LG | `20` | `20` | 25 | START | 25 | 119 |
| ✅ EXACT | `Action_PassBlock` | RG | `21` | `21` | 25 | START | 25 | 63 |
| ✅ EXACT | `Action_SnapReceive` | QB | `8` | `8` | 34 | END | 22 | 34 |
| ✅ EXACT | `Action_RunPostRoute` | WR1 | `0` | `0` | 35 | START | 35 | 139 |
| ✅ EXACT | `Action_ThrowPass` | QB | `8` | `8` | 88 | START | 88 | 100 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–169
- **Visible Samples:** 161

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 21 | 22 | inferred_complete_timeline |
| `Action_SnapReceive` | 22 | 34 | 13 | inferred_complete_timeline |
| `Action_None` | 35 | 51 | 17 | inferred_complete_timeline |
| `Action_None` | 55 | 87 | 33 | inferred_complete_timeline |
| `Action_ThrowPass` | 88 | 100 | 13 | inferred_complete_timeline |
| `Action_None` | 101 | 161 | 61 | inferred_complete_timeline |
| `Action_None` | 168 | 169 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–99
- **Visible Samples:** 98

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 21 | 22 | inferred_complete_timeline |
| `Action_None` | 22 | 91 | 70 | inferred_complete_timeline |
| `Action_None` | 93 | 95 | 3 | inferred_complete_timeline |
| `Action_None` | 97 | 99 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–139
- **Visible Samples:** 140

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 34 | 35 | inferred_complete_timeline |
| `Action_RunPostRoute` | 35 | 139 | 105 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–112
- **Visible Samples:** 110

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 21 | 22 | inferred_complete_timeline |
| `Action_None` | 22 | 107 | 86 | inferred_complete_timeline |
| `Action_None` | 111 | 112 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–180
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 21 | 22 | inferred_complete_timeline |
| `Action_None` | 22 | 180 | 159 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–159
- **Visible Samples:** 159

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 21 | 22 | inferred_complete_timeline |
| `Action_None` | 22 | 36 | 15 | inferred_complete_timeline |
| `Action_None` | 38 | 159 | 122 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–175
- **Visible Samples:** 169

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 24 | 25 | inferred_complete_timeline |
| `Action_PassBlock` | 25 | 148 | 124 | inferred_complete_timeline |
| `Action_PassBlock` | 150 | 157 | 8 | inferred_complete_timeline |
| `Action_PassBlock` | 164 | 175 | 12 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–131
- **Visible Samples:** 122

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 24 | 25 | inferred_complete_timeline |
| `Action_PassBlock` | 25 | 119 | 95 | inferred_complete_timeline |
| `Action_PassBlock` | 130 | 131 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–169
- **Visible Samples:** 117

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 21 | 22 | inferred_complete_timeline |
| `Action_BallSnap` | 22 | 34 | 13 | inferred_complete_timeline |
| `Action_PassBlock` | 35 | 90 | 56 | inferred_complete_timeline |
| `Action_PassBlock` | 96 | 97 | 2 | inferred_complete_timeline |
| `Action_PassBlock` | 108 | 110 | 3 | inferred_complete_timeline |
| `Action_PassBlock` | 149 | 169 | 21 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `21`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–63
- **Visible Samples:** 64

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 24 | 25 | inferred_complete_timeline |
| `Action_PassBlock` | 25 | 63 | 39 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–41
- **Visible Samples:** 42

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 24 | 25 | inferred_complete_timeline |
| `Action_PassBlock` | 25 | 41 | 17 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–178
- **Visible Samples:** 169

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 21 | 22 | inferred_complete_timeline |
| `Action_None` | 22 | 107 | 86 | inferred_complete_timeline |
| `Action_None` | 118 | 178 | 61 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–152
- **Visible Samples:** 152

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 21 | 22 | inferred_complete_timeline |
| `Action_None` | 22 | 135 | 114 | inferred_complete_timeline |
| `Action_None` | 137 | 152 | 16 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `defense`
- **Visible Frames:** 0–178
- **Visible Samples:** 172

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 21 | 22 | inferred_complete_timeline |
| `Action_None` | 22 | 166 | 145 | inferred_complete_timeline |
| `Action_None` | 174 | 178 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–180
- **Visible Samples:** 169

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 21 | 22 | inferred_complete_timeline |
| `Action_None` | 22 | 120 | 99 | inferred_complete_timeline |
| `Action_None` | 127 | 165 | 39 | inferred_complete_timeline |
| `Action_None` | 170 | 171 | 2 | inferred_complete_timeline |
| `Action_None` | 174 | 180 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–180
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 21 | 22 | inferred_complete_timeline |
| `Action_None` | 22 | 180 | 159 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–165
- **Visible Samples:** 166

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 21 | 22 | inferred_complete_timeline |
| `Action_None` | 22 | 165 | 144 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–169
- **Visible Samples:** 166

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 21 | 22 | inferred_complete_timeline |
| `Action_None` | 22 | 160 | 139 | inferred_complete_timeline |
| `Action_None` | 165 | 169 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–180
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 21 | 22 | inferred_complete_timeline |
| `Action_None` | 22 | 180 | 159 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–180
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 21 | 22 | inferred_complete_timeline |
| `Action_None` | 22 | 180 | 159 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–169
- **Visible Samples:** 170

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 21 | 22 | inferred_complete_timeline |
| `Action_None` | 22 | 169 | 148 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–169
- **Visible Samples:** 170

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 21 | 22 | inferred_complete_timeline |
| `Action_None` | 22 | 169 | 148 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `22` | `22` | Position_Unknown | Team_Unknown | 32–37 | 5 | 2 | Undefined position; Undefined team |
| `23` | `23` | Position_Unknown | Team_Unknown | 57–180 | 97 | 8 | Undefined position; Undefined team |
| `24` | `24` | Position_Unknown | Team_Unknown | 77–180 | 86 | 4 | Undefined position; Undefined team |
| `25` | `25` | Position_Unknown | Team_Unknown | 108–110 | 3 | 1 | Undefined position; Undefined team |
| `26` | `26` | Position_Unknown | Team_Unknown | 126–146 | 19 | 2 | Undefined position; Undefined team |
| `27` | `27` | Position_Unknown | Team_Unknown | 138–146 | 9 | 1 | Undefined position; Undefined team |
| `28` | `28` | Position_Unknown | Team_Unknown | 140–141 | 2 | 1 | Undefined position; Undefined team |
| `29` | `29` | Position_Unknown | Team_Unknown | 155–156 | 2 | 1 | Undefined position; Undefined team |
| `30` | `30` | Position_Unknown | Team_Unknown | 160–165 | 6 | 1 | Undefined position; Undefined team |
| `31` | `31` | Position_Unknown | Team_Unknown | 160–175 | 16 | 1 | Undefined position; Undefined team |
| `32` | `36` | Position_Unknown | Team_Unknown | 167–169 | 3 | 1 | Undefined position; Undefined team |
| `33` | `37` | Position_Unknown | Team_Unknown | 167–180 | 13 | 2 | Undefined position; Undefined team |
| `34` | `40` | Position_Unknown | Team_Unknown | 170–180 | 11 | 1 | Undefined position; Undefined team |
| `35` | `41` | Position_Unknown | Team_Unknown | 170–180 | 11 | 1 | Undefined position; Undefined team |
| `36` | `42` | Position_Unknown | Team_Unknown | 170–175 | 6 | 1 | Undefined position; Undefined team |
| `37` | `43` | Position_Unknown | Team_Unknown | 171–180 | 10 | 1 | Undefined position; Undefined team |
| `38` | `46` | Position_Unknown | Team_Unknown | 173–180 | 8 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_PassBlock` and target `16` (4 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `19` (3 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `20` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `5` (actor_track_id `5`): `SAF1` position mapped to `defense` team
- ⚠️ Player track XML ID `6` (actor_track_id `6`): `SAF2` position mapped to `defense` team
- ⚠️ 17 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 17 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 34 |
| Missing visible bounding boxes during action | 71 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Resolved action overlap for track '16' (C): higher_priority='Action_BallSnap' [22–34], lower_priority='Action_PassBlock' annotated_start=25, effective_Action_PassBlock_start=35.
- ⚠️ Action 'Action_RunPostRoute' range [35-139] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [22-160] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [165-169] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [22-180] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [22-107] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [111-112] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [22-135] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [137-152] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [22-169] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [22-169] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [22-91] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [93-95] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [97-99] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [35-51] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [101-161] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [168-169] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [22-180] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [22-107] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [118-178] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [22-180] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [22-165] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [22-120] for track '13' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [127-165] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [170-171] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [174-180] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [22-36] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [38-159] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [22-180] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [35-90] for track '16' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [96-97] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [108-110] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [149-169] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [25-41] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [22-166] for track '18' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [174-178] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [25-148] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [150-157] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [164-175] for track '19' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [25-119] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [130-131] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [25-63] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [32-34] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [36-37] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [57-59] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [65-66] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [70-72] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [75-81] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [86-124] for track '23' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [127-165] for track '23' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [174-175] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [179-180] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [77-81] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [88-93] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [95-96] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [108-180] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [108-110] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [126-141] for track '26' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [144-146] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [138-146] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [140-141] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [155-156] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [160-165] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [160-175] for track '31' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [167-169] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [167-168] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [170-180] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [170-180] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [170-180] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [170-175] for track '36' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [171-180] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [173-180] for track '38' has 1 frames without a visible bounding box.
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
- ⚠️ Player track '38' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '38' has undefined team_side. Will map to Team_Unknown.

</details>