# Play-Annotation-Generator Annotation Review — OutsideZoneRead_34

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `OutsideZoneRead_34`
- **Frame Range:** 0 to 329 (330 total frames)
- **Play:** `Play_Run_OutsideZoneRead`
- **Result:** `Result_OutOfBounds`
- **Result Frame:** 329
- **Player Tracks:** 47
- **Ball Tracks:** 0
- **Action Segments:** 105
- **Validation Warnings:** 144
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 18
- **Exact Matches:** 8
- **Group Expanded Events:** 9
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 0
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 88
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB2 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB1 | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `9` | `Group` |
| ✅ EXACT | `Action_ZoneBlock` | RT | offense | `16` | `16` |
| ✅ EXACT | `Action_ZoneBlock` | LT | offense | `4` | `4` |
| ✅ EXACT | `Action_ZoneBlock` | LG | offense | `5` | `5` |
| ✅ EXACT | `Action_ZoneBlock` | RG | offense | `7` | `7` |
| ✅ EXACT | `Action_ZoneBlock` | C | offense | `9` | `9` |
| ✅ EXACT | `Action_PressEdge` | RB1 | offense | `3` | `3` |
| ✅ EXACT | `Action_ReadEdgeDefender` | QB | offense | `10` | `10` |
| ✅ EXACT | `Action_Handoff` | QB | offense | `10` | `10` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB2 | `1` | `Group` | 0 | START | 0 | 224 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `10` | `Group` | 0 | START | 0 | 115 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `15` | `Group` | 0 | START | 0 | 329 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `16` | `Group` | 0 | START | 0 | 99 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB1 | `3` | `Group` | 0 | START | 0 | 106 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `4` | `Group` | 0 | START | 0 | 99 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `5` | `Group` | 0 | START | 0 | 99 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `7` | `Group` | 0 | START | 0 | 99 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `9` | `Group` | 0 | START | 0 | 99 |
| ✅ EXACT | `Action_ZoneBlock` | RT | `16` | `16` | 100 | START | 100 | 133 |
| ✅ EXACT | `Action_ZoneBlock` | LT | `4` | `4` | 100 | START | 100 | 133 |
| ✅ EXACT | `Action_ZoneBlock` | LG | `5` | `5` | 100 | START | 100 | 133 |
| ✅ EXACT | `Action_ZoneBlock` | RG | `7` | `7` | 100 | START | 100 | 133 |
| ✅ EXACT | `Action_ZoneBlock` | C | `9` | `9` | 100 | START | 100 | 133 |
| ✅ EXACT | `Action_PressEdge` | RB1 | `3` | `3` | 107 | START | 107 | 128 |
| ✅ EXACT | `Action_ReadEdgeDefender` | QB | `10` | `10` | 116 | START | 116 | 125 |
| ✅ EXACT | `Action_Handoff` | QB | `10` | `10` | 126 | START | 126 | 138 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–185
- **Visible Samples:** 186

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 115 | 116 | inferred_complete_timeline |
| `Action_ReadEdgeDefender` | 116 | 125 | 10 | inferred_complete_timeline |
| `Action_Handoff` | 126 | 138 | 13 | inferred_complete_timeline |
| `Action_None` | 139 | 185 | 47 | inferred_complete_timeline |

</details>

<details>
<summary>RB1 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–128
- **Visible Samples:** 129

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 106 | 107 | inferred_complete_timeline |
| `Action_PressEdge` | 107 | 128 | 22 | inferred_complete_timeline |

</details>

