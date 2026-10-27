# Play-Annotation-Generator Annotation Review — Counter_64

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Counter_64`
- **Frame Range:** 0 to 389 (390 total frames)
- **Play:** `Play_Run_Counter`
- **Result:** `Result_Touchdown`
- **Result Frame:** 389
- **Player Tracks:** 38
- **Ball Tracks:** 0
- **Action Segments:** 132
- **Validation Warnings:** 153
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 20
- **Exact Matches:** 4
- **Group Expanded Events:** 8
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 1
- **Missing Segments:** 1
- **Ambiguous Matches:** 4
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 109
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `8` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `9` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `9` | `8` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | Position_Unknown | Team_Unknown | `16` | `15` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | LG | offense | `3` | `2` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | TE | offense | `7` | `6` |
| ✅ EXACT | `Action_PullBlock` | RG | offense | `5` | `4` |
| ⚠️ AMBIGUOUS MATCH | `Action_PullLeadBlock` | RT | offense | `6` | `5` |
| ✅ EXACT | `Action_PlaySideFakeStep` | RB | offense | `8` | `7` |
| ⚠️ END CHANGED | `Action_SnapReceive` | QB | offense | `11` | `10` |
| ✅ EXACT | `Action_Handoff` | QB | offense | `11` | `10` |
| ❌ MISSING SEGMENT | `Action_BallCarry` | RB | offense | `8` | `7` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `11` | `Group` | 0 | START | 0 | 157 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `3` | `Group` | 0 | START | 0 | 116 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `4` | `Group` | 0 | START | 0 | 107 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `5` | `Group` | 0 | START | 0 | 160 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `6` | `Group` | 0 | START | 0 | 160 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `7` | `Group` | 0 | START | 0 | 100 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `8` | `Group` | 0 | START | 0 | 164 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `9` | `Group` | 0 | START | 0 | 157 |
| ✅ EXACT | `Action_BallSnap` | C | `9` | `8` | 158 | START | 158 | 171 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | Position_Unknown | `16` | `15` | 161 | START | 161 | 191 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | LG | `3` | `2` | 161 | START | 161 | 184 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | TE | `7` | `6` | 161 | START | 161 | 162 |
| ✅ EXACT | `Action_PullBlock` | RG | `5` | `4` | 161 | START | 161 | 245 |
| ⚠️ AMBIGUOUS MATCH | `Action_PullLeadBlock` | RT | `6` | `5` | 161 | START | 161 | 235 |
| ✅ EXACT | `Action_PlaySideFakeStep` | RB | `8` | `7` | 165 | START | 165 | 202 |
| ⚠️ END CHANGED | `Action_SnapReceive` | QB | `11` | `10` | 171 | END | 158 | 169 |
| ✅ EXACT | `Action_Handoff` | QB | `11` | `10` | 185 | START | 185 | 203 |
| ❌ MISSING SEGMENT | `Action_BallCarry` | RB | `8` | `7` | 204 | START | N/A | N/A |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 245 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–240
- **Visible Samples:** 238

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 157 | 158 | inferred_complete_timeline |
| `Action_SnapReceive` | 158 | 169 | 12 | inferred_complete_timeline |
| `Action_None` | 173 | 184 | 12 | inferred_complete_timeline |
| `Action_Handoff` | 185 | 203 | 19 | inferred_complete_timeline |
| `Action_None` | 204 | 240 | 37 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–202
- **Visible Samples:** 203

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 164 | 165 | inferred_complete_timeline |
| `Action_PlaySideFakeStep` | 165 | 202 | 38 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–389
- **Visible Samples:** 388

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 100 | 101 | inferred_complete_timeline |
| `Action_PreSnap` | 102 | 160 | 59 | inferred_complete_timeline |
| `Action_DownBlock` | 161 | 162 | 2 | inferred_complete_timeline |
| `Action_DownBlock` | 164 | 245 | 82 | inferred_complete_timeline |
| `Action_None` | 246 | 389 | 144 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–300
- **Visible Samples:** 281

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 107 | 108 | inferred_complete_timeline |
| `Action_PreSnap` | 109 | 157 | 49 | inferred_complete_timeline |
| `Action_None` | 158 | 192 | 35 | inferred_complete_timeline |
| `Action_None` | 195 | 204 | 10 | inferred_complete_timeline |
| `Action_None` | 209 | 214 | 6 | inferred_complete_timeline |
| `Action_None` | 216 | 231 | 16 | inferred_complete_timeline |
| `Action_None` | 237 | 243 | 7 | inferred_complete_timeline |
| `Action_None` | 251 | 300 | 50 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–258
- **Visible Samples:** 216

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 116 | 117 | inferred_complete_timeline |
| `Action_PreSnap` | 128 | 135 | 8 | inferred_complete_timeline |
| `Action_PreSnap` | 143 | 160 | 18 | inferred_complete_timeline |
| `Action_DownBlock` | 161 | 184 | 24 | inferred_complete_timeline |
| `Action_DownBlock` | 189 | 194 | 6 | inferred_complete_timeline |
| `Action_DownBlock` | 209 | 226 | 18 | inferred_complete_timeline |
| `Action_DownBlock` | 228 | 237 | 10 | inferred_complete_timeline |
| `Action_DownBlock` | 244 | 245 | 2 | inferred_complete_timeline |
| `Action_None` | 246 | 258 | 13 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–389
- **Visible Samples:** 364

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 157 | 158 | inferred_complete_timeline |
| `Action_BallSnap` | 158 | 171 | 14 | inferred_complete_timeline |
| `Action_None` | 184 | 187 | 4 | inferred_complete_timeline |
| `Action_None` | 201 | 375 | 175 | inferred_complete_timeline |
| `Action_None` | 377 | 389 | 13 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–326
- **Visible Samples:** 320

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 160 | 161 | inferred_complete_timeline |
| `Action_PullBlock` | 161 | 245 | 85 | inferred_complete_timeline |
| `Action_None` | 246 | 254 | 9 | inferred_complete_timeline |
| `Action_None` | 262 | 326 | 65 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 263

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 160 | 161 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 161 | 235 | 75 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 243 | 245 | 3 | inferred_complete_timeline |
| `Action_None` | 246 | 269 | 24 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–220
- **Visible Samples:** 208

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 93 | 94 | inferred_complete_timeline |
| `Action_PreSnap` | 95 | 157 | 63 | inferred_complete_timeline |
| `Action_None` | 158 | 172 | 15 | inferred_complete_timeline |
| `Action_None` | 174 | 203 | 30 | inferred_complete_timeline |
| `Action_None` | 215 | 220 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–362
- **Visible Samples:** 363

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 157 | 158 | inferred_complete_timeline |
| `Action_None` | 158 | 362 | 205 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–162
- **Visible Samples:** 134

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 112 | 113 | inferred_complete_timeline |
| `Action_PreSnap` | 114 | 120 | 7 | inferred_complete_timeline |
| `Action_PreSnap` | 144 | 151 | 8 | inferred_complete_timeline |
| `Action_PreSnap` | 157 | 157 | 1 | inferred_complete_timeline |
| `Action_None` | 158 | 162 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–389
- **Visible Samples:** 374

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 157 | 158 | inferred_complete_timeline |
| `Action_None` | 158 | 164 | 7 | inferred_complete_timeline |
| `Action_None` | 166 | 173 | 8 | inferred_complete_timeline |
| `Action_None` | 175 | 184 | 10 | inferred_complete_timeline |
| `Action_None` | 197 | 212 | 16 | inferred_complete_timeline |
| `Action_None` | 214 | 217 | 4 | inferred_complete_timeline |
| `Action_None` | 219 | 389 | 171 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–389
- **Visible Samples:** 268

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 10 | 11 | inferred_complete_timeline |
| `Action_PreSnap` | 36 | 37 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 45 | 101 | 57 | inferred_complete_timeline |
| `Action_None` | 167 | 177 | 11 | inferred_complete_timeline |
| `Action_None` | 188 | 189 | 2 | inferred_complete_timeline |
| `Action_None` | 205 | 389 | 185 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–184
- **Visible Samples:** 178

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 157 | 158 | inferred_complete_timeline |
| `Action_None` | 158 | 164 | 7 | inferred_complete_timeline |
| `Action_None` | 169 | 171 | 3 | inferred_complete_timeline |
| `Action_None` | 175 | 184 | 10 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `1` | `2` | Position_Unknown | Team_Unknown | 0–286 | 262 | 5 | Undefined position; Undefined team |
| `15` | `16` | Position_Unknown | Team_Unknown | 84–339 | 180 | 6 | Undefined position; Undefined team |
| `16` | `18` | Position_Unknown | Team_Unknown | 97–161 | 65 | 2 | Undefined position; Undefined team |
| `17` | `21` | Position_Unknown | Team_Unknown | 216–341 | 113 | 4 | Undefined position; Undefined team |
| `18` | `22` | Position_Unknown | Team_Unknown | 218–238 | 21 | 1 | Undefined position; Undefined team |
| `19` | `23` | Position_Unknown | Team_Unknown | 232–269 | 34 | 2 | Undefined position; Undefined team |
| `20` | `24` | Position_Unknown | Team_Unknown | 234–263 | 25 | 2 | Undefined position; Undefined team |
| `21` | `25` | Position_Unknown | Team_Unknown | 237–268 | 27 | 2 | Undefined position; Undefined team |
| `22` | `29` | Position_Unknown | Team_Unknown | 240–389 | 145 | 2 | Undefined position; Undefined team |
| `23` | `35` | Position_Unknown | Team_Unknown | 265–389 | 125 | 1 | Undefined position; Undefined team |
| `24` | `36` | Position_Unknown | Team_Unknown | 266–272 | 7 | 1 | Undefined position; Undefined team |
| `25` | `37` | Position_Unknown | Team_Unknown | 270–389 | 117 | 4 | Undefined position; Undefined team |
| `26` | `38` | Position_Unknown | Team_Unknown | 273–377 | 105 | 1 | Undefined position; Undefined team |
| `27` | `39` | Position_Unknown | Team_Unknown | 279–342 | 62 | 2 | Undefined position; Undefined team |
| `28` | `40` | Position_Unknown | Team_Unknown | 282–389 | 98 | 4 | Undefined position; Undefined team |
| `29` | `41` | Position_Unknown | Team_Unknown | 287–389 | 100 | 3 | Undefined position; Undefined team |
| `30` | `42` | Position_Unknown | Team_Unknown | 306–310 | 5 | 1 | Undefined position; Undefined team |
| `31` | `43` | Position_Unknown | Team_Unknown | 313–342 | 28 | 2 | Undefined position; Undefined team |
| `32` | `44` | Position_Unknown | Team_Unknown | 315–325 | 10 | 2 | Undefined position; Undefined team |
| `33` | `45` | Position_Unknown | Team_Unknown | 321–389 | 25 | 3 | Undefined position; Undefined team |
| `34` | `46` | Position_Unknown | Team_Unknown | 347–389 | 43 | 1 | Undefined position; Undefined team |
| `35` | `49` | Position_Unknown | Team_Unknown | 353–388 | 22 | 4 | Undefined position; Undefined team |
| `36` | `50` | Position_Unknown | Team_Unknown | 360–389 | 23 | 4 | Undefined position; Undefined team |
| `37` | `52` | Position_Unknown | Team_Unknown | 375–389 | 14 | 2 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_DownBlock` and target `16` (2 segments found)
- ⚠️ Ambiguous match for action `Action_DownBlock` and target `3` (5 segments found)
- ⚠️ Ambiguous match for action `Action_DownBlock` and target `7` (2 segments found)
- ⚠️ Ambiguous match for action `Action_PullLeadBlock` and target `6` (2 segments found)
- ❌ Missing segment for action `Action_BallCarry` on target `8` (RB)

