# Play-Annotation-Generator Annotation Review — SplitZone_167

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `SplitZone_167`
- **Frame Range:** 0 to 329 (330 total frames)
- **Play:** `Play_Run_SplitZone`
- **Result:** `Result_OutOfBounds`
- **Result Frame:** 329
- **Player Tracks:** 34
- **Ball Tracks:** 0
- **Action Segments:** 103
- **Validation Warnings:** 99
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 21
- **Exact Matches:** 7
- **Group Expanded Events:** 9
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 1
- **Missing Segments:** 0
- **Ambiguous Matches:** 2
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 84
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | HB | offense | `6` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `18` | `18` |
| ✅ EXACT | `Action_ZoneBlock` | RT | offense | `14` | `14` |
| ✅ EXACT | `Action_ZoneBlock` | RG | offense | `15` | `15` |
| ⚠️ START CHANGED | `Action_ZoneBlock` | C | offense | `18` | `18` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | offense | `19` | `19` |
| ✅ EXACT | `Action_SplitBlock` | HB | offense | `6` | `6` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `20` | `20` |
| ✅ EXACT | `Action_Handoff` | QB | offense | `20` | `20` |
| ⚠️ AMBIGUOUS MATCH | `Action_BlockSecondLevel` | C | offense | `18` | `18` |
| ✅ EXACT | `Action_BallCarry` | RB | offense | `17` | `17` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `0` | `Group` | 3 | START | 4 | 91 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `13` | `Group` | 3 | START | 4 | 91 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `14` | `Group` | 3 | START | 4 | 94 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `15` | `Group` | 3 | START | 4 | 94 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `17` | `Group` | 3 | START | 4 | 117 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `18` | `Group` | 3 | START | 4 | 91 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `19` | `Group` | 3 | START | 4 | 94 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `20` | `Group` | 3 | START | 4 | 91 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | HB | `6` | `Group` | 3 | START | 4 | 96 |
| ✅ EXACT | `Action_BallSnap` | C | `18` | `18` | 92 | START | 92 | 96 |
| ✅ EXACT | `Action_ZoneBlock` | RT | `14` | `14` | 95 | START | 95 | 152 |
| ✅ EXACT | `Action_ZoneBlock` | RG | `15` | `15` | 95 | START | 95 | 121 |
| ⚠️ START CHANGED | `Action_ZoneBlock` | C | `18` | `18` | 95 | START | 107 | 108 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | `19` | `19` | 95 | START | 95 | 105 |
| ✅ EXACT | `Action_SplitBlock` | HB | `6` | `6` | 97 | START | 97 | 169 |
| ✅ EXACT | `Action_SnapReceive` | QB | `20` | `20` | 99 | END | 92 | 99 |
| ✅ EXACT | `Action_Handoff` | QB | `20` | `20` | 104 | START | 104 | 117 |
| ⚠️ AMBIGUOUS MATCH | `Action_BlockSecondLevel` | C | `18` | `18` | 109 | START | 109 | 151 |
| ✅ EXACT | `Action_BallCarry` | RB | `17` | `17` | 118 | START | 118 | 157 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 169 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 4–246
- **Visible Samples:** 238

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 4 | 91 | 88 | inferred_complete_timeline |
| `Action_SnapReceive` | 92 | 99 | 8 | inferred_complete_timeline |
| `Action_None` | 100 | 103 | 4 | inferred_complete_timeline |
| `Action_Handoff` | 104 | 117 | 14 | inferred_complete_timeline |
| `Action_None` | 118 | 142 | 25 | inferred_complete_timeline |
| `Action_None` | 144 | 192 | 49 | inferred_complete_timeline |
| `Action_None` | 194 | 202 | 9 | inferred_complete_timeline |
| `Action_None` | 206 | 246 | 41 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 4–157
- **Visible Samples:** 154

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 4 | 117 | 114 | inferred_complete_timeline |
| `Action_BallCarry` | 118 | 157 | 40 | inferred_complete_timeline |

</details>

