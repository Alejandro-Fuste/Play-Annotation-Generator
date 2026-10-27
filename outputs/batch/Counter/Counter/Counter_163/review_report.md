# Play-Annotation-Generator Annotation Review — Counter_163

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Counter_163`
- **Frame Range:** 0 to 299 (300 total frames)
- **Play:** `Play_Run_Counter`
- **Result:** `Result_Tackle`
- **Result Frame:** 299
- **Player Tracks:** 43
- **Ball Tracks:** 0
- **Action Segments:** 115
- **Validation Warnings:** 146
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 18
- **Exact Matches:** 4
- **Group Expanded Events:** 7
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 1
- **Ambiguous Matches:** 4
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 95
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `8` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `9` | `Group` |
| ✅ EXACT | `Action_BallSnap` | Position_Unknown | Team_Unknown | `20` | `19` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | Position_Unknown | Team_Unknown | `19` | `18` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | Position_Unknown | Team_Unknown | `20` | `19` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | Position_Unknown | Team_Unknown | `21` | `20` |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | Position_Unknown | Team_Unknown | `22` | `21` |
| ✅ EXACT | `Action_PullLeadBlock` | Position_Unknown | Team_Unknown | `14` | `13` |
| ✅ EXACT | `Action_SnapReceive` | LB1 | defense | `7` | `6` |
| ✅ EXACT | `Action_Handoff` | LB1 | defense | `7` | `6` |
| ❌ MISSING SEGMENT | `Action_BallCarry` | LB2 | defense | `4` | `3` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `1` | `Group` | 0 | START | 0 | 145 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `12` | `Group` | 0 | START | 0 | 145 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `2` | `Group` | 0 | START | 0 | 145 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `5` | `Group` | 0 | START | 0 | 145 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `6` | `Group` | 0 | START | 0 | 145 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `8` | `Group` | 0 | START | 0 | 145 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `9` | `Group` | 0 | START | 0 | 145 |
| ✅ EXACT | `Action_BallSnap` | Position_Unknown | `20` | `19` | 146 | START | 146 | 148 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | Position_Unknown | `19` | `18` | 149 | START | 149 | 158 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | Position_Unknown | `20` | `19` | 149 | START | 149 | 153 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | Position_Unknown | `21` | `20` | 149 | START | 149 | 151 |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | Position_Unknown | `22` | `21` | 149 | START | 149 | 155 |
| ✅ EXACT | `Action_PullLeadBlock` | Position_Unknown | `14` | `13` | 149 | START | 149 | 183 |
| ✅ EXACT | `Action_SnapReceive` | LB1 | `7` | `6` | 160 | END | 146 | 160 |
| ✅ EXACT | `Action_Handoff` | LB1 | `7` | `6` | 169 | START | 169 | 187 |
| ❌ MISSING SEGMENT | `Action_BallCarry` | LB2 | `4` | `3` | 188 | START | N/A | N/A |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 226 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 300

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 145 | 146 | inferred_complete_timeline |
| `Action_None` | 146 | 299 | 154 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–192
- **Visible Samples:** 193

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 145 | 146 | inferred_complete_timeline |
| `Action_None` | 146 | 192 | 47 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–264
- **Visible Samples:** 265

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 145 | 146 | inferred_complete_timeline |
| `Action_None` | 146 | 264 | 119 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 300

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 145 | 146 | inferred_complete_timeline |
| `Action_None` | 146 | 299 | 154 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 281

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 145 | 146 | inferred_complete_timeline |
| `Action_None` | 146 | 273 | 128 | inferred_complete_timeline |
| `Action_None` | 292 | 295 | 4 | inferred_complete_timeline |
| `Action_None` | 297 | 299 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–196
- **Visible Samples:** 195

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 145 | 146 | inferred_complete_timeline |
| `Action_None` | 146 | 185 | 40 | inferred_complete_timeline |
| `Action_None` | 187 | 190 | 4 | inferred_complete_timeline |
| `Action_None` | 192 | 196 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 300

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 145 | 146 | inferred_complete_timeline |
| `Action_None` | 146 | 299 | 154 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–202
- **Visible Samples:** 203

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 145 | 146 | inferred_complete_timeline |
| `Action_None` | 146 | 202 | 57 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–257
- **Visible Samples:** 125

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 40 | 41 | inferred_complete_timeline |
| `Action_PreSnap` | 107 | 145 | 39 | inferred_complete_timeline |
| `Action_None` | 146 | 157 | 12 | inferred_complete_timeline |
| `Action_None` | 160 | 179 | 20 | inferred_complete_timeline |
| `Action_None` | 245 | 257 | 13 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–248
- **Visible Samples:** 233

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 145 | 146 | inferred_complete_timeline |
| `Action_None` | 146 | 186 | 41 | inferred_complete_timeline |
| `Action_None` | 200 | 220 | 21 | inferred_complete_timeline |
| `Action_None` | 222 | 240 | 19 | inferred_complete_timeline |
| `Action_None` | 243 | 248 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 289

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 145 | 146 | inferred_complete_timeline |
| `Action_SnapReceive` | 146 | 160 | 15 | inferred_complete_timeline |
| `Action_None` | 161 | 168 | 8 | inferred_complete_timeline |
| `Action_Handoff` | 169 | 187 | 19 | inferred_complete_timeline |
| `Action_None` | 188 | 207 | 20 | inferred_complete_timeline |
| `Action_None` | 212 | 224 | 13 | inferred_complete_timeline |
| `Action_None` | 232 | 299 | 68 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–174
- **Visible Samples:** 175

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 174 | 175 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `12` | `13` | Position_Unknown | Team_Unknown | 0–263 | 264 | 2 | Undefined position; Undefined team |
| `13` | `14` | Position_Unknown | Team_Unknown | 0–183 | 184 | 2 | Undefined position; Undefined team |
| `14` | `15` | Position_Unknown | Team_Unknown | 0–299 | 133 | 8 | Undefined position; Undefined team |
| `15` | `16` | Position_Unknown | Team_Unknown | 0–245 | 105 | 7 | Undefined position; Undefined team |
| `16` | `17` | Position_Unknown | Team_Unknown | 0–13 | 14 | 1 | Undefined position; Undefined team |
| `17` | `18` | Position_Unknown | Team_Unknown | 0–152 | 124 | 7 | Undefined position; Undefined team |
| `18` | `19` | Position_Unknown | Team_Unknown | 0–169 | 125 | 4 | Undefined position; Undefined team |
| `19` | `20` | Position_Unknown | Team_Unknown | 16–153 | 138 | 3 | Undefined position; Undefined team |
| `20` | `21` | Position_Unknown | Team_Unknown | 48–168 | 109 | 3 | Undefined position; Undefined team |
| `21` | `22` | Position_Unknown | Team_Unknown | 48–229 | 142 | 5 | Undefined position; Undefined team |
| `22` | `24` | Position_Unknown | Team_Unknown | 125–224 | 55 | 5 | Undefined position; Undefined team |
| `23` | `25` | Position_Unknown | Team_Unknown | 187–199 | 13 | 1 | Undefined position; Undefined team |
| `24` | `26` | Position_Unknown | Team_Unknown | 193–197 | 5 | 1 | Undefined position; Undefined team |
| `25` | `27` | Position_Unknown | Team_Unknown | 199–285 | 60 | 2 | Undefined position; Undefined team |
| `26` | `28` | Position_Unknown | Team_Unknown | 206–213 | 8 | 1 | Undefined position; Undefined team |
| `27` | `29` | Position_Unknown | Team_Unknown | 211–299 | 89 | 1 | Undefined position; Undefined team |
| `28` | `31` | Position_Unknown | Team_Unknown | 226–229 | 4 | 1 | Undefined position; Undefined team |
| `29` | `32` | Position_Unknown | Team_Unknown | 235–265 | 28 | 2 | Undefined position; Undefined team |
| `30` | `34` | Position_Unknown | Team_Unknown | 244–299 | 49 | 4 | Undefined position; Undefined team |
| `31` | `35` | Position_Unknown | Team_Unknown | 244–299 | 56 | 1 | Undefined position; Undefined team |
| `32` | `36` | Position_Unknown | Team_Unknown | 244–245 | 2 | 1 | Undefined position; Undefined team |
| `33` | `37` | Position_Unknown | Team_Unknown | 248–299 | 50 | 2 | Undefined position; Undefined team |
| `34` | `38` | Position_Unknown | Team_Unknown | 250–272 | 9 | 2 | Undefined position; Undefined team |
| `35` | `39` | Position_Unknown | Team_Unknown | 254–299 | 43 | 2 | Undefined position; Undefined team |
| `36` | `40` | Position_Unknown | Team_Unknown | 255–299 | 45 | 1 | Undefined position; Undefined team |
| `37` | `41` | Position_Unknown | Team_Unknown | 262–299 | 37 | 2 | Undefined position; Undefined team |
| `38` | `42` | Position_Unknown | Team_Unknown | 268–272 | 5 | 1 | Undefined position; Undefined team |
| `39` | `44` | Position_Unknown | Team_Unknown | 282–285 | 4 | 1 | Undefined position; Undefined team |
| `40` | `45` | Position_Unknown | Team_Unknown | 282–299 | 6 | 2 | Undefined position; Undefined team |
| `41` | `46` | Position_Unknown | Team_Unknown | 282–285 | 4 | 1 | Undefined position; Undefined team |
| `42` | `48` | Position_Unknown | Team_Unknown | 294–299 | 6 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_DownBlock` and target `19` (3 segments found)
- ⚠️ Ambiguous match for action `Action_DownBlock` and target `20` (3 segments found)
- ⚠️ Ambiguous match for action `Action_DownBlock` and target `21` (2 segments found)
- ⚠️ Ambiguous match for action `Action_PullBlock` and target `22` (3 segments found)
- ❌ Missing segment for action `Action_BallCarry` on target `4` (LB2)

