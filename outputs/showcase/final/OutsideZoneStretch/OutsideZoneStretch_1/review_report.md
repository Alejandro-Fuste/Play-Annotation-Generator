# Play-Annotation-Generator Annotation Review — OutsideZoneStretch_1

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `OutsideZoneStretch_1`
- **Frame Range:** 0 to 299 (300 total frames)
- **Play:** `Play_Run_OutsideZoneStretch`
- **Result:** `Result_OutOfBounds`
- **Result Frame:** 299
- **Player Tracks:** 39
- **Ball Tracks:** 0
- **Action Segments:** 142
- **Validation Warnings:** 169
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 16
- **Exact Matches:** 3
- **Group Expanded Events:** 9
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 1
- **Ambiguous Matches:** 2
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 116
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `4` | `Group` |
| ✅ EXACT | `Action_ZoneBlock` | LT | offense | `12` | `12` |
| ✅ EXACT | `Action_ZoneBlock` | RG | offense | `14` | `14` |
| ❌ MISSING SEGMENT | `Action_ZoneBlock` | LG | offense | `17` | `17` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | offense | `18` | `18` |
| ✅ EXACT | `Action_PressEdge` | QB | offense | `4` | `4` |
| ⚠️ AMBIGUOUS MATCH | `Action_Handoff` | CB2 | defense | `2` | `2` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `0` | `Group` | 0 | START | 0 | 145 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `1` | `Group` | 0 | START | 0 | 278 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | `10` | `Group` | 0 | START | 0 | 88 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `12` | `Group` | 0 | START | 0 | 69 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `14` | `Group` | 0 | START | 0 | 69 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | `16` | `Group` | 0 | START | 0 | 88 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `17` | `Group` | 0 | START | 0 | 68 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `18` | `Group` | 0 | START | 0 | 69 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `4` | `Group` | 0 | START | 0 | 72 |
| ✅ EXACT | `Action_ZoneBlock` | LT | `12` | `12` | 70 | START | 70 | 83 |
| ✅ EXACT | `Action_ZoneBlock` | RG | `14` | `14` | 70 | START | 70 | 74 |
| ❌ MISSING SEGMENT | `Action_ZoneBlock` | LG | `17` | `17` | 70 | START | N/A | N/A |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | `18` | `18` | 70 | START | 70 | 78 |
| ✅ EXACT | `Action_PressEdge` | QB | `4` | `4` | 73 | START | 73 | 131 |
| ⚠️ AMBIGUOUS MATCH | `Action_Handoff` | CB2 | `2` | `2` | 87 | START | 87 | 89 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 300

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 72 | 73 | inferred_complete_timeline |
| `Action_PressEdge` | 73 | 131 | 59 | inferred_complete_timeline |
| `Action_None` | 132 | 299 | 168 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 296

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 278 | 279 | inferred_complete_timeline |
| `Action_PreSnap` | 283 | 299 | 17 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 263

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 145 | 146 | inferred_complete_timeline |
| `Action_PreSnap` | 172 | 182 | 11 | inferred_complete_timeline |
| `Action_PreSnap` | 194 | 299 | 106 | inferred_complete_timeline |

</details>

<details>
<summary>TE1 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–286
- **Visible Samples:** 203

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 88 | 89 | inferred_complete_timeline |
| `Action_PreSnap` | 145 | 146 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 148 | 149 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 152 | 240 | 89 | inferred_complete_timeline |
| `Action_PreSnap` | 259 | 262 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 266 | 271 | 6 | inferred_complete_timeline |
| `Action_PreSnap` | 276 | 286 | 11 | inferred_complete_timeline |

</details>

