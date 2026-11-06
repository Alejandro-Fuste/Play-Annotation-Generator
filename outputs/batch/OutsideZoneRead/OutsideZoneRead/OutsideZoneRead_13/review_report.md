# Play-Annotation-Generator Annotation Review — OutsideZoneRead_13

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `OutsideZoneRead_13`
- **Frame Range:** 0 to 329 (330 total frames)
- **Play:** `Play_Run_OutsideZoneRead`
- **Result:** `Result_Tackle`
- **Result Frame:** 329
- **Player Tracks:** 40
- **Ball Tracks:** 0
- **Action Segments:** 96
- **Validation Warnings:** 114
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 19
- **Exact Matches:** 6
- **Group Expanded Events:** 10
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 1
- **Missing Segments:** 0
- **Ambiguous Matches:** 1
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 74
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `8` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `9` | `Group` |
| ✅ EXACT | `Action_ZoneBlock` | LG | offense | `11` | `11` |
| ✅ EXACT | `Action_ZoneBlock` | RT | offense | `13` | `13` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | offense | `19` | `19` |
| ✅ EXACT | `Action_ZoneBlock` | RG | offense | `20` | `20` |
| ✅ EXACT | `Action_ZoneBlock` | LT | offense | `8` | `8` |
| ⚠️ START CHANGED | `Action_PressEdge` | Position_Unknown | Team_Unknown | `21` | `21` |
| ✅ EXACT | `Action_ReadEdgeDefender` | CB1 | defense | `16` | `16` |
| ✅ EXACT | `Action_Handoff` | CB1 | defense | `16` | `16` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `0` | `Group` | 0 | START | 0 | 329 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `11` | `Group` | 0 | START | 0 | 73 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `12` | `Group` | 0 | START | 0 | 179 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `13` | `Group` | 0 | START | 0 | 73 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `17` | `Group` | 0 | START | 0 | 329 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `18` | `Group` | 0 | START | 0 | 321 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `19` | `Group` | 0 | START | 0 | 73 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `20` | `Group` | 0 | START | 0 | 73 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `8` | `Group` | 0 | START | 0 | 73 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `9` | `Group` | 0 | START | 0 | 329 |
| ✅ EXACT | `Action_ZoneBlock` | LG | `11` | `11` | 74 | START | 74 | 126 |
| ✅ EXACT | `Action_ZoneBlock` | RT | `13` | `13` | 74 | START | 74 | 126 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | `19` | `19` | 74 | START | 74 | 90 |
| ✅ EXACT | `Action_ZoneBlock` | RG | `20` | `20` | 74 | START | 74 | 126 |
| ✅ EXACT | `Action_ZoneBlock` | LT | `8` | `8` | 74 | START | 74 | 126 |
| ⚠️ START CHANGED | `Action_PressEdge` | Position_Unknown | `21` | `21` | 82 | START | 89 | 145 |
| ✅ EXACT | `Action_ReadEdgeDefender` | CB1 | `16` | `16` | 82 | START | 82 | 94 |
| ✅ EXACT | `Action_Handoff` | CB1 | `16` | `16` | 95 | START | 95 | 111 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–321
- **Visible Samples:** 322

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 321 | 322 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–329
- **Visible Samples:** 330

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 329 | 330 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–329
- **Visible Samples:** 330

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 329 | 330 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–329
- **Visible Samples:** 330

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 329 | 330 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–323
- **Visible Samples:** 304

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 179 | 180 | inferred_complete_timeline |
| `Action_PreSnap` | 183 | 197 | 15 | inferred_complete_timeline |
| `Action_PreSnap` | 200 | 205 | 6 | inferred_complete_timeline |
| `Action_PreSnap` | 208 | 221 | 14 | inferred_complete_timeline |
| `Action_PreSnap` | 235 | 323 | 89 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–138
- **Visible Samples:** 139

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 73 | 74 | inferred_complete_timeline |
| `Action_ZoneBlock` | 74 | 126 | 53 | inferred_complete_timeline |
| `Action_None` | 127 | 138 | 12 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–329
- **Visible Samples:** 330

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 73 | 74 | inferred_complete_timeline |
| `Action_ZoneBlock` | 74 | 126 | 53 | inferred_complete_timeline |
| `Action_None` | 127 | 329 | 203 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–157
- **Visible Samples:** 136

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 73 | 74 | inferred_complete_timeline |
| `Action_ZoneBlock` | 74 | 90 | 17 | inferred_complete_timeline |
| `Action_ZoneBlock` | 98 | 100 | 3 | inferred_complete_timeline |
| `Action_ZoneBlock` | 103 | 105 | 3 | inferred_complete_timeline |
| `Action_ZoneBlock` | 109 | 121 | 13 | inferred_complete_timeline |
| `Action_None` | 128 | 140 | 13 | inferred_complete_timeline |
| `Action_None` | 144 | 152 | 9 | inferred_complete_timeline |
| `Action_None` | 154 | 157 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–128
- **Visible Samples:** 129

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 73 | 74 | inferred_complete_timeline |
| `Action_ZoneBlock` | 74 | 126 | 53 | inferred_complete_timeline |
| `Action_None` | 127 | 128 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–156
- **Visible Samples:** 153

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 73 | 74 | inferred_complete_timeline |
| `Action_ZoneBlock` | 74 | 126 | 53 | inferred_complete_timeline |
| `Action_None` | 127 | 145 | 19 | inferred_complete_timeline |
| `Action_None` | 150 | 156 | 7 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–169
- **Visible Samples:** 170

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 169 | 170 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 308

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 120 | 121 | inferred_complete_timeline |
| `Action_PreSnap` | 126 | 158 | 33 | inferred_complete_timeline |
| `Action_PreSnap` | 165 | 166 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 170 | 172 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 174 | 180 | 7 | inferred_complete_timeline |
| `Action_PreSnap` | 187 | 193 | 7 | inferred_complete_timeline |
| `Action_PreSnap` | 195 | 329 | 135 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–235
- **Visible Samples:** 191

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 157 | 158 | inferred_complete_timeline |
| `Action_PreSnap` | 164 | 165 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 174 | 175 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 178 | 181 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 195 | 200 | 6 | inferred_complete_timeline |
| `Action_PreSnap` | 202 | 204 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 206 | 213 | 8 | inferred_complete_timeline |
| `Action_PreSnap` | 228 | 235 | 8 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–197
- **Visible Samples:** 168

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 157 | 158 | inferred_complete_timeline |
| `Action_PreSnap` | 180 | 182 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 184 | 185 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 192 | 194 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 196 | 197 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 330

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 329 | 330 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–126
- **Visible Samples:** 127

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 126 | 127 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–326
- **Visible Samples:** 323

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 81 | 82 | inferred_complete_timeline |
| `Action_ReadEdgeDefender` | 82 | 94 | 13 | inferred_complete_timeline |
| `Action_Handoff` | 95 | 111 | 17 | inferred_complete_timeline |
| `Action_None` | 112 | 249 | 138 | inferred_complete_timeline |
| `Action_None` | 252 | 288 | 37 | inferred_complete_timeline |
| `Action_None` | 291 | 326 | 36 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 330

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 329 | 330 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 330

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 329 | 330 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 328

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 315 | 316 | inferred_complete_timeline |
| `Action_PreSnap` | 318 | 329 | 12 | inferred_complete_timeline |

