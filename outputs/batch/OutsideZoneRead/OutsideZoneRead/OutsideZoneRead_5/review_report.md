# Play-Annotation-Generator Annotation Review — OutsideZoneRead_5

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `OutsideZoneRead_5`
- **Frame Range:** 0 to 329 (330 total frames)
- **Play:** `Play_Run_OutsideZoneRead`
- **Result:** `Result_OutOfBounds`
- **Result Frame:** 329
- **Player Tracks:** 33
- **Ball Tracks:** 0
- **Action Segments:** 94
- **Validation Warnings:** 102
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 20
- **Exact Matches:** 5
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 3
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 74
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `7` | `Group` |
| ✅ EXACT | `Action_PressEdge` | RB | offense | `7` | `7` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | offense | `17` | `17` |
| ✅ EXACT | `Action_ZoneBlock` | RG | offense | `18` | `18` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | offense | `19` | `19` |
| ✅ EXACT | `Action_ZoneBlock` | RT | offense | `21` | `21` |
| ✅ EXACT | `Action_ZoneBlock` | LT | offense | `6` | `6` |
| ✅ EXACT | `Action_ReadEdgeDefender` | QB | offense | `16` | `16` |
| ⚠️ AMBIGUOUS MATCH | `Action_Keep` | QB | offense | `16` | `16` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `0` | `Group` | 0 | START | 0 | 247 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `1` | `Group` | 0 | START | 0 | 217 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `12` | `Group` | 0 | START | 0 | 187 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `16` | `Group` | 0 | START | 0 | 75 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `17` | `Group` | 0 | START | 0 | 58 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `18` | `Group` | 0 | START | 0 | 58 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `19` | `Group` | 0 | START | 0 | 56 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `21` | `Group` | 0 | START | 0 | 58 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `4` | `Group` | 0 | START | 0 | 222 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `6` | `Group` | 0 | START | 0 | 58 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `7` | `Group` | 0 | START | 0 | 58 |
| ✅ EXACT | `Action_PressEdge` | RB | `7` | `7` | 59 | START | 59 | 111 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | `17` | `17` | 59 | START | 59 | 89 |
| ✅ EXACT | `Action_ZoneBlock` | RG | `18` | `18` | 59 | START | 59 | 119 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | `19` | `19` | 59 | START | 59 | 82 |
| ✅ EXACT | `Action_ZoneBlock` | RT | `21` | `21` | 59 | START | 59 | 90 |
| ✅ EXACT | `Action_ZoneBlock` | LT | `6` | `6` | 59 | START | 59 | 89 |
| ✅ EXACT | `Action_ReadEdgeDefender` | QB | `16` | `16` | 76 | START | 76 | 85 |
| ⚠️ AMBIGUOUS MATCH | `Action_Keep` | QB | `16` | `16` | 88 | START | 88 | 300 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–329
- **Visible Samples:** 329

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 75 | 76 | inferred_complete_timeline |
| `Action_ReadEdgeDefender` | 76 | 85 | 10 | inferred_complete_timeline |
| `Action_None` | 86 | 87 | 2 | inferred_complete_timeline |
| `Action_Keep` | 88 | 300 | 213 | inferred_complete_timeline |
| `Action_Keep` | 302 | 329 | 28 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–214
- **Visible Samples:** 215

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 58 | 59 | inferred_complete_timeline |
| `Action_PressEdge` | 59 | 111 | 53 | inferred_complete_timeline |
| `Action_None` | 112 | 214 | 103 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–247
- **Visible Samples:** 248

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 247 | 248 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–217
- **Visible Samples:** 218

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 217 | 218 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–222
- **Visible Samples:** 223

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 222 | 223 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–187
- **Visible Samples:** 188

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 187 | 188 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–89
- **Visible Samples:** 90

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 58 | 59 | inferred_complete_timeline |
| `Action_ZoneBlock` | 59 | 89 | 31 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–208
- **Visible Samples:** 193

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 58 | 59 | inferred_complete_timeline |
| `Action_ZoneBlock` | 59 | 89 | 31 | inferred_complete_timeline |
| `Action_ZoneBlock` | 91 | 92 | 2 | inferred_complete_timeline |
| `Action_ZoneBlock` | 97 | 109 | 13 | inferred_complete_timeline |
| `Action_ZoneBlock` | 117 | 118 | 2 | inferred_complete_timeline |
| `Action_None` | 123 | 208 | 86 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–108
- **Visible Samples:** 90

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 56 | 57 | inferred_complete_timeline |
| `Action_PreSnap` | 58 | 58 | 1 | inferred_complete_timeline |
| `Action_ZoneBlock` | 59 | 82 | 24 | inferred_complete_timeline |
| `Action_ZoneBlock` | 84 | 85 | 2 | inferred_complete_timeline |
| `Action_ZoneBlock` | 100 | 103 | 4 | inferred_complete_timeline |
| `Action_ZoneBlock` | 107 | 108 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–208
- **Visible Samples:** 209

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 58 | 59 | inferred_complete_timeline |
| `Action_ZoneBlock` | 59 | 119 | 61 | inferred_complete_timeline |
| `Action_None` | 120 | 208 | 89 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `21`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–90
- **Visible Samples:** 91

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 58 | 59 | inferred_complete_timeline |
| `Action_ZoneBlock` | 59 | 90 | 32 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–221
- **Visible Samples:** 216

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 161 | 162 | inferred_complete_timeline |
| `Action_PreSnap` | 164 | 171 | 8 | inferred_complete_timeline |
| `Action_PreSnap` | 175 | 176 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 178 | 221 | 44 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–153
- **Visible Samples:** 149

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 125 | 126 | inferred_complete_timeline |
| `Action_PreSnap` | 128 | 140 | 13 | inferred_complete_timeline |
| `Action_PreSnap` | 142 | 149 | 8 | inferred_complete_timeline |
| `Action_PreSnap` | 152 | 153 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `defense`
- **Visible Frames:** 0–214
- **Visible Samples:** 210

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 87 | 88 | inferred_complete_timeline |
| `Action_PreSnap` | 90 | 172 | 83 | inferred_complete_timeline |
| `Action_PreSnap` | 176 | 214 | 39 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–236
- **Visible Samples:** 227

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 89 | 90 | inferred_complete_timeline |
| `Action_PreSnap` | 99 | 159 | 61 | inferred_complete_timeline |
| `Action_PreSnap` | 161 | 236 | 76 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–255
- **Visible Samples:** 256

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 255 | 256 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–219
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 124 | 125 | inferred_complete_timeline |
| `Action_PreSnap` | 127 | 133 | 7 | inferred_complete_timeline |
| `Action_PreSnap` | 139 | 164 | 26 | inferred_complete_timeline |
| `Action_PreSnap` | 166 | 216 | 51 | inferred_complete_timeline |
| `Action_PreSnap` | 218 | 219 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–253
- **Visible Samples:** 254

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 253 | 254 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 327

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 286 | 287 | inferred_complete_timeline |
| `Action_PreSnap` | 289 | 309 | 21 | inferred_complete_timeline |
| `Action_PreSnap` | 311 | 329 | 19 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–194
- **Visible Samples:** 195

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 194 | 195 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–327
- **Visible Samples:** 324

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 299 | 300 | inferred_complete_timeline |
| `Action_PreSnap` | 304 | 327 | 24 | inferred_complete_timeline |