<details>
<summary>TE2 — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 293

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 88 | 89 | inferred_complete_timeline |
| `Action_PreSnap` | 92 | 163 | 72 | inferred_complete_timeline |
| `Action_PreSnap` | 167 | 296 | 130 | inferred_complete_timeline |
| `Action_PreSnap` | 298 | 299 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–133
- **Visible Samples:** 113

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 69 | 70 | inferred_complete_timeline |
| `Action_ZoneBlock` | 70 | 83 | 14 | inferred_complete_timeline |
| `Action_None` | 84 | 85 | 2 | inferred_complete_timeline |
| `Action_None` | 93 | 104 | 12 | inferred_complete_timeline |
| `Action_None` | 119 | 133 | 15 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–68
- **Visible Samples:** 69

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 68 | 69 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 247

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 69 | 70 | inferred_complete_timeline |
| `Action_ZoneBlock` | 70 | 74 | 5 | inferred_complete_timeline |
| `Action_None` | 88 | 90 | 3 | inferred_complete_timeline |
| `Action_None` | 106 | 161 | 56 | inferred_complete_timeline |
| `Action_None` | 163 | 232 | 70 | inferred_complete_timeline |
| `Action_None` | 236 | 240 | 5 | inferred_complete_timeline |
| `Action_None` | 247 | 254 | 8 | inferred_complete_timeline |
| `Action_None` | 267 | 268 | 2 | inferred_complete_timeline |
| `Action_None` | 270 | 276 | 7 | inferred_complete_timeline |
| `Action_None` | 278 | 288 | 11 | inferred_complete_timeline |
| `Action_None` | 290 | 299 | 10 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–93
- **Visible Samples:** 92

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 69 | 70 | inferred_complete_timeline |
| `Action_ZoneBlock` | 70 | 78 | 9 | inferred_complete_timeline |
| `Action_ZoneBlock` | 80 | 82 | 3 | inferred_complete_timeline |
| `Action_None` | 84 | 93 | 10 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 257

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 128 | 129 | inferred_complete_timeline |
| `Action_PreSnap` | 138 | 215 | 78 | inferred_complete_timeline |
| `Action_PreSnap` | 218 | 230 | 13 | inferred_complete_timeline |
| `Action_PreSnap` | 236 | 238 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 266 | 299 | 34 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 291

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 109 | 110 | inferred_complete_timeline |
| `Action_PreSnap` | 117 | 138 | 22 | inferred_complete_timeline |
| `Action_PreSnap` | 141 | 299 | 159 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–149
- **Visible Samples:** 149

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 146 | 147 | inferred_complete_timeline |
| `Action_PreSnap` | 148 | 149 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–201
- **Visible Samples:** 200

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 161 | 162 | inferred_complete_timeline |
| `Action_PreSnap` | 163 | 197 | 35 | inferred_complete_timeline |
| `Action_PreSnap` | 199 | 201 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 286

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 221 | 222 | inferred_complete_timeline |
| `Action_PreSnap` | 223 | 227 | 5 | inferred_complete_timeline |
| `Action_PreSnap` | 230 | 234 | 5 | inferred_complete_timeline |
| `Action_PreSnap` | 244 | 254 | 11 | inferred_complete_timeline |
| `Action_PreSnap` | 257 | 299 | 43 | inferred_complete_timeline |

</details>