<details>
<summary>HB — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 4–329
- **Visible Samples:** 316

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 4 | 96 | 93 | inferred_complete_timeline |
| `Action_SplitBlock` | 97 | 169 | 73 | inferred_complete_timeline |
| `Action_None` | 170 | 235 | 66 | inferred_complete_timeline |
| `Action_None` | 246 | 329 | 84 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 4–284
- **Visible Samples:** 281

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 4 | 91 | 88 | inferred_complete_timeline |
| `Action_None` | 92 | 284 | 193 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 4–196
- **Visible Samples:** 184

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 4 | 91 | 88 | inferred_complete_timeline |
| `Action_None` | 92 | 177 | 86 | inferred_complete_timeline |
| `Action_None` | 179 | 184 | 6 | inferred_complete_timeline |
| `Action_None` | 188 | 189 | 2 | inferred_complete_timeline |
| `Action_None` | 195 | 196 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 4–275
- **Visible Samples:** 271

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 4 | 94 | 91 | inferred_complete_timeline |
| `Action_ZoneBlock` | 95 | 105 | 11 | inferred_complete_timeline |
| `Action_ZoneBlock` | 107 | 169 | 63 | inferred_complete_timeline |
| `Action_None` | 170 | 275 | 106 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 4–278
- **Visible Samples:** 260

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 4 | 91 | 88 | inferred_complete_timeline |
| `Action_BallSnap` | 92 | 96 | 5 | inferred_complete_timeline |
| `Action_ZoneBlock` | 107 | 108 | 2 | inferred_complete_timeline |
| `Action_BlockSecondLevel` | 109 | 151 | 43 | inferred_complete_timeline |
| `Action_BlockSecondLevel` | 153 | 169 | 17 | inferred_complete_timeline |
| `Action_None` | 170 | 212 | 43 | inferred_complete_timeline |
| `Action_None` | 214 | 247 | 34 | inferred_complete_timeline |
| `Action_None` | 251 | 278 | 28 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 4–121
- **Visible Samples:** 118

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 4 | 94 | 91 | inferred_complete_timeline |
| `Action_ZoneBlock` | 95 | 121 | 27 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 4–152
- **Visible Samples:** 149

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 4 | 94 | 91 | inferred_complete_timeline |
| `Action_ZoneBlock` | 95 | 152 | 58 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 4–254
- **Visible Samples:** 247

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 4 | 91 | 88 | inferred_complete_timeline |
| `Action_None` | 92 | 222 | 131 | inferred_complete_timeline |
| `Action_None` | 224 | 225 | 2 | inferred_complete_timeline |
| `Action_None` | 229 | 254 | 26 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 4–256
- **Visible Samples:** 235

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 4 | 91 | 88 | inferred_complete_timeline |
| `Action_None` | 92 | 107 | 16 | inferred_complete_timeline |
| `Action_None` | 111 | 113 | 3 | inferred_complete_timeline |
| `Action_None` | 121 | 198 | 78 | inferred_complete_timeline |
| `Action_None` | 207 | 256 | 50 | inferred_complete_timeline |

</details>

<details>
<summary>DT — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 4–282
- **Visible Samples:** 268

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 4 | 91 | 88 | inferred_complete_timeline |
| `Action_None` | 92 | 108 | 17 | inferred_complete_timeline |
| `Action_None` | 117 | 119 | 3 | inferred_complete_timeline |
| `Action_None` | 121 | 136 | 16 | inferred_complete_timeline |
| `Action_None` | 139 | 282 | 144 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 4–317
- **Visible Samples:** 298

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 4 | 91 | 88 | inferred_complete_timeline |
| `Action_None` | 92 | 160 | 69 | inferred_complete_timeline |
| `Action_None` | 162 | 164 | 3 | inferred_complete_timeline |
| `Action_None` | 168 | 169 | 2 | inferred_complete_timeline |
| `Action_None` | 175 | 202 | 28 | inferred_complete_timeline |
| `Action_None` | 209 | 212 | 4 | inferred_complete_timeline |
| `Action_None` | 214 | 317 | 104 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 4–172
- **Visible Samples:** 169

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 4 | 91 | 88 | inferred_complete_timeline |
| `Action_None` | 92 | 172 | 81 | inferred_complete_timeline |

</details>