</details>

<details>
<summary>SAF3 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–275
- **Visible Samples:** 276

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 275 | 276 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `22` | `22` | Position_Unknown | Team_Unknown | 26–117 | 37 | 4 | Undefined position; Undefined team |
| `23` | `24` | Position_Unknown | Team_Unknown | 69–213 | 119 | 5 | Undefined position; Undefined team |
| `24` | `27` | Position_Unknown | Team_Unknown | 86–226 | 130 | 5 | Undefined position; Undefined team |
| `25` | `30` | Position_Unknown | Team_Unknown | 97–171 | 21 | 7 | Undefined position; Undefined team |
| `26` | `31` | Position_Unknown | Team_Unknown | 99–194 | 85 | 2 | Undefined position; Undefined team |
| `27` | `34` | Position_Unknown | Team_Unknown | 144–145 | 2 | 1 | Undefined position; Undefined team |
| `28` | `35` | Position_Unknown | Team_Unknown | 158–199 | 30 | 5 | Undefined position; Undefined team |
| `29` | `38` | Position_Unknown | Team_Unknown | 199–208 | 5 | 2 | Undefined position; Undefined team |
| `30` | `39` | Position_Unknown | Team_Unknown | 212–221 | 9 | 2 | Undefined position; Undefined team |
| `31` | `45` | Position_Unknown | Team_Unknown | 283–329 | 47 | 1 | Undefined position; Undefined team |
| `32` | `54` | Position_Unknown | Team_Unknown | 316–329 | 14 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `17` (4 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `19` (4 segments found)
- ⚠️ Ambiguous match for action `Action_Keep` and target `16` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `10` (actor_track_id `10`): `SAF3` position mapped to `defense` team
- ⚠️ Player track XML ID `14` (actor_track_id `14`): `SAF1` position mapped to `defense` team
- ⚠️ Player track XML ID `15` (actor_track_id `15`): `SAF2` position mapped to `defense` team
- ⚠️ 11 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 11 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 22 |
| Missing visible bounding boxes during action | 79 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 329 as fallback play end.
- ⚠️ Action 'Action_PreSnap' range [0-247] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-217] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-255] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-253] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-222] for track '4' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-89] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [99-159] for track '5' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [161-236] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [59-89] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [112-214] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-286] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [289-309] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-124] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [127-133] for track '9' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [139-164] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [166-216] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [218-219] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-275] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-161] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [164-171] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [175-176] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [178-221] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-187] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-125] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [128-140] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [142-149] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [152-153] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-194] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-299] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [304-327] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_Keep' range [88-300] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [59-89] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [91-92] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [97-109] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [117-118] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [123-208] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [120-208] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-56] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [59-82] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [84-85] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [100-103] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [107-108] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-87] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [90-172] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [176-214] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [59-90] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [26-38] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [92-105] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [107-112] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [114-117] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [69-70] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [88-129] for track '23' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [132-133] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [135-136] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [143-213] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [86-89] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [92-101] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [103-123] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [131-139] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [141-226] for track '24' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [97-98] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [103-104] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [128-129] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [137-140] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [146-147] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [158-163] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [169-171] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [99-100] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [112-194] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [144-145] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [158-159] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [161-163] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [166-169] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [178-185] for track '28' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [187-199] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [199-201] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [207-208] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [212-216] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [218-221] for track '30' has 1 frames without a visible bounding box.
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

</details>