<details>
<summary>OLB — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 300

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 299 | 300 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 300

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 299 | 300 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 256

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 86 | 87 | inferred_complete_timeline |
| `Action_Handoff` | 87 | 89 | 3 | inferred_complete_timeline |
| `Action_Handoff` | 92 | 95 | 4 | inferred_complete_timeline |
| `Action_None` | 96 | 120 | 25 | inferred_complete_timeline |
| `Action_None` | 127 | 139 | 13 | inferred_complete_timeline |
| `Action_None` | 146 | 269 | 124 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–296
- **Visible Samples:** 287

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 284 | 285 | inferred_complete_timeline |
| `Action_PreSnap` | 295 | 296 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–192
- **Visible Samples:** 193

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 192 | 193 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `8` | `8` | Position_Unknown | Team_Unknown | 0–299 | 290 | 2 | Undefined position; Undefined team |
| `20` | `22` | Position_Unknown | Team_Unknown | 8–134 | 111 | 2 | Undefined position; Undefined team |
| `21` | `23` | Position_Unknown | Team_Unknown | 14–73 | 56 | 2 | Undefined position; Undefined team |
| `22` | `24` | Position_Unknown | Team_Unknown | 25–299 | 247 | 7 | Undefined position; Undefined team |
| `23` | `25` | Position_Unknown | Team_Unknown | 103–298 | 88 | 18 | Undefined position; Undefined team |
| `24` | `27` | Position_Unknown | Team_Unknown | 108–299 | 118 | 8 | Undefined position; Undefined team |
| `25` | `28` | Position_Unknown | Team_Unknown | 109–111 | 3 | 1 | Undefined position; Undefined team |
| `26` | `33` | Position_Unknown | Team_Unknown | 172–299 | 94 | 6 | Undefined position; Undefined team |
| `27` | `34` | Position_Unknown | Team_Unknown | 176–260 | 56 | 7 | Undefined position; Undefined team |
| `28` | `36` | Position_Unknown | Team_Unknown | 181–182 | 2 | 1 | Undefined position; Undefined team |
| `29` | `37` | Position_Unknown | Team_Unknown | 183–184 | 2 | 1 | Undefined position; Undefined team |
| `30` | `38` | Position_Unknown | Team_Unknown | 187–299 | 106 | 2 | Undefined position; Undefined team |
| `31` | `40` | Position_Unknown | Team_Unknown | 198–200 | 3 | 1 | Undefined position; Undefined team |
| `32` | `41` | Position_Unknown | Team_Unknown | 203–288 | 79 | 4 | Undefined position; Undefined team |
| `33` | `42` | Position_Unknown | Team_Unknown | 207–240 | 32 | 2 | Undefined position; Undefined team |
| `34` | `43` | Position_Unknown | Team_Unknown | 210–224 | 14 | 2 | Undefined position; Undefined team |
| `35` | `44` | Position_Unknown | Team_Unknown | 224–239 | 6 | 3 | Undefined position; Undefined team |
| `36` | `45` | Position_Unknown | Team_Unknown | 225–228 | 4 | 1 | Undefined position; Undefined team |
| `37` | `46` | Position_Unknown | Team_Unknown | 273–299 | 27 | 1 | Undefined position; Undefined team |
| `38` | `48` | Position_Unknown | Team_Unknown | 280–299 | 19 | 2 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ❌ Missing segment for action `Action_ZoneBlock` on target `17` (LG)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `18` (2 segments found)
- ⚠️ Ambiguous match for action `Action_Handoff` and target `2` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `5` (actor_track_id `5`): `SAF` position mapped to `defense` team
- ⚠️ Player track XML ID `7` (actor_track_id `7`): `SAF` position mapped to `defense` team
- ⚠️ 20 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 20 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 40 |
| Missing visible bounding boxes during action | 124 |
| Track-related warning | 4 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 4: Duplicate assignment for track ID '7' in grid. Overwriting previous assignment.
- ⚠️ Row 4: Duplicate assignment for track ID '7' in grid. Overwriting previous assignment.
- ⚠️ Row 4: Duplicate assignment for track ID '2' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 299 as fallback play end.
- ⚠️ Segment 'Action_ZoneBlock' for track '17' has invalid range: start=70, end=68. Clamping end to start.
- ⚠️ Action 'Action_PreSnap' range [0-145] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [172-182] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-278] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_Handoff' range [87-89] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [96-120] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [127-139] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [146-269] for track '2' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PressEdge' range [73-131] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-284] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [295-296] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-146] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [148-149] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-192] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-256] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [267-299] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-221] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [223-227] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [230-234] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [244-254] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-88] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [145-146] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [148-149] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [152-240] for track '10' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [259-262] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [266-271] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [276-286] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-161] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [163-197] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [199-201] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [84-85] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [93-104] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [119-133] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-299] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-69] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [70-74] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [88-90] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [106-161] for track '14' has 6 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [163-232] for track '14' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [236-240] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [247-254] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [267-268] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [270-276] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [278-288] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-109] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [117-138] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-88] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [92-163] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [167-296] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-68] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [70-78] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [80-82] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [84-93] for track '18' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-128] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [138-215] for track '19' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [218-230] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [236-238] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [8-116] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [133-134] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [14-47] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [52-73] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [25-68] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [70-92] for track '22' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [94-98] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [106-124] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [126-137] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [151-160] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [103-110] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [115-118] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [168-169] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [172-177] for track '23' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [180-182] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [190-191] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [201-204] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [207-210] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [212-225] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [227-232] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [236-244] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [249-254] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [257-258] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [263-268] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [270-271] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [280-283] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [285-286] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [295-298] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [108-119] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [124-133] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [143-151] for track '24' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [160-238] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [273-275] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [277-278] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [284-285] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [109-111] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [172-217] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [224-226] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [228-244] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [251-254] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [268-272] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [281-299] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [176-177] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [184-209] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [218-219] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [224-225] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [227-244] for track '27' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [251-253] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [258-260] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [181-182] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [183-184] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [187-277] for track '30' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [285-299] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [198-200] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [203-232] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [235-268] for track '32' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [270-276] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [281-288] for track '32' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [207-232] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [235-240] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [210-220] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [222-224] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [224-225] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [228-229] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [238-239] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [225-228] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [273-299] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [280-288] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Player track '8' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '8' has undefined team_side. Will map to Team_Unknown.
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