# Play-Annotation-Generator Annotation Review — Sack_203

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Sack_203`
- **Frame Range:** 0 to 299 (300 total frames)
- **Play:** `Play_Defense_Sack`
- **Result:** `Result_Unknown`
- **Result Frame:** 299
- **Player Tracks:** 25
- **Ball Tracks:** 0
- **Action Segments:** 70
- **Validation Warnings:** 84
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 9
- **Exact Matches:** 3
- **Group Expanded Events:** 6
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 0
- **Global Events (no player segment expected):** 0
- **Inferred Coverage Segments (Action_None):** 49
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `6` | `Group` |
| ✅ EXACT | `Action_CloseOnQuarterback` | LB | defense | `7` | `7` |
| ✅ EXACT | `Action_WrapQuarterback` | LB | defense | `7` | `7` |
| ✅ EXACT | `Action_SackQuarterback` | LB | defense | `7` | `7` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `0` | `Group` | 0 | START | 0 | 79 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `1` | `Group` | 0 | START | 0 | 100 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `10` | `Group` | 0 | START | 0 | 299 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `3` | `Group` | 0 | START | 0 | 130 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `5` | `Group` | 0 | START | 0 | 111 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `6` | `Group` | 0 | START | 0 | 56 |
| ✅ EXACT | `Action_CloseOnQuarterback` | LB | `7` | `7` | 83 | START | 83 | 101 |
| ✅ EXACT | `Action_WrapQuarterback` | LB | `7` | `7` | 102 | START | 102 | 109 |
| ✅ EXACT | `Action_SackQuarterback` | LB | `7` | `7` | 110 | START | 110 | 113 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 283

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 111 | 112 | inferred_complete_timeline |
| `Action_PreSnap` | 121 | 144 | 24 | inferred_complete_timeline |
| `Action_PreSnap` | 148 | 150 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 156 | 299 | 144 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 296

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 100 | 101 | inferred_complete_timeline |
| `Action_PreSnap` | 105 | 299 | 195 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–83
- **Visible Samples:** 83

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 56 | 57 | inferred_complete_timeline |
| `Action_PreSnap` | 58 | 83 | 26 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–293
- **Visible Samples:** 283

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 130 | 131 | inferred_complete_timeline |
| `Action_PreSnap` | 134 | 135 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 137 | 240 | 104 | inferred_complete_timeline |
| `Action_PreSnap` | 243 | 261 | 19 | inferred_complete_timeline |
| `Action_PreSnap` | 264 | 266 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 268 | 283 | 16 | inferred_complete_timeline |
| `Action_PreSnap` | 285 | 286 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 288 | 293 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 300

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 299 | 300 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–79
- **Visible Samples:** 80

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 79 | 80 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 290

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 29 | 30 | inferred_complete_timeline |
| `Action_PreSnap` | 39 | 110 | 72 | inferred_complete_timeline |
| `Action_PreSnap` | 112 | 299 | 188 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–294
- **Visible Samples:** 253

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 94 | 95 | inferred_complete_timeline |
| `Action_PreSnap` | 111 | 112 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 139 | 294 | 156 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–144
- **Visible Samples:** 145

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 144 | 145 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–289
- **Visible Samples:** 284

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 262 | 263 | inferred_complete_timeline |
| `Action_PreSnap` | 269 | 289 | 21 | inferred_complete_timeline |

</details>

<details>
<summary>LB — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–113
- **Visible Samples:** 109

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 9 | 10 | inferred_complete_timeline |
| `Action_PreSnap` | 11 | 14 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 19 | 82 | 64 | inferred_complete_timeline |
| `Action_CloseOnQuarterback` | 83 | 101 | 19 | inferred_complete_timeline |
| `Action_WrapQuarterback` | 102 | 109 | 8 | inferred_complete_timeline |
| `Action_SackQuarterback` | 110 | 113 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–85
- **Visible Samples:** 86

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 85 | 86 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 277

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 153 | 154 | inferred_complete_timeline |
| `Action_PreSnap` | 161 | 265 | 105 | inferred_complete_timeline |
| `Action_PreSnap` | 271 | 272 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 281 | 282 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 284 | 285 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 288 | 299 | 12 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `13` | `17` | Position_Unknown | Team_Unknown | 90–115 | 19 | 2 | Undefined position; Undefined team |
| `14` | `18` | Position_Unknown | Team_Unknown | 96–143 | 43 | 3 | Undefined position; Undefined team |
| `15` | `20` | Position_Unknown | Team_Unknown | 111–135 | 25 | 1 | Undefined position; Undefined team |
| `16` | `21` | Position_Unknown | Team_Unknown | 121–135 | 14 | 2 | Undefined position; Undefined team |
| `17` | `24` | Position_Unknown | Team_Unknown | 176–294 | 107 | 8 | Undefined position; Undefined team |
| `18` | `25` | Position_Unknown | Team_Unknown | 193–284 | 79 | 3 | Undefined position; Undefined team |
| `19` | `26` | Position_Unknown | Team_Unknown | 207–299 | 93 | 1 | Undefined position; Undefined team |
| `20` | `27` | Position_Unknown | Team_Unknown | 220–299 | 79 | 2 | Undefined position; Undefined team |
| `21` | `28` | Position_Unknown | Team_Unknown | 242–275 | 27 | 5 | Undefined position; Undefined team |
| `22` | `29` | Position_Unknown | Team_Unknown | 271–299 | 29 | 1 | Undefined position; Undefined team |
| `23` | `32` | Position_Unknown | Team_Unknown | 284–299 | 16 | 1 | Undefined position; Undefined team |
| `24` | `34` | Position_Unknown | Team_Unknown | 291–299 | 9 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

None.

### Track Identity Issues

- ⚠️ Player track XML ID `2` (actor_track_id `2`): `SAF2` position mapped to `defense` team
- ⚠️ Player track XML ID `9` (actor_track_id `9`): `SAF1` position mapped to `defense` team
- ⚠️ 12 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 12 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 24 |
| Missing visible bounding boxes during action | 59 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 299 as fallback play end.
- ⚠️ Action 'Action_PreSnap' range [0-79] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-100] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [105-299] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-153] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [161-265] for track '2' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [271-272] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [281-282] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [284-285] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-130] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [134-135] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [137-240] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [243-261] for track '3' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [264-266] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [268-283] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [285-286] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [288-293] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-29] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [39-110] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-111] for track '5' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [121-144] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [148-150] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-56] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [58-83] for track '6' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-9] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [11-14] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [19-82] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_SackQuarterback' range [110-113] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-94] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [111-112] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [139-294] for track '8' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-85] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-262] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [269-289] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-144] for track '12' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [90-106] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [114-115] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [96-108] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [111-112] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [116-143] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [111-135] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [121-129] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [131-135] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [176-186] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [189-190] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [192-194] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [196-270] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [272-273] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [279-286] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [288-290] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [292-294] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [193-264] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [272-274] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [281-284] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [220-267] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [242-244] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [247-252] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [254-260] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [264-269] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [271-275] for track '21' has 2 frames without a visible bounding box.
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

</details>