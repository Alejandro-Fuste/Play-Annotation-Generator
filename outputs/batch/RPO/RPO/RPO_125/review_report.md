# Play-Annotation-Generator Annotation Review — RPO_125

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `RPO_125`
- **Frame Range:** 0 to 359 (360 total frames)
- **Play:** `Play_Pass_RPO`
- **Result:** `Result_Touchdown`
- **Result Frame:** 359
- **Player Tracks:** 41
- **Ball Tracks:** 0
- **Action Segments:** 117
- **Validation Warnings:** 108
- **Validation Errors:** 0
- **Overall Status:** WARNING
- **Non-Temporal Descriptors:** 1
  - **Non-Temporal Action Descriptor:** `Action_RunPostRoute` | actor_track_id `0` | source `Route` | no temporal frame

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 20
- **Exact Matches:** 7
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 1
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 98
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `4` | `Group` |
| ✅ EXACT | `Action_ReadDefender` | QB | offense | `16` | `16` |
| ✅ EXACT | `Action_RunBlock` | C | offense | `14` | `14` |
| ⚠️ AMBIGUOUS MATCH | `Action_RunBlock` | LT | offense | `17` | `17` |
| ✅ EXACT | `Action_RunBlock` | RT | offense | `19` | `19` |
| ✅ EXACT | `Action_RunBlock` | RG | offense | `20` | `20` |
| ✅ EXACT | `Action_RunBlock` | LG | offense | `21` | `21` |
| ✅ EXACT | `Action_PullBall` | QB | offense | `16` | `16` |
| ✅ EXACT | `Action_ThrowPass` | QB | offense | `16` | `16` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `0` | `Group` | 0 | START | 0 | 52 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `1` | `Group` | 0 | START | 0 | 52 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `13` | `Group` | 0 | START | 0 | 52 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `14` | `Group` | 0 | START | 0 | 52 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `16` | `Group` | 0 | START | 0 | 52 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `17` | `Group` | 0 | START | 0 | 52 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `18` | `Group` | 0 | START | 0 | 52 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `19` | `Group` | 0 | START | 0 | 52 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `20` | `Group` | 0 | START | 0 | 52 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `21` | `Group` | 0 | START | 0 | 52 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `4` | `Group` | 0 | START | 0 | 52 |
| ✅ EXACT | `Action_ReadDefender` | QB | `16` | `16` | 53 | START | 53 | 74 |
| ✅ EXACT | `Action_RunBlock` | C | `14` | `14` | 54 | START | 54 | 114 |
| ⚠️ AMBIGUOUS MATCH | `Action_RunBlock` | LT | `17` | `17` | 54 | START | 54 | 70 |
| ✅ EXACT | `Action_RunBlock` | RT | `19` | `19` | 54 | START | 54 | 114 |
| ✅ EXACT | `Action_RunBlock` | RG | `20` | `20` | 54 | START | 54 | 114 |
| ✅ EXACT | `Action_RunBlock` | LG | `21` | `21` | 54 | START | 54 | 114 |
| ✅ EXACT | `Action_PullBall` | QB | `16` | `16` | 75 | START | 75 | 88 |
| ✅ EXACT | `Action_ThrowPass` | QB | `16` | `16` | 109 | START | 109 | 114 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–359
- **Visible Samples:** 360

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 52 | 53 | inferred_complete_timeline |
| `Action_ReadDefender` | 53 | 74 | 22 | inferred_complete_timeline |
| `Action_PullBall` | 75 | 88 | 14 | inferred_complete_timeline |
| `Action_None` | 89 | 108 | 20 | inferred_complete_timeline |
| `Action_ThrowPass` | 109 | 114 | 6 | inferred_complete_timeline |
| `Action_None` | 115 | 359 | 245 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–359
- **Visible Samples:** 357

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 52 | 53 | inferred_complete_timeline |
| `Action_None` | 53 | 266 | 214 | inferred_complete_timeline |
| `Action_None` | 268 | 339 | 72 | inferred_complete_timeline |
| `Action_None` | 342 | 359 | 18 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–344
- **Visible Samples:** 341

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 52 | 53 | inferred_complete_timeline |
| `Action_None` | 53 | 336 | 284 | inferred_complete_timeline |
| `Action_None` | 341 | 344 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–359
- **Visible Samples:** 351

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 52 | 53 | inferred_complete_timeline |
| `Action_None` | 53 | 135 | 83 | inferred_complete_timeline |
| `Action_None` | 140 | 143 | 4 | inferred_complete_timeline |
| `Action_None` | 148 | 203 | 56 | inferred_complete_timeline |
| `Action_None` | 205 | 359 | 155 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–359
- **Visible Samples:** 360

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 52 | 53 | inferred_complete_timeline |
| `Action_None` | 53 | 359 | 307 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–359
- **Visible Samples:** 353

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 52 | 53 | inferred_complete_timeline |
| `Action_None` | 53 | 151 | 99 | inferred_complete_timeline |
| `Action_None` | 154 | 158 | 5 | inferred_complete_timeline |
| `Action_None` | 164 | 359 | 196 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–102
- **Visible Samples:** 98

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 52 | 53 | inferred_complete_timeline |
| `Action_None` | 53 | 53 | 1 | inferred_complete_timeline |
| `Action_RunBlock` | 54 | 70 | 17 | inferred_complete_timeline |
| `Action_RunBlock` | 76 | 102 | 27 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `21`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–359
- **Visible Samples:** 359

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 52 | 53 | inferred_complete_timeline |
| `Action_None` | 53 | 53 | 1 | inferred_complete_timeline |
| `Action_RunBlock` | 54 | 114 | 61 | inferred_complete_timeline |
| `Action_None` | 115 | 133 | 19 | inferred_complete_timeline |
| `Action_None` | 135 | 359 | 225 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–359
- **Visible Samples:** 360

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 52 | 53 | inferred_complete_timeline |
| `Action_None` | 53 | 53 | 1 | inferred_complete_timeline |
| `Action_RunBlock` | 54 | 114 | 61 | inferred_complete_timeline |
| `Action_None` | 115 | 359 | 245 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–359
- **Visible Samples:** 359

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 52 | 53 | inferred_complete_timeline |
| `Action_None` | 53 | 53 | 1 | inferred_complete_timeline |
| `Action_RunBlock` | 54 | 114 | 61 | inferred_complete_timeline |
| `Action_None` | 115 | 347 | 233 | inferred_complete_timeline |
| `Action_None` | 349 | 359 | 11 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–359
- **Visible Samples:** 356

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 52 | 53 | inferred_complete_timeline |
| `Action_None` | 53 | 53 | 1 | inferred_complete_timeline |
| `Action_RunBlock` | 54 | 114 | 61 | inferred_complete_timeline |
| `Action_None` | 115 | 240 | 126 | inferred_complete_timeline |
| `Action_None` | 244 | 254 | 11 | inferred_complete_timeline |
| `Action_None` | 256 | 359 | 104 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–359
- **Visible Samples:** 346

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 52 | 53 | inferred_complete_timeline |
| `Action_None` | 53 | 120 | 68 | inferred_complete_timeline |
| `Action_None` | 130 | 225 | 96 | inferred_complete_timeline |
| `Action_None` | 231 | 359 | 129 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–359
- **Visible Samples:** 351

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 52 | 53 | inferred_complete_timeline |
| `Action_None` | 53 | 192 | 140 | inferred_complete_timeline |
| `Action_None` | 195 | 203 | 9 | inferred_complete_timeline |
| `Action_None` | 209 | 318 | 110 | inferred_complete_timeline |
| `Action_None` | 321 | 359 | 39 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–79
- **Visible Samples:** 68

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 52 | 53 | inferred_complete_timeline |
| `Action_None` | 53 | 65 | 13 | inferred_complete_timeline |
| `Action_None` | 78 | 79 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–65
- **Visible Samples:** 66

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 52 | 53 | inferred_complete_timeline |
| `Action_None` | 53 | 65 | 13 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–359
- **Visible Samples:** 357

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 52 | 53 | inferred_complete_timeline |
| `Action_None` | 53 | 186 | 134 | inferred_complete_timeline |
| `Action_None` | 190 | 359 | 170 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–359
- **Visible Samples:** 360

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 52 | 53 | inferred_complete_timeline |
| `Action_None` | 53 | 359 | 307 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–359
- **Visible Samples:** 360

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 52 | 53 | inferred_complete_timeline |
| `Action_None` | 53 | 359 | 307 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–359
- **Visible Samples:** 360

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 52 | 53 | inferred_complete_timeline |
| `Action_None` | 53 | 359 | 307 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–170
- **Visible Samples:** 170

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 52 | 53 | inferred_complete_timeline |
| `Action_None` | 53 | 165 | 113 | inferred_complete_timeline |
| `Action_None` | 167 | 170 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–205
- **Visible Samples:** 206

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 52 | 53 | inferred_complete_timeline |
| `Action_None` | 53 | 205 | 153 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–149
- **Visible Samples:** 149

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 52 | 53 | inferred_complete_timeline |
| `Action_None` | 53 | 143 | 91 | inferred_complete_timeline |
| `Action_None` | 145 | 149 | 5 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `22` | `25` | Position_Unknown | Team_Unknown | 87–359 | 273 | 1 | Undefined position; Undefined team |
| `23` | `29` | Position_Unknown | Team_Unknown | 102–107 | 6 | 1 | Undefined position; Undefined team |
| `24` | `30` | Position_Unknown | Team_Unknown | 110–359 | 246 | 3 | Undefined position; Undefined team |
| `25` | `32` | Position_Unknown | Team_Unknown | 117–359 | 241 | 3 | Undefined position; Undefined team |
| `26` | `37` | Position_Unknown | Team_Unknown | 153–154 | 2 | 1 | Undefined position; Undefined team |
| `27` | `39` | Position_Unknown | Team_Unknown | 159–162 | 4 | 1 | Undefined position; Undefined team |
| `28` | `40` | Position_Unknown | Team_Unknown | 168–272 | 98 | 4 | Undefined position; Undefined team |
| `29` | `42` | Position_Unknown | Team_Unknown | 173–359 | 187 | 1 | Undefined position; Undefined team |
| `30` | `43` | Position_Unknown | Team_Unknown | 175–176 | 2 | 1 | Undefined position; Undefined team |
| `31` | `45` | Position_Unknown | Team_Unknown | 183–185 | 3 | 1 | Undefined position; Undefined team |
| `32` | `50` | Position_Unknown | Team_Unknown | 201–205 | 5 | 1 | Undefined position; Undefined team |
| `33` | `51` | Position_Unknown | Team_Unknown | 208–211 | 4 | 1 | Undefined position; Undefined team |
| `34` | `52` | Position_Unknown | Team_Unknown | 211–359 | 140 | 6 | Undefined position; Undefined team |
| `35` | `53` | Position_Unknown | Team_Unknown | 232–359 | 127 | 2 | Undefined position; Undefined team |
| `36` | `55` | Position_Unknown | Team_Unknown | 246–250 | 5 | 1 | Undefined position; Undefined team |
| `37` | `59` | Position_Unknown | Team_Unknown | 276–296 | 8 | 3 | Undefined position; Undefined team |
| `38` | `61` | Position_Unknown | Team_Unknown | 282–283 | 2 | 1 | Undefined position; Undefined team |
| `39` | `62` | Position_Unknown | Team_Unknown | 297–341 | 8 | 4 | Undefined position; Undefined team |
| `40` | `68` | Position_Unknown | Team_Unknown | 319–359 | 34 | 2 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_RunBlock` and target `17` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `5` (actor_track_id `5`): `SAF2` position mapped to `defense` team
- ⚠️ Player track XML ID `9` (actor_track_id `9`): `SAF1` position mapped to `defense` team
- ⚠️ 19 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 19 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 38 |
| Missing visible bounding boxes during action | 69 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 359 as fallback play end.
- ⚠️ Action 'Action_None' range [53-135] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [140-143] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [148-203] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [53-336] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [341-344] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [53-192] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [195-203] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [209-318] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [53-143] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [145-149] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [53-359] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [53-359] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [53-186] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [53-205] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [53-165] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [167-170] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [53-65] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [53-120] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [130-225] for track '12' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [231-359] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [53-151] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [154-158] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [115-359] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [53-65] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [78-79] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [54-70] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [76-102] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [53-266] for track '18' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [268-339] for track '18' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [115-240] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [244-254] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [256-359] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [115-347] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [115-133] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [87-359] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [102-107] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [110-119] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [122-123] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [117-247] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [249-274] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [153-154] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [159-162] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [168-172] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [175-191] for track '28' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [195-268] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [271-272] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [175-176] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [183-185] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [201-205] for track '32' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [208-211] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [211-310] for track '34' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [313-315] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [317-322] for track '34' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [327-337] for track '34' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [339-343] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [345-359] for track '34' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [232-235] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [237-359] for track '35' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [246-250] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [276-278] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [280-281] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [294-296] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [282-283] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [297-298] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [301-302] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [330-331] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [340-341] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [319-323] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [331-359] for track '40' has 2 frames without a visible bounding box.
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

</details>