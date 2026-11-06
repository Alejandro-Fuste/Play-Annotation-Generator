# Play-Annotation-Generator Annotation Review — OutsideZoneRead_96

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `OutsideZoneRead_96`
- **Frame Range:** 0 to 419 (420 total frames)
- **Play:** `Play_Run_OutsideZoneRead`
- **Result:** `Result_Tackle`
- **Result Frame:** 419
- **Player Tracks:** 46
- **Ball Tracks:** 0
- **Action Segments:** 82
- **Validation Warnings:** 121
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
- **Start-Frame Differences:** 3
- **Missing Segments:** 0
- **Ambiguous Matches:** 0
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 60
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `9` | `Group` |
| ⚠️ START CHANGED | `Action_ZoneBlock` | RG | offense | `12` | `12` |
| ✅ EXACT | `Action_ZoneBlock` | C | offense | `19` | `19` |
| ⚠️ START CHANGED | `Action_ZoneBlock` | LG | offense | `20` | `20` |
| ✅ EXACT | `Action_ZoneBlock` | RT | offense | `21` | `21` |
| ✅ EXACT | `Action_ZoneBlock` | LT | offense | `5` | `5` |
| ✅ EXACT | `Action_PressEdge` | DE1 | defense | `14` | `14` |
| ⚠️ START CHANGED | `Action_ReadEdgeDefender` | RG | offense | `12` | `12` |
| ✅ EXACT | `Action_Handoff` | RG | offense | `12` | `12` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `0` | `Group` | 0 | START | 0 | 294 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `1` | `Group` | 0 | START | 0 | 259 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `12` | `Group` | 0 | START | 0 | 135 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | `18` | `Group` | 0 | START | 0 | 256 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `19` | `Group` | 0 | START | 0 | 125 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | `2` | `Group` | 0 | START | 0 | 248 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `20` | `Group` | 0 | START | 0 | 135 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `21` | `Group` | 0 | START | 0 | 138 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `3` | `Group` | 0 | START | 0 | 244 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `5` | `Group` | 0 | START | 0 | 138 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `9` | `Group` | 0 | START | 0 | 183 |
| ⚠️ START CHANGED | `Action_ZoneBlock` | RG | `12` | `12` | 139 | START | 145 | 147 |
| ✅ EXACT | `Action_ZoneBlock` | C | `19` | `19` | 139 | START | 139 | 184 |
| ⚠️ START CHANGED | `Action_ZoneBlock` | LG | `20` | `20` | 139 | START | 140 | 184 |
| ✅ EXACT | `Action_ZoneBlock` | RT | `21` | `21` | 139 | START | 139 | 184 |
| ✅ EXACT | `Action_ZoneBlock` | LT | `5` | `5` | 139 | START | 139 | 184 |
| ✅ EXACT | `Action_PressEdge` | DE1 | `14` | `14` | 141 | START | 141 | 141 |
| ⚠️ START CHANGED | `Action_ReadEdgeDefender` | RG | `12` | `12` | 149 | START | 150 | 156 |
| ✅ EXACT | `Action_Handoff` | RG | `12` | `12` | 157 | START | 157 | 158 |

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
- **Visible Frames:** 0–294
- **Visible Samples:** 294

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 183 | 184 | inferred_complete_timeline |
| `Action_PreSnap` | 185 | 294 | 110 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–244
- **Visible Samples:** 245

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 244 | 245 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–321
- **Visible Samples:** 311

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 294 | 295 | inferred_complete_timeline |
| `Action_PreSnap` | 306 | 321 | 16 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–259
- **Visible Samples:** 260

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 259 | 260 | inferred_complete_timeline |

</details>

<details>
<summary>TE1 — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–256
- **Visible Samples:** 257

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 256 | 257 | inferred_complete_timeline |

</details>