<details>
<summary>LB3 — actor_track_id `21`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `21`
- **team_side:** `defense`
- **Visible Frames:** 4–329
- **Visible Samples:** 324

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 4 | 91 | 88 | inferred_complete_timeline |
| `Action_None` | 92 | 223 | 132 | inferred_complete_timeline |
| `Action_None` | 226 | 329 | 104 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 4–289
- **Visible Samples:** 286

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 4 | 91 | 88 | inferred_complete_timeline |
| `Action_None` | 92 | 289 | 198 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 4–258
- **Visible Samples:** 239

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 4 | 91 | 88 | inferred_complete_timeline |
| `Action_None` | 92 | 116 | 25 | inferred_complete_timeline |
| `Action_None` | 124 | 220 | 97 | inferred_complete_timeline |
| `Action_None` | 226 | 249 | 24 | inferred_complete_timeline |
| `Action_None` | 254 | 258 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 4–208
- **Visible Samples:** 200

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 4 | 91 | 88 | inferred_complete_timeline |
| `Action_None` | 92 | 190 | 99 | inferred_complete_timeline |
| `Action_None` | 195 | 198 | 4 | inferred_complete_timeline |
| `Action_None` | 200 | 208 | 9 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 4–329
- **Visible Samples:** 326

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 4 | 91 | 88 | inferred_complete_timeline |
| `Action_None` | 92 | 329 | 238 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 4–329
- **Visible Samples:** 322

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 4 | 91 | 88 | inferred_complete_timeline |
| `Action_None` | 92 | 222 | 131 | inferred_complete_timeline |
| `Action_None` | 224 | 228 | 5 | inferred_complete_timeline |
| `Action_None` | 230 | 320 | 91 | inferred_complete_timeline |
| `Action_None` | 323 | 329 | 7 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `1` | `1` | Position_Unknown | Team_Unknown | 4–294 | 291 | 2 | Undefined position; Undefined team |
| `9` | `9` | Position_Unknown | Team_Unknown | 4–288 | 285 | 2 | Undefined position; Undefined team |
| `22` | `22` | Position_Unknown | Team_Unknown | 105–329 | 165 | 3 | Undefined position; Undefined team |
| `23` | `24` | Position_Unknown | Team_Unknown | 129–189 | 41 | 2 | Undefined position; Undefined team |
| `24` | `25` | Position_Unknown | Team_Unknown | 163–267 | 105 | 1 | Undefined position; Undefined team |
| `25` | `26` | Position_Unknown | Team_Unknown | 169–264 | 96 | 1 | Undefined position; Undefined team |
| `26` | `30` | Position_Unknown | Team_Unknown | 198–202 | 5 | 1 | Undefined position; Undefined team |
| `27` | `33` | Position_Unknown | Team_Unknown | 256–289 | 34 | 1 | Undefined position; Undefined team |
| `28` | `34` | Position_Unknown | Team_Unknown | 275–313 | 32 | 3 | Undefined position; Undefined team |
| `29` | `35` | Position_Unknown | Team_Unknown | 275–329 | 54 | 2 | Undefined position; Undefined team |
| `30` | `36` | Position_Unknown | Team_Unknown | 289–328 | 40 | 1 | Undefined position; Undefined team |
| `31` | `39` | Position_Unknown | Team_Unknown | 320–329 | 10 | 1 | Undefined position; Undefined team |
| `32` | `40` | Position_Unknown | Team_Unknown | 320–329 | 10 | 1 | Undefined position; Undefined team |
| `33` | `42` | Position_Unknown | Team_Unknown | 324–329 | 6 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ `Action_ZoneBlock` for actor_track_id `18` (C): Annotated start 95 != Inferred start 107
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `19` (2 segments found)
- ⚠️ Ambiguous match for action `Action_BlockSecondLevel` and target `18` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `4` (actor_track_id `4`): `SAF2` position mapped to `defense` team
- ⚠️ Player track XML ID `7` (actor_track_id `7`): `SAF1` position mapped to `defense` team
- ⚠️ 14 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 14 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 28 |
| Missing visible bounding boxes during action | 67 |
| Track-related warning | 3 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 336: Duplicate assignment for track ID '11' in grid. Overwriting previous assignment.
- ⚠️ Row 336: Duplicate assignment for track ID '5' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 329 as fallback play end.
- ⚠️ Resolved action overlap for track '18' (C): higher_priority='Action_BallSnap' [92–99], lower_priority='Action_ZoneBlock' annotated_start=95, effective_Action_ZoneBlock_start=100.
- ⚠️ Action 'Action_None' range [92-284] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [92-294] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [92-222] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [224-225] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [229-254] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [92-289] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [92-222] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [224-228] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [230-320] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [92-116] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [124-220] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [226-249] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [254-258] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [170-235] for track '6' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [92-108] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [117-119] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [121-136] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [139-282] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [92-288] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [92-160] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [162-164] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [168-169] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [175-202] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [209-212] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [214-317] for track '10' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [92-107] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [111-113] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [121-198] for track '11' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [207-256] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [92-190] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [195-198] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [200-208] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [92-177] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [179-184] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [188-189] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [195-196] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [95-152] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [95-121] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [92-172] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [118-157] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallSnap' range [92-96] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BlockSecondLevel' range [109-151] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [170-212] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [214-247] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [251-278] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [95-105] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [170-275] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [118-142] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [144-192] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [194-202] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [206-246] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [4-91] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [92-223] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [105-107] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [165-178] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [129-166] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [187-189] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [163-267] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [169-264] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [198-202] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [256-289] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [275-298] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [305-309] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [311-313] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [275-297] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [289-328] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [324-329] for track '33' has 2 frames without a visible bounding box.
- ⚠️ Player track '1' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '1' has undefined team_side. Will map to Team_Unknown.
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

</details>