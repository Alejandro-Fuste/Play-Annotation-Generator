# Play-Annotation-Generator Annotation Review — OutsideZoneRead_63

**Overall Status:** FAILED

## 1. Clip & Validation Summary

- **Video:** `OutsideZoneRead_63`
- **Frame Range:** 0 to 329 (330 total frames)
- **Play:** `Play_Run_OutsideZoneRead`
- **Result:** `Result_OutOfBounds`
- **Result Frame:** 329
- **Player Tracks:** 44
- **Ball Tracks:** 0
- **Action Segments:** 120
- **Validation Warnings:** 154
- **Validation Errors:** 2
- **Overall Status:** FAILED

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 19
- **Exact Matches:** 3
- **Group Expanded Events:** 10
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 4
- **Ambiguous Matches:** 1
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 91
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | offense | `5` | `Group` |
| ✅ EXACT | `Action_Handoff` | QB | offense | `19` | `19` |
| ✅ EXACT | `Action_PressEdge` | Position_Unknown | Team_Unknown | `22` | `22` |
| ✅ EXACT | `Action_ZoneBlock` | LT | offense | `12` | `12` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | offense | `15` | `15` |
| ❌ MISSING SEGMENT | `Action_ZoneBlock` | LG | offense | `17` | `17` |
| ❌ MISSING SEGMENT | `Action_ZoneBlock` | RT | offense | `18` | `18` |
| ❌ MISSING SEGMENT | `Action_ZoneBlock` | C | offense | `20` | `20` |
| ❌ MISSING SEGMENT | `Action_ReadEdgeDefender` | LB2 | defense | `6` | `6` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `0` | `Group` | 0 | START | 0 | 142 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `1` | `Group` | 0 | START | 0 | 177 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `12` | `Group` | 0 | START | 0 | 90 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | `13` | `Group` | 0 | START | 0 | 258 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `15` | `Group` | 0 | START | 0 | 105 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `17` | `Group` | 0 | START | 0 | 98 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `18` | `Group` | 0 | START | 0 | 106 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `19` | `Group` | 0 | START | 0 | 110 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `20` | `Group` | 0 | START | 0 | 85 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | `5` | `Group` | 0 | START | 0 | 131 |
| ✅ EXACT | `Action_Handoff` | QB | `19` | `19` | 111 | START | 111 | 124 |
| ✅ EXACT | `Action_PressEdge` | Position_Unknown | `22` | `22` | 159 | START | 159 | 185 |
| ✅ EXACT | `Action_ZoneBlock` | LT | `12` | `12` | 193 | START | 193 | 329 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | `15` | `15` | 193 | START | 193 | 281 |
| ❌ MISSING SEGMENT | `Action_ZoneBlock` | LG | `17` | `17` | 193 | START | N/A | N/A |
| ❌ MISSING SEGMENT | `Action_ZoneBlock` | RT | `18` | `18` | 193 | START | N/A | N/A |
| ❌ MISSING SEGMENT | `Action_ZoneBlock` | C | `20` | `20` | 193 | START | N/A | N/A |
| ❌ MISSING SEGMENT | `Action_ReadEdgeDefender` | LB2 | `6` | `6` | 211 | START | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–329
- **Visible Samples:** 330

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 110 | 111 | inferred_complete_timeline |
| `Action_Handoff` | 111 | 124 | 14 | inferred_complete_timeline |
| `Action_None` | 125 | 329 | 205 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–329
- **Visible Samples:** 319

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 177 | 178 | inferred_complete_timeline |
| `Action_PreSnap` | 179 | 184 | 6 | inferred_complete_timeline |
| `Action_PreSnap` | 195 | 329 | 135 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–142
- **Visible Samples:** 143

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 142 | 143 | inferred_complete_timeline |

</details>

<details>
<summary>TE1 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–131
- **Visible Samples:** 132

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 131 | 132 | inferred_complete_timeline |

</details>

