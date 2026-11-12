# Play-Annotation-Generator Annotation Review — SplitZone_148

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `SplitZone_148`
- **Frame Range:** 0 to 299 (300 total frames)
- **Play:** `Play_Run_SplitZone`
- **Result:** `Result_Tackle`
- **Result Frame:** 299
- **Player Tracks:** 26
- **Ball Tracks:** 0
- **Action Segments:** 83
- **Validation Warnings:** 80
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 20
- **Exact Matches:** 3
- **Group Expanded Events:** 8
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 7
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 63
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `8` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `9` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `10` | `10` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | offense | `10` | `10` |
| ✅ EXACT | `Action_ZoneBlock` | RG | offense | `12` | `12` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | offense | `2` | `2` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | offense | `5` | `5` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | offense | `9` | `9` |
| ⚠️ AMBIGUOUS MATCH | `Action_SplitBlock` | TE | offense | `14` | `14` |
| ⚠️ AMBIGUOUS MATCH | `Action_SnapReceive` | QB | offense | `8` | `8` |
| ✅ EXACT | `Action_Handoff` | QB | offense | `8` | `8` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | offense | `7` | `7` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `10` | `Group` | 24 | START | 25 | 130 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `12` | `Group` | 24 | START | 45 | 133 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `14` | `Group` | 24 | START | 137 | 137 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `2` | `Group` | 24 | START | 25 | 133 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `5` | `Group` | 24 | START | 25 | 133 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `7` | `Group` | 24 | START | 25 | 155 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `8` | `Group` | 24 | START | 25 | 77 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `9` | `Group` | 24 | START | 25 | 133 |
| ✅ EXACT | `Action_BallSnap` | C | `10` | `10` | 131 | START | 131 | 142 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | `10` | `10` | 134 | START | 146 | 150 |
| ✅ EXACT | `Action_ZoneBlock` | RG | `12` | `12` | 134 | START | 134 | 204 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | `2` | `2` | 134 | START | 134 | 172 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | `5` | `5` | 134 | START | 134 | 143 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | `9` | `9` | 134 | START | 134 | 180 |
| ⚠️ AMBIGUOUS MATCH | `Action_SplitBlock` | TE | `14` | `14` | 138 | START | 138 | 164 |
| ⚠️ AMBIGUOUS MATCH | `Action_SnapReceive` | QB | `8` | `8` | 144 | END | 131 | 133 |
| ✅ EXACT | `Action_Handoff` | QB | `8` | `8` | 146 | START | 146 | 156 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | `7` | `7` | 157 | START | 158 | 161 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 204 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 25–256
- **Visible Samples:** 180

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 25 | 77 | 53 | inferred_complete_timeline |
| `Action_PreSnap` | 114 | 115 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 117 | 125 | 9 | inferred_complete_timeline |
| `Action_SnapReceive` | 131 | 133 | 3 | inferred_complete_timeline |
| `Action_SnapReceive` | 135 | 144 | 10 | inferred_complete_timeline |
| `Action_None` | 145 | 145 | 1 | inferred_complete_timeline |
| `Action_Handoff` | 146 | 156 | 11 | inferred_complete_timeline |
| `Action_None` | 157 | 163 | 7 | inferred_complete_timeline |
| `Action_None` | 166 | 167 | 2 | inferred_complete_timeline |
| `Action_None` | 171 | 172 | 2 | inferred_complete_timeline |
| `Action_None` | 176 | 189 | 14 | inferred_complete_timeline |
| `Action_None` | 191 | 256 | 66 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 25–167
- **Visible Samples:** 139

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 25 | 155 | 131 | inferred_complete_timeline |
| `Action_BallCarry` | 158 | 161 | 4 | inferred_complete_timeline |
| `Action_BallCarry` | 164 | 167 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 137–208
- **Visible Samples:** 70

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 137 | 137 | 1 | inferred_complete_timeline |
| `Action_SplitBlock` | 138 | 164 | 27 | inferred_complete_timeline |
| `Action_SplitBlock` | 167 | 204 | 38 | inferred_complete_timeline |
| `Action_None` | 205 | 208 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 25–299
- **Visible Samples:** 273

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 25 | 133 | 109 | inferred_complete_timeline |
| `Action_ZoneBlock` | 134 | 180 | 47 | inferred_complete_timeline |
| `Action_ZoneBlock` | 183 | 204 | 22 | inferred_complete_timeline |
| `Action_None` | 205 | 299 | 95 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 25–299
- **Visible Samples:** 251

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 25 | 133 | 109 | inferred_complete_timeline |
| `Action_ZoneBlock` | 134 | 143 | 10 | inferred_complete_timeline |
| `Action_ZoneBlock` | 157 | 168 | 12 | inferred_complete_timeline |
| `Action_ZoneBlock` | 180 | 204 | 25 | inferred_complete_timeline |
| `Action_None` | 205 | 299 | 95 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 25–186
- **Visible Samples:** 146

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 25 | 130 | 106 | inferred_complete_timeline |
| `Action_BallSnap` | 131 | 142 | 12 | inferred_complete_timeline |
| `Action_ZoneBlock` | 146 | 150 | 5 | inferred_complete_timeline |
| `Action_ZoneBlock` | 152 | 153 | 2 | inferred_complete_timeline |
| `Action_ZoneBlock` | 166 | 186 | 21 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 45–234
- **Visible Samples:** 190

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 45 | 133 | 89 | inferred_complete_timeline |
| `Action_ZoneBlock` | 134 | 204 | 71 | inferred_complete_timeline |
| `Action_None` | 205 | 234 | 30 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 25–299
- **Visible Samples:** 252

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 25 | 133 | 109 | inferred_complete_timeline |
| `Action_ZoneBlock` | 134 | 172 | 39 | inferred_complete_timeline |
| `Action_ZoneBlock` | 196 | 204 | 9 | inferred_complete_timeline |
| `Action_None` | 205 | 299 | 95 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 25–180
- **Visible Samples:** 155

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 25 | 130 | 106 | inferred_complete_timeline |
| `Action_None` | 131 | 171 | 41 | inferred_complete_timeline |
| `Action_None` | 173 | 180 | 8 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 60–196
- **Visible Samples:** 137

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 60 | 130 | 71 | inferred_complete_timeline |
| `Action_None` | 131 | 196 | 66 | inferred_complete_timeline |

