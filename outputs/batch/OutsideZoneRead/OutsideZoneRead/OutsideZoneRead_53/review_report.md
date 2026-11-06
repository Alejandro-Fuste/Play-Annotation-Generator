# Play-Annotation-Generator Annotation Review — OutsideZoneRead_53

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `OutsideZoneRead_53`
- **Frame Range:** 0 to 329 (330 total frames)
- **Play:** `Play_Run_OutsideZoneRead`
- **Result:** `Result_OutOfBounds`
- **Result Frame:** 329
- **Player Tracks:** 39
- **Ball Tracks:** 0
- **Action Segments:** 125
- **Validation Warnings:** 166
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 11
- **Exact Matches:** 3
- **Group Expanded Events:** 6
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 1
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 99
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `8` | `Group` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | offense | `13` | `13` |
| ✅ EXACT | `Action_PressEdge` | RB | offense | `8` | `8` |
| ✅ EXACT | `Action_ReadEdgeDefender` | QB | offense | `12` | `12` |
| ✅ EXACT | `Action_Handoff` | QB | offense | `12` | `12` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `0` | `Group` | 0 | START | 0 | 329 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `12` | `Group` | 0 | START | 0 | 81 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `13` | `Group` | 0 | START | 0 | 60 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `14` | `Group` | 0 | START | 0 | 1 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `6` | `Group` | 0 | START | 0 | 149 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `8` | `Group` | 0 | START | 0 | 69 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | `13` | `13` | 67 | START | 67 | 68 |
| ✅ EXACT | `Action_PressEdge` | RB | `8` | `8` | 70 | START | 70 | 127 |
| ✅ EXACT | `Action_ReadEdgeDefender` | QB | `12` | `12` | 82 | START | 82 | 84 |
| ✅ EXACT | `Action_Handoff` | QB | `12` | `12` | 85 | START | 85 | 102 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–258
- **Visible Samples:** 241

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 81 | 82 | inferred_complete_timeline |
| `Action_ReadEdgeDefender` | 82 | 84 | 3 | inferred_complete_timeline |
| `Action_Handoff` | 85 | 102 | 18 | inferred_complete_timeline |
| `Action_None` | 103 | 117 | 15 | inferred_complete_timeline |
| `Action_None` | 120 | 147 | 28 | inferred_complete_timeline |
| `Action_None` | 154 | 195 | 42 | inferred_complete_timeline |
| `Action_None` | 197 | 220 | 24 | inferred_complete_timeline |
| `Action_None` | 222 | 223 | 2 | inferred_complete_timeline |
| `Action_None` | 230 | 232 | 3 | inferred_complete_timeline |
| `Action_None` | 234 | 235 | 2 | inferred_complete_timeline |
| `Action_None` | 237 | 258 | 22 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–325
- **Visible Samples:** 326

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 69 | 70 | inferred_complete_timeline |
| `Action_PressEdge` | 70 | 127 | 58 | inferred_complete_timeline |
| `Action_None` | 128 | 325 | 198 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–323
- **Visible Samples:** 278

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 149 | 150 | inferred_complete_timeline |
| `Action_PreSnap` | 153 | 157 | 5 | inferred_complete_timeline |
| `Action_PreSnap` | 171 | 187 | 17 | inferred_complete_timeline |
| `Action_PreSnap` | 194 | 200 | 7 | inferred_complete_timeline |
| `Action_PreSnap` | 202 | 240 | 39 | inferred_complete_timeline |
| `Action_PreSnap` | 243 | 245 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 255 | 301 | 47 | inferred_complete_timeline |
| `Action_PreSnap` | 312 | 316 | 5 | inferred_complete_timeline |
| `Action_PreSnap` | 319 | 323 | 5 | inferred_complete_timeline |

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
<summary>TE — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–147
- **Visible Samples:** 106

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 9 | 27 | 19 | inferred_complete_timeline |
| `Action_PreSnap` | 30 | 35 | 6 | inferred_complete_timeline |
| `Action_PreSnap` | 51 | 53 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 68 | 70 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 73 | 74 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 76 | 112 | 37 | inferred_complete_timeline |
| `Action_PreSnap` | 114 | 147 | 34 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–329
- **Visible Samples:** 280

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 60 | 61 | inferred_complete_timeline |
| `Action_PreSnap` | 66 | 66 | 1 | inferred_complete_timeline |
| `Action_ZoneBlock` | 67 | 68 | 2 | inferred_complete_timeline |
| `Action_ZoneBlock` | 78 | 79 | 2 | inferred_complete_timeline |
| `Action_ZoneBlock` | 93 | 98 | 6 | inferred_complete_timeline |
| `Action_ZoneBlock` | 108 | 114 | 7 | inferred_complete_timeline |
| `Action_ZoneBlock` | 118 | 118 | 1 | inferred_complete_timeline |
| `Action_None` | 119 | 123 | 5 | inferred_complete_timeline |
| `Action_None` | 125 | 126 | 2 | inferred_complete_timeline |
| `Action_None` | 128 | 137 | 10 | inferred_complete_timeline |
| `Action_None` | 146 | 151 | 6 | inferred_complete_timeline |
| `Action_None` | 153 | 329 | 177 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>LB1 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–138
- **Visible Samples:** 138

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 132 | 133 | inferred_complete_timeline |
| `Action_PreSnap` | 134 | 138 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–69
- **Visible Samples:** 69

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 44 | 45 | inferred_complete_timeline |
| `Action_PreSnap` | 46 | 69 | 24 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–143
- **Visible Samples:** 138

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 112 | 113 | inferred_complete_timeline |
| `Action_PreSnap` | 114 | 132 | 19 | inferred_complete_timeline |
| `Action_PreSnap` | 138 | 143 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–201
- **Visible Samples:** 202

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 201 | 202 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 327

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 299 | 300 | inferred_complete_timeline |
| `Action_PreSnap` | 302 | 305 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 307 | 329 | 23 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
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
- **Visible Frames:** 0–310
- **Visible Samples:** 308

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 244 | 245 | inferred_complete_timeline |
| `Action_PreSnap` | 246 | 299 | 54 | inferred_complete_timeline |
| `Action_PreSnap` | 302 | 310 | 9 | inferred_complete_timeline |

