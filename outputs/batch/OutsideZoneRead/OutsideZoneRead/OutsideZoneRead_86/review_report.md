# Play-Annotation-Generator Annotation Review — OutsideZoneRead_86

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `OutsideZoneRead_86`
- **Frame Range:** 0 to 359 (360 total frames)
- **Play:** `Play_Run_OutsideZoneRead`
- **Result:** `Result_OutOfBounds`
- **Result Frame:** 359
- **Player Tracks:** 38
- **Ball Tracks:** 0
- **Action Segments:** 92
- **Validation Warnings:** 127
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 17
- **Exact Matches:** 4
- **Group Expanded Events:** 8
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 2
- **Ambiguous Matches:** 2
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 70
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `9` | `Group` |
| ⚠️ AMBIGUOUS MATCH | `Action_PressEdge` | RB | offense | `5` | `5` |
| ❌ MISSING SEGMENT | `Action_ZoneBlock` | RG | offense | `12` | `12` |
| ❌ MISSING SEGMENT | `Action_ZoneBlock` | C | offense | `13` | `13` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | offense | `14` | `14` |
| ✅ EXACT | `Action_ZoneBlock` | RT | offense | `3` | `3` |
| ✅ EXACT | `Action_ZoneBlock` | LT | offense | `6` | `6` |
| ✅ EXACT | `Action_ReadEdgeDefender` | QB | offense | `9` | `9` |
| ✅ EXACT | `Action_Handoff` | QB | offense | `9` | `9` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `12` | `Group` | 0 | START | 0 | 123 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `13` | `Group` | 0 | START | 0 | 13 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `14` | `Group` | 0 | START | 0 | 45 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `2` | `Group` | 0 | START | 0 | 144 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `3` | `Group` | 0 | START | 0 | 159 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `5` | `Group` | 0 | START | 0 | 186 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `6` | `Group` | 0 | START | 0 | 117 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `9` | `Group` | 0 | START | 0 | 191 |
| ⚠️ AMBIGUOUS MATCH | `Action_PressEdge` | RB | `5` | `5` | 187 | START | 187 | 204 |
| ❌ MISSING SEGMENT | `Action_ZoneBlock` | RG | `12` | `12` | 187 | START | N/A | N/A |
| ❌ MISSING SEGMENT | `Action_ZoneBlock` | C | `13` | `13` | 187 | START | N/A | N/A |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | `14` | `14` | 187 | START | 187 | 187 |
| ✅ EXACT | `Action_ZoneBlock` | RT | `3` | `3` | 187 | START | 187 | 232 |
| ✅ EXACT | `Action_ZoneBlock` | LT | `6` | `6` | 187 | START | 187 | 232 |
| ✅ EXACT | `Action_ReadEdgeDefender` | QB | `9` | `9` | 192 | START | 192 | 200 |
| ✅ EXACT | `Action_Handoff` | QB | `9` | `9` | 202 | START | 202 | 202 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–202
- **Visible Samples:** 203

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 191 | 192 | inferred_complete_timeline |
| `Action_ReadEdgeDefender` | 192 | 200 | 9 | inferred_complete_timeline |
| `Action_None` | 201 | 201 | 1 | inferred_complete_timeline |
| `Action_Handoff` | 202 | 202 | 1 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–274
- **Visible Samples:** 267

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 186 | 187 | inferred_complete_timeline |
| `Action_PressEdge` | 187 | 204 | 18 | inferred_complete_timeline |
| `Action_PressEdge` | 213 | 237 | 25 | inferred_complete_timeline |
| `Action_None` | 238 | 274 | 37 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–359
- **Visible Samples:** 254

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 144 | 145 | inferred_complete_timeline |
| `Action_PreSnap` | 161 | 233 | 73 | inferred_complete_timeline |
| `Action_PreSnap` | 258 | 259 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 261 | 277 | 17 | inferred_complete_timeline |
| `Action_PreSnap` | 343 | 359 | 17 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–347
- **Visible Samples:** 327

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 117 | 118 | inferred_complete_timeline |
| `Action_PreSnap` | 136 | 186 | 51 | inferred_complete_timeline |
| `Action_ZoneBlock` | 187 | 232 | 46 | inferred_complete_timeline |
| `Action_None` | 233 | 281 | 49 | inferred_complete_timeline |
| `Action_None` | 283 | 343 | 61 | inferred_complete_timeline |
| `Action_None` | 346 | 347 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–223
- **Visible Samples:** 187

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 45 | 46 | inferred_complete_timeline |
| `Action_PreSnap` | 49 | 186 | 138 | inferred_complete_timeline |
| `Action_ZoneBlock` | 187 | 187 | 1 | inferred_complete_timeline |
| `Action_ZoneBlock` | 222 | 223 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–13
- **Visible Samples:** 14

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 13 | 14 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–186
- **Visible Samples:** 176

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 123 | 124 | inferred_complete_timeline |
| `Action_PreSnap` | 135 | 186 | 52 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–262
- **Visible Samples:** 252

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 159 | 160 | inferred_complete_timeline |
| `Action_PreSnap` | 171 | 186 | 16 | inferred_complete_timeline |
| `Action_ZoneBlock` | 187 | 232 | 46 | inferred_complete_timeline |
| `Action_None` | 233 | 262 | 30 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–359
- **Visible Samples:** 354

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 262 | 263 | inferred_complete_timeline |
| `Action_PreSnap` | 265 | 282 | 18 | inferred_complete_timeline |
| `Action_PreSnap` | 284 | 286 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 288 | 307 | 20 | inferred_complete_timeline |
| `Action_PreSnap` | 310 | 359 | 50 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `defense`
- **Visible Frames:** 0–258
- **Visible Samples:** 259

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 258 | 259 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–336
- **Visible Samples:** 278

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 151 | 152 | inferred_complete_timeline |
| `Action_PreSnap` | 192 | 223 | 32 | inferred_complete_timeline |
| `Action_PreSnap` | 230 | 266 | 37 | inferred_complete_timeline |
| `Action_PreSnap` | 280 | 336 | 57 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–359
- **Visible Samples:** 337

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 69 | 70 | inferred_complete_timeline |
| `Action_PreSnap` | 73 | 105 | 33 | inferred_complete_timeline |
| `Action_PreSnap` | 123 | 248 | 126 | inferred_complete_timeline |
| `Action_PreSnap` | 252 | 359 | 108 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–291
- **Visible Samples:** 292

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 291 | 292 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–302
- **Visible Samples:** 303

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 302 | 303 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–359
- **Visible Samples:** 344

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 111 | 112 | inferred_complete_timeline |
| `Action_PreSnap` | 116 | 343 | 228 | inferred_complete_timeline |
| `Action_PreSnap` | 345 | 347 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 359 | 359 | 1 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `15` | `15` | Position_Unknown | Team_Unknown | 0–202 | 101 | 10 | Undefined position; Undefined team |
| `16` | `16` | Position_Unknown | Team_Unknown | 8–14 | 5 | 2 | Undefined position; Undefined team |
| `17` | `17` | Position_Unknown | Team_Unknown | 23–76 | 54 | 1 | Undefined position; Undefined team |
| `18` | `18` | Position_Unknown | Team_Unknown | 94–352 | 243 | 3 | Undefined position; Undefined team |
| `19` | `19` | Position_Unknown | Team_Unknown | 136–194 | 44 | 2 | Undefined position; Undefined team |
| `20` | `20` | Position_Unknown | Team_Unknown | 153–154 | 2 | 1 | Undefined position; Undefined team |
| `21` | `21` | Position_Unknown | Team_Unknown | 178–179 | 2 | 1 | Undefined position; Undefined team |
| `22` | `22` | Position_Unknown | Team_Unknown | 214–217 | 4 | 1 | Undefined position; Undefined team |
| `23` | `23` | Position_Unknown | Team_Unknown | 222–226 | 5 | 1 | Undefined position; Undefined team |
| `24` | `25` | Position_Unknown | Team_Unknown | 227–359 | 130 | 2 | Undefined position; Undefined team |
| `25` | `29` | Position_Unknown | Team_Unknown | 245–359 | 106 | 3 | Undefined position; Undefined team |
| `26` | `30` | Position_Unknown | Team_Unknown | 246–359 | 114 | 1 | Undefined position; Undefined team |
| `27` | `32` | Position_Unknown | Team_Unknown | 251–259 | 9 | 1 | Undefined position; Undefined team |
| `28` | `33` | Position_Unknown | Team_Unknown | 266–359 | 92 | 2 | Undefined position; Undefined team |
| `29` | `34` | Position_Unknown | Team_Unknown | 275–304 | 30 | 1 | Undefined position; Undefined team |
| `30` | `36` | Position_Unknown | Team_Unknown | 287–359 | 65 | 3 | Undefined position; Undefined team |
| `31` | `37` | Position_Unknown | Team_Unknown | 289–292 | 4 | 1 | Undefined position; Undefined team |
| `32` | `39` | Position_Unknown | Team_Unknown | 296–302 | 7 | 1 | Undefined position; Undefined team |
| `33` | `40` | Position_Unknown | Team_Unknown | 297–359 | 63 | 1 | Undefined position; Undefined team |
| `34` | `41` | Position_Unknown | Team_Unknown | 318–359 | 42 | 1 | Undefined position; Undefined team |
| `35` | `42` | Position_Unknown | Team_Unknown | 322–359 | 38 | 1 | Undefined position; Undefined team |
| `36` | `44` | Position_Unknown | Team_Unknown | 331–333 | 3 | 1 | Undefined position; Undefined team |
| `37` | `45` | Position_Unknown | Team_Unknown | 333–337 | 5 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_PressEdge` and target `5` (2 segments found)
- ❌ Missing segment for action `Action_ZoneBlock` on target `12` (RG)
- ❌ Missing segment for action `Action_ZoneBlock` on target `13` (C)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `14` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `7` (actor_track_id `7`): `SAF` position mapped to `defense` team
- ⚠️ 23 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 23 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 46 |
| Missing visible bounding boxes during action | 78 |
| Track-related warning | 2 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 359 as fallback play end.
- ⚠️ Segment 'Action_ZoneBlock' for track '12' has invalid range: start=187, end=186. Clamping end to start.
- ⚠️ Segment 'Action_ZoneBlock' for track '13' has invalid range: start=187, end=13. Clamping end to start.
- ⚠️ Action 'Action_PreSnap' range [0-258] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-262] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [265-282] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [284-286] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [288-307] for track '1' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [310-359] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-144] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [161-233] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [258-259] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [261-277] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-159] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [187-232] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [233-262] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-291] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PressEdge' range [187-204] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [238-274] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-117] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [233-281] for track '6' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [283-343] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [346-347] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-111] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [116-343] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [345-347] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-151] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [192-223] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [230-266] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [280-336] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ReadEdgeDefender' range [192-200] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_Handoff' for track '9' starts at frame 202, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_Handoff' range [202-202] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-302] for track '10' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-69] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [73-105] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [123-248] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-123] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [135-186] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-13] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-45] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' for track '14' starts at frame 187, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_ZoneBlock' range [187-187] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [222-223] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-4] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [6-8] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [32-56] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [77-80] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [91-121] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [133-134] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [152-155] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [165-168] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [177-195] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [199-202] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [8-9] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [12-14] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [23-76] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [94-201] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [216-259] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [262-352] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [136-158] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [174-194] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [153-154] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [178-179] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [214-217] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [222-226] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [227-312] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [245-266] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [271-275] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [246-359] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [251-259] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [266-298] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [275-304] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [287-291] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [298-314] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [317-359] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [289-292] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [296-302] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [322-359] for track '35' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [331-333] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [333-337] for track '37' has 1 frames without a visible bounding box.
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

</details>