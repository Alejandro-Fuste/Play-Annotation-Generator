# Play-Annotation-Generator Annotation Review — Counter_102

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Counter_102`
- **Frame Range:** 0 to 329 (330 total frames)
- **Play:** `Play_Run_Counter`
- **Result:** `Result_OutOfBounds`
- **Result Frame:** 329
- **Player Tracks:** 32
- **Ball Tracks:** 0
- **Action Segments:** 88
- **Validation Warnings:** 94
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 19
- **Exact Matches:** 3
- **Group Expanded Events:** 8
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 1
- **Ambiguous Matches:** 5
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 69
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `9` | `Group` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallSnap` | C | offense | `14` | `13` |
| ❌ MISSING SEGMENT | `Action_DownBlock` | C | offense | `14` | `13` |
| ✅ EXACT | `Action_DownBlock` | LG | offense | `9` | `8` |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | RT | offense | `15` | `14` |
| ⚠️ AMBIGUOUS MATCH | `Action_PullLeadBlock` | RG | offense | `1` | `0` |
| ✅ EXACT | `Action_PlaySideFakeStep` | RB | offense | `6` | `5` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `5` | `4` |
| ⚠️ AMBIGUOUS MATCH | `Action_Handoff` | QB | offense | `5` | `4` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | offense | `6` | `5` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `1` | `Group` | 0 | START | 0 | 96 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `10` | `Group` | 0 | START | 0 | 92 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `14` | `Group` | 0 | START | 0 | 92 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `15` | `Group` | 0 | START | 0 | 96 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `5` | `Group` | 0 | START | 0 | 92 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `6` | `Group` | 0 | START | 0 | 111 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `7` | `Group` | 0 | START | 0 | 92 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `9` | `Group` | 0 | START | 0 | 96 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallSnap` | C | `14` | `13` | 93 | START | 93 | 104 |
| ❌ MISSING SEGMENT | `Action_DownBlock` | C | `14` | `13` | 97 | START | N/A | N/A |
| ✅ EXACT | `Action_DownBlock` | LG | `9` | `8` | 97 | START | 97 | 184 |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | RT | `15` | `14` | 97 | START | 97 | 119 |
| ⚠️ AMBIGUOUS MATCH | `Action_PullLeadBlock` | RG | `1` | `0` | 97 | START | 97 | 128 |
| ✅ EXACT | `Action_PlaySideFakeStep` | RB | `6` | `5` | 112 | START | 112 | 151 |
| ✅ EXACT | `Action_SnapReceive` | QB | `5` | `4` | 113 | END | 93 | 113 |
| ⚠️ AMBIGUOUS MATCH | `Action_Handoff` | QB | `5` | `4` | 126 | START | 126 | 142 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | `6` | `5` | 152 | START | 152 | 166 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 184 | BOUNDARY | N/A | N/A |

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
- **Visible Frames:** 0–259
- **Visible Samples:** 257

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 92 | 93 | inferred_complete_timeline |
| `Action_SnapReceive` | 93 | 113 | 21 | inferred_complete_timeline |
| `Action_None` | 114 | 125 | 12 | inferred_complete_timeline |
| `Action_Handoff` | 126 | 142 | 17 | inferred_complete_timeline |
| `Action_Handoff` | 146 | 151 | 6 | inferred_complete_timeline |
| `Action_None` | 152 | 259 | 108 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–329
- **Visible Samples:** 289

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 111 | 112 | inferred_complete_timeline |
| `Action_PlaySideFakeStep` | 112 | 151 | 40 | inferred_complete_timeline |
| `Action_BallCarry` | 152 | 166 | 15 | inferred_complete_timeline |
| `Action_BallCarry` | 172 | 173 | 2 | inferred_complete_timeline |
| `Action_BallCarry` | 203 | 215 | 13 | inferred_complete_timeline |
| `Action_BallCarry` | 219 | 301 | 83 | inferred_complete_timeline |
| `Action_BallCarry` | 306 | 329 | 24 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–194
- **Visible Samples:** 195

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 92 | 93 | inferred_complete_timeline |
| `Action_None` | 93 | 194 | 102 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–306
- **Visible Samples:** 307

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 92 | 93 | inferred_complete_timeline |
| `Action_None` | 93 | 306 | 214 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–265
- **Visible Samples:** 261

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 96 | 97 | inferred_complete_timeline |
| `Action_DownBlock` | 97 | 184 | 88 | inferred_complete_timeline |
| `Action_None` | 185 | 207 | 23 | inferred_complete_timeline |
| `Action_None` | 211 | 222 | 12 | inferred_complete_timeline |
| `Action_None` | 225 | 265 | 41 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–111
- **Visible Samples:** 111

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 92 | 93 | inferred_complete_timeline |
| `Action_BallSnap` | 93 | 104 | 12 | inferred_complete_timeline |
| `Action_BallSnap` | 106 | 111 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–157
- **Visible Samples:** 138

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 96 | 97 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 97 | 128 | 32 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 132 | 133 | 2 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 149 | 153 | 5 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 156 | 157 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–329
- **Visible Samples:** 319

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 96 | 97 | inferred_complete_timeline |
| `Action_PullBlock` | 97 | 119 | 23 | inferred_complete_timeline |
| `Action_PullBlock` | 123 | 131 | 9 | inferred_complete_timeline |
| `Action_PullBlock` | 134 | 184 | 51 | inferred_complete_timeline |
| `Action_None` | 185 | 241 | 57 | inferred_complete_timeline |
| `Action_None` | 245 | 261 | 17 | inferred_complete_timeline |
| `Action_None` | 264 | 270 | 7 | inferred_complete_timeline |
| `Action_None` | 272 | 329 | 58 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–182
- **Visible Samples:** 180

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 92 | 93 | inferred_complete_timeline |
| `Action_None` | 93 | 154 | 62 | inferred_complete_timeline |
| `Action_None` | 158 | 182 | 25 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 330

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 92 | 93 | inferred_complete_timeline |
| `Action_None` | 93 | 329 | 237 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–324
- **Visible Samples:** 323

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 92 | 93 | inferred_complete_timeline |
| `Action_None` | 93 | 186 | 94 | inferred_complete_timeline |
| `Action_None` | 189 | 324 | 136 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–326
- **Visible Samples:** 327

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 92 | 93 | inferred_complete_timeline |
| `Action_None` | 93 | 326 | 234 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–301
- **Visible Samples:** 302

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 92 | 93 | inferred_complete_timeline |
| `Action_None` | 93 | 301 | 209 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 330

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 92 | 93 | inferred_complete_timeline |
| `Action_None` | 93 | 329 | 237 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 328

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 92 | 93 | inferred_complete_timeline |
| `Action_None` | 93 | 192 | 100 | inferred_complete_timeline |
| `Action_None` | 195 | 329 | 135 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `15` | `16` | Position_Unknown | Team_Unknown | 114–143 | 28 | 3 | Undefined position; Undefined team |
| `16` | `17` | Position_Unknown | Team_Unknown | 145–329 | 183 | 2 | Undefined position; Undefined team |
| `17` | `18` | Position_Unknown | Team_Unknown | 148–329 | 182 | 1 | Undefined position; Undefined team |
| `18` | `21` | Position_Unknown | Team_Unknown | 169–308 | 140 | 1 | Undefined position; Undefined team |
| `19` | `22` | Position_Unknown | Team_Unknown | 176–205 | 28 | 2 | Undefined position; Undefined team |
| `20` | `25` | Position_Unknown | Team_Unknown | 185–258 | 68 | 3 | Undefined position; Undefined team |
| `21` | `26` | Position_Unknown | Team_Unknown | 191–329 | 139 | 1 | Undefined position; Undefined team |
| `22` | `28` | Position_Unknown | Team_Unknown | 199–269 | 56 | 5 | Undefined position; Undefined team |
| `23` | `29` | Position_Unknown | Team_Unknown | 201–235 | 34 | 2 | Undefined position; Undefined team |
| `24` | `30` | Position_Unknown | Team_Unknown | 205–329 | 125 | 1 | Undefined position; Undefined team |
| `25` | `31` | Position_Unknown | Team_Unknown | 237–329 | 92 | 2 | Undefined position; Undefined team |
| `26` | `32` | Position_Unknown | Team_Unknown | 251–329 | 79 | 1 | Undefined position; Undefined team |
| `27` | `36` | Position_Unknown | Team_Unknown | 280–281 | 2 | 1 | Undefined position; Undefined team |
| `28` | `39` | Position_Unknown | Team_Unknown | 285–329 | 31 | 2 | Undefined position; Undefined team |
| `29` | `43` | Position_Unknown | Team_Unknown | 296–329 | 22 | 4 | Undefined position; Undefined team |
| `30` | `47` | Position_Unknown | Team_Unknown | 325–329 | 5 | 1 | Undefined position; Undefined team |
| `31` | `50` | Position_Unknown | Team_Unknown | 328–329 | 2 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_BallSnap` and target `14` (2 segments found)
- ❌ Missing segment for action `Action_DownBlock` on target `14` (C)
- ⚠️ Ambiguous match for action `Action_PullBlock` and target `15` (3 segments found)
- ⚠️ Ambiguous match for action `Action_PullLeadBlock` and target `1` (4 segments found)
- ⚠️ Ambiguous match for action `Action_Handoff` and target `5` (2 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `6` (5 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `11` (actor_track_id `12`): `SAF` position mapped to `defense` team
- ⚠️ 17 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 17 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 34 |
| Missing visible bounding boxes during action | 58 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 329 as fallback play end.
- ⚠️ Resolved action overlap for track '13' (C): higher_priority='Action_BallSnap' [93–111], lower_priority='Action_DownBlock' annotated_start=97, effective_Action_DownBlock_start=112.
- ⚠️ Action 'Action_PullLeadBlock' range [97-128] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullLeadBlock' range [132-133] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullLeadBlock' range [149-153] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullLeadBlock' range [156-157] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [93-301] for track '1' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [93-329] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_SnapReceive' range [93-113] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_Handoff' range [126-142] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [152-259] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [152-166] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [172-173] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [203-215] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [219-301] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [93-306] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [93-154] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [158-182] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [185-207] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [211-222] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [225-265] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [93-194] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [93-186] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [189-324] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [93-192] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [93-326] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallSnap' range [93-104] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallSnap' range [106-111] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [97-119] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [123-131] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [185-241] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [245-261] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [264-270] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [114-123] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [125-136] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [138-143] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [145-210] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [169-308] for track '18' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [176-181] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [184-205] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [185-235] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [238-239] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [244-258] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [199-203] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [207-227] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [231-236] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [241-244] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [250-269] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [201-211] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [213-235] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [205-329] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [237-306] for track '25' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [280-281] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [285-289] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [304-329] for track '28' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [296-298] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [300-302] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [307-316] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [324-329] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [325-329] for track '30' has 1 frames without a visible bounding box.
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

</details>