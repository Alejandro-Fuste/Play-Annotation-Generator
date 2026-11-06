# Play-Annotation-Generator Annotation Review — OutsideZoneRead_75

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `OutsideZoneRead_75`
- **Frame Range:** 0 to 299 (300 total frames)
- **Play:** `Play_Run_OutsideZoneRead`
- **Result:** `Result_Tackle`
- **Result Frame:** 299
- **Player Tracks:** 38
- **Ball Tracks:** 1
- **Action Segments:** 81
- **Validation Warnings:** 97
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 17
- **Exact Matches:** 7
- **Group Expanded Events:** 8
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 1
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 63
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `9` | `Group` |
| ✅ EXACT | `Action_ZoneBlock` | RT | offense | `2` | `2` |
| ✅ EXACT | `Action_ZoneBlock` | LG | offense | `5` | `5` |
| ✅ EXACT | `Action_ZoneBlock` | C | offense | `6` | `6` |
| ✅ EXACT | `Action_ZoneBlock` | RG | offense | `7` | `7` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | offense | `9` | `9` |
| ✅ EXACT | `Action_PressEdge` | RT | offense | `2` | `2` |
| ✅ EXACT | `Action_ReadEdgeDefender` | LT | offense | `9` | `9` |
| ✅ EXACT | `Action_Handoff` | LT | offense | `9` | `9` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `11` | `Group` | 2 | START | 2 | 299 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `2` | `Group` | 2 | START | 2 | 52 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `3` | `Group` | 2 | START | 2 | 221 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `4` | `Group` | 2 | START | 2 | 112 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `5` | `Group` | 2 | START | 2 | 52 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `6` | `Group` | 2 | START | 2 | 52 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `7` | `Group` | 2 | START | 2 | 52 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `9` | `Group` | 2 | START | 2 | 52 |
| ✅ EXACT | `Action_ZoneBlock` | RT | `2` | `2` | 53 | START | 53 | 60 |
| ✅ EXACT | `Action_ZoneBlock` | LG | `5` | `5` | 53 | START | 53 | 91 |
| ✅ EXACT | `Action_ZoneBlock` | C | `6` | `6` | 53 | START | 53 | 91 |
| ✅ EXACT | `Action_ZoneBlock` | RG | `7` | `7` | 53 | START | 53 | 91 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | `9` | `9` | 53 | START | 53 | 60 |
| ✅ EXACT | `Action_PressEdge` | RT | `2` | `2` | 61 | START | 61 | 114 |
| ✅ EXACT | `Action_ReadEdgeDefender` | LT | `9` | `9` | 61 | START | 61 | 69 |
| ✅ EXACT | `Action_Handoff` | LT | `9` | `9` | 70 | START | 70 | 78 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 2–299
- **Visible Samples:** 298

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 2 | 299 | 298 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 2–270
- **Visible Samples:** 264

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 2 | 221 | 220 | inferred_complete_timeline |
| `Action_PreSnap` | 227 | 270 | 44 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 2–130
- **Visible Samples:** 126

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 2 | 112 | 111 | inferred_complete_timeline |
| `Action_PreSnap` | 116 | 130 | 15 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 2–299
- **Visible Samples:** 298

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 2 | 52 | 51 | inferred_complete_timeline |
| `Action_ZoneBlock` | 53 | 60 | 8 | inferred_complete_timeline |
| `Action_ReadEdgeDefender` | 61 | 69 | 9 | inferred_complete_timeline |
| `Action_Handoff` | 70 | 78 | 9 | inferred_complete_timeline |
| `Action_ZoneBlock` | 79 | 91 | 13 | inferred_complete_timeline |
| `Action_None` | 92 | 299 | 208 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 2–299
- **Visible Samples:** 298

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 2 | 52 | 51 | inferred_complete_timeline |
| `Action_ZoneBlock` | 53 | 91 | 39 | inferred_complete_timeline |
| `Action_None` | 92 | 299 | 208 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 2–299
- **Visible Samples:** 298

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 2 | 52 | 51 | inferred_complete_timeline |
| `Action_ZoneBlock` | 53 | 91 | 39 | inferred_complete_timeline |
| `Action_None` | 92 | 299 | 208 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 2–299
- **Visible Samples:** 298

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 2 | 52 | 51 | inferred_complete_timeline |
| `Action_ZoneBlock` | 53 | 91 | 39 | inferred_complete_timeline |
| `Action_None` | 92 | 299 | 208 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 2–299
- **Visible Samples:** 298

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 2 | 52 | 51 | inferred_complete_timeline |
| `Action_ZoneBlock` | 53 | 60 | 8 | inferred_complete_timeline |
| `Action_PressEdge` | 61 | 114 | 54 | inferred_complete_timeline |
| `Action_None` | 115 | 299 | 185 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 2–162
- **Visible Samples:** 150

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 2 | 146 | 145 | inferred_complete_timeline |
| `Action_PreSnap` | 158 | 162 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 2–299
- **Visible Samples:** 298

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 2 | 299 | 298 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 2–43
- **Visible Samples:** 39

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 2 | 37 | 36 | inferred_complete_timeline |
| `Action_PreSnap` | 41 | 43 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 2–289
- **Visible Samples:** 283

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 2 | 236 | 235 | inferred_complete_timeline |
| `Action_PreSnap` | 241 | 259 | 19 | inferred_complete_timeline |
| `Action_PreSnap` | 261 | 289 | 29 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 2–299
- **Visible Samples:** 287

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 2 | 131 | 130 | inferred_complete_timeline |
| `Action_PreSnap` | 143 | 299 | 157 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `defense`
- **Visible Frames:** 2–74
- **Visible Samples:** 68

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 2 | 67 | 66 | inferred_complete_timeline |
| `Action_PreSnap` | 73 | 74 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 2–10
- **Visible Samples:** 9

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 2 | 10 | 9 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `15` | `15` | Position_Unknown | Team_Unknown | 6–45 | 40 | 1 | Undefined position; Undefined team |
| `16` | `17` | Position_Unknown | Team_Unknown | 11–126 | 90 | 4 | Undefined position; Undefined team |
| `18` | `19` | Position_Unknown | Team_Unknown | 62–181 | 114 | 2 | Undefined position; Undefined team |
| `19` | `20` | Position_Unknown | Team_Unknown | 65–299 | 235 | 1 | Undefined position; Undefined team |
| `20` | `21` | Position_Unknown | Team_Unknown | 84–299 | 216 | 1 | Undefined position; Undefined team |
| `21` | `22` | Position_Unknown | Team_Unknown | 89–299 | 202 | 5 | Undefined position; Undefined team |
| `22` | `23` | Position_Unknown | Team_Unknown | 94–156 | 63 | 1 | Undefined position; Undefined team |
| `23` | `24` | Position_Unknown | Team_Unknown | 94–299 | 201 | 3 | Undefined position; Undefined team |
| `24` | `25` | Position_Unknown | Team_Unknown | 103–299 | 195 | 3 | Undefined position; Undefined team |
| `25` | `26` | Position_Unknown | Team_Unknown | 118–299 | 182 | 1 | Undefined position; Undefined team |
| `26` | `28` | Position_Unknown | Team_Unknown | 123–299 | 156 | 3 | Undefined position; Undefined team |
| `27` | `29` | Position_Unknown | Team_Unknown | 129–299 | 171 | 1 | Undefined position; Undefined team |
| `28` | `30` | Position_Unknown | Team_Unknown | 133–299 | 161 | 3 | Undefined position; Undefined team |
| `29` | `33` | Position_Unknown | Team_Unknown | 154–299 | 146 | 1 | Undefined position; Undefined team |
| `30` | `36` | Position_Unknown | Team_Unknown | 180–299 | 119 | 2 | Undefined position; Undefined team |
| `31` | `38` | Position_Unknown | Team_Unknown | 184–187 | 4 | 1 | Undefined position; Undefined team |
| `32` | `39` | Position_Unknown | Team_Unknown | 193–245 | 23 | 4 | Undefined position; Undefined team |
| `33` | `40` | Position_Unknown | Team_Unknown | 212–299 | 88 | 1 | Undefined position; Undefined team |
| `34` | `41` | Position_Unknown | Team_Unknown | 219–229 | 11 | 1 | Undefined position; Undefined team |
| `35` | `42` | Position_Unknown | Team_Unknown | 254–255 | 2 | 1 | Undefined position; Undefined team |
| `36` | `43` | Position_Unknown | Team_Unknown | 257–258 | 2 | 1 | Undefined position; Undefined team |
| `37` | `48` | Position_Unknown | Team_Unknown | 276–299 | 23 | 2 | Undefined position; Undefined team |
| `38` | `50` | Position_Unknown | Team_Unknown | 283–286 | 4 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

