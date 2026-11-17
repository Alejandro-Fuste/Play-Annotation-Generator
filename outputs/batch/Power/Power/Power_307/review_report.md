# Play-Annotation-Generator Annotation Review — Power_307

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Power_307`
- **Frame Range:** 0 to 299 (300 total frames)
- **Play:** `Play_Run_Power`
- **Result:** `Result_Tackle`
- **Result Frame:** 299
- **Player Tracks:** 35
- **Ball Tracks:** 0
- **Action Segments:** 79
- **Validation Warnings:** 90
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 15
- **Exact Matches:** 4
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 0
- **Global Events (no player segment expected):** 0
- **Inferred Coverage Segments (Action_None):** 57
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `5` | `Group` |
| ✅ EXACT | `Action_DownBlock` | LT | offense | `12` | `12` |
| ✅ EXACT | `Action_DownBlock` | LG | offense | `14` | `14` |
| ✅ EXACT | `Action_DownBlock` | C | offense | `17` | `17` |
| ✅ EXACT | `Action_PullBlock` | RG | offense | `18` | `18` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `0` | `Group` | 7 | START | 7 | 215 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `1` | `Group` | 7 | START | 7 | 134 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `12` | `Group` | 7 | START | 7 | 78 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `14` | `Group` | 7 | START | 7 | 78 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `15` | `Group` | 7 | START | 7 | 299 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `17` | `Group` | 7 | START | 7 | 78 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `18` | `Group` | 7 | START | 7 | 78 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `19` | `Group` | 7 | START | 7 | 195 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `2` | `Group` | 7 | START | 7 | 299 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `20` | `Group` | 7 | START | 7 | 286 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `5` | `Group` | 7 | START | 7 | 299 |
| ✅ EXACT | `Action_DownBlock` | LT | `12` | `12` | 79 | START | 79 | 167 |
| ✅ EXACT | `Action_DownBlock` | LG | `14` | `14` | 79 | START | 79 | 140 |
| ✅ EXACT | `Action_DownBlock` | C | `17` | `17` | 79 | START | 79 | 167 |
| ✅ EXACT | `Action_PullBlock` | RG | `18` | `18` | 79 | START | 79 | 167 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 7–243
- **Visible Samples:** 202

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 7 | 195 | 189 | inferred_complete_timeline |
| `Action_PreSnap` | 221 | 222 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 229 | 232 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 236 | 237 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 239 | 243 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 7–299
- **Visible Samples:** 293

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 7 | 299 | 293 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 7–299
- **Visible Samples:** 285

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 7 | 215 | 209 | inferred_complete_timeline |
| `Action_PreSnap` | 222 | 248 | 27 | inferred_complete_timeline |
| `Action_PreSnap` | 251 | 299 | 49 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 7–134
- **Visible Samples:** 128

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 7 | 134 | 128 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 7–299
- **Visible Samples:** 293

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 7 | 299 | 293 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 7–299
- **Visible Samples:** 293

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 7 | 299 | 293 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 7–299
- **Visible Samples:** 293

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 7 | 78 | 72 | inferred_complete_timeline |
| `Action_DownBlock` | 79 | 167 | 89 | inferred_complete_timeline |
| `Action_None` | 168 | 299 | 132 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 7–140
- **Visible Samples:** 134

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 7 | 78 | 72 | inferred_complete_timeline |
| `Action_DownBlock` | 79 | 140 | 62 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 7–299
- **Visible Samples:** 285

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 7 | 78 | 72 | inferred_complete_timeline |
| `Action_DownBlock` | 79 | 167 | 89 | inferred_complete_timeline |
| `Action_None` | 168 | 189 | 22 | inferred_complete_timeline |
| `Action_None` | 198 | 299 | 102 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 7–299
- **Visible Samples:** 288

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 7 | 78 | 72 | inferred_complete_timeline |
| `Action_PullBlock` | 79 | 167 | 89 | inferred_complete_timeline |
| `Action_None` | 168 | 253 | 86 | inferred_complete_timeline |
| `Action_None` | 259 | 299 | 41 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 7–294
- **Visible Samples:** 287

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 7 | 286 | 280 | inferred_complete_timeline |
| `Action_PreSnap` | 288 | 294 | 7 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 7–299
- **Visible Samples:** 287

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 7 | 234 | 228 | inferred_complete_timeline |
| `Action_PreSnap` | 241 | 299 | 59 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 7–299
- **Visible Samples:** 291

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 7 | 119 | 113 | inferred_complete_timeline |
| `Action_PreSnap` | 122 | 299 | 178 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 7–178
- **Visible Samples:** 153

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 7 | 155 | 149 | inferred_complete_timeline |
| `Action_PreSnap` | 158 | 159 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 177 | 178 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 7–299
- **Visible Samples:** 293

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 7 | 299 | 293 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 7–299
- **Visible Samples:** 289

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 7 | 175 | 169 | inferred_complete_timeline |
| `Action_PreSnap` | 180 | 299 | 120 | inferred_complete_timeline |

</details>

<details>
<summary>OLB1 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 7–299
- **Visible Samples:** 293

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 7 | 299 | 293 | inferred_complete_timeline |

</details>

<details>
<summary>OLB2 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 7–299
- **Visible Samples:** 260

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 7 | 187 | 181 | inferred_complete_timeline |
| `Action_PreSnap` | 189 | 211 | 23 | inferred_complete_timeline |
| `Action_PreSnap` | 216 | 219 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 245 | 246 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 250 | 299 | 50 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 7–299
- **Visible Samples:** 293

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 7 | 299 | 293 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 7–299
- **Visible Samples:** 293

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 7 | 299 | 293 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 7–299
- **Visible Samples:** 274

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 7 | 209 | 203 | inferred_complete_timeline |
| `Action_PreSnap` | 211 | 212 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 229 | 273 | 45 | inferred_complete_timeline |
| `Action_PreSnap` | 276 | 299 | 24 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `21`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `21`
- **team_side:** `defense`
- **Visible Frames:** 7–299
- **Visible Samples:** 284

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 7 | 130 | 124 | inferred_complete_timeline |
| `Action_PreSnap` | 134 | 195 | 62 | inferred_complete_timeline |
| `Action_PreSnap` | 202 | 299 | 98 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `22` | `22` | Position_Unknown | Team_Unknown | 44–275 | 184 | 6 | Undefined position; Undefined team |
| `23` | `29` | Position_Unknown | Team_Unknown | 143–299 | 157 | 1 | Undefined position; Undefined team |
| `24` | `30` | Position_Unknown | Team_Unknown | 149–299 | 114 | 6 | Undefined position; Undefined team |
| `25` | `32` | Position_Unknown | Team_Unknown | 159–269 | 107 | 2 | Undefined position; Undefined team |
| `26` | `36` | Position_Unknown | Team_Unknown | 205–299 | 95 | 1 | Undefined position; Undefined team |
| `27` | `37` | Position_Unknown | Team_Unknown | 223–228 | 6 | 1 | Undefined position; Undefined team |
| `28` | `39` | Position_Unknown | Team_Unknown | 245–289 | 17 | 2 | Undefined position; Undefined team |
| `29` | `45` | Position_Unknown | Team_Unknown | 276–277 | 2 | 1 | Undefined position; Undefined team |
| `30` | `46` | Position_Unknown | Team_Unknown | 277–293 | 10 | 2 | Undefined position; Undefined team |
| `31` | `47` | Position_Unknown | Team_Unknown | 281–291 | 10 | 2 | Undefined position; Undefined team |
| `32` | `49` | Position_Unknown | Team_Unknown | 296–299 | 4 | 1 | Undefined position; Undefined team |
| `33` | `50` | Position_Unknown | Team_Unknown | 296–298 | 3 | 1 | Undefined position; Undefined team |
| `34` | `51` | Position_Unknown | Team_Unknown | 296–299 | 4 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

None.

### Track Identity Issues

- ⚠️ Player track XML ID `13` (actor_track_id `13`): `SAF1` position mapped to `defense` team
- ⚠️ Player track XML ID `21` (actor_track_id `21`): `SAF2` position mapped to `defense` team
- ⚠️ 13 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 13 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 26 |
| Missing visible bounding boxes during action | 63 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 299 as fallback play end.
- ⚠️ Action 'Action_PreSnap' range [7-215] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [222-248] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [251-299] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [7-134] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [7-234] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [7-119] for track '6' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [7-155] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [158-159] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [177-178] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [7-187] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [189-211] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [216-219] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [245-246] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [250-299] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [7-299] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [7-175] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [180-299] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [79-167] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [168-299] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [7-209] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [211-212] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [229-273] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [79-140] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [7-299] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [7-299] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [79-167] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [168-189] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [198-299] for track '17' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [168-253] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [7-195] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [221-222] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [229-232] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [236-237] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [239-243] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [7-286] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [288-294] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [7-130] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [134-195] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [44-123] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [148-182] for track '22' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [184-185] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [201-203] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [208-257] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [262-275] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [143-299] for track '23' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [149-211] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [213-215] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [217-241] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [265-266] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [276-278] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [159-259] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [264-269] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [205-299] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [223-228] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [245-249] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [278-289] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [276-277] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [277-284] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [292-293] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [281-282] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [284-291] for track '31' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [296-298] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [296-299] for track '34' has 1 frames without a visible bounding box.
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