# Play-Annotation-Generator Annotation Review — SplitZone_22

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `SplitZone_22`
- **Frame Range:** 0 to 419 (420 total frames)
- **Play:** `Play_Run_SplitZone`
- **Result:** `Result_OutOfBounds`
- **Result Frame:** 419
- **Player Tracks:** 43
- **Ball Tracks:** 0
- **Action Segments:** 108
- **Validation Warnings:** 135
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 20
- **Exact Matches:** 5
- **Group Expanded Events:** 8
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 1
- **Missing Segments:** 0
- **Ambiguous Matches:** 4
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 90
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | HB | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `7` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `10` | `10` |
| ⚠️ AMBIGUOUS MATCH | `Action_SplitBlock` | HB | offense | `14` | `14` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | offense | `1` | `1` |
| ⚠️ START CHANGED | `Action_ZoneBlock` | C | offense | `10` | `10` |
| ✅ EXACT | `Action_ZoneBlock` | RT | offense | `11` | `11` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | offense | `15` | `15` |
| ✅ EXACT | `Action_ZoneBlock` | LG | offense | `7` | `7` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `16` | `16` |
| ✅ EXACT | `Action_Handoff` | QB | offense | `16` | `16` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | Position_Unknown | Team_Unknown | `18` | `18` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `1` | `Group` | 2 | START | 2 | 64 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `10` | `Group` | 2 | START | 2 | 61 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `11` | `Group` | 2 | START | 2 | 64 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `13` | `Group` | 2 | START | 2 | 61 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | HB | `14` | `Group` | 2 | START | 2 | 63 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `15` | `Group` | 2 | START | 2 | 64 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `16` | `Group` | 2 | START | 2 | 61 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `7` | `Group` | 2 | START | 2 | 64 |
| ✅ EXACT | `Action_BallSnap` | C | `10` | `10` | 62 | START | 62 | 77 |
| ⚠️ AMBIGUOUS MATCH | `Action_SplitBlock` | HB | `14` | `14` | 64 | START | 64 | 71 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | `1` | `1` | 65 | START | 65 | 129 |
| ⚠️ START CHANGED | `Action_ZoneBlock` | C | `10` | `10` | 65 | START | 78 | 101 |
| ✅ EXACT | `Action_ZoneBlock` | RT | `11` | `11` | 65 | START | 65 | 99 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | `15` | `15` | 65 | START | 65 | 132 |
| ✅ EXACT | `Action_ZoneBlock` | LG | `7` | `7` | 65 | START | 65 | 82 |
| ✅ EXACT | `Action_SnapReceive` | QB | `16` | `16` | 77 | END | 62 | 77 |
| ✅ EXACT | `Action_Handoff` | QB | `16` | `16` | 89 | START | 89 | 104 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | Position_Unknown | `18` | `18` | 105 | START | 105 | 188 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 155 | BOUNDARY | N/A | N/A |

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
- **Visible Frames:** 2–179
- **Visible Samples:** 177

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 2 | 61 | 60 | inferred_complete_timeline |
| `Action_SnapReceive` | 62 | 77 | 16 | inferred_complete_timeline |
| `Action_None` | 78 | 88 | 11 | inferred_complete_timeline |
| `Action_Handoff` | 89 | 104 | 16 | inferred_complete_timeline |
| `Action_None` | 105 | 119 | 15 | inferred_complete_timeline |
| `Action_None` | 121 | 179 | 59 | inferred_complete_timeline |

</details>

