# Play-Annotation-Generator Annotation Review — OutsideZoneRead_19

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `OutsideZoneRead_19`
- **Frame Range:** 0 to 299 (300 total frames)
- **Play:** `Play_Run_OutsideZoneRead`
- **Result:** `Result_OutOfBounds`
- **Result Frame:** 299
- **Player Tracks:** 33
- **Ball Tracks:** 0
- **Action Segments:** 98
- **Validation Warnings:** 103
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 20
- **Exact Matches:** 7
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 1
- **Ambiguous Matches:** 0
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 73
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `6` | `Group` |
| ✅ EXACT | `Action_ZoneBlock` | LG | offense | `17` | `17` |
| ❌ MISSING SEGMENT | `Action_ZoneBlock` | LT | offense | `19` | `19` |
| ✅ EXACT | `Action_ZoneBlock` | RG | offense | `20` | `20` |
| ✅ EXACT | `Action_ZoneBlock` | RT | offense | `3` | `3` |
| ✅ EXACT | `Action_ZoneBlock` | C | offense | `6` | `6` |
| ✅ EXACT | `Action_PressEdge` | RB | offense | `21` | `21` |
| ✅ EXACT | `Action_ReadEdgeDefender` | QB | offense | `18` | `18` |
| ✅ EXACT | `Action_Handoff` | QB | offense | `18` | `18` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `0` | `Group` | 0 | START | 0 | 176 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `13` | `Group` | 0 | START | 0 | 296 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `16` | `Group` | 0 | START | 0 | 114 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `17` | `Group` | 0 | START | 0 | 121 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `18` | `Group` | 0 | START | 0 | 133 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `19` | `Group` | 0 | START | 0 | 120 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `20` | `Group` | 0 | START | 0 | 121 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `21` | `Group` | 0 | START | 0 | 1 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `3` | `Group` | 0 | START | 0 | 121 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `5` | `Group` | 0 | START | 0 | 161 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `6` | `Group` | 0 | START | 0 | 121 |
| ✅ EXACT | `Action_ZoneBlock` | LG | `17` | `17` | 122 | START | 122 | 123 |
| ❌ MISSING SEGMENT | `Action_ZoneBlock` | LT | `19` | `19` | 122 | START | N/A | N/A |
| ✅ EXACT | `Action_ZoneBlock` | RG | `20` | `20` | 122 | START | 122 | 126 |
| ✅ EXACT | `Action_ZoneBlock` | RT | `3` | `3` | 122 | START | 122 | 166 |
| ✅ EXACT | `Action_ZoneBlock` | C | `6` | `6` | 122 | START | 122 | 128 |
| ✅ EXACT | `Action_PressEdge` | RB | `21` | `21` | 134 | START | 134 | 166 |
| ✅ EXACT | `Action_ReadEdgeDefender` | QB | `18` | `18` | 134 | START | 134 | 141 |
| ✅ EXACT | `Action_Handoff` | QB | `18` | `18` | 142 | START | 142 | 150 |

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
- **Visible Frames:** 0–217
- **Visible Samples:** 218

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 133 | 134 | inferred_complete_timeline |
| `Action_ReadEdgeDefender` | 134 | 141 | 8 | inferred_complete_timeline |
| `Action_Handoff` | 142 | 150 | 9 | inferred_complete_timeline |
| `Action_None` | 151 | 217 | 67 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `21`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–228
- **Visible Samples:** 154

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 3 | 17 | 15 | inferred_complete_timeline |
| `Action_PreSnap` | 22 | 66 | 45 | inferred_complete_timeline |
| `Action_PressEdge` | 134 | 166 | 33 | inferred_complete_timeline |
| `Action_None` | 167 | 176 | 10 | inferred_complete_timeline |
| `Action_None` | 179 | 220 | 42 | inferred_complete_timeline |
| `Action_None` | 222 | 228 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–161
- **Visible Samples:** 162

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 161 | 162 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–296
- **Visible Samples:** 297

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 296 | 297 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 297

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 176 | 177 | inferred_complete_timeline |
| `Action_PreSnap` | 180 | 299 | 120 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 273

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 114 | 115 | inferred_complete_timeline |
| `Action_PreSnap` | 116 | 124 | 9 | inferred_complete_timeline |
| `Action_PreSnap` | 130 | 134 | 5 | inferred_complete_timeline |
| `Action_PreSnap` | 152 | 178 | 27 | inferred_complete_timeline |
| `Action_PreSnap` | 183 | 299 | 117 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–120
- **Visible Samples:** 121

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 120 | 121 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–123
- **Visible Samples:** 124

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 121 | 122 | inferred_complete_timeline |
| `Action_ZoneBlock` | 122 | 123 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–128
- **Visible Samples:** 129

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 121 | 122 | inferred_complete_timeline |
| `Action_ZoneBlock` | 122 | 128 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–126
- **Visible Samples:** 127

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 121 | 122 | inferred_complete_timeline |
| `Action_ZoneBlock` | 122 | 126 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–291
- **Visible Samples:** 272

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 121 | 122 | inferred_complete_timeline |
| `Action_ZoneBlock` | 122 | 166 | 45 | inferred_complete_timeline |
| `Action_None` | 176 | 196 | 21 | inferred_complete_timeline |
| `Action_None` | 200 | 201 | 2 | inferred_complete_timeline |
| `Action_None` | 204 | 232 | 29 | inferred_complete_timeline |
| `Action_None` | 239 | 291 | 53 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 292

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 217 | 218 | inferred_complete_timeline |
| `Action_PreSnap` | 226 | 299 | 74 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–296
- **Visible Samples:** 296

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 290 | 291 | inferred_complete_timeline |
| `Action_PreSnap` | 292 | 296 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–212
- **Visible Samples:** 198

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 179 | 180 | inferred_complete_timeline |
| `Action_PreSnap` | 192 | 193 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 195 | 196 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 199 | 212 | 14 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–280
- **Visible Samples:** 268

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 156 | 157 | inferred_complete_timeline |
| `Action_PreSnap` | 169 | 173 | 5 | inferred_complete_timeline |
| `Action_PreSnap` | 175 | 280 | 106 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–186
- **Visible Samples:** 180

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 167 | 168 | inferred_complete_timeline |
| `Action_PreSnap` | 169 | 178 | 10 | inferred_complete_timeline |
| `Action_PreSnap` | 185 | 186 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–282
- **Visible Samples:** 278

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 187 | 188 | inferred_complete_timeline |
| `Action_PreSnap` | 189 | 274 | 86 | inferred_complete_timeline |
| `Action_PreSnap` | 279 | 282 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–290
- **Visible Samples:** 223

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 190 | 191 | inferred_complete_timeline |
| `Action_PreSnap` | 193 | 203 | 11 | inferred_complete_timeline |
| `Action_PreSnap` | 270 | 290 | 21 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–249
- **Visible Samples:** 239

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 178 | 179 | inferred_complete_timeline |
| `Action_PreSnap` | 186 | 227 | 42 | inferred_complete_timeline |
| `Action_PreSnap` | 232 | 249 | 18 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 300

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 299 | 300 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 287

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 216 | 217 | inferred_complete_timeline |
| `Action_PreSnap` | 218 | 220 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 227 | 228 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 232 | 277 | 46 | inferred_complete_timeline |
| `Action_PreSnap` | 281 | 299 | 19 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–256
- **Visible Samples:** 253

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 168 | 169 | inferred_complete_timeline |
| `Action_PreSnap` | 170 | 171 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 175 | 256 | 82 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `22` | `23` | Position_Unknown | Team_Unknown | 62–98 | 33 | 2 | Undefined position; Undefined team |
| `23` | `24` | Position_Unknown | Team_Unknown | 148–299 | 113 | 4 | Undefined position; Undefined team |
| `24` | `25` | Position_Unknown | Team_Unknown | 155–238 | 78 | 3 | Undefined position; Undefined team |
| `25` | `27` | Position_Unknown | Team_Unknown | 194–291 | 27 | 6 | Undefined position; Undefined team |
| `26` | `28` | Position_Unknown | Team_Unknown | 196–299 | 88 | 5 | Undefined position; Undefined team |
| `27` | `29` | Position_Unknown | Team_Unknown | 204–299 | 87 | 2 | Undefined position; Undefined team |
| `28` | `31` | Position_Unknown | Team_Unknown | 237–299 | 62 | 2 | Undefined position; Undefined team |
| `29` | `32` | Position_Unknown | Team_Unknown | 244–299 | 45 | 3 | Undefined position; Undefined team |
| `30` | `33` | Position_Unknown | Team_Unknown | 252–299 | 48 | 1 | Undefined position; Undefined team |
| `31` | `34` | Position_Unknown | Team_Unknown | 257–288 | 25 | 3 | Undefined position; Undefined team |
| `32` | `37` | Position_Unknown | Team_Unknown | 273–299 | 23 | 2 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ❌ Missing segment for action `Action_ZoneBlock` on target `19` (LT)

