# Play-Annotation-Generator Annotation Review — OutsideZoneStretch_136

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `OutsideZoneStretch_136`
- **Frame Range:** 0 to 509 (510 total frames)
- **Play:** `Play_Run_OutsideZoneStretch`
- **Result:** `Result_Tackle`
- **Result Frame:** 509
- **Player Tracks:** 47
- **Ball Tracks:** 0
- **Action Segments:** 134
- **Validation Warnings:** 182
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 15
- **Exact Matches:** 3
- **Group Expanded Events:** 7
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 4
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 117
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `9` | `Group` |
| ✅ EXACT | `Action_ZoneBlock` | RG | offense | `10` | `10` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | offense | `12` | `12` |
| ✅ EXACT | `Action_ZoneBlock` | RT | offense | `5` | `5` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | offense | `6` | `6` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | offense | `7` | `7` |
| ⚠️ AMBIGUOUS MATCH | `Action_PressEdge` | Position_Unknown | Team_Unknown | `19` | `17` |
| ✅ EXACT | `Action_Handoff` | QB | offense | `13` | `13` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `10` | `Group` | 19 | START | 19 | 170 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `12` | `Group` | 19 | START | 19 | 170 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `13` | `Group` | 19 | START | 19 | 186 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `5` | `Group` | 19 | START | 19 | 170 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `6` | `Group` | 19 | START | 19 | 170 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `7` | `Group` | 19 | START | 19 | 132 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `9` | `Group` | 19 | START | 19 | 85 |
| ✅ EXACT | `Action_ZoneBlock` | RG | `10` | `10` | 171 | START | 171 | 216 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | `12` | `12` | 171 | START | 171 | 177 |
| ✅ EXACT | `Action_ZoneBlock` | RT | `5` | `5` | 171 | START | 171 | 216 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | `6` | `6` | 171 | START | 171 | 190 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | `7` | `7` | 171 | START | 171 | 194 |
| ⚠️ AMBIGUOUS MATCH | `Action_PressEdge` | Position_Unknown | `19` | `17` | 182 | START | 190 | 191 |
| ✅ EXACT | `Action_Handoff` | QB | `13` | `13` | 187 | START | 187 | 209 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 19–244
- **Visible Samples:** 226

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 19 | 186 | 168 | inferred_complete_timeline |
| `Action_Handoff` | 187 | 209 | 23 | inferred_complete_timeline |
| `Action_None` | 210 | 244 | 35 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 19–242
- **Visible Samples:** 199

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 19 | 85 | 67 | inferred_complete_timeline |
| `Action_PreSnap` | 87 | 210 | 124 | inferred_complete_timeline |
| `Action_PreSnap` | 235 | 242 | 8 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 19–509
- **Visible Samples:** 390

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 19 | 170 | 152 | inferred_complete_timeline |
| `Action_ZoneBlock` | 171 | 190 | 20 | inferred_complete_timeline |
| `Action_ZoneBlock` | 202 | 205 | 4 | inferred_complete_timeline |
| `Action_None` | 258 | 272 | 15 | inferred_complete_timeline |
| `Action_None` | 307 | 350 | 44 | inferred_complete_timeline |
| `Action_None` | 355 | 509 | 155 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 19–205
- **Visible Samples:** 147

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 19 | 132 | 114 | inferred_complete_timeline |
| `Action_PreSnap` | 166 | 170 | 5 | inferred_complete_timeline |
| `Action_ZoneBlock` | 171 | 194 | 24 | inferred_complete_timeline |
| `Action_ZoneBlock` | 199 | 200 | 2 | inferred_complete_timeline |
| `Action_ZoneBlock` | 204 | 205 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 19–208
- **Visible Samples:** 185

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 19 | 170 | 152 | inferred_complete_timeline |
| `Action_ZoneBlock` | 171 | 177 | 7 | inferred_complete_timeline |
| `Action_ZoneBlock` | 180 | 193 | 14 | inferred_complete_timeline |
| `Action_ZoneBlock` | 196 | 198 | 3 | inferred_complete_timeline |
| `Action_ZoneBlock` | 200 | 208 | 9 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 19–250
- **Visible Samples:** 232

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 19 | 170 | 152 | inferred_complete_timeline |
| `Action_ZoneBlock` | 171 | 216 | 46 | inferred_complete_timeline |
| `Action_None` | 217 | 250 | 34 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 19–255
- **Visible Samples:** 237

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 19 | 170 | 152 | inferred_complete_timeline |
| `Action_ZoneBlock` | 171 | 216 | 46 | inferred_complete_timeline |
| `Action_None` | 217 | 255 | 39 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE2 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `defense`
- **Visible Frames:** 19–315
- **Visible Samples:** 297

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 19 | 315 | 297 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 19–328
- **Visible Samples:** 249

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 19 | 25 | 7 | inferred_complete_timeline |
| `Action_PreSnap` | 29 | 30 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 34 | 57 | 24 | inferred_complete_timeline |
| `Action_PreSnap` | 59 | 61 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 63 | 109 | 47 | inferred_complete_timeline |
| `Action_PreSnap` | 123 | 135 | 13 | inferred_complete_timeline |
| `Action_PreSnap` | 173 | 204 | 32 | inferred_complete_timeline |
| `Action_PreSnap` | 208 | 328 | 121 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 19–248
- **Visible Samples:** 222

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 19 | 84 | 66 | inferred_complete_timeline |
| `Action_PreSnap` | 88 | 159 | 72 | inferred_complete_timeline |
| `Action_PreSnap` | 162 | 191 | 30 | inferred_complete_timeline |
| `Action_PreSnap` | 195 | 248 | 54 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 19–509
- **Visible Samples:** 429

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 19 | 31 | 13 | inferred_complete_timeline |
| `Action_PreSnap` | 34 | 136 | 103 | inferred_complete_timeline |
| `Action_PreSnap` | 138 | 139 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 172 | 246 | 75 | inferred_complete_timeline |
| `Action_PreSnap` | 249 | 259 | 11 | inferred_complete_timeline |
| `Action_PreSnap` | 267 | 284 | 18 | inferred_complete_timeline |
| `Action_PreSnap` | 286 | 335 | 50 | inferred_complete_timeline |
| `Action_PreSnap` | 351 | 366 | 16 | inferred_complete_timeline |
| `Action_PreSnap` | 369 | 509 | 141 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 19–509
- **Visible Samples:** 435

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 19 | 61 | 43 | inferred_complete_timeline |
| `Action_PreSnap` | 64 | 84 | 21 | inferred_complete_timeline |
| `Action_PreSnap` | 89 | 101 | 13 | inferred_complete_timeline |
| `Action_PreSnap` | 121 | 160 | 40 | inferred_complete_timeline |
| `Action_PreSnap` | 170 | 292 | 123 | inferred_complete_timeline |
| `Action_PreSnap` | 294 | 295 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 299 | 365 | 67 | inferred_complete_timeline |
| `Action_PreSnap` | 382 | 419 | 38 | inferred_complete_timeline |
| `Action_PreSnap` | 422 | 509 | 88 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 19–68
- **Visible Samples:** 50

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 19 | 68 | 50 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `3` | `3` | Position_Unknown | Team_Unknown | 19–240 | 214 | 3 | Undefined position; Undefined team |
| `14` | `14` | Position_Unknown | Team_Unknown | 19–122 | 82 | 5 | Undefined position; Undefined team |
| `15` | `15` | Position_Unknown | Team_Unknown | 35–175 | 133 | 2 | Undefined position; Undefined team |
| `16` | `17` | Position_Unknown | Team_Unknown | 101–355 | 239 | 4 | Undefined position; Undefined team |
| `17` | `19` | Position_Unknown | Team_Unknown | 177–350 | 75 | 7 | Undefined position; Undefined team |
| `18` | `20` | Position_Unknown | Team_Unknown | 200–294 | 95 | 1 | Undefined position; Undefined team |
| `19` | `21` | Position_Unknown | Team_Unknown | 201–202 | 2 | 1 | Undefined position; Undefined team |
| `20` | `23` | Position_Unknown | Team_Unknown | 206–506 | 294 | 3 | Undefined position; Undefined team |
| `21` | `25` | Position_Unknown | Team_Unknown | 210–509 | 287 | 7 | Undefined position; Undefined team |
| `22` | `30` | Position_Unknown | Team_Unknown | 220–232 | 13 | 1 | Undefined position; Undefined team |
| `23` | `32` | Position_Unknown | Team_Unknown | 222–509 | 284 | 3 | Undefined position; Undefined team |
| `24` | `33` | Position_Unknown | Team_Unknown | 230–322 | 76 | 2 | Undefined position; Undefined team |
| `25` | `35` | Position_Unknown | Team_Unknown | 249–250 | 2 | 1 | Undefined position; Undefined team |
| `26` | `36` | Position_Unknown | Team_Unknown | 257–301 | 45 | 1 | Undefined position; Undefined team |
| `27` | `37` | Position_Unknown | Team_Unknown | 257–451 | 189 | 2 | Undefined position; Undefined team |
| `28` | `38` | Position_Unknown | Team_Unknown | 276–334 | 59 | 1 | Undefined position; Undefined team |
| `29` | `39` | Position_Unknown | Team_Unknown | 281–487 | 207 | 1 | Undefined position; Undefined team |
| `30` | `40` | Position_Unknown | Team_Unknown | 301–345 | 36 | 3 | Undefined position; Undefined team |
| `31` | `42` | Position_Unknown | Team_Unknown | 333–509 | 169 | 4 | Undefined position; Undefined team |
| `32` | `46` | Position_Unknown | Team_Unknown | 351–489 | 138 | 2 | Undefined position; Undefined team |
| `33` | `50` | Position_Unknown | Team_Unknown | 400–402 | 3 | 1 | Undefined position; Undefined team |
| `34` | `51` | Position_Unknown | Team_Unknown | 401–509 | 106 | 2 | Undefined position; Undefined team |
| `35` | `53` | Position_Unknown | Team_Unknown | 403–509 | 106 | 2 | Undefined position; Undefined team |
| `36` | `57` | Position_Unknown | Team_Unknown | 441–442 | 2 | 1 | Undefined position; Undefined team |
| `37` | `58` | Position_Unknown | Team_Unknown | 456–470 | 12 | 2 | Undefined position; Undefined team |
| `38` | `60` | Position_Unknown | Team_Unknown | 461–509 | 49 | 1 | Undefined position; Undefined team |
| `39` | `62` | Position_Unknown | Team_Unknown | 469–473 | 5 | 1 | Undefined position; Undefined team |
| `40` | `63` | Position_Unknown | Team_Unknown | 481–487 | 7 | 1 | Undefined position; Undefined team |
| `41` | `68` | Position_Unknown | Team_Unknown | 498–504 | 6 | 2 | Undefined position; Undefined team |
| `42` | `69` | Position_Unknown | Team_Unknown | 499–509 | 11 | 1 | Undefined position; Undefined team |
| `43` | `70` | Position_Unknown | Team_Unknown | 500–509 | 8 | 2 | Undefined position; Undefined team |
| `44` | `71` | Position_Unknown | Team_Unknown | 502–509 | 6 | 2 | Undefined position; Undefined team |
| `45` | `72` | Position_Unknown | Team_Unknown | 504–509 | 6 | 1 | Undefined position; Undefined team |
| `46` | `73` | Position_Unknown | Team_Unknown | 505–509 | 5 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `12` (4 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `6` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `7` (3 segments found)
- ⚠️ Ambiguous match for action `Action_PressEdge` and target `19` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `1` (actor_track_id `1`): `SAF` position mapped to `defense` team
- ⚠️ Player track XML ID `2` (actor_track_id `2`): `SAF` position mapped to `defense` team
- ⚠️ 34 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 34 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 68 |
| Missing visible bounding boxes during action | 113 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 509 as fallback play end.
- ⚠️ Action 'Action_PreSnap' range [19-315] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [19-61] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [64-84] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [89-101] for track '1' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [121-160] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [170-292] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [294-295] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [299-365] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [382-419] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [19-68] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [19-165] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [170-233] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [238-240] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [19-84] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [88-159] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [162-191] for track '4' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [195-248] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [217-255] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [171-190] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [202-205] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [258-272] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [307-350] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [19-132] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [171-194] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [199-200] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [204-205] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [19-31] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [34-136] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [138-139] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [172-246] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [249-259] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [267-284] for track '8' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [286-335] for track '8' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [351-366] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [369-509] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [19-85] for track '9' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [87-210] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [235-242] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [217-250] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [19-25] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [29-30] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [34-57] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [59-61] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [63-109] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [123-135] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [173-204] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [208-328] for track '11' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [171-177] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [180-193] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [196-198] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [200-208] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [210-244] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [19-32] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [34-83] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [93-98] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [100-107] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [119-122] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [35-54] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [63-175] for track '15' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [101-107] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [118-120] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [125-163] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [166-355] for track '16' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [177-180] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PressEdge' range [190-191] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [216-234] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [320-323] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [327-328] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [330-350] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [200-294] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [201-202] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [206-217] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [222-223] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [227-506] for track '20' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [210-223] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [225-241] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [243-246] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [253-391] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [393-403] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [407-507] for track '21' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [220-232] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [222-344] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [348-357] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [230-275] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [293-322] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [249-250] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [257-301] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [257-258] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [265-451] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [276-334] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [281-487] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [301-313] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [315-317] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [326-345] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [333-396] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [400-407] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [412-504] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [351-486] for track '32' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [488-489] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [400-402] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [401-441] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [403-449] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [441-442] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [456-463] for track '37' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [467-470] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [469-473] for track '39' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [481-487] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [498-499] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [501-504] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [499-509] for track '42' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [500-505] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [508-509] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [502-506] for track '44' has 1 frames without a visible bounding box.
- ⚠️ Player track '3' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '3' has undefined team_side. Will map to Team_Unknown.
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
- ⚠️ Player track '43' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '43' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '44' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '44' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '45' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '45' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '46' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '46' has undefined team_side. Will map to Team_Unknown.

</details>