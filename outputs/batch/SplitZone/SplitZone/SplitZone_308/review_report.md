# Play-Annotation-Generator Annotation Review — SplitZone_308

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `SplitZone_308`
- **Frame Range:** 0 to 359 (360 total frames)
- **Play:** `Play_Run_SplitZone`
- **Result:** `Result_Tackle`
- **Result Frame:** 359
- **Player Tracks:** 29
- **Ball Tracks:** 0
- **Action Segments:** 83
- **Validation Warnings:** 64
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 22
- **Exact Matches:** 10
- **Group Expanded Events:** 9
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 2
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 62
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `7` | `Group` |
| ✅ EXACT | `Action_BallSnap` | QB | offense | `11` | `11` |
| ✅ EXACT | `Action_SplitBlock` | LT | offense | `2` | `2` |
| ✅ EXACT | `Action_ZoneBlock` | RG | offense | `12` | `12` |
| ✅ EXACT | `Action_ZoneBlock` | C | offense | `15` | `15` |
| ✅ EXACT | `Action_ZoneBlock` | LT | offense | `2` | `2` |
| ✅ EXACT | `Action_ZoneBlock` | LG | offense | `3` | `3` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | offense | `4` | `4` |
| ✅ EXACT | `Action_SnapReceive` | Position_Unknown | Team_Unknown | `20` | `20` |
| ✅ EXACT | `Action_PressEdge` | Position_Unknown | Team_Unknown | `21` | `21` |
| ✅ EXACT | `Action_ReadEdgeDefender` | Position_Unknown | Team_Unknown | `20` | `20` |
| ✅ EXACT | `Action_Handoff` | Position_Unknown | Team_Unknown | `20` | `20` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | Position_Unknown | Team_Unknown | `21` | `21` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `11` | `Group` | 0 | START | 0 | 96 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `12` | `Group` | 0 | START | 0 | 108 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `15` | `Group` | 0 | START | 0 | 108 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `16` | `Group` | 0 | START | 0 | 96 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR | `17` | `Group` | 0 | START | 0 | 96 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `2` | `Group` | 0 | START | 0 | 107 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `3` | `Group` | 0 | START | 0 | 108 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `4` | `Group` | 0 | START | 0 | 108 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `7` | `Group` | 0 | START | 0 | 96 |
| ✅ EXACT | `Action_BallSnap` | QB | `11` | `11` | 97 | START | 97 | 110 |
| ✅ EXACT | `Action_SplitBlock` | LT | `2` | `2` | 108 | START | 108 | 108 |
| ✅ EXACT | `Action_ZoneBlock` | RG | `12` | `12` | 109 | START | 109 | 163 |
| ✅ EXACT | `Action_ZoneBlock` | C | `15` | `15` | 109 | START | 109 | 163 |
| ✅ EXACT | `Action_ZoneBlock` | LT | `2` | `2` | 109 | START | 109 | 163 |
| ✅ EXACT | `Action_ZoneBlock` | LG | `3` | `3` | 109 | START | 109 | 163 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | `4` | `4` | 109 | START | 109 | 154 |
| ✅ EXACT | `Action_SnapReceive` | Position_Unknown | `20` | `20` | 110 | END | 97 | 110 |
| ✅ EXACT | `Action_PressEdge` | Position_Unknown | `21` | `21` | 113 | START | 113 | 138 |
| ✅ EXACT | `Action_ReadEdgeDefender` | Position_Unknown | `20` | `20` | 113 | START | 113 | 132 |
| ✅ EXACT | `Action_Handoff` | Position_Unknown | `20` | `20` | 133 | START | 133 | 143 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | Position_Unknown | `21` | `21` | 139 | START | 139 | 323 |

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
- **Visible Frames:** 0–118
- **Visible Samples:** 119

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 96 | 97 | inferred_complete_timeline |
| `Action_BallSnap` | 97 | 110 | 14 | inferred_complete_timeline |
| `Action_None` | 111 | 118 | 8 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–359
- **Visible Samples:** 360

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 96 | 97 | inferred_complete_timeline |
| `Action_None` | 97 | 359 | 263 | inferred_complete_timeline |

</details>