<details>
<summary>HB — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 2–419
- **Visible Samples:** 400

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 2 | 63 | 62 | inferred_complete_timeline |
| `Action_SplitBlock` | 64 | 71 | 8 | inferred_complete_timeline |
| `Action_SplitBlock` | 81 | 92 | 12 | inferred_complete_timeline |
| `Action_SplitBlock` | 101 | 155 | 55 | inferred_complete_timeline |
| `Action_None` | 157 | 419 | 263 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 2–184
- **Visible Samples:** 176

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 2 | 61 | 60 | inferred_complete_timeline |
| `Action_None` | 62 | 94 | 33 | inferred_complete_timeline |
| `Action_None` | 102 | 184 | 83 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 2–214
- **Visible Samples:** 182

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 2 | 64 | 63 | inferred_complete_timeline |
| `Action_ZoneBlock` | 65 | 129 | 65 | inferred_complete_timeline |
| `Action_ZoneBlock` | 138 | 139 | 2 | inferred_complete_timeline |
| `Action_ZoneBlock` | 151 | 154 | 4 | inferred_complete_timeline |
| `Action_None` | 159 | 177 | 19 | inferred_complete_timeline |
| `Action_None` | 185 | 187 | 3 | inferred_complete_timeline |
| `Action_None` | 189 | 214 | 26 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 2–82
- **Visible Samples:** 81

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 2 | 64 | 63 | inferred_complete_timeline |
| `Action_ZoneBlock` | 65 | 82 | 18 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 2–101
- **Visible Samples:** 100

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 2 | 61 | 60 | inferred_complete_timeline |
| `Action_BallSnap` | 62 | 77 | 16 | inferred_complete_timeline |
| `Action_ZoneBlock` | 78 | 101 | 24 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 2–208
- **Visible Samples:** 200

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 2 | 64 | 63 | inferred_complete_timeline |
| `Action_ZoneBlock` | 65 | 132 | 68 | inferred_complete_timeline |
| `Action_ZoneBlock` | 139 | 155 | 17 | inferred_complete_timeline |
| `Action_None` | 156 | 204 | 49 | inferred_complete_timeline |
| `Action_None` | 206 | 208 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 2–99
- **Visible Samples:** 98

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 2 | 64 | 63 | inferred_complete_timeline |
| `Action_ZoneBlock` | 65 | 99 | 35 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 2–277
- **Visible Samples:** 276

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 2 | 61 | 60 | inferred_complete_timeline |
| `Action_None` | 62 | 277 | 216 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 2–153
- **Visible Samples:** 152

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 2 | 61 | 60 | inferred_complete_timeline |
| `Action_None` | 62 | 153 | 92 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 2–136
- **Visible Samples:** 135

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 2 | 61 | 60 | inferred_complete_timeline |
| `Action_None` | 62 | 136 | 75 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 2–193
- **Visible Samples:** 189

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 2 | 61 | 60 | inferred_complete_timeline |
| `Action_None` | 62 | 183 | 122 | inferred_complete_timeline |
| `Action_None` | 186 | 189 | 4 | inferred_complete_timeline |
| `Action_None` | 191 | 193 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `defense`
- **Visible Frames:** 2–344
- **Visible Samples:** 340

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 2 | 61 | 60 | inferred_complete_timeline |
| `Action_None` | 62 | 201 | 140 | inferred_complete_timeline |
| `Action_None` | 204 | 287 | 84 | inferred_complete_timeline |
| `Action_None` | 289 | 344 | 56 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 2–143
- **Visible Samples:** 107

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 2 | 61 | 60 | inferred_complete_timeline |
| `Action_None` | 62 | 102 | 41 | inferred_complete_timeline |
| `Action_None` | 138 | 143 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>CB — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 2–261
- **Visible Samples:** 254

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 2 | 61 | 60 | inferred_complete_timeline |
| `Action_None` | 62 | 119 | 58 | inferred_complete_timeline |
| `Action_None` | 121 | 162 | 42 | inferred_complete_timeline |
| `Action_None` | 164 | 171 | 8 | inferred_complete_timeline |
| `Action_None` | 173 | 208 | 36 | inferred_complete_timeline |
| `Action_None` | 212 | 261 | 50 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 2–419
- **Visible Samples:** 395

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 2 | 61 | 60 | inferred_complete_timeline |
| `Action_None` | 62 | 92 | 31 | inferred_complete_timeline |
| `Action_None` | 116 | 419 | 304 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 2–175
- **Visible Samples:** 174

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 2 | 61 | 60 | inferred_complete_timeline |
| `Action_None` | 62 | 175 | 114 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `17` | `17` | Position_Unknown | Team_Unknown | 43–44 | 2 | 1 | Undefined position; Undefined team |
| `18` | `18` | Position_Unknown | Team_Unknown | 72–314 | 218 | 6 | Undefined position; Undefined team |
| `19` | `19` | Position_Unknown | Team_Unknown | 89–124 | 29 | 4 | Undefined position; Undefined team |
| `20` | `22` | Position_Unknown | Team_Unknown | 113–184 | 71 | 2 | Undefined position; Undefined team |
| `21` | `23` | Position_Unknown | Team_Unknown | 141–194 | 54 | 1 | Undefined position; Undefined team |
| `22` | `24` | Position_Unknown | Team_Unknown | 152–205 | 44 | 4 | Undefined position; Undefined team |
| `23` | `25` | Position_Unknown | Team_Unknown | 158–354 | 197 | 1 | Undefined position; Undefined team |
| `24` | `29` | Position_Unknown | Team_Unknown | 178–419 | 239 | 2 | Undefined position; Undefined team |
| `25` | `30` | Position_Unknown | Team_Unknown | 194–419 | 222 | 2 | Undefined position; Undefined team |
| `26` | `31` | Position_Unknown | Team_Unknown | 197–419 | 220 | 2 | Undefined position; Undefined team |
| `27` | `32` | Position_Unknown | Team_Unknown | 200–256 | 57 | 1 | Undefined position; Undefined team |
| `28` | `34` | Position_Unknown | Team_Unknown | 222–419 | 197 | 2 | Undefined position; Undefined team |
| `29` | `35` | Position_Unknown | Team_Unknown | 226–247 | 22 | 1 | Undefined position; Undefined team |
| `30` | `36` | Position_Unknown | Team_Unknown | 238–288 | 44 | 3 | Undefined position; Undefined team |
| `31` | `39` | Position_Unknown | Team_Unknown | 248–419 | 172 | 1 | Undefined position; Undefined team |
| `32` | `40` | Position_Unknown | Team_Unknown | 254–283 | 30 | 1 | Undefined position; Undefined team |
| `33` | `41` | Position_Unknown | Team_Unknown | 270–320 | 49 | 2 | Undefined position; Undefined team |
| `34` | `42` | Position_Unknown | Team_Unknown | 301–419 | 119 | 1 | Undefined position; Undefined team |
| `35` | `45` | Position_Unknown | Team_Unknown | 304–413 | 110 | 1 | Undefined position; Undefined team |
| `36` | `49` | Position_Unknown | Team_Unknown | 324–356 | 32 | 2 | Undefined position; Undefined team |
| `37` | `51` | Position_Unknown | Team_Unknown | 392–395 | 4 | 1 | Undefined position; Undefined team |
| `38` | `52` | Position_Unknown | Team_Unknown | 399–419 | 17 | 2 | Undefined position; Undefined team |
| `39` | `53` | Position_Unknown | Team_Unknown | 406–419 | 14 | 1 | Undefined position; Undefined team |
| `40` | `54` | Position_Unknown | Team_Unknown | 413–419 | 7 | 1 | Undefined position; Undefined team |
| `41` | `55` | Position_Unknown | Team_Unknown | 417–419 | 3 | 1 | Undefined position; Undefined team |
| `42` | `56` | Position_Unknown | Team_Unknown | 418–419 | 2 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_SplitBlock` and target `14` (3 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `1` (3 segments found)
- ⚠️ `Action_ZoneBlock` for actor_track_id `10` (C): Annotated start 65 != Inferred start 78
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `15` (2 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `18` (5 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `2` (actor_track_id `2`): `SAF2` position mapped to `defense` team
- ⚠️ Player track XML ID `12` (actor_track_id `12`): `SAF1` position mapped to `defense` team
- ⚠️ 26 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 26 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 52 |
| Missing visible bounding boxes during action | 79 |
| Track-related warning | 3 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 419 as fallback play end.
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '1' (LT) duration 91 frames exceeds threshold 90 frames [start=65, end=155].
- ⚠️ Resolved action overlap for track '10' (C): higher_priority='Action_BallSnap' [62–77], lower_priority='Action_ZoneBlock' annotated_start=65, effective_Action_ZoneBlock_start=78.
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '15' (RG) duration 91 frames exceeds threshold 90 frames [start=65, end=155].
- ⚠️ Action 'Action_None' range [62-201] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [204-287] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [289-344] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [65-129] for track '1' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [138-139] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [151-154] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [159-177] for track '1' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [185-187] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [189-214] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [62-175] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [62-119] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [121-162] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [164-171] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [173-208] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [212-261] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [62-102] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [138-143] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [62-136] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [62-277] for track '6' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [65-82] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [62-183] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [186-189] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [191-193] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [62-153] for track '9' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [78-101] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [65-99] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [62-92] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [116-419] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [62-94] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [102-184] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_SplitBlock' range [64-71] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_SplitBlock' range [81-92] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_SplitBlock' range [101-155] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [157-419] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [65-132] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [139-155] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [156-204] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [206-208] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [105-119] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [121-179] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [43-44] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [105-188] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [193-249] for track '18' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [253-290] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [301-304] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [313-314] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [89-94] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [98-106] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [108-115] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [119-124] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [113-136] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [138-184] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [141-194] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [152-153] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [156-187] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [189-196] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [204-205] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [158-354] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [178-204] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [194-227] for track '25' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [197-293] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [200-256] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [222-344] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [226-247] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [238-276] for track '30' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [278-279] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [286-288] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [254-283] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [270-308] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [311-320] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [304-413] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [324-351] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [353-356] for track '36' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [392-395] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [399-413] for track '38' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [418-419] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [406-419] for track '39' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [417-419] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [418-419] for track '42' has 1 frames without a visible bounding box.
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

</details>