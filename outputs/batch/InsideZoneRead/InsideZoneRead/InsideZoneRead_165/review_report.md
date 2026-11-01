# Play-Annotation-Generator Annotation Review — InsideZoneRead_165

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `InsideZoneRead_165`
- **Frame Range:** 0 to 449 (450 total frames)
- **Play:** `Play_Run_InsideZoneRead`
- **Result:** `Result_Tackle`
- **Result Frame:** 449
- **Player Tracks:** 44
- **Ball Tracks:** 0
- **Action Segments:** 117
- **Validation Warnings:** 152
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 19
- **Exact Matches:** 7
- **Group Expanded Events:** 7
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 3
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 96
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `9` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `12` | `11` |
| ✅ EXACT | `Action_ZoneBlock` | LG | offense | `10` | `9` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | offense | `12` | `11` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | offense | `3` | `2` |
| ✅ EXACT | `Action_ZoneBlock` | RT | offense | `4` | `3` |
| ✅ EXACT | `Action_ZoneBlock` | RG | offense | `6` | `5` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `9` | `8` |
| ✅ EXACT | `Action_ReadDefender` | QB | offense | `9` | `8` |
| ✅ EXACT | `Action_Handoff` | QB | offense | `9` | `8` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | offense | `5` | `4` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `10` | `Group` | 0 | START | 0 | 122 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `12` | `Group` | 0 | START | 0 | 33 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `3` | `Group` | 0 | START | 0 | 122 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `4` | `Group` | 0 | START | 0 | 122 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `5` | `Group` | 0 | START | 0 | 164 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `6` | `Group` | 0 | START | 0 | 122 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `9` | `Group` | 0 | START | 0 | 120 |
| ✅ EXACT | `Action_BallSnap` | C | `12` | `11` | 121 | START | 121 | 129 |
| ✅ EXACT | `Action_ZoneBlock` | LG | `10` | `9` | 123 | START | 123 | 216 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | `12` | `11` | 123 | START | 130 | 213 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | `3` | `2` | 123 | START | 123 | 226 |
| ✅ EXACT | `Action_ZoneBlock` | RT | `4` | `3` | 123 | START | 123 | 163 |
| ✅ EXACT | `Action_ZoneBlock` | RG | `6` | `5` | 123 | START | 123 | 226 |
| ✅ EXACT | `Action_SnapReceive` | QB | `9` | `8` | 129 | END | 121 | 129 |
| ✅ EXACT | `Action_ReadDefender` | QB | `9` | `8` | 135 | START | 135 | 151 |
| ✅ EXACT | `Action_Handoff` | QB | `9` | `8` | 152 | START | 152 | 166 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | `5` | `4` | 167 | START | 193 | 316 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 226 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–262
- **Visible Samples:** 263

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 120 | 121 | inferred_complete_timeline |
| `Action_SnapReceive` | 121 | 129 | 9 | inferred_complete_timeline |
| `Action_None` | 130 | 134 | 5 | inferred_complete_timeline |
| `Action_ReadDefender` | 135 | 151 | 17 | inferred_complete_timeline |
| `Action_Handoff` | 152 | 166 | 15 | inferred_complete_timeline |
| `Action_None` | 167 | 262 | 96 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–449
- **Visible Samples:** 419

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 164 | 165 | inferred_complete_timeline |
| `Action_BallCarry` | 193 | 316 | 124 | inferred_complete_timeline |
| `Action_BallCarry` | 320 | 449 | 130 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–251
- **Visible Samples:** 252

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 122 | 123 | inferred_complete_timeline |
| `Action_ZoneBlock` | 123 | 226 | 104 | inferred_complete_timeline |
| `Action_None` | 227 | 251 | 25 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–216
- **Visible Samples:** 217

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 122 | 123 | inferred_complete_timeline |
| `Action_ZoneBlock` | 123 | 216 | 94 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–262
- **Visible Samples:** 253

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 33 | 34 | inferred_complete_timeline |
| `Action_PreSnap` | 43 | 120 | 78 | inferred_complete_timeline |
| `Action_BallSnap` | 121 | 129 | 9 | inferred_complete_timeline |
| `Action_ZoneBlock` | 130 | 213 | 84 | inferred_complete_timeline |
| `Action_ZoneBlock` | 215 | 226 | 12 | inferred_complete_timeline |
| `Action_None` | 227 | 262 | 36 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–278
- **Visible Samples:** 279

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 122 | 123 | inferred_complete_timeline |
| `Action_ZoneBlock` | 123 | 226 | 104 | inferred_complete_timeline |
| `Action_None` | 227 | 278 | 52 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–163
- **Visible Samples:** 164

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 122 | 123 | inferred_complete_timeline |
| `Action_ZoneBlock` | 123 | 163 | 41 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–184
- **Visible Samples:** 185

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 120 | 121 | inferred_complete_timeline |
| `Action_None` | 121 | 184 | 64 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–281
- **Visible Samples:** 268

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 120 | 121 | inferred_complete_timeline |
| `Action_None` | 121 | 149 | 29 | inferred_complete_timeline |
| `Action_None` | 164 | 281 | 118 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–146
- **Visible Samples:** 136

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 62 | 63 | inferred_complete_timeline |
| `Action_PreSnap` | 69 | 120 | 52 | inferred_complete_timeline |
| `Action_None` | 121 | 122 | 2 | inferred_complete_timeline |
| `Action_None` | 124 | 132 | 9 | inferred_complete_timeline |
| `Action_None` | 137 | 146 | 10 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–271
- **Visible Samples:** 272

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 120 | 121 | inferred_complete_timeline |
| `Action_None` | 121 | 271 | 151 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–274
- **Visible Samples:** 234

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 120 | 121 | inferred_complete_timeline |
| `Action_None` | 121 | 153 | 33 | inferred_complete_timeline |
| `Action_None` | 155 | 172 | 18 | inferred_complete_timeline |
| `Action_None` | 176 | 177 | 2 | inferred_complete_timeline |
| `Action_None` | 215 | 274 | 60 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–449
- **Visible Samples:** 357

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 120 | 121 | inferred_complete_timeline |
| `Action_None` | 121 | 172 | 52 | inferred_complete_timeline |
| `Action_None` | 195 | 342 | 148 | inferred_complete_timeline |
| `Action_None` | 410 | 418 | 9 | inferred_complete_timeline |
| `Action_None` | 420 | 427 | 8 | inferred_complete_timeline |
| `Action_None` | 431 | 449 | 19 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–449
- **Visible Samples:** 449

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 120 | 121 | inferred_complete_timeline |
| `Action_None` | 121 | 403 | 283 | inferred_complete_timeline |
| `Action_None` | 405 | 449 | 45 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `14` | `16` | Position_Unknown | Team_Unknown | 165–190 | 26 | 1 | Undefined position; Undefined team |
| `15` | `17` | Position_Unknown | Team_Unknown | 170–381 | 203 | 2 | Undefined position; Undefined team |
| `16` | `18` | Position_Unknown | Team_Unknown | 171–336 | 165 | 2 | Undefined position; Undefined team |
| `17` | `19` | Position_Unknown | Team_Unknown | 184–449 | 253 | 5 | Undefined position; Undefined team |
| `18` | `22` | Position_Unknown | Team_Unknown | 198–230 | 9 | 3 | Undefined position; Undefined team |
| `19` | `25` | Position_Unknown | Team_Unknown | 207–339 | 133 | 1 | Undefined position; Undefined team |
| `20` | `27` | Position_Unknown | Team_Unknown | 218–449 | 229 | 2 | Undefined position; Undefined team |
| `21` | `28` | Position_Unknown | Team_Unknown | 220–431 | 180 | 4 | Undefined position; Undefined team |
| `22` | `30` | Position_Unknown | Team_Unknown | 235–396 | 106 | 4 | Undefined position; Undefined team |
| `23` | `31` | Position_Unknown | Team_Unknown | 257–434 | 177 | 2 | Undefined position; Undefined team |
| `24` | `32` | Position_Unknown | Team_Unknown | 257–258 | 2 | 1 | Undefined position; Undefined team |
| `25` | `33` | Position_Unknown | Team_Unknown | 261–281 | 14 | 5 | Undefined position; Undefined team |
| `26` | `34` | Position_Unknown | Team_Unknown | 264–449 | 153 | 6 | Undefined position; Undefined team |
| `27` | `36` | Position_Unknown | Team_Unknown | 289–336 | 48 | 1 | Undefined position; Undefined team |
| `28` | `37` | Position_Unknown | Team_Unknown | 296–312 | 9 | 2 | Undefined position; Undefined team |
| `29` | `39` | Position_Unknown | Team_Unknown | 340–342 | 3 | 1 | Undefined position; Undefined team |
| `30` | `40` | Position_Unknown | Team_Unknown | 349–431 | 76 | 3 | Undefined position; Undefined team |
| `31` | `41` | Position_Unknown | Team_Unknown | 375–449 | 69 | 2 | Undefined position; Undefined team |
| `32` | `42` | Position_Unknown | Team_Unknown | 382–443 | 59 | 2 | Undefined position; Undefined team |
| `33` | `43` | Position_Unknown | Team_Unknown | 388–449 | 62 | 1 | Undefined position; Undefined team |
| `34` | `44` | Position_Unknown | Team_Unknown | 395–449 | 39 | 2 | Undefined position; Undefined team |
| `35` | `45` | Position_Unknown | Team_Unknown | 396–400 | 5 | 1 | Undefined position; Undefined team |
| `36` | `47` | Position_Unknown | Team_Unknown | 411–423 | 13 | 1 | Undefined position; Undefined team |
| `37` | `48` | Position_Unknown | Team_Unknown | 411–446 | 33 | 3 | Undefined position; Undefined team |
| `38` | `50` | Position_Unknown | Team_Unknown | 412–418 | 7 | 1 | Undefined position; Undefined team |
| `39` | `53` | Position_Unknown | Team_Unknown | 424–449 | 19 | 2 | Undefined position; Undefined team |
| `40` | `54` | Position_Unknown | Team_Unknown | 426–448 | 16 | 2 | Undefined position; Undefined team |
| `41` | `56` | Position_Unknown | Team_Unknown | 434–449 | 16 | 1 | Undefined position; Undefined team |
| `42` | `58` | Position_Unknown | Team_Unknown | 437–449 | 10 | 2 | Undefined position; Undefined team |
| `43` | `59` | Position_Unknown | Team_Unknown | 447–449 | 3 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `12` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `3` (2 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `5` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `0` (actor_track_id `1`): `SAF` position mapped to `defense` team
- ⚠️ 30 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 30 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 60 |
| Missing visible bounding boxes during action | 86 |
| Track-related warning | 5 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 449 as fallback play end.
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '2' (LT) duration 104 frames exceeds threshold 90 frames [start=123, end=226].
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '5' (RG) duration 104 frames exceeds threshold 90 frames [start=123, end=226].
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '9' (LG) duration 94 frames exceeds threshold 90 frames [start=123, end=216].
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '11' (C) duration 104 frames exceeds threshold 90 frames [start=123, end=226].
- ⚠️ Resolved action overlap for track '11' (C): higher_priority='Action_BallSnap' [121–129], lower_priority='Action_ZoneBlock' annotated_start=123, effective_Action_ZoneBlock_start=130.
- ⚠️ Action 'Action_None' range [121-403] for track '0' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [121-172] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [195-342] for track '1' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [410-418] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [420-427] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [227-251] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [123-163] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-164] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [193-316] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [227-278] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [121-149] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [164-281] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [121-184] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [167-262] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [123-216] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [121-271] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-33] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [130-213] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [227-262] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [121-153] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [155-172] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [176-177] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [215-274] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-62] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [69-120] for track '13' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [121-122] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [124-132] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [137-146] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [165-190] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [170-216] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [226-381] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [171-333] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [335-336] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [184-199] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [201-282] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [290-291] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [295-320] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [198-199] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [219-222] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [228-230] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [207-339] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [218-248] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [252-449] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [220-374] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [376-393] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [405-409] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [430-431] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [235-301] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [305-313] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [338-365] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [395-396] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [257-328] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [330-434] for track '23' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [257-258] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [261-263] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [267-268] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [270-273] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [276-277] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [279-281] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [264-314] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [316-343] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [350-352] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [361-386] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [395-419] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [289-336] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [296-300] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [309-312] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [340-342] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [349-419] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [426-428] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [430-431] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [375-378] for track '31' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [385-449] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [382-401] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [405-443] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [395-405] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [396-400] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [411-423] for track '36' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [411-416] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [418-419] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [422-446] for track '37' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [412-418] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [424-436] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [426-438] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [446-448] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [437-441] for track '42' has 1 frames without a visible bounding box.
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

</details>