<details>
<summary>TE2 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–282
- **Visible Samples:** 261

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 258 | 259 | inferred_complete_timeline |
| `Action_PreSnap` | 281 | 282 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–329
- **Visible Samples:** 322

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 90 | 91 | inferred_complete_timeline |
| `Action_PreSnap` | 98 | 106 | 9 | inferred_complete_timeline |
| `Action_PreSnap` | 108 | 192 | 85 | inferred_complete_timeline |
| `Action_ZoneBlock` | 193 | 329 | 137 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–98
- **Visible Samples:** 99

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 98 | 99 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–124
- **Visible Samples:** 109

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 85 | 86 | inferred_complete_timeline |
| `Action_PreSnap` | 87 | 89 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 102 | 119 | 18 | inferred_complete_timeline |
| `Action_PreSnap` | 123 | 124 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–329
- **Visible Samples:** 311

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 105 | 106 | inferred_complete_timeline |
| `Action_PreSnap` | 109 | 141 | 33 | inferred_complete_timeline |
| `Action_PreSnap` | 145 | 156 | 12 | inferred_complete_timeline |
| `Action_PreSnap` | 166 | 168 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 170 | 192 | 23 | inferred_complete_timeline |
| `Action_ZoneBlock` | 193 | 281 | 89 | inferred_complete_timeline |
| `Action_ZoneBlock` | 285 | 329 | 45 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–155
- **Visible Samples:** 146

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 106 | 107 | inferred_complete_timeline |
| `Action_PreSnap` | 113 | 141 | 29 | inferred_complete_timeline |
| `Action_PreSnap` | 144 | 149 | 6 | inferred_complete_timeline |
| `Action_PreSnap` | 152 | 155 | 4 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 321

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 162 | 163 | inferred_complete_timeline |
| `Action_PreSnap` | 170 | 296 | 127 | inferred_complete_timeline |
| `Action_PreSnap` | 299 | 329 | 31 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 320

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 149 | 150 | inferred_complete_timeline |
| `Action_PreSnap` | 153 | 158 | 6 | inferred_complete_timeline |
| `Action_PreSnap` | 160 | 239 | 80 | inferred_complete_timeline |
| `Action_PreSnap` | 242 | 248 | 7 | inferred_complete_timeline |
| `Action_PreSnap` | 252 | 271 | 20 | inferred_complete_timeline |
| `Action_PreSnap` | 273 | 329 | 57 | inferred_complete_timeline |

</details>

<details>
<summary>DT — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 327

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 219 | 220 | inferred_complete_timeline |
| `Action_PreSnap` | 222 | 239 | 18 | inferred_complete_timeline |
| `Action_PreSnap` | 241 | 329 | 89 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
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
- **Visible Frames:** 0–158
- **Visible Samples:** 153

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 149 | 150 | inferred_complete_timeline |
| `Action_PreSnap` | 156 | 158 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>OLB1 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–291
- **Visible Samples:** 287

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 126 | 127 | inferred_complete_timeline |
| `Action_PreSnap` | 131 | 287 | 157 | inferred_complete_timeline |
| `Action_PreSnap` | 289 | 291 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>OLB2 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 323

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 129 | 130 | inferred_complete_timeline |
| `Action_PreSnap` | 137 | 329 | 193 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–195
- **Visible Samples:** 191

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 158 | 159 | inferred_complete_timeline |
| `Action_PreSnap` | 164 | 195 | 32 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–291
- **Visible Samples:** 290

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 285 | 286 | inferred_complete_timeline |
| `Action_PreSnap` | 288 | 291 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 329

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 212 | 213 | inferred_complete_timeline |
| `Action_PreSnap` | 214 | 329 | 116 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
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
| `21` | `21` | Position_Unknown | Team_Unknown | 5–91 | 17 | 3 | Undefined position; Undefined team |
| `22` | `22` | Position_Unknown | Team_Unknown | 6–329 | 316 | 4 | Undefined position; Undefined team |
| `23` | `27` | Position_Unknown | Team_Unknown | 109–265 | 136 | 6 | Undefined position; Undefined team |
| `24` | `29` | Position_Unknown | Team_Unknown | 135–138 | 4 | 1 | Undefined position; Undefined team |
| `25` | `30` | Position_Unknown | Team_Unknown | 137–329 | 193 | 1 | Undefined position; Undefined team |
| `26` | `32` | Position_Unknown | Team_Unknown | 143–288 | 132 | 6 | Undefined position; Undefined team |
| `27` | `35` | Position_Unknown | Team_Unknown | 159–329 | 170 | 2 | Undefined position; Undefined team |
| `28` | `37` | Position_Unknown | Team_Unknown | 161–171 | 11 | 1 | Undefined position; Undefined team |
| `29` | `38` | Position_Unknown | Team_Unknown | 163–329 | 166 | 2 | Undefined position; Undefined team |
| `30` | `41` | Position_Unknown | Team_Unknown | 174–175 | 2 | 1 | Undefined position; Undefined team |
| `31` | `42` | Position_Unknown | Team_Unknown | 176–329 | 126 | 10 | Undefined position; Undefined team |
| `32` | `43` | Position_Unknown | Team_Unknown | 185–329 | 145 | 1 | Undefined position; Undefined team |
| `33` | `44` | Position_Unknown | Team_Unknown | 187–188 | 2 | 1 | Undefined position; Undefined team |
| `34` | `45` | Position_Unknown | Team_Unknown | 187–329 | 101 | 9 | Undefined position; Undefined team |
| `35` | `48` | Position_Unknown | Team_Unknown | 213–216 | 4 | 1 | Undefined position; Undefined team |
| `36` | `50` | Position_Unknown | Team_Unknown | 222–225 | 4 | 1 | Undefined position; Undefined team |
| `37` | `51` | Position_Unknown | Team_Unknown | 223–224 | 2 | 1 | Undefined position; Undefined team |
| `38` | `54` | Position_Unknown | Team_Unknown | 238–329 | 49 | 2 | Undefined position; Undefined team |
| `39` | `55` | Position_Unknown | Team_Unknown | 239–243 | 5 | 1 | Undefined position; Undefined team |
| `40` | `56` | Position_Unknown | Team_Unknown | 240–298 | 42 | 6 | Undefined position; Undefined team |
| `41` | `58` | Position_Unknown | Team_Unknown | 258–264 | 7 | 1 | Undefined position; Undefined team |
| `42` | `67` | Position_Unknown | Team_Unknown | 303–329 | 27 | 1 | Undefined position; Undefined team |
| `43` | `71` | Position_Unknown | Team_Unknown | 321–329 | 9 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `15` (2 segments found)
- ❌ Missing segment for action `Action_ZoneBlock` on target `17` (LG)
- ❌ Missing segment for action `Action_ZoneBlock` on target `18` (RT)
- ❌ Missing segment for action `Action_ZoneBlock` on target `20` (C)
- ❌ Missing segment for action `Action_ReadEdgeDefender` on target `6` (LB2)