</details>

<details>
<summary>SAF3 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 330

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 329 | 330 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `21` | `21` | Position_Unknown | Team_Unknown | 3–329 | 313 | 4 | Undefined position; Undefined team |
| `22` | `23` | Position_Unknown | Team_Unknown | 94–97 | 4 | 1 | Undefined position; Undefined team |
| `23` | `24` | Position_Unknown | Team_Unknown | 116–329 | 166 | 4 | Undefined position; Undefined team |
| `24` | `25` | Position_Unknown | Team_Unknown | 117–118 | 2 | 1 | Undefined position; Undefined team |
| `25` | `29` | Position_Unknown | Team_Unknown | 130–134 | 5 | 1 | Undefined position; Undefined team |
| `26` | `31` | Position_Unknown | Team_Unknown | 137–329 | 181 | 5 | Undefined position; Undefined team |
| `27` | `33` | Position_Unknown | Team_Unknown | 141–154 | 13 | 2 | Undefined position; Undefined team |
| `28` | `36` | Position_Unknown | Team_Unknown | 153–166 | 6 | 2 | Undefined position; Undefined team |
| `29` | `37` | Position_Unknown | Team_Unknown | 156–157 | 2 | 1 | Undefined position; Undefined team |
| `30` | `38` | Position_Unknown | Team_Unknown | 156–319 | 120 | 2 | Undefined position; Undefined team |
| `31` | `41` | Position_Unknown | Team_Unknown | 192–329 | 138 | 1 | Undefined position; Undefined team |
| `32` | `45` | Position_Unknown | Team_Unknown | 194–199 | 6 | 1 | Undefined position; Undefined team |
| `33` | `46` | Position_Unknown | Team_Unknown | 198–329 | 132 | 1 | Undefined position; Undefined team |
| `34` | `47` | Position_Unknown | Team_Unknown | 212–329 | 118 | 1 | Undefined position; Undefined team |
| `35` | `48` | Position_Unknown | Team_Unknown | 218–313 | 96 | 1 | Undefined position; Undefined team |
| `36` | `50` | Position_Unknown | Team_Unknown | 266–267 | 2 | 1 | Undefined position; Undefined team |
| `37` | `52` | Position_Unknown | Team_Unknown | 276–316 | 41 | 1 | Undefined position; Undefined team |
| `38` | `53` | Position_Unknown | Team_Unknown | 281–282 | 2 | 1 | Undefined position; Undefined team |
| `39` | `56` | Position_Unknown | Team_Unknown | 298–299 | 2 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `19` (4 segments found)
- ⚠️ `Action_PressEdge` for actor_track_id `21` (Position_Unknown): Annotated start 82 != Inferred start 89

