# Play-Annotation-Generator Annotation Review — Power_192

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Power_192`
- **Frame Range:** 0 to 329 (330 total frames)
- **Play:** `Play_Run_Power`
- **Result:** `Result_Tackle`
- **Result Frame:** 329
- **Player Tracks:** 36
- **Ball Tracks:** 0
- **Action Segments:** 77
- **Validation Warnings:** 104
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 11
- **Exact Matches:** 2
- **Group Expanded Events:** 7
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 2
- **Global Events (no player segment expected):** 0
- **Inferred Coverage Segments (Action_None):** 59
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `9` | `Group` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | DT1 | defense | `15` | `14` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | RG | offense | `4` | `4` |
| ✅ EXACT | `Action_DownBlock` | Position_Unknown | Team_Unknown | `8` | `8` |
| ✅ EXACT | `Action_PullBlock` | LG | offense | `7` | `7` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `0` | `Group` | 14 | START | 14 | 278 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `10` | `Group` | 14 | START | 14 | 269 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `2` | `Group` | 14 | START | 14 | 237 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `4` | `Group` | 14 | START | 14 | 178 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | `5` | `Group` | 14 | START | 14 | 289 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `7` | `Group` | 14 | START | 14 | 178 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `9` | `Group` | 14 | START | 14 | 248 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | DT1 | `15` | `14` | 179 | START | 179 | 185 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | RG | `4` | `4` | 179 | START | 179 | 196 |
| ✅ EXACT | `Action_DownBlock` | Position_Unknown | `8` | `8` | 179 | START | 179 | 233 |
| ✅ EXACT | `Action_PullBlock` | LG | `7` | `7` | 179 | START | 179 | 233 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 14–296
- **Visible Samples:** 282

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 14 | 269 | 256 | inferred_complete_timeline |
| `Action_PreSnap` | 271 | 296 | 26 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 14–329
- **Visible Samples:** 315

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 14 | 278 | 265 | inferred_complete_timeline |
| `Action_PreSnap` | 280 | 329 | 50 | inferred_complete_timeline |

</details>

<details>
<summary>TE2 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 14–329
- **Visible Samples:** 309

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 14 | 289 | 276 | inferred_complete_timeline |
| `Action_PreSnap` | 295 | 297 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 299 | 302 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 304 | 329 | 26 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 14–248
- **Visible Samples:** 235

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 14 | 248 | 235 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 14–329
- **Visible Samples:** 316

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 14 | 178 | 165 | inferred_complete_timeline |
| `Action_PullBlock` | 179 | 233 | 55 | inferred_complete_timeline |
| `Action_None` | 234 | 329 | 96 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 14–329
- **Visible Samples:** 310

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 14 | 178 | 165 | inferred_complete_timeline |
| `Action_DownBlock` | 179 | 196 | 18 | inferred_complete_timeline |
| `Action_DownBlock` | 198 | 233 | 36 | inferred_complete_timeline |
| `Action_None` | 234 | 245 | 12 | inferred_complete_timeline |
| `Action_None` | 251 | 329 | 79 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 14–329
- **Visible Samples:** 307

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 14 | 237 | 224 | inferred_complete_timeline |
| `Action_PreSnap` | 246 | 248 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 250 | 329 | 80 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 14–176
- **Visible Samples:** 163

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 14 | 176 | 163 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 14–329
- **Visible Samples:** 244

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 14 | 198 | 185 | inferred_complete_timeline |
| `Action_PreSnap` | 271 | 329 | 59 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 22–255
- **Visible Samples:** 148

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 22 | 23 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 50 | 56 | 7 | inferred_complete_timeline |
| `Action_PreSnap` | 84 | 87 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 96 | 123 | 28 | inferred_complete_timeline |
| `Action_PreSnap` | 140 | 178 | 39 | inferred_complete_timeline |
| `Action_DownBlock` | 179 | 185 | 7 | inferred_complete_timeline |
| `Action_DownBlock` | 193 | 231 | 39 | inferred_complete_timeline |
| `Action_None` | 234 | 255 | 22 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 14–179
- **Visible Samples:** 166

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 14 | 179 | 166 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 14–226
- **Visible Samples:** 213

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 14 | 226 | 213 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 14–329
- **Visible Samples:** 316

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 14 | 329 | 316 | inferred_complete_timeline |

</details>

<details>
<summary>LB3 — actor_track_id `22`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `22`
- **team_side:** `defense`
- **Visible Frames:** 79–329
- **Visible Samples:** 243

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 79 | 315 | 237 | inferred_complete_timeline |
| `Action_PreSnap` | 324 | 329 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `20`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `20`
- **team_side:** `defense`
- **Visible Frames:** 33–176
- **Visible Samples:** 114

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 33 | 36 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 57 | 66 | 10 | inferred_complete_timeline |
| `Action_PreSnap` | 70 | 85 | 16 | inferred_complete_timeline |
| `Action_PreSnap` | 89 | 168 | 80 | inferred_complete_timeline |
| `Action_PreSnap` | 173 | 176 | 4 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `1` | `1` | Position_Unknown | Team_Unknown | 14–29 | 16 | 1 | Undefined position; Undefined team |
| `8` | `8` | Position_Unknown | Team_Unknown | 14–329 | 279 | 7 | Undefined position; Undefined team |
| `17` | `23` | Position_Unknown | Team_Unknown | 133–217 | 85 | 1 | Undefined position; Undefined team |
| `18` | `28` | Position_Unknown | Team_Unknown | 183–188 | 6 | 1 | Undefined position; Undefined team |
| `19` | `30` | Position_Unknown | Team_Unknown | 186–329 | 144 | 1 | Undefined position; Undefined team |
| `20` | `31` | Position_Unknown | Team_Unknown | 187–251 | 47 | 3 | Undefined position; Undefined team |
| `21` | `32` | Position_Unknown | Team_Unknown | 194–203 | 10 | 1 | Undefined position; Undefined team |
| `22` | `33` | Position_Unknown | Team_Unknown | 205–329 | 45 | 2 | Undefined position; Undefined team |
| `23` | `35` | Position_Unknown | Team_Unknown | 224–226 | 3 | 1 | Undefined position; Undefined team |
| `24` | `38` | Position_Unknown | Team_Unknown | 235–241 | 4 | 2 | Undefined position; Undefined team |
| `25` | `42` | Position_Unknown | Team_Unknown | 246–294 | 41 | 4 | Undefined position; Undefined team |
| `26` | `43` | Position_Unknown | Team_Unknown | 252–263 | 12 | 1 | Undefined position; Undefined team |
| `27` | `44` | Position_Unknown | Team_Unknown | 252–326 | 73 | 2 | Undefined position; Undefined team |
| `28` | `45` | Position_Unknown | Team_Unknown | 273–329 | 57 | 1 | Undefined position; Undefined team |
| `29` | `46` | Position_Unknown | Team_Unknown | 285–329 | 45 | 1 | Undefined position; Undefined team |
| `30` | `47` | Position_Unknown | Team_Unknown | 287–292 | 6 | 1 | Undefined position; Undefined team |
| `31` | `48` | Position_Unknown | Team_Unknown | 287–319 | 4 | 2 | Undefined position; Undefined team |
| `32` | `49` | Position_Unknown | Team_Unknown | 305–329 | 25 | 1 | Undefined position; Undefined team |
| `33` | `51` | Position_Unknown | Team_Unknown | 318–329 | 12 | 1 | Undefined position; Undefined team |
| `34` | `52` | Position_Unknown | Team_Unknown | 322–329 | 8 | 1 | Undefined position; Undefined team |
| `35` | `54` | Position_Unknown | Team_Unknown | 323–329 | 7 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_DownBlock` and target `15` (2 segments found)
- ⚠️ Ambiguous match for action `Action_DownBlock` and target `4` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `15` (actor_track_id `20`): `SAF` position mapped to `defense` team
- ⚠️ 21 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 21 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 42 |
| Missing visible bounding boxes during action | 59 |
| Track-related warning | 2 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 386: Duplicate assignment for track ID '12' in grid. Overwriting previous assignment.
- ⚠️ Track ID '18' in Player Track ID sheet does not exist in MOT gt.txt.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 329 as fallback play end.
- ⚠️ Action 'Action_PreSnap' range [14-278] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [14-29] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [14-237] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [246-248] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [14-226] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [179-196] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [234-245] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [251-329] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [14-289] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [295-297] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [299-302] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [179-233] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [234-329] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [14-168] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [234-246] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [249-251] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [273-276] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [14-248] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [14-269] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [271-296] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [14-179] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [14-198] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [271-329] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [14-176] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [22-23] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [50-56] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [84-87] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [96-123] for track '14' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [140-178] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [179-185] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [193-231] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [234-255] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [33-36] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [57-66] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [70-85] for track '15' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [89-168] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [173-176] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [79-315] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [133-217] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [183-188] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [187-188] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [204-244] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [248-251] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [194-203] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [205-248] for track '22' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [224-226] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [235-236] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [240-241] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [246-249] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [251-280] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [285-287] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [291-294] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [252-263] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [252-322] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [325-326] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [273-329] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [287-292] for track '30' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [287-288] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [318-319] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Player track '1' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '1' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '8' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '8' has undefined team_side. Will map to Team_Unknown.
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