# Play-Annotation-Generator Annotation Review — Counter_94

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Counter_94`
- **Frame Range:** 0 to 389 (390 total frames)
- **Play:** `Play_Run_Counter`
- **Result:** `Result_Tackle`
- **Result Frame:** 389
- **Player Tracks:** 34
- **Ball Tracks:** 0
- **Action Segments:** 85
- **Validation Warnings:** 99
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 18
- **Exact Matches:** 4
- **Group Expanded Events:** 8
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 4
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 63
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `9` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `14` | `13` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | C | offense | `14` | `13` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | LG | offense | `6` | `5` |
| ✅ EXACT | `Action_PullBlock` | RG | offense | `9` | `8` |
| ⚠️ AMBIGUOUS MATCH | `Action_PullLeadBlock` | TE | offense | `10` | `9` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `12` | `11` |
| ✅ EXACT | `Action_Handoff` | QB | offense | `12` | `11` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | offense | `5` | `4` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `1` | `Group` | 0 | START | 0 | 92 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `10` | `Group` | 0 | START | 0 | 95 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `12` | `Group` | 0 | START | 0 | 92 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `14` | `Group` | 0 | START | 0 | 92 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `5` | `Group` | 0 | START | 0 | 133 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `6` | `Group` | 0 | START | 0 | 95 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `7` | `Group` | 0 | START | 0 | 92 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `9` | `Group` | 0 | START | 0 | 95 |
| ✅ EXACT | `Action_BallSnap` | C | `14` | `13` | 93 | START | 93 | 106 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | C | `14` | `13` | 96 | START | 107 | 109 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | LG | `6` | `5` | 96 | START | 96 | 115 |
| ✅ EXACT | `Action_PullBlock` | RG | `9` | `8` | 96 | START | 96 | 190 |
| ⚠️ AMBIGUOUS MATCH | `Action_PullLeadBlock` | TE | `10` | `9` | 96 | START | 96 | 127 |
| ✅ EXACT | `Action_SnapReceive` | QB | `12` | `11` | 106 | END | 93 | 106 |
| ✅ EXACT | `Action_Handoff` | QB | `12` | `11` | 114 | START | 114 | 133 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | `5` | `4` | 134 | START | 134 | 134 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 192 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–176
- **Visible Samples:** 177

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 92 | 93 | inferred_complete_timeline |
| `Action_SnapReceive` | 93 | 106 | 14 | inferred_complete_timeline |
| `Action_None` | 107 | 113 | 7 | inferred_complete_timeline |
| `Action_Handoff` | 114 | 133 | 20 | inferred_complete_timeline |
| `Action_None` | 134 | 176 | 43 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–356
- **Visible Samples:** 347

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 133 | 134 | inferred_complete_timeline |
| `Action_BallCarry` | 134 | 134 | 1 | inferred_complete_timeline |
| `Action_BallCarry` | 136 | 344 | 209 | inferred_complete_timeline |
| `Action_BallCarry` | 354 | 356 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–389
- **Visible Samples:** 376

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 95 | 96 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 96 | 127 | 32 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 131 | 192 | 62 | inferred_complete_timeline |
| `Action_None` | 193 | 198 | 6 | inferred_complete_timeline |
| `Action_None` | 209 | 219 | 11 | inferred_complete_timeline |
| `Action_None` | 221 | 389 | 169 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–389
- **Visible Samples:** 355

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 92 | 93 | inferred_complete_timeline |
| `Action_None` | 93 | 137 | 45 | inferred_complete_timeline |
| `Action_None` | 152 | 174 | 23 | inferred_complete_timeline |
| `Action_None` | 176 | 222 | 47 | inferred_complete_timeline |
| `Action_None` | 243 | 389 | 147 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–284
- **Visible Samples:** 281

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 95 | 96 | inferred_complete_timeline |
| `Action_DownBlock` | 96 | 115 | 20 | inferred_complete_timeline |
| `Action_DownBlock` | 118 | 192 | 75 | inferred_complete_timeline |
| `Action_None` | 193 | 248 | 56 | inferred_complete_timeline |
| `Action_None` | 251 | 284 | 34 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–113
- **Visible Samples:** 112

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 92 | 93 | inferred_complete_timeline |
| `Action_BallSnap` | 93 | 106 | 14 | inferred_complete_timeline |
| `Action_DownBlock` | 107 | 109 | 3 | inferred_complete_timeline |
| `Action_DownBlock` | 112 | 113 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–389
- **Visible Samples:** 388

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 95 | 96 | inferred_complete_timeline |
| `Action_PullBlock` | 96 | 190 | 95 | inferred_complete_timeline |
| `Action_None` | 193 | 389 | 197 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–389
- **Visible Samples:** 390

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 92 | 93 | inferred_complete_timeline |
| `Action_None` | 93 | 389 | 297 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–389
- **Visible Samples:** 378

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 92 | 93 | inferred_complete_timeline |
| `Action_None` | 93 | 219 | 127 | inferred_complete_timeline |
| `Action_None` | 232 | 389 | 158 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–107
- **Visible Samples:** 108

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 92 | 93 | inferred_complete_timeline |
| `Action_None` | 93 | 107 | 15 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–152
- **Visible Samples:** 123

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 92 | 93 | inferred_complete_timeline |
| `Action_None` | 93 | 111 | 19 | inferred_complete_timeline |
| `Action_None` | 142 | 152 | 11 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–101
- **Visible Samples:** 102

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 92 | 93 | inferred_complete_timeline |
| `Action_None` | 93 | 101 | 9 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–334
- **Visible Samples:** 307

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 92 | 93 | inferred_complete_timeline |
| `Action_None` | 93 | 155 | 63 | inferred_complete_timeline |
| `Action_None` | 183 | 203 | 21 | inferred_complete_timeline |
| `Action_None` | 205 | 334 | 130 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–186
- **Visible Samples:** 187

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 92 | 93 | inferred_complete_timeline |
| `Action_None` | 93 | 186 | 94 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–99
- **Visible Samples:** 90

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 45 | 46 | inferred_complete_timeline |
| `Action_PreSnap` | 56 | 92 | 37 | inferred_complete_timeline |
| `Action_None` | 93 | 99 | 7 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `15` | `16` | Position_Unknown | Team_Unknown | 104–131 | 28 | 1 | Undefined position; Undefined team |
| `16` | `17` | Position_Unknown | Team_Unknown | 111–122 | 12 | 1 | Undefined position; Undefined team |
| `17` | `18` | Position_Unknown | Team_Unknown | 116–149 | 33 | 2 | Undefined position; Undefined team |
| `18` | `19` | Position_Unknown | Team_Unknown | 118–342 | 216 | 3 | Undefined position; Undefined team |
| `19` | `21` | Position_Unknown | Team_Unknown | 125–145 | 21 | 1 | Undefined position; Undefined team |
| `20` | `23` | Position_Unknown | Team_Unknown | 130–366 | 227 | 3 | Undefined position; Undefined team |
| `21` | `24` | Position_Unknown | Team_Unknown | 142–274 | 133 | 1 | Undefined position; Undefined team |
| `22` | `25` | Position_Unknown | Team_Unknown | 154–322 | 169 | 1 | Undefined position; Undefined team |
| `23` | `26` | Position_Unknown | Team_Unknown | 162–174 | 9 | 2 | Undefined position; Undefined team |
| `24` | `27` | Position_Unknown | Team_Unknown | 173–174 | 2 | 1 | Undefined position; Undefined team |
| `25` | `28` | Position_Unknown | Team_Unknown | 175–389 | 215 | 1 | Undefined position; Undefined team |
| `26` | `29` | Position_Unknown | Team_Unknown | 179–389 | 211 | 1 | Undefined position; Undefined team |
| `27` | `30` | Position_Unknown | Team_Unknown | 191–386 | 195 | 2 | Undefined position; Undefined team |
| `28` | `31` | Position_Unknown | Team_Unknown | 216–267 | 52 | 1 | Undefined position; Undefined team |
| `29` | `35` | Position_Unknown | Team_Unknown | 272–374 | 97 | 5 | Undefined position; Undefined team |
| `30` | `37` | Position_Unknown | Team_Unknown | 329–351 | 11 | 2 | Undefined position; Undefined team |
| `31` | `38` | Position_Unknown | Team_Unknown | 342–389 | 32 | 2 | Undefined position; Undefined team |
| `32` | `41` | Position_Unknown | Team_Unknown | 356–389 | 34 | 1 | Undefined position; Undefined team |
| `33` | `42` | Position_Unknown | Team_Unknown | 383–389 | 7 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_DownBlock` and target `14` (2 segments found)
- ⚠️ Ambiguous match for action `Action_DownBlock` and target `6` (2 segments found)
- ⚠️ Ambiguous match for action `Action_PullLeadBlock` and target `10` (2 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `5` (3 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `7` (actor_track_id `8`): `SAF` position mapped to `defense` team
- ⚠️ 19 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 19 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 38 |
| Missing visible bounding boxes during action | 57 |
| Track-related warning | 3 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 389 as fallback play end.
- ⚠️ Validation warning: Action 'Action_DownBlock' for track '5' (LG) duration 97 frames exceeds threshold 90 frames [start=96, end=192].
- ⚠️ Validation warning: Action 'Action_PullBlock' for track '8' (RG) duration 97 frames exceeds threshold 90 frames [start=96, end=192].
- ⚠️ Resolved action overlap for track '13' (C): higher_priority='Action_BallSnap' [93–106], lower_priority='Action_DownBlock' annotated_start=96, effective_Action_DownBlock_start=107.
- ⚠️ Action 'Action_None' range [93-137] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [152-174] for track '0' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [176-222] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [93-219] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [93-186] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [93-155] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [183-203] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [205-334] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' for track '4' starts at frame 134, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_BallCarry' range [134-134] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [136-344] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [354-356] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [96-115] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [193-248] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [251-284] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [93-389] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-45] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [93-99] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [96-190] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullLeadBlock' range [96-127] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [193-198] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [209-219] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [93-111] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [142-152] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [134-176] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [93-101] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [107-109] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [112-113] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [93-107] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [104-131] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [111-122] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [116-145] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [147-149] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [118-219] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [224-230] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [236-342] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [125-145] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [130-170] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [178-361] for track '20' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [365-366] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [142-274] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [154-322] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [162-167] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [172-174] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [173-174] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [191-240] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [242-386] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [216-267] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [272-349] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [351-353] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [355-360] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [364-366] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [368-374] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [329-330] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [343-351] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [342-343] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [383-389] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Player track '15' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '15' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '16' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '16' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '17' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '17' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '18' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '18' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '19' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '19' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '20' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '20' has undefined team_side. Will map to Team_Unknown.
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