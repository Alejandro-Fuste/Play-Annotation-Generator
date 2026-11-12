# Play-Annotation-Generator Annotation Review — SplitZone_248

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `SplitZone_248`
- **Frame Range:** 0 to 329 (330 total frames)
- **Play:** `Play_Run_SplitZone`
- **Result:** `Result_Touchdown`
- **Result Frame:** 329
- **Player Tracks:** 28
- **Ball Tracks:** 0
- **Action Segments:** 95
- **Validation Warnings:** 92
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 21
- **Exact Matches:** 4
- **Group Expanded Events:** 8
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 1
- **Missing Segments:** 0
- **Ambiguous Matches:** 6
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 66
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `8` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | HB | offense | `9` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `16` | `16` |
| ✅ EXACT | `Action_ZoneBlock` | RT | offense | `0` | `0` |
| ⚠️ START CHANGED | `Action_ZoneBlock` | C | offense | `16` | `16` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | offense | `3` | `3` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | offense | `4` | `4` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | offense | `7` | `7` |
| ⚠️ AMBIGUOUS MATCH | `Action_SplitBlock` | HB | offense | `9` | `9` |
| ⚠️ AMBIGUOUS MATCH | `Action_SnapReceive` | QB | offense | `15` | `15` |
| ✅ EXACT | `Action_Handoff` | QB | offense | `15` | `15` |
| ✅ EXACT | `Action_BallCarry` | RB | offense | `8` | `8` |
| ⚠️ AMBIGUOUS MATCH | `Action_BlockSecondLevel` | RT | offense | `0` | `0` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `0` | `Group` | 5 | START | 6 | 121 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `15` | `Group` | 5 | START | 6 | 13 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `16` | `Group` | 5 | START | 6 | 118 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `3` | `Group` | 5 | START | 6 | 121 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `4` | `Group` | 5 | START | 6 | 121 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `7` | `Group` | 5 | START | 6 | 121 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `8` | `Group` | 5 | START | 6 | 27 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | HB | `9` | `Group` | 5 | START | 6 | 126 |
| ✅ EXACT | `Action_BallSnap` | C | `16` | `16` | 119 | START | 119 | 131 |
| ✅ EXACT | `Action_ZoneBlock` | RT | `0` | `0` | 122 | START | 122 | 152 |
| ⚠️ START CHANGED | `Action_ZoneBlock` | C | `16` | `16` | 122 | START | 132 | 192 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | `3` | `3` | 122 | START | 122 | 169 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | `4` | `4` | 122 | START | 122 | 146 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | `7` | `7` | 122 | START | 122 | 178 |
| ⚠️ AMBIGUOUS MATCH | `Action_SplitBlock` | HB | `9` | `9` | 127 | START | 127 | 160 |
| ⚠️ AMBIGUOUS MATCH | `Action_SnapReceive` | QB | `15` | `15` | 131 | END | 121 | 123 |
| ✅ EXACT | `Action_Handoff` | QB | `15` | `15` | 136 | START | 136 | 146 |
| ✅ EXACT | `Action_BallCarry` | RB | `8` | `8` | 147 | START | 147 | 151 |
| ⚠️ AMBIGUOUS MATCH | `Action_BlockSecondLevel` | RT | `0` | `0` | 153 | START | 153 | 179 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 230 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 6–329
- **Visible Samples:** 267

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 6 | 13 | 8 | inferred_complete_timeline |
| `Action_PreSnap` | 43 | 65 | 23 | inferred_complete_timeline |
| `Action_PreSnap` | 71 | 76 | 6 | inferred_complete_timeline |
| `Action_PreSnap` | 86 | 89 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 93 | 94 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 96 | 112 | 17 | inferred_complete_timeline |
| `Action_PreSnap` | 116 | 118 | 3 | inferred_complete_timeline |
| `Action_SnapReceive` | 121 | 123 | 3 | inferred_complete_timeline |
| `Action_SnapReceive` | 127 | 131 | 5 | inferred_complete_timeline |
| `Action_None` | 132 | 135 | 4 | inferred_complete_timeline |
| `Action_Handoff` | 136 | 146 | 11 | inferred_complete_timeline |
| `Action_None` | 147 | 149 | 3 | inferred_complete_timeline |
| `Action_None` | 152 | 329 | 178 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 6–151
- **Visible Samples:** 131

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 6 | 27 | 22 | inferred_complete_timeline |
| `Action_PreSnap` | 35 | 80 | 46 | inferred_complete_timeline |
| `Action_PreSnap` | 84 | 88 | 5 | inferred_complete_timeline |
| `Action_PreSnap` | 91 | 105 | 15 | inferred_complete_timeline |
| `Action_PreSnap` | 109 | 146 | 38 | inferred_complete_timeline |
| `Action_BallCarry` | 147 | 151 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>HB — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 6–329
- **Visible Samples:** 323

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 6 | 126 | 121 | inferred_complete_timeline |
| `Action_SplitBlock` | 127 | 160 | 34 | inferred_complete_timeline |
| `Action_SplitBlock` | 162 | 230 | 69 | inferred_complete_timeline |
| `Action_None` | 231 | 329 | 99 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 6–280
- **Visible Samples:** 265

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 6 | 121 | 116 | inferred_complete_timeline |
| `Action_ZoneBlock` | 122 | 169 | 48 | inferred_complete_timeline |
| `Action_ZoneBlock` | 172 | 176 | 5 | inferred_complete_timeline |
| `Action_ZoneBlock` | 178 | 191 | 14 | inferred_complete_timeline |
| `Action_ZoneBlock` | 198 | 230 | 33 | inferred_complete_timeline |
| `Action_None` | 231 | 277 | 47 | inferred_complete_timeline |
| `Action_None` | 279 | 280 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 6–267
- **Visible Samples:** 254

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 6 | 121 | 116 | inferred_complete_timeline |
| `Action_ZoneBlock` | 122 | 178 | 57 | inferred_complete_timeline |
| `Action_ZoneBlock` | 185 | 189 | 5 | inferred_complete_timeline |
| `Action_ZoneBlock` | 191 | 192 | 2 | inferred_complete_timeline |
| `Action_ZoneBlock` | 194 | 230 | 37 | inferred_complete_timeline |
| `Action_None` | 231 | 267 | 37 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 6–192
- **Visible Samples:** 187

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 6 | 118 | 113 | inferred_complete_timeline |
| `Action_BallSnap` | 119 | 131 | 13 | inferred_complete_timeline |
| `Action_ZoneBlock` | 132 | 192 | 61 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 6–276
- **Visible Samples:** 269

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 6 | 121 | 116 | inferred_complete_timeline |
| `Action_ZoneBlock` | 122 | 146 | 25 | inferred_complete_timeline |
| `Action_ZoneBlock` | 149 | 230 | 82 | inferred_complete_timeline |
| `Action_None` | 231 | 276 | 46 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 6–295
- **Visible Samples:** 255

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 6 | 121 | 116 | inferred_complete_timeline |
| `Action_ZoneBlock` | 122 | 152 | 31 | inferred_complete_timeline |
| `Action_BlockSecondLevel` | 153 | 179 | 27 | inferred_complete_timeline |
| `Action_BlockSecondLevel` | 183 | 212 | 30 | inferred_complete_timeline |
| `Action_None` | 244 | 248 | 5 | inferred_complete_timeline |
| `Action_None` | 250 | 295 | 46 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 6–329
- **Visible Samples:** 324

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 6 | 118 | 113 | inferred_complete_timeline |
| `Action_None` | 119 | 329 | 211 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 6–318
- **Visible Samples:** 310

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 6 | 118 | 113 | inferred_complete_timeline |
| `Action_None` | 119 | 164 | 46 | inferred_complete_timeline |
| `Action_None` | 168 | 318 | 151 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 6–270
- **Visible Samples:** 222

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 6 | 118 | 113 | inferred_complete_timeline |
| `Action_None` | 119 | 139 | 21 | inferred_complete_timeline |
| `Action_None` | 143 | 158 | 16 | inferred_complete_timeline |
| `Action_None` | 178 | 205 | 28 | inferred_complete_timeline |
| `Action_None` | 218 | 222 | 5 | inferred_complete_timeline |
| `Action_None` | 232 | 270 | 39 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 6–186
- **Visible Samples:** 179

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 6 | 118 | 113 | inferred_complete_timeline |
| `Action_None` | 119 | 142 | 24 | inferred_complete_timeline |
| `Action_None` | 145 | 186 | 42 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 6–296
- **Visible Samples:** 285

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 6 | 118 | 113 | inferred_complete_timeline |
| `Action_None` | 119 | 171 | 53 | inferred_complete_timeline |
| `Action_None` | 176 | 187 | 12 | inferred_complete_timeline |
| `Action_None` | 190 | 296 | 107 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 6–329
- **Visible Samples:** 324

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 6 | 118 | 113 | inferred_complete_timeline |
| `Action_None` | 119 | 329 | 211 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 6–283
- **Visible Samples:** 242

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 6 | 118 | 113 | inferred_complete_timeline |
| `Action_None` | 119 | 149 | 31 | inferred_complete_timeline |
| `Action_None` | 153 | 169 | 17 | inferred_complete_timeline |
| `Action_None` | 203 | 283 | 81 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 6–193
- **Visible Samples:** 185

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 6 | 11 | 6 | inferred_complete_timeline |
| `Action_PreSnap` | 15 | 118 | 104 | inferred_complete_timeline |
| `Action_None` | 119 | 193 | 75 | inferred_complete_timeline |