<details>
<summary>RB2 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–224
- **Visible Samples:** 225

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 224 | 225 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–329
- **Visible Samples:** 330

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 329 | 330 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–256
- **Visible Samples:** 256

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 99 | 100 | inferred_complete_timeline |
| `Action_ZoneBlock` | 100 | 133 | 34 | inferred_complete_timeline |
| `Action_None` | 134 | 217 | 84 | inferred_complete_timeline |
| `Action_None` | 219 | 256 | 38 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–231
- **Visible Samples:** 232

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 99 | 100 | inferred_complete_timeline |
| `Action_ZoneBlock` | 100 | 133 | 34 | inferred_complete_timeline |
| `Action_None` | 134 | 231 | 98 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–220
- **Visible Samples:** 219

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 99 | 100 | inferred_complete_timeline |
| `Action_ZoneBlock` | 100 | 133 | 34 | inferred_complete_timeline |
| `Action_None` | 134 | 142 | 9 | inferred_complete_timeline |
| `Action_None` | 145 | 220 | 76 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–271
- **Visible Samples:** 272

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 99 | 100 | inferred_complete_timeline |
| `Action_ZoneBlock` | 100 | 133 | 34 | inferred_complete_timeline |
| `Action_None` | 134 | 271 | 138 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–205
- **Visible Samples:** 206

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 99 | 100 | inferred_complete_timeline |
| `Action_ZoneBlock` | 100 | 133 | 34 | inferred_complete_timeline |
| `Action_None` | 134 | 205 | 72 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–180
- **Visible Samples:** 159

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 101 | 102 | inferred_complete_timeline |
| `Action_PreSnap` | 124 | 180 | 57 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–108
- **Visible Samples:** 109

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 108 | 109 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `defense`
- **Visible Frames:** 0–204
- **Visible Samples:** 185

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 138 | 139 | inferred_complete_timeline |
| `Action_PreSnap` | 140 | 154 | 15 | inferred_complete_timeline |
| `Action_PreSnap` | 160 | 161 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 176 | 204 | 29 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–247
- **Visible Samples:** 244

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 221 | 222 | inferred_complete_timeline |
| `Action_PreSnap` | 223 | 231 | 9 | inferred_complete_timeline |
| `Action_PreSnap` | 235 | 247 | 13 | inferred_complete_timeline |

</details>

<details>
<summary>OLB1 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–326
- **Visible Samples:** 317

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 263 | 264 | inferred_complete_timeline |
| `Action_PreSnap` | 265 | 302 | 38 | inferred_complete_timeline |
| `Action_PreSnap` | 307 | 310 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 313 | 314 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 316 | 319 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 322 | 326 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>OLB2 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–186
- **Visible Samples:** 187

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 186 | 187 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 257

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 125 | 126 | inferred_complete_timeline |
| `Action_PreSnap` | 199 | 329 | 131 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 321

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 160 | 161 | inferred_complete_timeline |
| `Action_PreSnap` | 164 | 296 | 133 | inferred_complete_timeline |
| `Action_PreSnap` | 301 | 311 | 11 | inferred_complete_timeline |
| `Action_PreSnap` | 314 | 329 | 16 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `17` | `17` | Position_Unknown | Team_Unknown | 2–114 | 61 | 6 | Undefined position; Undefined team |
| `18` | `18` | Position_Unknown | Team_Unknown | 19–25 | 7 | 1 | Undefined position; Undefined team |
| `19` | `19` | Position_Unknown | Team_Unknown | 114–165 | 9 | 2 | Undefined position; Undefined team |
| `20` | `21` | Position_Unknown | Team_Unknown | 128–175 | 48 | 1 | Undefined position; Undefined team |
| `21` | `22` | Position_Unknown | Team_Unknown | 134–329 | 185 | 6 | Undefined position; Undefined team |
| `22` | `23` | Position_Unknown | Team_Unknown | 137–194 | 26 | 3 | Undefined position; Undefined team |
| `23` | `24` | Position_Unknown | Team_Unknown | 141–179 | 39 | 1 | Undefined position; Undefined team |
| `24` | `25` | Position_Unknown | Team_Unknown | 146–329 | 177 | 3 | Undefined position; Undefined team |
| `25` | `27` | Position_Unknown | Team_Unknown | 159–160 | 2 | 1 | Undefined position; Undefined team |
| `26` | `32` | Position_Unknown | Team_Unknown | 194–197 | 4 | 1 | Undefined position; Undefined team |
| `27` | `33` | Position_Unknown | Team_Unknown | 194–196 | 3 | 1 | Undefined position; Undefined team |
| `28` | `34` | Position_Unknown | Team_Unknown | 197–329 | 133 | 1 | Undefined position; Undefined team |
| `29` | `36` | Position_Unknown | Team_Unknown | 201–207 | 7 | 1 | Undefined position; Undefined team |
| `30` | `37` | Position_Unknown | Team_Unknown | 205–234 | 28 | 2 | Undefined position; Undefined team |
| `31` | `38` | Position_Unknown | Team_Unknown | 211–219 | 5 | 2 | Undefined position; Undefined team |
| `32` | `40` | Position_Unknown | Team_Unknown | 218–219 | 2 | 1 | Undefined position; Undefined team |
| `33` | `41` | Position_Unknown | Team_Unknown | 219–329 | 15 | 4 | Undefined position; Undefined team |
| `34` | `42` | Position_Unknown | Team_Unknown | 225–315 | 91 | 1 | Undefined position; Undefined team |
| `35` | `45` | Position_Unknown | Team_Unknown | 237–329 | 91 | 3 | Undefined position; Undefined team |
| `36` | `46` | Position_Unknown | Team_Unknown | 240–329 | 87 | 2 | Undefined position; Undefined team |
| `37` | `48` | Position_Unknown | Team_Unknown | 244–254 | 6 | 2 | Undefined position; Undefined team |
| `38` | `49` | Position_Unknown | Team_Unknown | 262–267 | 6 | 1 | Undefined position; Undefined team |
| `39` | `50` | Position_Unknown | Team_Unknown | 277–329 | 53 | 1 | Undefined position; Undefined team |
| `40` | `52` | Position_Unknown | Team_Unknown | 281–314 | 34 | 1 | Undefined position; Undefined team |
| `41` | `53` | Position_Unknown | Team_Unknown | 284–329 | 27 | 2 | Undefined position; Undefined team |
| `42` | `56` | Position_Unknown | Team_Unknown | 293–300 | 8 | 1 | Undefined position; Undefined team |
| `43` | `57` | Position_Unknown | Team_Unknown | 294–329 | 36 | 1 | Undefined position; Undefined team |
| `44` | `58` | Position_Unknown | Team_Unknown | 297–324 | 6 | 3 | Undefined position; Undefined team |
| `45` | `61` | Position_Unknown | Team_Unknown | 308–329 | 22 | 1 | Undefined position; Undefined team |
| `46` | `63` | Position_Unknown | Team_Unknown | 322–323 | 2 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