### Track Identity Issues

- ⚠️ Player track XML ID `2` (actor_track_id `2`): `SAF2` position mapped to `defense` team
- ⚠️ Player track XML ID `14` (actor_track_id `14`): `SAF1` position mapped to `defense` team
- ⚠️ 11 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 11 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 22 |
| Missing visible bounding boxes during action | 79 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 299 as fallback play end.
- ⚠️ Segment 'Action_ZoneBlock' for track '19' has invalid range: start=122, end=120. Clamping end to start.
- ⚠️ Action 'Action_PreSnap' range [0-176] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [180-299] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-178] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [186-227] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [232-249] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-168] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [170-171] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [175-256] for track '2' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [122-166] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [176-196] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [200-201] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [204-232] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [239-291] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-179] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [192-193] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [195-196] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [199-212] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-161] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [122-128] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-187] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [189-274] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [279-282] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-217] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-290] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [292-296] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-167] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [169-178] for track '10' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [185-186] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-156] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [169-173] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [175-280] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-296] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-216] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [218-220] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [227-228] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [232-277] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-190] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [193-203] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [270-290] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-114] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [116-124] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [130-134] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [152-178] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [122-123] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [151-217] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-120] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [122-126] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-1] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [3-17] for track '21' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [22-66] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [167-176] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [179-220] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [222-228] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [62-67] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [72-98] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [148-153] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [189-225] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [228-238] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [155-209] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [214-216] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [219-238] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [194-196] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [199-200] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [207-208] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [269-275] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [277-280] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [283-291] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [196-246] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [251-277] for track '26' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [280-283] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [290-294] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [204-229] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [237-280] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [244-259] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [262-267] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [257-262] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [267-274] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [278-288] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [273-277] for track '32' has 1 frames without a visible bounding box.
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