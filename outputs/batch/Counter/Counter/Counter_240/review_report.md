# Play-Annotation-Generator Annotation Review — Counter_240

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Counter_240`
- **Frame Range:** 0 to 269 (270 total frames)
- **Play:** `Play_Run_Counter`
- **Result:** `Result_Tackle`
- **Result Frame:** 269
- **Player Tracks:** 35
- **Ball Tracks:** 0
- **Action Segments:** 97
- **Validation Warnings:** 114
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
- **Start-Frame Differences:** 1
- **Missing Segments:** 0
- **Ambiguous Matches:** 3
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 73
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `9` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `16` | `15` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | RT | offense | `1` | `0` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | RG | offense | `5` | `4` |
| ⚠️ START CHANGED | `Action_PullBlock` | C | offense | `16` | `15` |
| ✅ EXACT | `Action_PullLeadBlock` | RB | offense | `11` | `10` |
| ✅ EXACT | `Action_SnapReceive` | Position_Unknown | Team_Unknown | `19` | `17` |
| ✅ EXACT | `Action_Handoff` | Position_Unknown | Team_Unknown | `19` | `17` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | QB | offense | `10` | `9` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `1` | `Group` | 0 | START | 0 | 118 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `10` | `Group` | 0 | START | 0 | 154 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `11` | `Group` | 0 | START | 0 | 118 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `12` | `Group` | 0 | START | 0 | 116 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `16` | `Group` | 0 | START | 0 | 14 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `5` | `Group` | 0 | START | 0 | 118 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `6` | `Group` | 0 | START | 0 | 116 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `9` | `Group` | 0 | START | 0 | 116 |
| ✅ EXACT | `Action_BallSnap` | C | `16` | `15` | 117 | START | 117 | 129 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | RT | `1` | `0` | 119 | START | 119 | 142 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | RG | `5` | `4` | 119 | START | 119 | 138 |
| ⚠️ START CHANGED | `Action_PullBlock` | C | `16` | `15` | 119 | START | 130 | 207 |
| ✅ EXACT | `Action_PullLeadBlock` | RB | `11` | `10` | 119 | START | 119 | 146 |
| ✅ EXACT | `Action_SnapReceive` | Position_Unknown | `19` | `17` | 129 | END | 121 | 129 |
| ✅ EXACT | `Action_Handoff` | Position_Unknown | `19` | `17` | 142 | START | 142 | 154 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | QB | `10` | `9` | 155 | START | 155 | 176 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 207 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 269

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 154 | 155 | inferred_complete_timeline |
| `Action_BallCarry` | 155 | 176 | 22 | inferred_complete_timeline |
| `Action_BallCarry` | 178 | 269 | 92 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–146
- **Visible Samples:** 147

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 118 | 119 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 119 | 146 | 28 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–222
- **Visible Samples:** 223

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 116 | 117 | inferred_complete_timeline |
| `Action_None` | 117 | 222 | 106 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–195
- **Visible Samples:** 196

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 116 | 117 | inferred_complete_timeline |
| `Action_None` | 117 | 195 | 79 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–216
- **Visible Samples:** 217

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 116 | 117 | inferred_complete_timeline |
| `Action_None` | 117 | 216 | 100 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 242

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 14 | 15 | inferred_complete_timeline |
| `Action_PreSnap` | 16 | 17 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 23 | 27 | 5 | inferred_complete_timeline |
| `Action_PreSnap` | 32 | 49 | 18 | inferred_complete_timeline |
| `Action_PreSnap` | 68 | 116 | 49 | inferred_complete_timeline |
| `Action_BallSnap` | 117 | 129 | 13 | inferred_complete_timeline |
| `Action_PullBlock` | 130 | 207 | 78 | inferred_complete_timeline |
| `Action_None` | 208 | 269 | 62 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–236
- **Visible Samples:** 158

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 118 | 119 | inferred_complete_timeline |
| `Action_DownBlock` | 119 | 138 | 20 | inferred_complete_timeline |
| `Action_DownBlock` | 162 | 175 | 14 | inferred_complete_timeline |
| `Action_None` | 232 | 236 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 265

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 118 | 119 | inferred_complete_timeline |
| `Action_DownBlock` | 119 | 142 | 24 | inferred_complete_timeline |
| `Action_DownBlock` | 147 | 207 | 61 | inferred_complete_timeline |
| `Action_None` | 208 | 219 | 12 | inferred_complete_timeline |
| `Action_None` | 221 | 269 | 49 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–25
- **Visible Samples:** 24

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 21 | 22 | inferred_complete_timeline |
| `Action_PreSnap` | 24 | 25 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 256

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 116 | 117 | inferred_complete_timeline |
| `Action_None` | 117 | 151 | 35 | inferred_complete_timeline |
| `Action_None` | 160 | 161 | 2 | inferred_complete_timeline |
| `Action_None` | 166 | 172 | 7 | inferred_complete_timeline |
| `Action_None` | 175 | 269 | 95 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–51
- **Visible Samples:** 52

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 51 | 52 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–234
- **Visible Samples:** 206

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 116 | 117 | inferred_complete_timeline |
| `Action_None` | 117 | 127 | 11 | inferred_complete_timeline |
| `Action_None` | 144 | 162 | 19 | inferred_complete_timeline |
| `Action_None` | 176 | 234 | 59 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–193
- **Visible Samples:** 189

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 116 | 117 | inferred_complete_timeline |
| `Action_None` | 117 | 149 | 33 | inferred_complete_timeline |
| `Action_None` | 155 | 193 | 39 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–204
- **Visible Samples:** 205

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 116 | 117 | inferred_complete_timeline |
| `Action_None` | 117 | 204 | 88 | inferred_complete_timeline |

</details>

<details>
<summary>CB — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 116 | 117 | inferred_complete_timeline |
| `Action_None` | 117 | 269 | 153 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–264
- **Visible Samples:** 245

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 116 | 117 | inferred_complete_timeline |
| `Action_None` | 117 | 196 | 80 | inferred_complete_timeline |
| `Action_None` | 198 | 202 | 5 | inferred_complete_timeline |
| `Action_None` | 206 | 223 | 18 | inferred_complete_timeline |
| `Action_None` | 236 | 255 | 20 | inferred_complete_timeline |
| `Action_None` | 260 | 264 | 5 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `16` | `18` | Position_Unknown | Team_Unknown | 75–224 | 126 | 10 | Undefined position; Undefined team |
| `17` | `19` | Position_Unknown | Team_Unknown | 121–194 | 74 | 4 | Undefined position; Undefined team |
| `18` | `20` | Position_Unknown | Team_Unknown | 138–143 | 6 | 1 | Undefined position; Undefined team |
| `19` | `22` | Position_Unknown | Team_Unknown | 150–269 | 81 | 3 | Undefined position; Undefined team |
| `20` | `24` | Position_Unknown | Team_Unknown | 163–171 | 4 | 2 | Undefined position; Undefined team |
| `21` | `26` | Position_Unknown | Team_Unknown | 164–234 | 71 | 1 | Undefined position; Undefined team |
| `22` | `27` | Position_Unknown | Team_Unknown | 176–241 | 48 | 6 | Undefined position; Undefined team |
| `23` | `28` | Position_Unknown | Team_Unknown | 186–191 | 6 | 1 | Undefined position; Undefined team |
| `24` | `29` | Position_Unknown | Team_Unknown | 188–253 | 62 | 3 | Undefined position; Undefined team |
| `25` | `32` | Position_Unknown | Team_Unknown | 213–224 | 12 | 1 | Undefined position; Undefined team |
| `26` | `33` | Position_Unknown | Team_Unknown | 217–248 | 21 | 2 | Undefined position; Undefined team |
| `27` | `35` | Position_Unknown | Team_Unknown | 219–236 | 18 | 1 | Undefined position; Undefined team |
| `28` | `36` | Position_Unknown | Team_Unknown | 224–258 | 27 | 2 | Undefined position; Undefined team |
| `29` | `37` | Position_Unknown | Team_Unknown | 229–269 | 41 | 1 | Undefined position; Undefined team |
| `30` | `38` | Position_Unknown | Team_Unknown | 232–269 | 38 | 1 | Undefined position; Undefined team |
| `31` | `39` | Position_Unknown | Team_Unknown | 237–269 | 33 | 1 | Undefined position; Undefined team |
| `32` | `40` | Position_Unknown | Team_Unknown | 239–269 | 31 | 1 | Undefined position; Undefined team |
| `33` | `41` | Position_Unknown | Team_Unknown | 258–264 | 7 | 1 | Undefined position; Undefined team |
| `34` | `42` | Position_Unknown | Team_Unknown | 266–269 | 3 | 2 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_DownBlock` and target `1` (2 segments found)
- ⚠️ Ambiguous match for action `Action_DownBlock` and target `5` (2 segments found)
- ⚠️ `Action_PullBlock` for actor_track_id `16` (C): Annotated start 119 != Inferred start 130
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `10` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `1` (actor_track_id `2`): `SAF` position mapped to `defense` team
- ⚠️ 19 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 19 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 38 |
| Missing visible bounding boxes during action | 74 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 269 as fallback play end.
- ⚠️ Resolved action overlap for track '15' (C): higher_priority='Action_BallSnap' [117–129], lower_priority='Action_PullBlock' annotated_start=119, effective_Action_PullBlock_start=130.
- ⚠️ Action 'Action_DownBlock' range [119-142] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [147-207] for track '0' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' for track '0' starts at frame 208, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_None' range [208-219] for track '0' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [117-196] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [198-202] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [206-223] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [236-255] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [260-264] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [117-269] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [117-204] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [119-138] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [162-175] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [232-236] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [117-195] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [117-127] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [144-162] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [176-234] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [117-151] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [160-161] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [166-172] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [117-222] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [155-176] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [178-269] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullLeadBlock' range [119-146] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [117-216] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-51] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [117-149] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [155-193] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-21] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [24-25] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-14] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [16-17] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [23-27] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [32-49] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [68-116] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [130-207] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [117-119] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [126-130] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [134-138] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [144-148] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [151-159] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [161-165] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [167-207] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [211-212] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [216-224] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_Handoff' range [142-154] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [155-194] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [138-143] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [150-167] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [205-206] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [209-269] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [163-164] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [170-171] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [164-234] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [176-184] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [186-187] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [189-197] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [200-203] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [217-238] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [240-241] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [186-191] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [188-215] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [218-243] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [246-253] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [213-224] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [217-235] for track '26' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [247-248] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [219-236] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [224-247] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [256-258] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [239-269] for track '32' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [258-264] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [266-267] for track '34' has 1 frames without a visible bounding box.
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

</details>