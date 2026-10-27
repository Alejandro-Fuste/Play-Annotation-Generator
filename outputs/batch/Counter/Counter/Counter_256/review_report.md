# Play-Annotation-Generator Annotation Review — Counter_256

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Counter_256`
- **Frame Range:** 0 to 359 (360 total frames)
- **Play:** `Play_Run_Counter`
- **Result:** `Result_OutOfBounds`
- **Result Frame:** 359
- **Player Tracks:** 31
- **Ball Tracks:** 0
- **Action Segments:** 120
- **Validation Warnings:** 119
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 21
- **Exact Matches:** 4
- **Group Expanded Events:** 9
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 1
- **Ambiguous Matches:** 5
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 93
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `8` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `9` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `11` | `10` |
| ❌ MISSING SEGMENT | `Action_DownBlock` | C | offense | `11` | `10` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | DE2 | defense | `3` | `2` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | LT | offense | `6` | `5` |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | RG | offense | `7` | `6` |
| ⚠️ AMBIGUOUS MATCH | `Action_PullLeadBlock` | C | offense | `11` | `10` |
| ⚠️ AMBIGUOUS MATCH | `Action_PlaySideFakeStep` | RB | offense | `9` | `8` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `5` | `4` |
| ✅ EXACT | `Action_Handoff` | QB | offense | `5` | `4` |
| ✅ EXACT | `Action_BallCarry` | RB | offense | `9` | `8` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | `1` | `Group` | 0 | START | 0 | 130 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `11` | `Group` | 0 | START | 0 | 89 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `13` | `Group` | 0 | START | 0 | 73 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | `4` | `Group` | 0 | START | 0 | 130 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `5` | `Group` | 0 | START | 0 | 82 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `6` | `Group` | 0 | START | 0 | 132 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `7` | `Group` | 0 | START | 0 | 132 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `8` | `Group` | 0 | START | 0 | 130 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `9` | `Group` | 0 | START | 0 | 69 |
| ✅ EXACT | `Action_BallSnap` | C | `11` | `10` | 131 | START | 131 | 145 |
| ❌ MISSING SEGMENT | `Action_DownBlock` | C | `11` | `10` | 133 | START | N/A | N/A |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | DE2 | `3` | `2` | 133 | START | 133 | 149 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | LT | `6` | `5` | 133 | START | 133 | 156 |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | RG | `7` | `6` | 133 | START | 133 | 165 |
| ⚠️ AMBIGUOUS MATCH | `Action_PullLeadBlock` | C | `11` | `10` | 133 | START | 146 | 151 |
| ⚠️ AMBIGUOUS MATCH | `Action_PlaySideFakeStep` | RB | `9` | `8` | 140 | START | 140 | 173 |
| ✅ EXACT | `Action_SnapReceive` | QB | `5` | `4` | 145 | END | 131 | 145 |
| ✅ EXACT | `Action_Handoff` | QB | `5` | `4` | 160 | START | 160 | 177 |
| ✅ EXACT | `Action_BallCarry` | RB | `9` | `8` | 178 | START | 178 | 209 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 217 | BOUNDARY | N/A | N/A |

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
- **Visible Frames:** 0–359
- **Visible Samples:** 311

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 82 | 83 | inferred_complete_timeline |
| `Action_PreSnap` | 85 | 130 | 46 | inferred_complete_timeline |
| `Action_SnapReceive` | 131 | 145 | 15 | inferred_complete_timeline |
| `Action_None` | 146 | 159 | 14 | inferred_complete_timeline |
| `Action_Handoff` | 160 | 177 | 18 | inferred_complete_timeline |
| `Action_None` | 178 | 201 | 24 | inferred_complete_timeline |
| `Action_None` | 234 | 240 | 7 | inferred_complete_timeline |
| `Action_None` | 246 | 264 | 19 | inferred_complete_timeline |
| `Action_None` | 275 | 359 | 85 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–209
- **Visible Samples:** 202

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 69 | 70 | inferred_complete_timeline |
| `Action_PreSnap` | 75 | 139 | 65 | inferred_complete_timeline |
| `Action_PlaySideFakeStep` | 140 | 173 | 34 | inferred_complete_timeline |
| `Action_PlaySideFakeStep` | 177 | 177 | 1 | inferred_complete_timeline |
| `Action_BallCarry` | 178 | 209 | 32 | inferred_complete_timeline |

</details>

<details>
<summary>TE1 — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–359
- **Visible Samples:** 360

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 130 | 131 | inferred_complete_timeline |
| `Action_None` | 131 | 359 | 229 | inferred_complete_timeline |

</details>

<details>
<summary>TE2 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–359
- **Visible Samples:** 353

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 130 | 131 | inferred_complete_timeline |
| `Action_None` | 131 | 188 | 58 | inferred_complete_timeline |
| `Action_None` | 191 | 239 | 49 | inferred_complete_timeline |
| `Action_None` | 245 | 359 | 115 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–245
- **Visible Samples:** 236

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 132 | 133 | inferred_complete_timeline |
| `Action_DownBlock` | 133 | 156 | 24 | inferred_complete_timeline |
| `Action_DownBlock` | 158 | 159 | 2 | inferred_complete_timeline |
| `Action_DownBlock` | 161 | 163 | 3 | inferred_complete_timeline |
| `Action_DownBlock` | 166 | 198 | 33 | inferred_complete_timeline |
| `Action_DownBlock` | 205 | 217 | 13 | inferred_complete_timeline |
| `Action_None` | 218 | 245 | 28 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–350
- **Visible Samples:** 269

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 73 | 74 | inferred_complete_timeline |
| `Action_PreSnap` | 75 | 130 | 56 | inferred_complete_timeline |
| `Action_None` | 131 | 162 | 32 | inferred_complete_timeline |
| `Action_None` | 165 | 169 | 5 | inferred_complete_timeline |
| `Action_None` | 195 | 209 | 15 | inferred_complete_timeline |
| `Action_None` | 237 | 255 | 19 | inferred_complete_timeline |
| `Action_None` | 281 | 340 | 60 | inferred_complete_timeline |
| `Action_None` | 343 | 350 | 8 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–355
- **Visible Samples:** 329

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 89 | 90 | inferred_complete_timeline |
| `Action_PreSnap` | 91 | 130 | 40 | inferred_complete_timeline |
| `Action_BallSnap` | 131 | 145 | 15 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 146 | 151 | 6 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 159 | 175 | 17 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 185 | 217 | 33 | inferred_complete_timeline |
| `Action_None` | 218 | 256 | 39 | inferred_complete_timeline |
| `Action_None` | 264 | 297 | 34 | inferred_complete_timeline |
| `Action_None` | 301 | 355 | 55 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–359
- **Visible Samples:** 356

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 132 | 133 | inferred_complete_timeline |
| `Action_PullBlock` | 133 | 165 | 33 | inferred_complete_timeline |
| `Action_PullBlock` | 170 | 217 | 48 | inferred_complete_timeline |
| `Action_None` | 218 | 359 | 142 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–359
- **Visible Samples:** 325

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 130 | 131 | inferred_complete_timeline |
| `Action_None` | 131 | 213 | 83 | inferred_complete_timeline |
| `Action_None` | 218 | 272 | 55 | inferred_complete_timeline |
| `Action_None` | 280 | 281 | 2 | inferred_complete_timeline |
| `Action_None` | 283 | 287 | 5 | inferred_complete_timeline |
| `Action_None` | 290 | 291 | 2 | inferred_complete_timeline |
| `Action_None` | 311 | 327 | 17 | inferred_complete_timeline |
| `Action_None` | 330 | 359 | 30 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–220
- **Visible Samples:** 213

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 130 | 131 | inferred_complete_timeline |
| `Action_None` | 131 | 185 | 55 | inferred_complete_timeline |
| `Action_None` | 194 | 220 | 27 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–317
- **Visible Samples:** 317

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 132 | 133 | inferred_complete_timeline |
| `Action_DownBlock` | 133 | 149 | 17 | inferred_complete_timeline |
| `Action_DownBlock` | 151 | 217 | 67 | inferred_complete_timeline |
| `Action_None` | 218 | 317 | 100 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–162
- **Visible Samples:** 127

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 70 | 71 | inferred_complete_timeline |
| `Action_PreSnap` | 78 | 130 | 53 | inferred_complete_timeline |
| `Action_None` | 131 | 131 | 1 | inferred_complete_timeline |
| `Action_None` | 161 | 162 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–313
- **Visible Samples:** 258

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 34 | 35 | inferred_complete_timeline |
| `Action_PreSnap` | 37 | 38 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 40 | 70 | 31 | inferred_complete_timeline |
| `Action_PreSnap` | 73 | 85 | 13 | inferred_complete_timeline |
| `Action_PreSnap` | 92 | 94 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 98 | 130 | 33 | inferred_complete_timeline |
| `Action_None` | 131 | 141 | 11 | inferred_complete_timeline |
| `Action_None` | 153 | 169 | 17 | inferred_complete_timeline |
| `Action_None` | 177 | 226 | 50 | inferred_complete_timeline |
| `Action_None` | 228 | 230 | 3 | inferred_complete_timeline |
| `Action_None` | 238 | 260 | 23 | inferred_complete_timeline |
| `Action_None` | 276 | 278 | 3 | inferred_complete_timeline |
| `Action_None` | 280 | 313 | 34 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–191
- **Visible Samples:** 192

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 130 | 131 | inferred_complete_timeline |
| `Action_None` | 131 | 191 | 61 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–302
- **Visible Samples:** 273

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 130 | 131 | inferred_complete_timeline |
| `Action_None` | 131 | 198 | 68 | inferred_complete_timeline |
| `Action_None` | 211 | 218 | 8 | inferred_complete_timeline |
| `Action_None` | 232 | 238 | 7 | inferred_complete_timeline |
| `Action_None` | 244 | 302 | 59 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–22
- **Visible Samples:** 23

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 22 | 23 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `16` | `17` | Position_Unknown | Team_Unknown | 31–359 | 289 | 4 | Undefined position; Undefined team |
| `17` | `18` | Position_Unknown | Team_Unknown | 102–256 | 155 | 2 | Undefined position; Undefined team |
| `18` | `19` | Position_Unknown | Team_Unknown | 164–165 | 2 | 1 | Undefined position; Undefined team |
| `19` | `20` | Position_Unknown | Team_Unknown | 199–332 | 128 | 3 | Undefined position; Undefined team |
| `20` | `21` | Position_Unknown | Team_Unknown | 204–359 | 113 | 3 | Undefined position; Undefined team |
| `21` | `22` | Position_Unknown | Team_Unknown | 212–346 | 122 | 2 | Undefined position; Undefined team |
| `22` | `23` | Position_Unknown | Team_Unknown | 216–331 | 104 | 4 | Undefined position; Undefined team |
| `23` | `24` | Position_Unknown | Team_Unknown | 228–359 | 132 | 1 | Undefined position; Undefined team |
| `24` | `25` | Position_Unknown | Team_Unknown | 228–359 | 131 | 2 | Undefined position; Undefined team |
| `25` | `26` | Position_Unknown | Team_Unknown | 235–359 | 122 | 2 | Undefined position; Undefined team |
| `26` | `27` | Position_Unknown | Team_Unknown | 250–281 | 30 | 2 | Undefined position; Undefined team |
| `27` | `28` | Position_Unknown | Team_Unknown | 262–359 | 82 | 3 | Undefined position; Undefined team |
| `28` | `31` | Position_Unknown | Team_Unknown | 313–316 | 4 | 1 | Undefined position; Undefined team |
| `29` | `32` | Position_Unknown | Team_Unknown | 338–358 | 21 | 1 | Undefined position; Undefined team |
| `30` | `33` | Position_Unknown | Team_Unknown | 344–345 | 2 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ❌ Missing segment for action `Action_DownBlock` on target `11` (C)
- ⚠️ Ambiguous match for action `Action_DownBlock` and target `3` (2 segments found)
- ⚠️ Ambiguous match for action `Action_DownBlock` and target `6` (5 segments found)
- ⚠️ Ambiguous match for action `Action_PullBlock` and target `7` (2 segments found)
- ⚠️ Ambiguous match for action `Action_PullLeadBlock` and target `11` (3 segments found)
- ⚠️ Ambiguous match for action `Action_PlaySideFakeStep` and target `9` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `15` (actor_track_id `16`): `SAF` position mapped to `defense` team
- ⚠️ 15 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 15 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 30 |
| Missing visible bounding boxes during action | 86 |
| Track-related warning | 2 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 359 as fallback play end.
- ⚠️ Overlapping action conflict at frame 133 for track '10': 'Action_DownBlock' vs 'Action_PullLeadBlock'. Overriding with 'Action_PullLeadBlock'.
- ⚠️ Resolved action overlap for track '10' (C): higher_priority='Action_BallSnap' [131–145], lower_priority='Action_PullLeadBlock' annotated_start=133, effective_Action_PullLeadBlock_start=146.
- ⚠️ Action 'Action_None' range [131-188] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [191-239] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [131-198] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [211-218] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [232-238] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [244-302] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [133-149] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [218-317] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-82] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [178-201] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [234-240] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [246-264] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [133-156] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [158-159] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [161-163] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [166-198] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [218-245] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [133-165] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [131-213] for track '7' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [218-272] for track '7' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [280-281] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [283-287] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [290-291] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [311-327] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-69] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PlaySideFakeStep' range [140-173] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [178-209] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [131-191] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-89] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [91-130] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullLeadBlock' range [146-151] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullLeadBlock' range [159-175] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [218-256] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [264-297] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [301-355] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [131-185] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [194-220] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-73] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [131-162] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [165-169] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [195-209] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [237-255] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [281-340] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [343-350] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-70] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' for track '13' starts at frame 131, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_None' range [131-131] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [161-162] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-34] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [37-38] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [40-70] for track '14' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [73-85] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [92-94] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [131-141] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [153-169] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [177-226] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [228-230] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [238-260] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [276-278] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [280-313] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-22] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [131-154] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [171-244] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [131-256] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [164-165] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [199-224] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [226-253] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [259-332] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [204-223] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [260-289] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [212-266] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [280-346] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [216-241] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [245-305] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [312-313] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [317-331] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [228-359] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [228-346] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [235-320] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [250-276] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [279-281] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [262-280] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [290-316] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [313-316] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [338-358] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [344-345] for track '30' has 1 frames without a visible bounding box.
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

</details>