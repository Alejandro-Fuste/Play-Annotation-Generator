# Play-Annotation-Generator Annotation Review — OutsideZoneRead_87

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `OutsideZoneRead_87`
- **Frame Range:** 0 to 329 (330 total frames)
- **Play:** `Play_Run_OutsideZoneRead`
- **Result:** `Result_Touchdown`
- **Result Frame:** 329
- **Player Tracks:** 37
- **Ball Tracks:** 0
- **Action Segments:** 103
- **Validation Warnings:** 122
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 20
- **Exact Matches:** 8
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 0
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 76
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `8` | `Group` |
| ✅ EXACT | `Action_ZoneBlock` | RT | offense | `17` | `17` |
| ✅ EXACT | `Action_ZoneBlock` | LG | offense | `18` | `18` |
| ✅ EXACT | `Action_ZoneBlock` | LT | offense | `19` | `19` |
| ✅ EXACT | `Action_ZoneBlock` | RG | offense | `21` | `21` |
| ✅ EXACT | `Action_ZoneBlock` | C | offense | `8` | `8` |
| ✅ EXACT | `Action_PressEdge` | RB | offense | `7` | `7` |
| ✅ EXACT | `Action_ReadEdgeDefender` | QB | offense | `13` | `13` |
| ✅ EXACT | `Action_Handoff` | QB | offense | `13` | `13` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `0` | `Group` | 0 | START | 0 | 74 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `1` | `Group` | 0 | START | 0 | 166 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `13` | `Group` | 0 | START | 0 | 59 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `17` | `Group` | 0 | START | 0 | 51 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `18` | `Group` | 0 | START | 0 | 51 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `19` | `Group` | 0 | START | 0 | 51 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `21` | `Group` | 0 | START | 0 | 3 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `3` | `Group` | 0 | START | 0 | 191 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `6` | `Group` | 0 | START | 0 | 178 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `7` | `Group` | 0 | START | 0 | 56 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `8` | `Group` | 0 | START | 0 | 51 |
| ✅ EXACT | `Action_ZoneBlock` | RT | `17` | `17` | 52 | START | 52 | 91 |
| ✅ EXACT | `Action_ZoneBlock` | LG | `18` | `18` | 52 | START | 52 | 91 |
| ✅ EXACT | `Action_ZoneBlock` | LT | `19` | `19` | 52 | START | 52 | 91 |
| ✅ EXACT | `Action_ZoneBlock` | RG | `21` | `21` | 52 | START | 52 | 61 |
| ✅ EXACT | `Action_ZoneBlock` | C | `8` | `8` | 52 | START | 52 | 91 |
| ✅ EXACT | `Action_PressEdge` | RB | `7` | `7` | 57 | START | 57 | 91 |
| ✅ EXACT | `Action_ReadEdgeDefender` | QB | `13` | `13` | 60 | START | 60 | 66 |
| ✅ EXACT | `Action_Handoff` | QB | `13` | `13` | 71 | START | 71 | 77 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–163
- **Visible Samples:** 162

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 59 | 60 | inferred_complete_timeline |
| `Action_ReadEdgeDefender` | 60 | 66 | 7 | inferred_complete_timeline |
| `Action_None` | 69 | 70 | 2 | inferred_complete_timeline |
| `Action_Handoff` | 71 | 77 | 7 | inferred_complete_timeline |
| `Action_None` | 78 | 163 | 86 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–116
- **Visible Samples:** 117

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 56 | 57 | inferred_complete_timeline |
| `Action_PressEdge` | 57 | 91 | 35 | inferred_complete_timeline |
| `Action_None` | 92 | 116 | 25 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–222
- **Visible Samples:** 197

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 178 | 179 | inferred_complete_timeline |
| `Action_PreSnap` | 182 | 190 | 9 | inferred_complete_timeline |
| `Action_PreSnap` | 194 | 196 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 202 | 203 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 219 | 222 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–118
- **Visible Samples:** 117

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 74 | 75 | inferred_complete_timeline |
| `Action_PreSnap` | 77 | 118 | 42 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–166
- **Visible Samples:** 167

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 166 | 167 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–191
- **Visible Samples:** 192

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 191 | 192 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–221
- **Visible Samples:** 222

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 51 | 52 | inferred_complete_timeline |
| `Action_ZoneBlock` | 52 | 91 | 40 | inferred_complete_timeline |
| `Action_None` | 92 | 221 | 130 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–260
- **Visible Samples:** 219

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 51 | 52 | inferred_complete_timeline |
| `Action_ZoneBlock` | 52 | 91 | 40 | inferred_complete_timeline |
| `Action_None` | 92 | 196 | 105 | inferred_complete_timeline |
| `Action_None` | 211 | 215 | 5 | inferred_complete_timeline |
| `Action_None` | 219 | 222 | 4 | inferred_complete_timeline |
| `Action_None` | 225 | 229 | 5 | inferred_complete_timeline |
| `Action_None` | 240 | 241 | 2 | inferred_complete_timeline |
| `Action_None` | 252 | 254 | 3 | inferred_complete_timeline |
| `Action_None` | 258 | 260 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–215
- **Visible Samples:** 176

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 51 | 52 | inferred_complete_timeline |
| `Action_ZoneBlock` | 52 | 91 | 40 | inferred_complete_timeline |
| `Action_None` | 92 | 107 | 16 | inferred_complete_timeline |
| `Action_None` | 113 | 143 | 31 | inferred_complete_timeline |
| `Action_None` | 168 | 196 | 29 | inferred_complete_timeline |
| `Action_None` | 208 | 215 | 8 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `21`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–61
- **Visible Samples:** 54

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 3 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 7 | 13 | 7 | inferred_complete_timeline |
| `Action_PreSnap` | 16 | 33 | 18 | inferred_complete_timeline |
| `Action_PreSnap` | 37 | 51 | 15 | inferred_complete_timeline |
| `Action_ZoneBlock` | 52 | 61 | 10 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–252
- **Visible Samples:** 248

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 51 | 52 | inferred_complete_timeline |
| `Action_ZoneBlock` | 52 | 91 | 40 | inferred_complete_timeline |
| `Action_None` | 92 | 110 | 19 | inferred_complete_timeline |
| `Action_None` | 116 | 252 | 137 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–234
- **Visible Samples:** 232

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 87 | 88 | inferred_complete_timeline |
| `Action_PreSnap` | 90 | 141 | 52 | inferred_complete_timeline |
| `Action_PreSnap` | 143 | 234 | 92 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 210 | 211 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–271
- **Visible Samples:** 256

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 228 | 229 | inferred_complete_timeline |
| `Action_PreSnap` | 243 | 245 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 248 | 271 | 24 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `defense`
- **Visible Frames:** 0–275
- **Visible Samples:** 276

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 275 | 276 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–124
- **Visible Samples:** 112

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 92 | 93 | inferred_complete_timeline |
| `Action_PreSnap` | 101 | 117 | 17 | inferred_complete_timeline |
| `Action_PreSnap` | 123 | 124 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–326
- **Visible Samples:** 327

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 326 | 327 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–310
- **Visible Samples:** 311

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 310 | 311 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `5`</summary>

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
<summary>SAF1 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 287

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 196 | 197 | inferred_complete_timeline |
| `Action_PreSnap` | 200 | 203 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 215 | 247 | 33 | inferred_complete_timeline |
| `Action_PreSnap` | 254 | 255 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 260 | 266 | 7 | inferred_complete_timeline |
| `Action_PreSnap` | 268 | 269 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 275 | 277 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 279 | 298 | 20 | inferred_complete_timeline |
| `Action_PreSnap` | 301 | 303 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 310 | 315 | 6 | inferred_complete_timeline |
| `Action_PreSnap` | 319 | 324 | 6 | inferred_complete_timeline |
| `Action_PreSnap` | 326 | 329 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 328

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 258 | 259 | inferred_complete_timeline |
| `Action_PreSnap` | 260 | 299 | 40 | inferred_complete_timeline |
| `Action_PreSnap` | 301 | 329 | 29 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `9` | `9` | Position_Unknown | Team_Unknown | 0–235 | 236 | 1 | Undefined position; Undefined team |
| `22` | `23` | Position_Unknown | Team_Unknown | 9–10 | 2 | 1 | Undefined position; Undefined team |
| `23` | `26` | Position_Unknown | Team_Unknown | 68–272 | 199 | 2 | Undefined position; Undefined team |
| `24` | `30` | Position_Unknown | Team_Unknown | 126–281 | 155 | 2 | Undefined position; Undefined team |
| `25` | `31` | Position_Unknown | Team_Unknown | 127–204 | 78 | 1 | Undefined position; Undefined team |
| `26` | `32` | Position_Unknown | Team_Unknown | 137–138 | 2 | 1 | Undefined position; Undefined team |
| `27` | `33` | Position_Unknown | Team_Unknown | 140–266 | 127 | 1 | Undefined position; Undefined team |
| `28` | `35` | Position_Unknown | Team_Unknown | 181–256 | 53 | 8 | Undefined position; Undefined team |
| `29` | `41` | Position_Unknown | Team_Unknown | 246–247 | 2 | 1 | Undefined position; Undefined team |
| `30` | `42` | Position_Unknown | Team_Unknown | 254–284 | 25 | 3 | Undefined position; Undefined team |
| `31` | `43` | Position_Unknown | Team_Unknown | 267–269 | 3 | 1 | Undefined position; Undefined team |
| `32` | `44` | Position_Unknown | Team_Unknown | 275–277 | 3 | 1 | Undefined position; Undefined team |
| `33` | `45` | Position_Unknown | Team_Unknown | 279–281 | 3 | 1 | Undefined position; Undefined team |
| `34` | `46` | Position_Unknown | Team_Unknown | 282–284 | 3 | 1 | Undefined position; Undefined team |
| `35` | `47` | Position_Unknown | Team_Unknown | 287–329 | 38 | 4 | Undefined position; Undefined team |
| `36` | `48` | Position_Unknown | Team_Unknown | 303–305 | 3 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

