# Play-Annotation-Generator Annotation Review — Counter_92

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Counter_92`
- **Frame Range:** 0 to 359 (360 total frames)
- **Play:** `Play_Run_Counter`
- **Result:** `Result_OutOfBounds`
- **Result Frame:** 359
- **Player Tracks:** 36
- **Ball Tracks:** 0
- **Action Segments:** 80
- **Validation Warnings:** 95
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 20
- **Exact Matches:** 8
- **Group Expanded Events:** 8
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 2
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 60
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `7` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `10` | `9` |
| ✅ EXACT | `Action_DownBlock` | TE | offense | `1` | `0` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | C | offense | `10` | `9` |
| ✅ EXACT | `Action_DownBlock` | RG | offense | `4` | `3` |
| ✅ EXACT | `Action_PullBlock` | LG | offense | `7` | `6` |
| ✅ EXACT | `Action_PullLeadBlock` | LT | offense | `3` | `2` |
| ⚠️ AMBIGUOUS MATCH | `Action_PlaySideFakeStep` | RB | offense | `6` | `5` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `5` | `4` |
| ✅ EXACT | `Action_Handoff` | QB | offense | `5` | `4` |
| ✅ EXACT | `Action_BallCarry` | RB | offense | `6` | `5` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `1` | `Group` | 0 | START | 0 | 75 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `10` | `Group` | 0 | START | 0 | 74 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `2` | `Group` | 0 | START | 0 | 74 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `3` | `Group` | 0 | START | 0 | 75 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `4` | `Group` | 0 | START | 0 | 75 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `5` | `Group` | 0 | START | 0 | 74 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `6` | `Group` | 0 | START | 0 | 85 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `7` | `Group` | 0 | START | 0 | 75 |
| ✅ EXACT | `Action_BallSnap` | C | `10` | `9` | 75 | START | 75 | 93 |
| ✅ EXACT | `Action_DownBlock` | TE | `1` | `0` | 76 | START | 76 | 138 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | C | `10` | `9` | 76 | START | 94 | 122 |
| ✅ EXACT | `Action_DownBlock` | RG | `4` | `3` | 76 | START | 76 | 181 |
| ✅ EXACT | `Action_PullBlock` | LG | `7` | `6` | 76 | START | 76 | 181 |
| ✅ EXACT | `Action_PullLeadBlock` | LT | `3` | `2` | 76 | START | 76 | 181 |
| ⚠️ AMBIGUOUS MATCH | `Action_PlaySideFakeStep` | RB | `6` | `5` | 86 | START | 86 | 125 |
| ✅ EXACT | `Action_SnapReceive` | QB | `5` | `4` | 93 | END | 75 | 93 |
| ✅ EXACT | `Action_Handoff` | QB | `5` | `4` | 105 | START | 105 | 128 |
| ✅ EXACT | `Action_BallCarry` | RB | `6` | `5` | 129 | START | 129 | 359 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 181 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–202
- **Visible Samples:** 203

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 74 | 75 | inferred_complete_timeline |
| `Action_SnapReceive` | 75 | 93 | 19 | inferred_complete_timeline |
| `Action_None` | 94 | 104 | 11 | inferred_complete_timeline |
| `Action_Handoff` | 105 | 128 | 24 | inferred_complete_timeline |
| `Action_None` | 129 | 202 | 74 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–359
- **Visible Samples:** 358

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 85 | 86 | inferred_complete_timeline |
| `Action_PlaySideFakeStep` | 86 | 125 | 40 | inferred_complete_timeline |
| `Action_PlaySideFakeStep` | 128 | 128 | 1 | inferred_complete_timeline |
| `Action_BallCarry` | 129 | 359 | 231 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 150

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 75 | 76 | inferred_complete_timeline |
| `Action_DownBlock` | 76 | 138 | 63 | inferred_complete_timeline |
| `Action_None` | 229 | 239 | 11 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–258
- **Visible Samples:** 259

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 75 | 76 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 76 | 181 | 106 | inferred_complete_timeline |
| `Action_None` | 182 | 258 | 77 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–252
- **Visible Samples:** 253

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 75 | 76 | inferred_complete_timeline |
| `Action_PullBlock` | 76 | 181 | 106 | inferred_complete_timeline |
| `Action_None` | 182 | 252 | 71 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–252
- **Visible Samples:** 252

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 74 | 75 | inferred_complete_timeline |
| `Action_BallSnap` | 75 | 93 | 19 | inferred_complete_timeline |
| `Action_DownBlock` | 94 | 122 | 29 | inferred_complete_timeline |
| `Action_DownBlock` | 124 | 181 | 58 | inferred_complete_timeline |
| `Action_None` | 182 | 252 | 71 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–260
- **Visible Samples:** 261

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 75 | 76 | inferred_complete_timeline |
| `Action_DownBlock` | 76 | 181 | 106 | inferred_complete_timeline |
| `Action_None` | 182 | 260 | 79 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–262
- **Visible Samples:** 263

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 74 | 75 | inferred_complete_timeline |
| `Action_None` | 75 | 262 | 188 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–285
- **Visible Samples:** 282

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 74 | 75 | inferred_complete_timeline |
| `Action_None` | 75 | 184 | 110 | inferred_complete_timeline |
| `Action_None` | 189 | 285 | 97 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–263
- **Visible Samples:** 256

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 74 | 75 | inferred_complete_timeline |
| `Action_None` | 75 | 96 | 22 | inferred_complete_timeline |
| `Action_None` | 99 | 106 | 8 | inferred_complete_timeline |
| `Action_None` | 110 | 140 | 31 | inferred_complete_timeline |
| `Action_None` | 144 | 263 | 120 | inferred_complete_timeline |

</details>

<details>
<summary>DT — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–139
- **Visible Samples:** 128

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 74 | 75 | inferred_complete_timeline |
| `Action_None` | 75 | 115 | 41 | inferred_complete_timeline |
| `Action_None` | 125 | 131 | 7 | inferred_complete_timeline |
| `Action_None` | 133 | 135 | 3 | inferred_complete_timeline |
| `Action_None` | 138 | 139 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–359
- **Visible Samples:** 360

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 74 | 75 | inferred_complete_timeline |
| `Action_None` | 75 | 359 | 285 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–134
- **Visible Samples:** 135

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 74 | 75 | inferred_complete_timeline |
| `Action_None` | 75 | 134 | 60 | inferred_complete_timeline |

</details>

<details>
<summary>LB3 — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–346
- **Visible Samples:** 347

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 74 | 75 | inferred_complete_timeline |
| `Action_None` | 75 | 346 | 272 | inferred_complete_timeline |

</details>

<details>
<summary>CB — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–57
- **Visible Samples:** 58

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 57 | 58 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–295
- **Visible Samples:** 296

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 74 | 75 | inferred_complete_timeline |
| `Action_None` | 75 | 295 | 221 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `16` | `17` | Position_Unknown | Team_Unknown | 118–119 | 2 | 1 | Undefined position; Undefined team |
| `17` | `20` | Position_Unknown | Team_Unknown | 145–359 | 210 | 2 | Undefined position; Undefined team |
| `18` | `21` | Position_Unknown | Team_Unknown | 147–164 | 13 | 2 | Undefined position; Undefined team |
| `19` | `22` | Position_Unknown | Team_Unknown | 147–260 | 114 | 1 | Undefined position; Undefined team |
| `20` | `25` | Position_Unknown | Team_Unknown | 164–274 | 111 | 1 | Undefined position; Undefined team |
| `21` | `26` | Position_Unknown | Team_Unknown | 165–359 | 195 | 1 | Undefined position; Undefined team |
| `22` | `27` | Position_Unknown | Team_Unknown | 168–355 | 188 | 1 | Undefined position; Undefined team |
| `23` | `28` | Position_Unknown | Team_Unknown | 169–347 | 175 | 2 | Undefined position; Undefined team |
| `24` | `29` | Position_Unknown | Team_Unknown | 172–223 | 43 | 2 | Undefined position; Undefined team |
| `25` | `30` | Position_Unknown | Team_Unknown | 179–359 | 181 | 1 | Undefined position; Undefined team |
| `26` | `31` | Position_Unknown | Team_Unknown | 223–225 | 3 | 1 | Undefined position; Undefined team |
| `27` | `34` | Position_Unknown | Team_Unknown | 233–359 | 126 | 2 | Undefined position; Undefined team |
| `28` | `35` | Position_Unknown | Team_Unknown | 249–292 | 44 | 1 | Undefined position; Undefined team |
| `29` | `37` | Position_Unknown | Team_Unknown | 259–260 | 2 | 1 | Undefined position; Undefined team |
| `30` | `40` | Position_Unknown | Team_Unknown | 314–350 | 30 | 4 | Undefined position; Undefined team |
| `31` | `41` | Position_Unknown | Team_Unknown | 321–359 | 4 | 2 | Undefined position; Undefined team |
| `32` | `43` | Position_Unknown | Team_Unknown | 347–359 | 13 | 1 | Undefined position; Undefined team |
| `33` | `44` | Position_Unknown | Team_Unknown | 348–357 | 8 | 2 | Undefined position; Undefined team |
| `34` | `46` | Position_Unknown | Team_Unknown | 358–359 | 2 | 1 | Undefined position; Undefined team |
| `35` | `47` | Position_Unknown | Team_Unknown | 358–359 | 2 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_DownBlock` and target `10` (2 segments found)
- ⚠️ Ambiguous match for action `Action_PlaySideFakeStep` and target `6` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `12` (actor_track_id `13`): `SAF` position mapped to `defense` team
- ⚠️ 20 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 20 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 40 |
| Missing visible bounding boxes during action | 49 |
| Track-related warning | 5 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 359 as fallback play end.
- ⚠️ Validation warning: Action 'Action_DownBlock' for track '0' (TE) duration 106 frames exceeds threshold 90 frames [start=76, end=181].
- ⚠️ Validation warning: Action 'Action_DownBlock' for track '3' (RG) duration 106 frames exceeds threshold 90 frames [start=76, end=181].
- ⚠️ Validation warning: Action 'Action_PullBlock' for track '6' (LG) duration 106 frames exceeds threshold 90 frames [start=76, end=181].
- ⚠️ Validation warning: Action 'Action_DownBlock' for track '9' (C) duration 106 frames exceeds threshold 90 frames [start=76, end=181].
- ⚠️ Resolved action overlap for track '9' (C): higher_priority='Action_BallSnap' [75–93], lower_priority='Action_DownBlock' annotated_start=76, effective_Action_DownBlock_start=94.
- ⚠️ Action 'Action_DownBlock' range [76-138] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [229-239] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [75-262] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [182-258] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [182-260] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [129-202] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PlaySideFakeStep' range [86-125] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [129-359] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [182-252] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-57] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [75-96] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [99-106] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [110-140] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [144-263] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [94-122] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [124-181] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [182-252] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [75-184] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [189-285] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [75-295] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [75-134] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [75-115] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [125-131] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [133-135] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [138-139] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [75-346] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [118-119] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [145-351] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [147-157] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [163-164] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [147-260] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [164-274] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [168-355] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [169-337] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [342-347] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [172-212] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [222-223] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [223-225] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [233-350] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [249-292] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [259-260] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [314-329] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [331-332] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [335-340] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [345-350] for track '30' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [321-322] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [358-359] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [348-350] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [353-357] for track '33' has 1 frames without a visible bounding box.
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
- ⚠️ Player track '34' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '34' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '35' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '35' has undefined team_side. Will map to Team_Unknown.

</details>