### Track Identity Issues

- ⚠️ Player track XML ID `1` (actor_track_id `1`): `SAF3` position mapped to `defense` team
- ⚠️ Player track XML ID `2` (actor_track_id `2`): `SAF1` position mapped to `defense` team
- ⚠️ Player track XML ID `10` (actor_track_id `10`): `SAF2` position mapped to `defense` team
- ⚠️ 19 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 19 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 38 |
| Missing visible bounding boxes during action | 75 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 329 as fallback play end.
- ⚠️ Action 'Action_PreSnap' range [0-329] for track '1' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-169] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-329] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-126] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-120] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [126-158] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [165-166] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [170-172] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [174-180] for track '7' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [187-193] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [74-126] for track '8' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [127-138] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-329] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-315] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-179] for track '12' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [183-197] for track '12' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [200-205] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [208-221] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [235-323] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [74-126] for track '13' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [127-145] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [150-156] for track '13' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-157] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [164-165] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [174-175] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [178-181] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [195-200] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [202-204] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [206-213] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [228-235] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-157] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [180-182] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [184-185] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [192-194] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [196-197] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [112-249] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [252-288] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [291-326] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-321] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [74-90] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [98-100] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [103-105] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [109-121] for track '19' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [128-140] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [144-152] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [154-157] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [127-128] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [3-80] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [146-166] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [173-329] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [94-97] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [116-132] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [176-181] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [186-187] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [117-118] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [130-134] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [137-161] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [163-166] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [168-173] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [178-185] for track '26' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [192-329] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [141-151] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [153-154] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [153-154] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [163-166] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [156-157] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [156-157] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [202-319] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [194-199] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [212-329] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [218-313] for track '35' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [266-267] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [276-316] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [281-282] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [298-299] for track '39' has 1 frames without a visible bounding box.
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

</details>