<details>
<summary>TE2 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–248
- **Visible Samples:** 249

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 248 | 249 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–256
- **Visible Samples:** 257

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 138 | 139 | inferred_complete_timeline |
| `Action_ZoneBlock` | 139 | 184 | 46 | inferred_complete_timeline |
| `Action_None` | 185 | 256 | 72 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–225
- **Visible Samples:** 222

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 135 | 136 | inferred_complete_timeline |
| `Action_ZoneBlock` | 140 | 184 | 45 | inferred_complete_timeline |
| `Action_None` | 185 | 225 | 41 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–237
- **Visible Samples:** 234

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 125 | 126 | inferred_complete_timeline |
| `Action_PreSnap` | 130 | 138 | 9 | inferred_complete_timeline |
| `Action_ZoneBlock` | 139 | 184 | 46 | inferred_complete_timeline |
| `Action_None` | 185 | 237 | 53 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–158
- **Visible Samples:** 148

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 135 | 136 | inferred_complete_timeline |
| `Action_ZoneBlock` | 145 | 147 | 3 | inferred_complete_timeline |
| `Action_ReadEdgeDefender` | 150 | 156 | 7 | inferred_complete_timeline |
| `Action_Handoff` | 157 | 158 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `21`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–247
- **Visible Samples:** 248

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 138 | 139 | inferred_complete_timeline |
| `Action_ZoneBlock` | 139 | 184 | 46 | inferred_complete_timeline |
| `Action_None` | 185 | 247 | 63 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–141
- **Visible Samples:** 142

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 140 | 141 | inferred_complete_timeline |
| `Action_PressEdge` | 141 | 141 | 1 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–256
- **Visible Samples:** 255

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 159 | 160 | inferred_complete_timeline |
| `Action_PreSnap` | 162 | 256 | 95 | inferred_complete_timeline |

</details>

<details>
<summary>DT — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–302
- **Visible Samples:** 301

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 193 | 194 | inferred_complete_timeline |
| `Action_PreSnap` | 196 | 302 | 107 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–250
- **Visible Samples:** 239

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 191 | 192 | inferred_complete_timeline |
| `Action_PreSnap` | 193 | 198 | 6 | inferred_complete_timeline |
| `Action_PreSnap` | 210 | 250 | 41 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–294
- **Visible Samples:** 292

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 237 | 238 | inferred_complete_timeline |
| `Action_PreSnap` | 241 | 294 | 54 | inferred_complete_timeline |

</details>