### Track Identity Issues

- ⚠️ 31 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 31 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 62 |
| Missing visible bounding boxes during action | 82 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 299 as fallback play end.
- ⚠️ Segment 'Action_BallCarry' for track '3' has invalid range: start=188, end=174. Clamping end to start.
- ⚠️ Action 'Action_None' range [146-264] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [146-202] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-174] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [146-185] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [187-190] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [192-196] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [146-273] for track '5' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [292-295] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [188-207] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [212-224] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [232-299] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [146-192] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-40] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [146-157] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [160-179] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [245-257] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [146-186] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [200-220] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [222-240] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [243-248] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [146-263] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PullLeadBlock' range [149-183] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-38] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [146-151] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [166-170] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [245-254] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [262-272] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [274-289] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-13] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [16-30] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [35-86] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [123-126] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [138-145] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [146-149] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [238-245] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-13] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-11] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [18-71] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [89-92] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [95-100] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [104-105] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [146-152] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-6] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [149-158] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [164-169] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [149-153] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [149-151] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [164-168] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [48-148] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [149-155] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [164-184] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [217-226] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [227-229] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [125-131] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [133-145] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [146-149] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [168-192] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [219-224] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [187-199] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [193-197] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [199-253] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [281-285] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [206-213] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [226-229] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [235-243] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [247-265] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [244-266] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [269-272] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [276-278] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [281-299] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [244-245] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [248-290] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [293-299] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [250-251] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [266-272] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [254-255] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [262-275] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [277-299] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [268-272] for track '38' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [282-285] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [282-285] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [282-285] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Player track '12' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '12' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '13' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '13' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '14' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '14' has undefined team_side. Will map to Team_Unknown.
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
- ⚠️ Player track '38' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '38' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '39' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '39' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '40' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '40' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '41' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '41' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '42' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '42' has undefined team_side. Will map to Team_Unknown.

</details>