### Track Identity Issues

- ⚠️ Player track XML ID `7` (actor_track_id `7`): `SAF1` position mapped to `defense` team
- ⚠️ Player track XML ID `8` (actor_track_id `8`): `SAF2` position mapped to `defense` team
- ⚠️ 23 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 23 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

- ❌ Event 'Action_ZoneBlock' at frame 193 targets track ID '137', but it is not found in XML.
- ❌ Event 'Action_ReadEdgeDefender' at frame 211 targets track ID '110', but it is not found in XML.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 46 |
| Missing visible bounding boxes during action | 101 |
| Track-related warning | 6 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 329 as fallback play end.
- ⚠️ Segment 'Action_ReadEdgeDefender' for track '6' has invalid range: start=211, end=158. Clamping end to start.
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '12' (LT) duration 137 frames exceeds threshold 90 frames [start=193, end=329].
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '15' (RG) duration 137 frames exceeds threshold 90 frames [start=193, end=329].
- ⚠️ Segment 'Action_ZoneBlock' for track '17' has invalid range: start=193, end=98. Clamping end to start.
- ⚠️ Segment 'Action_ZoneBlock' for track '18' has invalid range: start=193, end=155. Clamping end to start.
- ⚠️ Segment 'Action_ZoneBlock' for track '20' has invalid range: start=193, end=124. Clamping end to start.
- ⚠️ Action 'Action_PreSnap' range [0-142] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-177] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [179-184] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [195-329] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-126] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [131-287] for track '2' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [289-291] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-129] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [137-329] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-158] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [164-195] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-131] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-149] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [156-158] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-212] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [214-329] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-285] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [288-291] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-219] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [222-239] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-90] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [98-106] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [108-192] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-258] for track '13' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [281-282] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-149] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [153-158] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [160-239] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [242-248] for track '14' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [252-271] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-105] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [109-141] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [145-156] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [166-168] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [193-281] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [285-329] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-162] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [170-296] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-98] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-106] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [113-141] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [144-149] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [152-155] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [125-329] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-85] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [87-89] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [102-119] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [123-124] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [5-12] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [57-60] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [87-91] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [6-92] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [109-138] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [141-144] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [154-239] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [241-244] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [253-255] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [257-265] for track '23' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [135-138] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [143-173] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [178-198] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [202-239] for track '26' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [241-271] for track '26' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [275-283] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [287-288] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [159-198] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [161-171] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [163-214] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [174-175] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [176-177] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [181-200] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [202-209] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [215-226] for track '31' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [230-239] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [244-289] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [295-307] for track '31' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [311-314] for track '31' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [316-323] for track '31' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [327-329] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [185-329] for track '32' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [187-188] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [187-188] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [202-207] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [215-218] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [224-272] for track '34' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [275-280] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [285-289] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [295-301] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [306-314] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [213-216] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [222-225] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [223-224] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [238-239] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [239-243] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [240-241] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [245-246] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [252-280] for track '40' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [282-283] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [288-290] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [295-298] for track '40' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [258-264] for track '41' has 1 frames without a visible bounding box.
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