<details>
<summary>OLB1 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–309
- **Visible Samples:** 299

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 294 | 295 | inferred_complete_timeline |
| `Action_PreSnap` | 306 | 309 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>OLB2 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–259
- **Visible Samples:** 249

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 169 | 170 | inferred_complete_timeline |
| `Action_PreSnap` | 178 | 187 | 10 | inferred_complete_timeline |
| `Action_PreSnap` | 191 | 259 | 69 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–294
- **Visible Samples:** 295

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 294 | 295 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 0–294
- **Visible Samples:** 292

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 191 | 192 | inferred_complete_timeline |
| `Action_PreSnap` | 195 | 294 | 100 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–419
- **Visible Samples:** 375

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 294 | 295 | inferred_complete_timeline |
| `Action_PreSnap` | 340 | 419 | 80 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–201
- **Visible Samples:** 202

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 201 | 202 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `22` | `22` | Position_Unknown | Team_Unknown | 144–231 | 80 | 2 | Undefined position; Undefined team |
| `23` | `25` | Position_Unknown | Team_Unknown | 157–237 | 81 | 1 | Undefined position; Undefined team |
| `24` | `26` | Position_Unknown | Team_Unknown | 168–169 | 2 | 1 | Undefined position; Undefined team |
| `25` | `27` | Position_Unknown | Team_Unknown | 169–170 | 2 | 1 | Undefined position; Undefined team |
| `26` | `29` | Position_Unknown | Team_Unknown | 173–180 | 8 | 1 | Undefined position; Undefined team |
| `27` | `30` | Position_Unknown | Team_Unknown | 176–192 | 9 | 2 | Undefined position; Undefined team |
| `28` | `31` | Position_Unknown | Team_Unknown | 196–202 | 7 | 1 | Undefined position; Undefined team |
| `29` | `33` | Position_Unknown | Team_Unknown | 219–412 | 153 | 2 | Undefined position; Undefined team |
| `30` | `38` | Position_Unknown | Team_Unknown | 295–405 | 81 | 6 | Undefined position; Undefined team |
| `31` | `39` | Position_Unknown | Team_Unknown | 295–419 | 90 | 2 | Undefined position; Undefined team |
| `32` | `40` | Position_Unknown | Team_Unknown | 295–383 | 89 | 1 | Undefined position; Undefined team |
| `33` | `41` | Position_Unknown | Team_Unknown | 295–336 | 42 | 1 | Undefined position; Undefined team |
| `34` | `42` | Position_Unknown | Team_Unknown | 295–302 | 8 | 1 | Undefined position; Undefined team |
| `35` | `43` | Position_Unknown | Team_Unknown | 295–302 | 8 | 1 | Undefined position; Undefined team |
| `36` | `44` | Position_Unknown | Team_Unknown | 295–296 | 2 | 1 | Undefined position; Undefined team |
| `37` | `48` | Position_Unknown | Team_Unknown | 303–306 | 4 | 1 | Undefined position; Undefined team |
| `38` | `49` | Position_Unknown | Team_Unknown | 303–321 | 17 | 2 | Undefined position; Undefined team |
| `39` | `50` | Position_Unknown | Team_Unknown | 303–320 | 6 | 2 | Undefined position; Undefined team |
| `40` | `51` | Position_Unknown | Team_Unknown | 303–306 | 4 | 1 | Undefined position; Undefined team |
| `41` | `53` | Position_Unknown | Team_Unknown | 307–319 | 13 | 1 | Undefined position; Undefined team |
| `42` | `55` | Position_Unknown | Team_Unknown | 307–310 | 4 | 1 | Undefined position; Undefined team |
| `43` | `59` | Position_Unknown | Team_Unknown | 363–419 | 57 | 1 | Undefined position; Undefined team |
| `44` | `60` | Position_Unknown | Team_Unknown | 364–385 | 22 | 1 | Undefined position; Undefined team |
| `45` | `63` | Position_Unknown | Team_Unknown | 418–419 | 2 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ `Action_ZoneBlock` for actor_track_id `12` (RG): Annotated start 139 != Inferred start 145
- ⚠️ `Action_ZoneBlock` for actor_track_id `20` (LG): Annotated start 139 != Inferred start 140
- ⚠️ `Action_ReadEdgeDefender` for actor_track_id `12` (RG): Annotated start 149 != Inferred start 150

### Track Identity Issues

- ⚠️ Player track XML ID `10` (actor_track_id `10`): `SAF` position mapped to `defense` team
- ⚠️ 24 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 24 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 48 |
| Missing visible bounding boxes during action | 72 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 419 as fallback play end.
- ⚠️ Action 'Action_PreSnap' range [0-294] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [306-321] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-259] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-248] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-244] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-294] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [306-309] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [185-256] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-169] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [178-187] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [191-259] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-191] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [193-198] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [210-250] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-294] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-183] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [185-294] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-201] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-237] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [241-294] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-135] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [145-147] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_Handoff' range [157-158] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-294] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PressEdge' for track '14' starts at frame 141, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_PressEdge' range [141-141] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-193] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [196-302] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-159] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [162-256] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-191] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [195-294] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-256] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-125] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [139-184] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [185-237] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-135] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [140-184] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [185-225] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [185-247] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [144-187] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [196-231] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [157-237] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [168-169] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [169-170] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [173-180] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [176-182] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [191-192] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [196-202] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [219-294] for track '29' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [336-412] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [295-302] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [321-379] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [384-385] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [387-388] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [390-392] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [399-405] for track '30' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [295-302] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [295-383] for track '32' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [295-336] for track '33' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [295-302] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [295-302] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [295-296] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [303-306] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [303-306] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [309-321] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [303-306] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [319-320] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [303-306] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [307-319] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [307-310] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [364-385] for track '44' has 1 frames without a visible bounding box.
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
- ⚠️ Player track '44' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '44' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '45' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '45' has undefined team_side. Will map to Team_Unknown.

</details>