<details>
<summary>WR — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–254
- **Visible Samples:** 255

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 96 | 97 | inferred_complete_timeline |
| `Action_None` | 97 | 254 | 158 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–359
- **Visible Samples:** 355

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 96 | 97 | inferred_complete_timeline |
| `Action_None` | 97 | 319 | 223 | inferred_complete_timeline |
| `Action_None` | 321 | 349 | 29 | inferred_complete_timeline |
| `Action_None` | 353 | 354 | 2 | inferred_complete_timeline |
| `Action_None` | 356 | 359 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–359
- **Visible Samples:** 360

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 107 | 108 | inferred_complete_timeline |
| `Action_SplitBlock` | 108 | 108 | 1 | inferred_complete_timeline |
| `Action_ZoneBlock` | 109 | 163 | 55 | inferred_complete_timeline |
| `Action_None` | 164 | 359 | 196 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–305
- **Visible Samples:** 301

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 108 | 109 | inferred_complete_timeline |
| `Action_ZoneBlock` | 109 | 163 | 55 | inferred_complete_timeline |
| `Action_None` | 164 | 240 | 77 | inferred_complete_timeline |
| `Action_None` | 244 | 287 | 44 | inferred_complete_timeline |
| `Action_None` | 290 | 305 | 16 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–359
- **Visible Samples:** 360

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 108 | 109 | inferred_complete_timeline |
| `Action_ZoneBlock` | 109 | 163 | 55 | inferred_complete_timeline |
| `Action_None` | 164 | 359 | 196 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–359
- **Visible Samples:** 360

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 108 | 109 | inferred_complete_timeline |
| `Action_ZoneBlock` | 109 | 163 | 55 | inferred_complete_timeline |
| `Action_None` | 164 | 359 | 196 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–353
- **Visible Samples:** 344

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 108 | 109 | inferred_complete_timeline |
| `Action_ZoneBlock` | 109 | 154 | 46 | inferred_complete_timeline |
| `Action_ZoneBlock` | 156 | 163 | 8 | inferred_complete_timeline |
| `Action_None` | 164 | 325 | 162 | inferred_complete_timeline |
| `Action_None` | 329 | 336 | 8 | inferred_complete_timeline |
| `Action_None` | 340 | 348 | 9 | inferred_complete_timeline |
| `Action_None` | 352 | 353 | 2 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–353
- **Visible Samples:** 354

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 96 | 97 | inferred_complete_timeline |
| `Action_None` | 97 | 353 | 257 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–250
- **Visible Samples:** 244

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 96 | 97 | inferred_complete_timeline |
| `Action_None` | 97 | 180 | 84 | inferred_complete_timeline |
| `Action_None` | 184 | 197 | 14 | inferred_complete_timeline |
| `Action_None` | 202 | 250 | 49 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–110
- **Visible Samples:** 111

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 96 | 97 | inferred_complete_timeline |
| `Action_None` | 97 | 110 | 14 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–149
- **Visible Samples:** 150

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 96 | 97 | inferred_complete_timeline |
| `Action_None` | 97 | 149 | 53 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–359
- **Visible Samples:** 360

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 96 | 97 | inferred_complete_timeline |
| `Action_None` | 97 | 359 | 263 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–359
- **Visible Samples:** 360

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 96 | 97 | inferred_complete_timeline |
| `Action_None` | 97 | 359 | 263 | inferred_complete_timeline |

</details>

<details>
<summary>LB3 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–298
- **Visible Samples:** 299

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 96 | 97 | inferred_complete_timeline |
| `Action_None` | 97 | 298 | 202 | inferred_complete_timeline |

</details>

<details>
<summary>CB — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `defense`
- **Visible Frames:** 0–359
- **Visible Samples:** 360

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 96 | 97 | inferred_complete_timeline |
| `Action_None` | 97 | 359 | 263 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–224
- **Visible Samples:** 225

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 96 | 97 | inferred_complete_timeline |
| `Action_None` | 97 | 224 | 128 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `18` | `18` | Position_Unknown | Team_Unknown | 0–359 | 360 | 2 | Undefined position; Undefined team |
| `19` | `19` | Position_Unknown | Team_Unknown | 0–238 | 235 | 5 | Undefined position; Undefined team |
| `20` | `20` | Position_Unknown | Team_Unknown | 0–231 | 232 | 6 | Undefined position; Undefined team |
| `21` | `21` | Position_Unknown | Team_Unknown | 20–341 | 309 | 5 | Undefined position; Undefined team |
| `22` | `23` | Position_Unknown | Team_Unknown | 116–263 | 146 | 3 | Undefined position; Undefined team |
| `23` | `25` | Position_Unknown | Team_Unknown | 154–156 | 3 | 1 | Undefined position; Undefined team |
| `24` | `26` | Position_Unknown | Team_Unknown | 161–293 | 133 | 1 | Undefined position; Undefined team |
| `25` | `28` | Position_Unknown | Team_Unknown | 168–290 | 123 | 1 | Undefined position; Undefined team |
| `26` | `32` | Position_Unknown | Team_Unknown | 220–359 | 140 | 1 | Undefined position; Undefined team |
| `27` | `34` | Position_Unknown | Team_Unknown | 234–304 | 24 | 3 | Undefined position; Undefined team |
| `28` | `37` | Position_Unknown | Team_Unknown | 294–297 | 4 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `4` (2 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `21` (3 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `8` (actor_track_id `8`): `SAF` position mapped to `defense` team
- ⚠️ 11 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 11 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 22 |
| Missing visible bounding boxes during action | 41 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 359 as fallback play end.
- ⚠️ Action 'Action_None' range [164-240] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [244-287] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [290-305] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [109-154] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [164-325] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [329-336] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [340-348] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [352-353] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [97-353] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [97-359] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [97-319] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [321-349] for track '7' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [353-354] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [97-224] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [97-180] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [184-197] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [202-250] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [97-298] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [111-118] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [97-149] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [97-110] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [97-359] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [97-254] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [97-135] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [138-153] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [155-156] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [158-238] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [144-231] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [139-323] for track '21' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [325-327] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [340-341] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [116-128] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [130-169] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [171-263] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [154-156] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [161-293] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [168-290] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [234-240] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [242-248] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [295-304] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [294-297] for track '28' has 2 frames without a visible bounding box.
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

</details>