</details>

<details>
<summary>DT — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 25–278
- **Visible Samples:** 234

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 25 | 130 | 106 | inferred_complete_timeline |
| `Action_None` | 131 | 168 | 38 | inferred_complete_timeline |
| `Action_None` | 174 | 176 | 3 | inferred_complete_timeline |
| `Action_None` | 178 | 198 | 21 | inferred_complete_timeline |
| `Action_None` | 203 | 206 | 4 | inferred_complete_timeline |
| `Action_None` | 214 | 224 | 11 | inferred_complete_timeline |
| `Action_None` | 228 | 278 | 51 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 25–295
- **Visible Samples:** 261

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 25 | 130 | 106 | inferred_complete_timeline |
| `Action_None` | 131 | 186 | 56 | inferred_complete_timeline |
| `Action_None` | 188 | 223 | 36 | inferred_complete_timeline |
| `Action_None` | 233 | 295 | 63 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 25–299
- **Visible Samples:** 275

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 25 | 130 | 106 | inferred_complete_timeline |
| `Action_None` | 131 | 299 | 169 | inferred_complete_timeline |

</details>

<details>
<summary>OLB1 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 25–299
- **Visible Samples:** 254

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 25 | 130 | 106 | inferred_complete_timeline |
| `Action_None` | 131 | 189 | 59 | inferred_complete_timeline |
| `Action_None` | 191 | 215 | 25 | inferred_complete_timeline |
| `Action_None` | 229 | 265 | 37 | inferred_complete_timeline |
| `Action_None` | 267 | 268 | 2 | inferred_complete_timeline |
| `Action_None` | 275 | 299 | 25 | inferred_complete_timeline |

