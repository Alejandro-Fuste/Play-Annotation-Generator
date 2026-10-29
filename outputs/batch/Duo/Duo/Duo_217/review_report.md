# Play-Annotation-Generator Annotation Review — Duo_217

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Duo_217`
- **Frame Range:** 0 to 299 (300 total frames)
- **Play:** `Play_Run_Duo`
- **Result:** `Result_Tackle`
- **Result Frame:** 299
- **Player Tracks:** 33
- **Ball Tracks:** 1
- **Action Segments:** 70
- **Validation Warnings:** 88
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 14
- **Exact Matches:** 2
- **Group Expanded Events:** 10
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 0
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 33
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `28` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `3` | `Group` |
| ✅ EXACT | `Action_ComboBlock` | LT | offense | `14` | `10` |
| ✅ EXACT | `Action_ComboBlock` | TE | offense | `3` | `3` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `0` | `Group` | 4 | START | 0 | 299 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `11` | `Group` | 4 | START | 4 | 299 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `12` | `Group` | 4 | START | 4 | 250 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `14` | `Group` | 4 | START | 4 | 211 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `16` | `Group` | 4 | START | 4 | 216 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `17` | `Group` | 4 | START | 4 | 86 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `18` | `Group` | 4 | START | 4 | 61 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `2` | `Group` | 4 | START | 0 | 202 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `28` | `Group` | 4 | START | 74 | 148 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `3` | `Group` | 4 | START | 0 | 211 |
| ✅ EXACT | `Action_ComboBlock` | LT | `14` | `10` | 212 | START | 212 | 216 |
| ✅ EXACT | `Action_ComboBlock` | TE | `3` | `3` | 212 | START | 212 | 244 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 244 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `11`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 4–299
- **Visible Samples:** 296

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 4 | 299 | 296 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `12`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 4–299
- **Visible Samples:** 291

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 4 | 250 | 247 | inferred_complete_timeline |
| `Action_PreSnap` | 255 | 285 | 31 | inferred_complete_timeline |
| `Action_PreSnap` | 287 | 299 | 13 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `28`</summary>

- **xml_track_id:** `22`
- **actor_track_id:** `28`
- **team_side:** `offense`
- **Visible Frames:** 74–148
- **Visible Samples:** 75

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 74 | 148 | 75 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `16`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 4–299
- **Visible Samples:** 292

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 4 | 216 | 213 | inferred_complete_timeline |
| `Action_PreSnap` | 218 | 253 | 36 | inferred_complete_timeline |
| `Action_PreSnap` | 256 | 260 | 5 | inferred_complete_timeline |
| `Action_PreSnap` | 262 | 299 | 38 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–285
- **Visible Samples:** 286

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 211 | 212 | inferred_complete_timeline |
| `Action_ComboBlock` | 212 | 244 | 33 | inferred_complete_timeline |
| `Action_None` | 245 | 285 | 41 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `14`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 4–216
- **Visible Samples:** 213

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 4 | 211 | 208 | inferred_complete_timeline |
| `Action_ComboBlock` | 212 | 216 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `18`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 4–299
- **Visible Samples:** 294

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 4 | 61 | 58 | inferred_complete_timeline |
| `Action_PreSnap` | 64 | 299 | 236 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 291

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 202 | 203 | inferred_complete_timeline |
| `Action_PreSnap` | 212 | 299 | 88 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `17`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 4–299
- **Visible Samples:** 292

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 4 | 86 | 83 | inferred_complete_timeline |
| `Action_PreSnap` | 90 | 261 | 172 | inferred_complete_timeline |
| `Action_PreSnap` | 263 | 299 | 37 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 300

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 299 | 300 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `10`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 4–156
- **Visible Samples:** 153

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 4 | 156 | 153 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `21`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `21`
- **team_side:** `defense`
- **Visible Frames:** 4–299
- **Visible Samples:** 294

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 4 | 234 | 231 | inferred_complete_timeline |
| `Action_PreSnap` | 237 | 299 | 63 | inferred_complete_timeline |

</details>

<details>
<summary>DT — actor_track_id `24`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `24`
- **team_side:** `defense`
- **Visible Frames:** 4–277
- **Visible Samples:** 253

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 4 | 43 | 40 | inferred_complete_timeline |
| `Action_PreSnap` | 45 | 255 | 211 | inferred_complete_timeline |
| `Action_PreSnap` | 276 | 277 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `19`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `19`
- **team_side:** `defense`
- **Visible Frames:** 4–281
- **Visible Samples:** 278

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 4 | 281 | 278 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `13`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 4–275
- **Visible Samples:** 268

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 4 | 268 | 265 | inferred_complete_timeline |
| `Action_PreSnap` | 273 | 275 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `20`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `20`
- **team_side:** `defense`
- **Visible Frames:** 4–205
- **Visible Samples:** 195

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 4 | 27 | 24 | inferred_complete_timeline |
| `Action_PreSnap` | 31 | 45 | 15 | inferred_complete_timeline |
| `Action_PreSnap` | 49 | 55 | 7 | inferred_complete_timeline |
| `Action_PreSnap` | 57 | 205 | 149 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `15`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 4–299
- **Visible Samples:** 295

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 4 | 80 | 77 | inferred_complete_timeline |
| `Action_PreSnap` | 82 | 299 | 218 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `22`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `22`
- **team_side:** `defense`
- **Visible Frames:** 4–288
- **Visible Samples:** 257

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 4 | 187 | 184 | inferred_complete_timeline |
| `Action_PreSnap` | 196 | 208 | 13 | inferred_complete_timeline |
| `Action_PreSnap` | 219 | 220 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 231 | 288 | 58 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `1` | `1` | Position_Unknown | Team_Unknown | 0–3 | 4 | 1 | Undefined position; Undefined team |
| `4` | `4` | Position_Unknown | Team_Unknown | 0–3 | 4 | 1 | Undefined position; Undefined team |
| `5` | `5` | Position_Unknown | Team_Unknown | 0–3 | 4 | 1 | Undefined position; Undefined team |
| `19` | `23` | Position_Unknown | Team_Unknown | 4–263 | 258 | 2 | Undefined position; Undefined team |
| `23` | `30` | Position_Unknown | Team_Unknown | 116–122 | 7 | 1 | Undefined position; Undefined team |
| `24` | `31` | Position_Unknown | Team_Unknown | 151–200 | 47 | 3 | Undefined position; Undefined team |
| `25` | `33` | Position_Unknown | Team_Unknown | 158–277 | 29 | 3 | Undefined position; Undefined team |
| `26` | `34` | Position_Unknown | Team_Unknown | 196–299 | 104 | 1 | Undefined position; Undefined team |
| `27` | `37` | Position_Unknown | Team_Unknown | 231–299 | 55 | 6 | Undefined position; Undefined team |
| `28` | `38` | Position_Unknown | Team_Unknown | 233–268 | 29 | 4 | Undefined position; Undefined team |
| `29` | `41` | Position_Unknown | Team_Unknown | 249–299 | 51 | 1 | Undefined position; Undefined team |
| `30` | `42` | Position_Unknown | Team_Unknown | 260–299 | 36 | 2 | Undefined position; Undefined team |
| `31` | `43` | Position_Unknown | Team_Unknown | 265–299 | 35 | 1 | Undefined position; Undefined team |
| `32` | `45` | Position_Unknown | Team_Unknown | 281–299 | 19 | 1 | Undefined position; Undefined team |
| `33` | `46` | Position_Unknown | Team_Unknown | 296–299 | 4 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

| xml_track_id | actor_track_id | First Visible Frame | Last Visible Frame | Visible Samples | Coverage | Missing Frame Ranges |
| --- | --- | --- | --- | --- | --- | --- |
| `21` | `27` | 56 | 100 | 18 | 40.0% | 69–95 |

## 5. Issues Requiring Review

### Action Mapping Issues

None.

### Track Identity Issues

- ⚠️ Player track XML ID `18` (actor_track_id `22`): `SAF` position mapped to `defense` team
- ⚠️ 15 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 15 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 30 |
| Missing visible bounding boxes during action | 55 |
| Track-related warning | 2 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 436: Duplicate assignment for track ID '15' in grid. Overwriting previous assignment.
- ⚠️ Track ID '6' in Player Track ID sheet does not exist in MOT gt.txt.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 299 as fallback play end.
- ⚠️ Action 'Action_PreSnap' range [0-3] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-202] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ComboBlock' range [212-244] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [245-285] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-3] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-3] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [4-156] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [4-299] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [4-250] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [255-285] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [4-268] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [273-275] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ComboBlock' range [212-216] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [4-80] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [4-216] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [218-253] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [256-260] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [4-86] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [90-261] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [4-61] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [4-281] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [4-27] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [31-45] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [49-55] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [57-205] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [4-234] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [237-299] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [4-187] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [196-208] for track '18' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [219-220] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [231-288] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [4-256] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [259-263] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [4-43] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [45-255] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [276-277] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [74-148] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [116-122] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [151-173] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [175-196] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [199-200] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [158-165] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [173-191] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [276-277] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [231-234] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [242-243] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [245-246] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [248-249] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [254-257] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [233-235] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [240-241] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [243-244] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [247-268] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [260-276] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [265-299] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Player track '1' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '1' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '4' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '4' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '5' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '5' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '19' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '19' has undefined team_side. Will map to Team_Unknown.
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

</details>