### Track Identity Issues

- ⚠️ 24 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 24 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 48 |
| Missing visible bounding boxes during action | 103 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 389 as fallback play end.
- ⚠️ Segment 'Action_BallCarry' for track '7' has invalid range: start=204, end=202. Clamping end to start.
- ⚠️ Action 'Action_PreSnap' range [0-93] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [158-172] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [174-203] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [215-220] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [158-187] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [191-216] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [238-281] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [283-286] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-116] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [128-135] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [161-184] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [189-194] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [209-226] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [228-237] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [246-258] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-107] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [158-192] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [195-204] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [209-214] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [216-231] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [237-243] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [251-300] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [161-245] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [246-254] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [262-326] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullLeadBlock' range [161-235] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [246-269] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-100] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [161-162] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PlaySideFakeStep' range [165-202] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallSnap' range [158-171] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [184-187] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [201-375] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [377-389] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [158-362] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_SnapReceive' range [158-169] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [204-240] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-157] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [158-164] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [169-171] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [175-184] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-112] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [114-120] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [144-151] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [158-162] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [158-164] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [166-173] for track '13' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [175-184] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [197-212] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [214-217] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [219-389] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-10] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [36-37] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [45-101] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [167-177] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [188-189] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [84-153] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [161-191] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [227-232] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [252-277] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [299-339] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [158-161] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [216-220] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [225-228] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [237-332] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [334-341] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [218-238] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [232-258] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [263-269] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [234-254] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [260-263] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [237-246] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [252-268] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [240-278] for track '22' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [266-272] for track '24' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [270-296] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [298-302] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [304-321] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [273-377] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [279-308] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [311-342] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [282-289] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [293-300] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [307-316] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [287-295] for track '29' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [297-317] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [320-389] for track '29' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [306-310] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [313-336] for track '31' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [339-342] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [315-319] for track '32' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [321-325] for track '32' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [321-324] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [366-368] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [353-354] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [364-369] for track '35' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [372-380] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [384-388] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [360-361] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [364-370] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [374-380] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [375-376] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [378-389] for track '37' has 2 frames without a visible bounding box.
- ⚠️ Player track '1' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '1' has undefined team_side. Will map to Team_Unknown.
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
- ⚠️ Player track '34' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '34' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '35' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '35' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '36' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '36' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '37' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '37' has undefined team_side. Will map to Team_Unknown.

</details>