None.

### Track Identity Issues

- ⚠️ Player track XML ID `11` (actor_track_id `11`): `SAF1` position mapped to `defense` team
- ⚠️ Player track XML ID `16` (actor_track_id `16`): `SAF2` position mapped to `defense` team
- ⚠️ 16 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 16 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 32 |
| Missing visible bounding boxes during action | 89 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 329 as fallback play end.
- ⚠️ Action 'Action_PreSnap' range [0-74] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [77-118] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-166] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-87] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [90-141] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [143-234] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-191] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-210] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-178] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [182-190] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [194-196] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [202-203] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [219-222] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [92-116] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [52-91] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [92-107] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [113-143] for track '8' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [168-196] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [208-215] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-235] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-92] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [101-117] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [123-124] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-196] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [200-203] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [215-247] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [254-255] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [260-266] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [268-269] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [275-277] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [279-298] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [301-303] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [310-315] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [319-324] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-326] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ReadEdgeDefender' range [60-66] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [78-163] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-310] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-228] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [243-245] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [248-271] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-258] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [260-299] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [301-329] for track '16' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [92-110] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [116-252] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [52-91] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [92-196] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [211-215] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [219-222] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [225-229] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [240-241] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [252-254] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [258-260] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [92-221] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-275] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-3] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [7-13] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [16-33] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [37-51] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [52-61] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [9-10] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [68-190] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [197-272] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [126-128] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [130-281] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [127-204] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [137-138] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [140-266] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [181-190] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [193-194] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [203-210] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [213-221] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [225-229] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [231-243] for track '28' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [247-248] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [253-256] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [246-247] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [254-260] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [262-264] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [270-284] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [267-269] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [275-277] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [279-281] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [282-284] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [287-291] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [294-299] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [301-323] for track '35' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [303-305] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Player track '9' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '9' has undefined team_side. Will map to Team_Unknown.
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

</details>