</details>

<details>
<summary>SAF3 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 6–185
- **Visible Samples:** 180

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 6 | 118 | 113 | inferred_complete_timeline |
| `Action_None` | 119 | 185 | 67 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `1` | `1` | Position_Unknown | Team_Unknown | 6–147 | 142 | 2 | Undefined position; Undefined team |
| `18` | `18` | Position_Unknown | Team_Unknown | 156–329 | 170 | 2 | Undefined position; Undefined team |
| `19` | `19` | Position_Unknown | Team_Unknown | 165–317 | 153 | 1 | Undefined position; Undefined team |
| `20` | `20` | Position_Unknown | Team_Unknown | 176–329 | 153 | 2 | Undefined position; Undefined team |
| `21` | `23` | Position_Unknown | Team_Unknown | 203–292 | 90 | 1 | Undefined position; Undefined team |
| `22` | `25` | Position_Unknown | Team_Unknown | 219–329 | 111 | 1 | Undefined position; Undefined team |
| `23` | `26` | Position_Unknown | Team_Unknown | 231–287 | 50 | 2 | Undefined position; Undefined team |
| `24` | `27` | Position_Unknown | Team_Unknown | 241–313 | 73 | 1 | Undefined position; Undefined team |
| `25` | `29` | Position_Unknown | Team_Unknown | 248–329 | 80 | 2 | Undefined position; Undefined team |
| `26` | `30` | Position_Unknown | Team_Unknown | 271–310 | 40 | 1 | Undefined position; Undefined team |
| `27` | `31` | Position_Unknown | Team_Unknown | 289–306 | 16 | 2 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ `Action_ZoneBlock` for actor_track_id `16` (C): Annotated start 122 != Inferred start 132
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `3` (4 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `4` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `7` (4 segments found)
- ⚠️ Ambiguous match for action `Action_SplitBlock` and target `9` (2 segments found)
- ⚠️ Ambiguous match for action `Action_SnapReceive` and target `15` (2 segments found)
- ⚠️ Ambiguous match for action `Action_BlockSecondLevel` and target `0` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `6` (actor_track_id `6`): `SAF1` position mapped to `defense` team
- ⚠️ Player track XML ID `11` (actor_track_id `11`): `SAF3` position mapped to `defense` team
- ⚠️ Player track XML ID `17` (actor_track_id `17`): `SAF2` position mapped to `defense` team
- ⚠️ 11 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 11 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 22 |
| Missing visible bounding boxes during action | 65 |
| Track-related warning | 4 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 329 as fallback play end.
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '3' (LT) duration 109 frames exceeds threshold 90 frames [start=122, end=230].
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '4' (RG) duration 109 frames exceeds threshold 90 frames [start=122, end=230].
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '7' (LG) duration 109 frames exceeds threshold 90 frames [start=122, end=230].
- ⚠️ Resolved action overlap for track '16' (C): higher_priority='Action_BallSnap' [119–131], lower_priority='Action_ZoneBlock' annotated_start=122, effective_Action_ZoneBlock_start=132.
- ⚠️ Action 'Action_BlockSecondLevel' range [153-179] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BlockSecondLevel' range [183-212] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [244-248] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [250-295] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [119-147] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [122-169] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [172-176] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [178-191] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [231-277] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [279-280] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [122-146] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [149-230] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [231-276] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [119-171] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [176-187] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [190-296] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [119-149] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [153-169] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [203-283] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [122-178] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [185-189] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [191-192] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [231-267] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [6-27] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [35-80] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [84-88] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [91-105] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [147-151] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_SplitBlock' range [127-160] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_SplitBlock' range [162-230] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [119-139] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [143-158] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [178-205] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [218-222] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [232-270] for track '10' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [119-185] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [119-164] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [168-318] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [119-142] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [145-186] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [6-13] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [43-65] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [71-76] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [86-89] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [93-94] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [96-112] for track '15' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [116-118] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_SnapReceive' range [121-123] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [147-149] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [132-192] for track '16' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [6-11] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [119-193] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [156-217] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [222-329] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [165-317] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [176-230] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [232-329] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [203-292] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [231-239] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [247-287] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [241-313] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [248-252] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [271-310] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [289-291] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [294-306] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Player track '1' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '1' has undefined team_side. Will map to Team_Unknown.
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

</details>