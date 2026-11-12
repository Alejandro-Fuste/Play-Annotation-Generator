# Play-Annotation-Generator Annotation Review — SplitZone_28

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `SplitZone_28`
- **Frame Range:** 0 to 509 (510 total frames)
- **Play:** `Play_Run_SplitZone`
- **Result:** `Result_Touchdown`
- **Result Frame:** 509
- **Player Tracks:** 35
- **Ball Tracks:** 0
- **Action Segments:** 82
- **Validation Warnings:** 96
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 19
- **Exact Matches:** 6
- **Group Expanded Events:** 8
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 1
- **Missing Segments:** 0
- **Ambiguous Matches:** 2
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 65
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `8` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `9` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `10` | `10` |
| ⚠️ START CHANGED | `Action_ZoneBlock` | C | offense | `10` | `10` |
| ✅ EXACT | `Action_ZoneBlock` | RG | offense | `11` | `11` |
| ✅ EXACT | `Action_ZoneBlock` | LT | offense | `5` | `5` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | offense | `7` | `7` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | offense | `9` | `9` |
| ✅ EXACT | `Action_SplitBlock` | TE | offense | `3` | `3` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `6` | `6` |
| ✅ EXACT | `Action_BallCarry` | QB | offense | `6` | `6` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `10` | `Group` | 0 | START | 0 | 188 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `11` | `Group` | 0 | START | 0 | 191 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `3` | `Group` | 0 | START | 0 | 193 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `5` | `Group` | 0 | START | 0 | 191 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `6` | `Group` | 0 | START | 0 | 188 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `7` | `Group` | 0 | START | 0 | 191 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `8` | `Group` | 0 | START | 0 | 188 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `9` | `Group` | 0 | START | 0 | 191 |
| ✅ EXACT | `Action_BallSnap` | C | `10` | `10` | 189 | START | 189 | 204 |
| ⚠️ START CHANGED | `Action_ZoneBlock` | C | `10` | `10` | 192 | START | 205 | 279 |
| ✅ EXACT | `Action_ZoneBlock` | RG | `11` | `11` | 192 | START | 192 | 279 |
| ✅ EXACT | `Action_ZoneBlock` | LT | `5` | `5` | 192 | START | 192 | 277 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | `7` | `7` | 192 | START | 192 | 210 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | `9` | `9` | 192 | START | 192 | 231 |
| ✅ EXACT | `Action_SplitBlock` | TE | `3` | `3` | 194 | START | 194 | 279 |
| ✅ EXACT | `Action_SnapReceive` | QB | `6` | `6` | 204 | END | 189 | 204 |
| ✅ EXACT | `Action_BallCarry` | QB | `6` | `6` | 237 | START | 237 | 287 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 279 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–287
- **Visible Samples:** 288

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 188 | 189 | inferred_complete_timeline |
| `Action_SnapReceive` | 189 | 204 | 16 | inferred_complete_timeline |
| `Action_None` | 205 | 236 | 32 | inferred_complete_timeline |
| `Action_BallCarry` | 237 | 287 | 51 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–509
- **Visible Samples:** 510

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 188 | 189 | inferred_complete_timeline |
| `Action_None` | 189 | 509 | 321 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–367
- **Visible Samples:** 368

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 193 | 194 | inferred_complete_timeline |
| `Action_SplitBlock` | 194 | 279 | 86 | inferred_complete_timeline |
| `Action_None` | 280 | 367 | 88 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–277
- **Visible Samples:** 278

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 191 | 192 | inferred_complete_timeline |
| `Action_ZoneBlock` | 192 | 277 | 86 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–288
- **Visible Samples:** 275

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 191 | 192 | inferred_complete_timeline |
| `Action_ZoneBlock` | 192 | 231 | 40 | inferred_complete_timeline |
| `Action_ZoneBlock` | 238 | 242 | 5 | inferred_complete_timeline |
| `Action_ZoneBlock` | 245 | 253 | 9 | inferred_complete_timeline |
| `Action_ZoneBlock` | 260 | 279 | 20 | inferred_complete_timeline |
| `Action_None` | 280 | 288 | 9 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–293
- **Visible Samples:** 293

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 188 | 189 | inferred_complete_timeline |
| `Action_BallSnap` | 189 | 204 | 16 | inferred_complete_timeline |
| `Action_ZoneBlock` | 205 | 279 | 75 | inferred_complete_timeline |
| `Action_None` | 280 | 289 | 10 | inferred_complete_timeline |
| `Action_None` | 291 | 293 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–301
- **Visible Samples:** 302

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 191 | 192 | inferred_complete_timeline |
| `Action_ZoneBlock` | 192 | 279 | 88 | inferred_complete_timeline |
| `Action_None` | 280 | 301 | 22 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–242
- **Visible Samples:** 229

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 191 | 192 | inferred_complete_timeline |
| `Action_ZoneBlock` | 192 | 210 | 19 | inferred_complete_timeline |
| `Action_ZoneBlock` | 224 | 232 | 9 | inferred_complete_timeline |
| `Action_ZoneBlock` | 234 | 242 | 9 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–273
- **Visible Samples:** 274

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 188 | 189 | inferred_complete_timeline |
| `Action_None` | 189 | 273 | 85 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–470
- **Visible Samples:** 454

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 188 | 189 | inferred_complete_timeline |
| `Action_None` | 189 | 446 | 258 | inferred_complete_timeline |
| `Action_None` | 448 | 450 | 3 | inferred_complete_timeline |
| `Action_None` | 467 | 470 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–291
- **Visible Samples:** 289

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 188 | 189 | inferred_complete_timeline |
| `Action_None` | 189 | 248 | 60 | inferred_complete_timeline |
| `Action_None` | 252 | 291 | 40 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–295
- **Visible Samples:** 290

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 188 | 189 | inferred_complete_timeline |
| `Action_None` | 189 | 236 | 48 | inferred_complete_timeline |
| `Action_None` | 243 | 295 | 53 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `defense`
- **Visible Frames:** 0–509
- **Visible Samples:** 510

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 188 | 189 | inferred_complete_timeline |
| `Action_None` | 189 | 509 | 321 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–509
- **Visible Samples:** 510

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 188 | 189 | inferred_complete_timeline |
| `Action_None` | 189 | 509 | 321 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–280
- **Visible Samples:** 281

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 188 | 189 | inferred_complete_timeline |
| `Action_None` | 189 | 280 | 92 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `15` | `18` | Position_Unknown | Team_Unknown | 237–266 | 30 | 1 | Undefined position; Undefined team |
| `16` | `21` | Position_Unknown | Team_Unknown | 243–425 | 178 | 3 | Undefined position; Undefined team |
| `17` | `23` | Position_Unknown | Team_Unknown | 302–306 | 5 | 1 | Undefined position; Undefined team |
| `18` | `25` | Position_Unknown | Team_Unknown | 304–394 | 91 | 1 | Undefined position; Undefined team |
| `19` | `27` | Position_Unknown | Team_Unknown | 324–330 | 7 | 1 | Undefined position; Undefined team |
| `20` | `30` | Position_Unknown | Team_Unknown | 368–373 | 6 | 1 | Undefined position; Undefined team |
| `21` | `32` | Position_Unknown | Team_Unknown | 375–509 | 135 | 1 | Undefined position; Undefined team |
| `22` | `35` | Position_Unknown | Team_Unknown | 406–456 | 44 | 5 | Undefined position; Undefined team |
| `23` | `37` | Position_Unknown | Team_Unknown | 411–509 | 99 | 1 | Undefined position; Undefined team |
| `24` | `39` | Position_Unknown | Team_Unknown | 440–508 | 43 | 4 | Undefined position; Undefined team |
| `25` | `40` | Position_Unknown | Team_Unknown | 442–443 | 2 | 1 | Undefined position; Undefined team |
| `26` | `43` | Position_Unknown | Team_Unknown | 445–446 | 2 | 1 | Undefined position; Undefined team |
| `27` | `44` | Position_Unknown | Team_Unknown | 447–509 | 63 | 1 | Undefined position; Undefined team |
| `28` | `45` | Position_Unknown | Team_Unknown | 447–507 | 25 | 6 | Undefined position; Undefined team |
| `29` | `46` | Position_Unknown | Team_Unknown | 453–454 | 2 | 1 | Undefined position; Undefined team |
| `30` | `47` | Position_Unknown | Team_Unknown | 455–509 | 55 | 1 | Undefined position; Undefined team |
| `31` | `50` | Position_Unknown | Team_Unknown | 486–509 | 21 | 2 | Undefined position; Undefined team |
| `32` | `51` | Position_Unknown | Team_Unknown | 495–505 | 11 | 1 | Undefined position; Undefined team |
| `33` | `52` | Position_Unknown | Team_Unknown | 498–509 | 12 | 1 | Undefined position; Undefined team |
| `34` | `53` | Position_Unknown | Team_Unknown | 500–503 | 4 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ `Action_ZoneBlock` for actor_track_id `10` (C): Annotated start 192 != Inferred start 205
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `7` (3 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `9` (4 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `4` (actor_track_id `4`): `SAF` position mapped to `defense` team
- ⚠️ 20 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 20 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 40 |
| Missing visible bounding boxes during action | 54 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 509 as fallback play end.
- ⚠️ Resolved action overlap for track '10' (C): higher_priority='Action_BallSnap' [189–204], lower_priority='Action_ZoneBlock' annotated_start=192, effective_Action_ZoneBlock_start=205.
- ⚠️ Action 'Action_None' range [189-273] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [280-367] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [189-280] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [192-277] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [237-287] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [192-210] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [224-232] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [234-242] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [192-231] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [238-242] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [245-253] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [260-279] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [280-288] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [280-289] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [291-293] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [192-279] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [280-301] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [189-248] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [252-291] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [189-446] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [448-450] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [467-470] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [189-236] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [243-295] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [237-266] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [243-244] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [249-417] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [419-425] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [302-306] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [304-394] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [324-330] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [368-373] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [406-416] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [421-423] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [425-427] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [429-439] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [441-456] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [440-441] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [444-462] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [485-491] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [494-508] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [442-443] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [445-446] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [447-450] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [456-460] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [478-480] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [485-487] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [495-497] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [501-507] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [453-454] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [486-497] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [501-509] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [495-505] for track '32' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [500-503] for track '34' has 1 frames without a visible bounding box.
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

</details>