None.

### Track Identity Issues

- ⚠️ Player track XML ID `6` (actor_track_id `6`): `SAF2` position mapped to `defense` team
- ⚠️ Player track XML ID `14` (actor_track_id `14`): `SAF1` position mapped to `defense` team
- ⚠️ 30 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 30 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 60 |
| Missing visible bounding boxes during action | 83 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 329 as fallback play end.
- ⚠️ Action 'Action_PreSnap' range [0-138] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [140-154] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [160-161] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [176-204] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-224] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-221] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [223-231] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [235-247] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PressEdge' range [107-128] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [134-217] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [219-256] for track '4' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [134-231] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-160] for track '6' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [164-296] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [301-311] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [314-329] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [134-271] for track '7' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-263] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [265-302] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [307-310] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [313-314] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [316-319] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [322-326] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [134-142] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [145-220] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [139-185] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-108] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-101] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [124-180] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-186] for track '13' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-125] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [199-329] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [134-205] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [2-3] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [5-29] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [32-33] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [50-67] for track '17' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [100-107] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [109-114] for track '17' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [19-25] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [114-120] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [164-165] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [128-175] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [134-252] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [255-256] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [258-259] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [261-299] for track '21' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [302-307] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [137-139] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [162-171] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [182-194] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [141-179] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [146-178] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [183-271] for track '24' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [159-160] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [194-197] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [194-196] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [201-207] for track '29' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [205-229] for track '30' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [232-234] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [211-212] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [217-219] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [218-219] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [219-220] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [298-301] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [313-319] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [225-315] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [237-245] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [247-275] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [277-329] for track '35' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [240-317] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [321-329] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [244-247] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [253-254] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [262-267] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [281-314] for track '40' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [284-287] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [293-300] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [294-329] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [297-298] for track '44' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [301-302] for track '44' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [323-324] for track '44' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [322-323] for track '46' has 1 frames without a visible bounding box.
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
- ⚠️ Player track '46' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '46' has undefined team_side. Will map to Team_Unknown.

</details>