</details>

<details>
<summary>OLB2 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `defense`
- **Visible Frames:** 25–299
- **Visible Samples:** 269

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 25 | 130 | 106 | inferred_complete_timeline |
| `Action_None` | 131 | 215 | 85 | inferred_complete_timeline |
| `Action_None` | 217 | 236 | 20 | inferred_complete_timeline |
| `Action_None` | 241 | 252 | 12 | inferred_complete_timeline |
| `Action_None` | 254 | 299 | 46 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `15` | `15` | Position_Unknown | Team_Unknown | 170–175 | 6 | 1 | Undefined position; Undefined team |
| `16` | `16` | Position_Unknown | Team_Unknown | 186–292 | 107 | 1 | Undefined position; Undefined team |
| `17` | `17` | Position_Unknown | Team_Unknown | 187–299 | 112 | 2 | Undefined position; Undefined team |
| `18` | `19` | Position_Unknown | Team_Unknown | 194–282 | 85 | 2 | Undefined position; Undefined team |
| `19` | `20` | Position_Unknown | Team_Unknown | 210–299 | 90 | 1 | Undefined position; Undefined team |
| `20` | `22` | Position_Unknown | Team_Unknown | 244–299 | 56 | 1 | Undefined position; Undefined team |
| `21` | `23` | Position_Unknown | Team_Unknown | 251–299 | 49 | 1 | Undefined position; Undefined team |
| `22` | `25` | Position_Unknown | Team_Unknown | 255–267 | 13 | 1 | Undefined position; Undefined team |
| `23` | `26` | Position_Unknown | Team_Unknown | 255–299 | 45 | 1 | Undefined position; Undefined team |
| `24` | `29` | Position_Unknown | Team_Unknown | 270–284 | 9 | 2 | Undefined position; Undefined team |
| `25` | `31` | Position_Unknown | Team_Unknown | 288–289 | 2 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `10` (3 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `2` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `5` (3 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `9` (2 segments found)
- ⚠️ Ambiguous match for action `Action_SplitBlock` and target `14` (2 segments found)
- ⚠️ Ambiguous match for action `Action_SnapReceive` and target `8` (2 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `7` (2 segments found)

### Track Identity Issues

- ⚠️ 11 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 11 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 22 |
| Missing visible bounding boxes during action | 56 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 299 as fallback play end.
- ⚠️ Resolved action overlap for track '10' (C): higher_priority='Action_BallSnap' [131–144], lower_priority='Action_ZoneBlock' annotated_start=134, effective_Action_ZoneBlock_start=145.
- ⚠️ Action 'Action_None' range [131-215] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [217-236] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [241-252] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [254-299] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [131-189] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [191-215] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [229-265] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [267-268] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [134-172] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [196-204] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [131-186] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [188-223] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [233-295] for track '3' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [131-171] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [173-180] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [134-143] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [157-168] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [180-204] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [131-299] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [25-155] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [158-161] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [164-167] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [25-77] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [114-115] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [117-125] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_SnapReceive' range [131-133] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [157-163] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [166-167] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [171-172] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [176-189] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [191-256] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [134-180] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallSnap' range [131-142] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [146-150] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [152-153] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [166-186] for track '10' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [131-168] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [174-176] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [178-198] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [203-206] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [214-224] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [228-278] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [205-234] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [131-196] for track '13' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_SplitBlock' range [138-164] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [205-208] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [170-175] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [186-292] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [187-205] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [194-234] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [239-282] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [251-299] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [255-267] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [270-276] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [283-284] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [288-289] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Player track '15' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '15' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '16' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '16' has undefined team_side. Will map to Team_Unknown.
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

</details>