| xml_track_id | actor_track_id | First Visible Frame | Last Visible Frame | Visible Samples | Coverage | Missing Frame Ranges |
| --- | --- | --- | --- | --- | --- | --- |
| `17` | `18` | 54 | 55 | 2 | 100.0% | None |

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `9` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `12` (actor_track_id `12`): `SAF` position mapped to `defense` team
- ⚠️ 23 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 23 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 46 |
| Missing visible bounding boxes during action | 50 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 299 as fallback play end.
- ⚠️ Action 'Action_PreSnap' range [2-67] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [73-74] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [2-131] for track '1' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [2-221] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [227-270] for track '3' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [2-112] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [116-130] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [2-146] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [158-162] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [2-10] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [2-236] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [241-259] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [261-289] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [2-37] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [41-43] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [6-45] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [11-94] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [105-106] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [117-118] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [125-126] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [62-128] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [135-181] for track '18' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [89-232] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [234-255] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [257-260] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [262-264] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [94-156] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [94-100] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [105-113] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [115-299] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [103-231] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [233-275] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [123-242] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [260-271] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [133-169] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [171-227] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [233-299] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [154-299] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [180-189] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [191-299] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [184-187] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [193-202] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [231-232] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [234-235] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [237-245] for track '32' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [219-229] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [254-255] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [257-258] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [276-278] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [283-286] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Player track '15' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '15' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '16' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '16' has undefined team_side. Will map to Team_Unknown.
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

</details>