</details>

<details>
<summary>SAF3 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–285
- **Visible Samples:** 271

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 149 | 150 | inferred_complete_timeline |
| `Action_PreSnap` | 159 | 161 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 163 | 178 | 16 | inferred_complete_timeline |
| `Action_PreSnap` | 181 | 183 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 185 | 205 | 21 | inferred_complete_timeline |
| `Action_PreSnap` | 208 | 285 | 78 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `5` | `5` | Position_Unknown | Team_Unknown | 0–329 | 327 | 3 | Undefined position; Undefined team |
| `15` | `16` | Position_Unknown | Team_Unknown | 77–132 | 49 | 4 | Undefined position; Undefined team |
| `16` | `17` | Position_Unknown | Team_Unknown | 78–98 | 20 | 2 | Undefined position; Undefined team |
| `17` | `18` | Position_Unknown | Team_Unknown | 79–144 | 59 | 2 | Undefined position; Undefined team |
| `18` | `19` | Position_Unknown | Team_Unknown | 79–311 | 229 | 3 | Undefined position; Undefined team |
| `19` | `20` | Position_Unknown | Team_Unknown | 80–329 | 240 | 5 | Undefined position; Undefined team |
| `20` | `21` | Position_Unknown | Team_Unknown | 86–329 | 218 | 9 | Undefined position; Undefined team |
| `21` | `22` | Position_Unknown | Team_Unknown | 110–119 | 10 | 1 | Undefined position; Undefined team |
| `22` | `23` | Position_Unknown | Team_Unknown | 144–145 | 2 | 1 | Undefined position; Undefined team |
| `23` | `24` | Position_Unknown | Team_Unknown | 152–329 | 178 | 1 | Undefined position; Undefined team |
| `24` | `25` | Position_Unknown | Team_Unknown | 152–323 | 169 | 3 | Undefined position; Undefined team |
| `25` | `27` | Position_Unknown | Team_Unknown | 160–242 | 44 | 5 | Undefined position; Undefined team |
| `26` | `28` | Position_Unknown | Team_Unknown | 164–253 | 90 | 1 | Undefined position; Undefined team |
| `27` | `29` | Position_Unknown | Team_Unknown | 172–186 | 15 | 1 | Undefined position; Undefined team |
| `28` | `32` | Position_Unknown | Team_Unknown | 197–304 | 105 | 3 | Undefined position; Undefined team |
| `29` | `34` | Position_Unknown | Team_Unknown | 201–329 | 129 | 1 | Undefined position; Undefined team |
| `30` | `39` | Position_Unknown | Team_Unknown | 230–302 | 72 | 2 | Undefined position; Undefined team |
| `31` | `40` | Position_Unknown | Team_Unknown | 236–312 | 72 | 3 | Undefined position; Undefined team |
| `32` | `41` | Position_Unknown | Team_Unknown | 241–242 | 2 | 1 | Undefined position; Undefined team |
| `33` | `42` | Position_Unknown | Team_Unknown | 244–245 | 2 | 1 | Undefined position; Undefined team |
| `34` | `48` | Position_Unknown | Team_Unknown | 266–292 | 10 | 4 | Undefined position; Undefined team |
| `35` | `51` | Position_Unknown | Team_Unknown | 296–297 | 2 | 1 | Undefined position; Undefined team |
| `36` | `52` | Position_Unknown | Team_Unknown | 298–301 | 4 | 1 | Undefined position; Undefined team |
| `37` | `55` | Position_Unknown | Team_Unknown | 312–329 | 18 | 1 | Undefined position; Undefined team |
| `38` | `58` | Position_Unknown | Team_Unknown | 318–329 | 12 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `13` (5 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `1` (actor_track_id `1`): `SAF3` position mapped to `defense` team
- ⚠️ Player track XML ID `9` (actor_track_id `9`): `SAF1` position mapped to `defense` team
- ⚠️ Player track XML ID `10` (actor_track_id `10`): `SAF2` position mapped to `defense` team
- ⚠️ 25 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 25 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 50 |
| Missing visible bounding boxes during action | 114 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Track ID '15' in Player Track ID sheet does not exist in MOT gt.txt.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 329 as fallback play end.
- ⚠️ Action 'Action_PreSnap' range [0-329] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-149] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [159-161] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [163-178] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [181-183] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [185-205] for track '1' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [208-285] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-201] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-299] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [302-305] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [307-329] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-112] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [114-132] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [138-143] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-304] for track '5' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [306-311] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-149] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [153-157] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [171-187] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [194-200] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [202-240] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [243-245] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [255-301] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [312-316] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [319-323] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-132] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [134-138] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [128-325] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-244] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [246-299] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [302-310] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-44] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [46-69] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_Handoff' range [85-102] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [103-117] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [120-147] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [154-195] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [197-220] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [222-223] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [230-232] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [234-235] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [237-258] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-60] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [67-68] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [78-79] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [93-98] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [108-114] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' for track '13' starts at frame 119, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_None' range [119-123] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [125-126] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [128-137] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [146-151] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [153-329] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-1] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [9-27] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [30-35] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [51-53] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [68-70] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [73-74] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [76-112] for track '14' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [114-147] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [77-100] for track '15' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [104-105] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [108-122] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [125-132] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [78-88] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [90-98] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [79-135] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [143-144] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [79-116] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [120-261] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [263-311] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [80-96] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [102-105] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [108-182] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [185-209] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [86-98] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [103-106] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [108-123] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [128-130] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [135-144] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [146-149] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [151-222] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [230-234] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [110-119] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [144-145] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [152-329] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [152-154] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [157-302] for track '24' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [304-323] for track '24' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [160-167] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [179-183] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [187-212] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [214-216] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [241-242] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [164-253] for track '26' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [172-186] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [197-248] for track '28' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [251-299] for track '28' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [301-304] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [201-329] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [230-299] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [301-302] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [236-252] for track '31' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [255-301] for track '31' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [305-312] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [241-242] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [244-245] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [266-267] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [272-274] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [285-287] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [291-292] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [296-297] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [298-301] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Player track '5' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '5' has undefined team_side. Will map to Team_Unknown.
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

</details>