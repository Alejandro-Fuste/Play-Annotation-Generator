# Play-Annotation-Generator Annotation Review — Counter_270

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Counter_270`
- **Frame Range:** 0 to 359 (360 total frames)
- **Play:** `Play_Run_Counter`
- **Result:** `Result_Tackle`
- **Result Frame:** 359
- **Player Tracks:** 37
- **Ball Tracks:** 0
- **Action Segments:** 105
- **Validation Warnings:** 118
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 18
- **Exact Matches:** 3
- **Group Expanded Events:** 8
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 1
- **Ambiguous Matches:** 4
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 88
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Group | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `8` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `11` | `10` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | RG | offense | `16` | `14` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | RT | offense | `4` | `3` |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | C | offense | `11` | `10` |
| ✅ EXACT | `Action_PullLeadBlock` | TE | offense | `8` | `7` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `6` | `5` |
| ⚠️ AMBIGUOUS MATCH | `Action_Handoff` | QB | offense | `6` | `5` |
| ❌ MISSING SEGMENT | `Action_BallCarry` | RB | offense | `7` | `6` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `10` | `Group` | 0 | START | 0 | 143 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `11` | `Group` | 0 | START | 0 | 143 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `12` | `Group` | 0 | START | 0 | 143 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Group | `16` | `Group` | 0 | START | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `4` | `Group` | 0 | START | 0 | 146 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `6` | `Group` | 0 | START | 0 | 143 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `7` | `Group` | 0 | START | 0 | 180 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `8` | `Group` | 0 | START | 0 | 146 |
| ✅ EXACT | `Action_BallSnap` | C | `11` | `10` | 144 | START | 144 | 158 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | RG | `16` | `14` | 147 | START | 147 | 149 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | RT | `4` | `3` | 147 | START | 147 | 175 |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | C | `11` | `10` | 147 | START | 159 | 164 |
| ✅ EXACT | `Action_PullLeadBlock` | TE | `8` | `7` | 147 | START | 147 | 163 |
| ✅ EXACT | `Action_SnapReceive` | QB | `6` | `5` | 158 | END | 144 | 158 |
| ⚠️ AMBIGUOUS MATCH | `Action_Handoff` | QB | `6` | `5` | 168 | START | 168 | 175 |
| ❌ MISSING SEGMENT | `Action_BallCarry` | RB | `7` | `6` | 187 | START | N/A | N/A |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 227 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–314
- **Visible Samples:** 302

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 143 | 144 | inferred_complete_timeline |
| `Action_SnapReceive` | 144 | 158 | 15 | inferred_complete_timeline |
| `Action_None` | 159 | 167 | 9 | inferred_complete_timeline |
| `Action_Handoff` | 168 | 175 | 8 | inferred_complete_timeline |
| `Action_Handoff` | 186 | 186 | 1 | inferred_complete_timeline |
| `Action_None` | 187 | 256 | 70 | inferred_complete_timeline |
| `Action_None` | 260 | 314 | 55 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–180
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 180 | 181 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–163
- **Visible Samples:** 164

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 146 | 147 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 147 | 163 | 17 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–359
- **Visible Samples:** 342

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 143 | 144 | inferred_complete_timeline |
| `Action_None` | 144 | 203 | 60 | inferred_complete_timeline |
| `Action_None` | 208 | 213 | 6 | inferred_complete_timeline |
| `Action_None` | 215 | 218 | 4 | inferred_complete_timeline |
| `Action_None` | 225 | 228 | 4 | inferred_complete_timeline |
| `Action_None` | 235 | 253 | 19 | inferred_complete_timeline |
| `Action_None` | 255 | 359 | 105 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–288
- **Visible Samples:** 242

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 143 | 144 | inferred_complete_timeline |
| `Action_None` | 144 | 161 | 18 | inferred_complete_timeline |
| `Action_None` | 173 | 176 | 4 | inferred_complete_timeline |
| `Action_None` | 213 | 288 | 76 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–359
- **Visible Samples:** 344

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 143 | 144 | inferred_complete_timeline |
| `Action_BallSnap` | 144 | 158 | 15 | inferred_complete_timeline |
| `Action_PullBlock` | 159 | 164 | 6 | inferred_complete_timeline |
| `Action_PullBlock` | 167 | 171 | 5 | inferred_complete_timeline |
| `Action_PullBlock` | 176 | 177 | 2 | inferred_complete_timeline |
| `Action_PullBlock` | 179 | 216 | 38 | inferred_complete_timeline |
| `Action_PullBlock` | 224 | 227 | 4 | inferred_complete_timeline |
| `Action_None` | 228 | 230 | 3 | inferred_complete_timeline |
| `Action_None` | 232 | 319 | 88 | inferred_complete_timeline |
| `Action_None` | 321 | 359 | 39 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `16`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 147–234
- **Visible Samples:** 80

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_DownBlock` | 147 | 149 | 3 | inferred_complete_timeline |
| `Action_DownBlock` | 155 | 188 | 34 | inferred_complete_timeline |
| `Action_DownBlock` | 190 | 224 | 35 | inferred_complete_timeline |
| `Action_DownBlock` | 227 | 227 | 1 | inferred_complete_timeline |
| `Action_None` | 228 | 234 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–359
- **Visible Samples:** 357

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 146 | 147 | inferred_complete_timeline |
| `Action_DownBlock` | 147 | 175 | 29 | inferred_complete_timeline |
| `Action_DownBlock` | 179 | 227 | 49 | inferred_complete_timeline |
| `Action_None` | 228 | 359 | 132 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–318
- **Visible Samples:** 319

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 143 | 144 | inferred_complete_timeline |
| `Action_None` | 144 | 318 | 175 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–345
- **Visible Samples:** 315

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 143 | 144 | inferred_complete_timeline |
| `Action_None` | 144 | 226 | 83 | inferred_complete_timeline |
| `Action_None` | 244 | 250 | 7 | inferred_complete_timeline |
| `Action_None` | 259 | 337 | 79 | inferred_complete_timeline |
| `Action_None` | 344 | 345 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–191
- **Visible Samples:** 192

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 143 | 144 | inferred_complete_timeline |
| `Action_None` | 144 | 191 | 48 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–199
- **Visible Samples:** 198

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 143 | 144 | inferred_complete_timeline |
| `Action_None` | 144 | 193 | 50 | inferred_complete_timeline |
| `Action_None` | 195 | 196 | 2 | inferred_complete_timeline |
| `Action_None` | 198 | 199 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–359
- **Visible Samples:** 338

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 143 | 144 | inferred_complete_timeline |
| `Action_None` | 144 | 185 | 42 | inferred_complete_timeline |
| `Action_None` | 189 | 196 | 8 | inferred_complete_timeline |
| `Action_None` | 213 | 216 | 4 | inferred_complete_timeline |
| `Action_None` | 220 | 359 | 140 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–304
- **Visible Samples:** 297

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 143 | 144 | inferred_complete_timeline |
| `Action_None` | 144 | 286 | 143 | inferred_complete_timeline |
| `Action_None` | 292 | 293 | 2 | inferred_complete_timeline |
| `Action_None` | 297 | 304 | 8 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–359
- **Visible Samples:** 360

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 143 | 144 | inferred_complete_timeline |
| `Action_None` | 144 | 359 | 216 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `15` | `17` | Position_Unknown | Team_Unknown | 168–281 | 114 | 1 | Undefined position; Undefined team |
| `16` | `18` | Position_Unknown | Team_Unknown | 178–184 | 6 | 2 | Undefined position; Undefined team |
| `17` | `19` | Position_Unknown | Team_Unknown | 193–196 | 4 | 1 | Undefined position; Undefined team |
| `18` | `20` | Position_Unknown | Team_Unknown | 201–359 | 107 | 4 | Undefined position; Undefined team |
| `19` | `21` | Position_Unknown | Team_Unknown | 201–282 | 79 | 2 | Undefined position; Undefined team |
| `20` | `22` | Position_Unknown | Team_Unknown | 219–221 | 3 | 1 | Undefined position; Undefined team |
| `21` | `23` | Position_Unknown | Team_Unknown | 228–359 | 130 | 2 | Undefined position; Undefined team |
| `22` | `24` | Position_Unknown | Team_Unknown | 236–359 | 91 | 5 | Undefined position; Undefined team |
| `23` | `29` | Position_Unknown | Team_Unknown | 249–344 | 53 | 3 | Undefined position; Undefined team |
| `24` | `31` | Position_Unknown | Team_Unknown | 262–359 | 94 | 2 | Undefined position; Undefined team |
| `25` | `32` | Position_Unknown | Team_Unknown | 265–305 | 34 | 3 | Undefined position; Undefined team |
| `26` | `33` | Position_Unknown | Team_Unknown | 272–295 | 15 | 3 | Undefined position; Undefined team |
| `27` | `35` | Position_Unknown | Team_Unknown | 287–359 | 73 | 1 | Undefined position; Undefined team |
| `28` | `36` | Position_Unknown | Team_Unknown | 291–359 | 69 | 1 | Undefined position; Undefined team |
| `29` | `37` | Position_Unknown | Team_Unknown | 292–359 | 65 | 2 | Undefined position; Undefined team |
| `30` | `40` | Position_Unknown | Team_Unknown | 330–359 | 30 | 1 | Undefined position; Undefined team |
| `31` | `41` | Position_Unknown | Team_Unknown | 330–359 | 28 | 2 | Undefined position; Undefined team |
| `32` | `42` | Position_Unknown | Team_Unknown | 337–359 | 23 | 1 | Undefined position; Undefined team |
| `33` | `43` | Position_Unknown | Team_Unknown | 346–359 | 14 | 1 | Undefined position; Undefined team |
| `34` | `44` | Position_Unknown | Team_Unknown | 349–359 | 11 | 1 | Undefined position; Undefined team |
| `35` | `45` | Position_Unknown | Team_Unknown | 356–359 | 4 | 1 | Undefined position; Undefined team |
| `36` | `47` | Position_Unknown | Team_Unknown | 359–359 | 1 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_DownBlock` and target `16` (4 segments found)
- ⚠️ Ambiguous match for action `Action_DownBlock` and target `4` (2 segments found)
- ⚠️ Ambiguous match for action `Action_PullBlock` and target `11` (5 segments found)
- ⚠️ Ambiguous match for action `Action_Handoff` and target `6` (2 segments found)
- ❌ Missing segment for action `Action_BallCarry` on target `7` (RB)

### Track Identity Issues

- ⚠️ Player track XML ID `1` (actor_track_id `2`): `SAF` position mapped to `defense` team
- ⚠️ 22 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 22 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 44 |
| Missing visible bounding boxes during action | 71 |
| Track-related warning | 2 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 359 as fallback play end.
- ⚠️ Segment 'Action_BallCarry' for track '6' has invalid range: start=187, end=180. Clamping end to start.
- ⚠️ Resolved action overlap for track '10' (C): higher_priority='Action_BallSnap' [144–158], lower_priority='Action_PullBlock' annotated_start=147, effective_Action_PullBlock_start=159.
- ⚠️ Action 'Action_None' range [144-226] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [244-250] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [259-337] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [344-345] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [144-359] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [144-286] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [292-293] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [297-304] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [147-175] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [144-185] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [189-196] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [213-216] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [220-359] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_Handoff' range [168-175] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [187-256] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [260-314] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-180] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullLeadBlock' range [147-163] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [144-191] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [144-161] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [173-176] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [213-288] for track '9' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [159-164] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [167-171] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [176-177] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [179-216] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [228-230] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [232-319] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [144-203] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [208-213] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [215-218] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [225-228] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [235-253] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [144-193] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [195-196] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [198-199] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [144-318] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [147-149] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [155-188] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [190-224] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [228-234] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [168-281] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [178-181] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [183-184] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [193-196] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [201-209] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [215-259] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [291-339] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [201-235] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [239-282] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [219-221] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [228-249] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [236-252] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [257-259] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [279-338] for track '22' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [343-351] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [249-251] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [262-276] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [310-344] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [262-351] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [265-266] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [273-301] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [303-305] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [272-278] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [287-288] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [290-295] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [287-359] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [291-359] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [292-323] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [330-343] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [346-359] for track '31' has 1 frames without a visible bounding box.
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

</details>